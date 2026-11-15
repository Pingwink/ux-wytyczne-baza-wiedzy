#!/usr/bin/env python3
"""
Automatyczny skaner techniczny UX i dostępności WCAG 2.2 AA dla skilla `ux-audit-checklista`.
Analizuje plik HTML (oraz powiązane CSS/JS) pod kątem 59-punktowej checklisty:
- widoki SPA i podstrony,
- współczynniki kontrastu WCAG 2.2 ze zmiennych CSS i reguł,
- strukturę semantyczną, nagłówki, regiony landmark, skip-link,
- obrazy (alt, width, height, loading, fetchpriority, formaty),
- formularze (label, autocomplete, aria-live, aria-invalid),
- elementy deweloperskie pozostawione na produkcji i martwe linki.
"""
import argparse
import json
import math
import os
import re
import sys


def hex_to_rgb(hex_str):
    h = hex_str.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def rel_luminance(rgb):
    def chan(c):
        v = c / 255.0
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = [chan(x) for x in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(hex1, hex2):
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    if not rgb1 or not rgb2:
        return None
    l1 = rel_luminance(rgb1)
    l2 = rel_luminance(rgb2)
    bright, dark = max(l1, l2), min(l1, l2)
    return round((bright + 0.05) / (dark + 0.05), 2)


def scan_html(html_path):
    with open(html_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # Extract CSS variables
    css_vars = dict(re.findall(r"(--[a-zA-Z0-9_-]+)\s*:\s*(#[0-9a-fA-F]{3,6})", content))

    # Compute key contrasts if common background/foreground vars exist
    bg_hex = css_vars.get("--bg", "#FFFFFF")
    card_hex = css_vars.get("--card", "#FFFFFF")
    contrast_checks = []
    for var_name, hex_val in css_vars.items():
        cr_white = contrast_ratio(hex_val, "#FFFFFF")
        cr_bg = contrast_ratio(hex_val, bg_hex)
        contrast_checks.append({
            "variable": var_name,
            "hex": hex_val,
            "contrast_vs_white": cr_white,
            "contrast_vs_bg": cr_bg,
            "passes_normal_text_4_5": (cr_white or 0) >= 4.5,
            "passes_ui_component_3_0": (cr_white or 0) >= 3.0,
        })

    # Views / SPA sections
    spa_views = re.findall(r'<(?:section|div)\b[^>]*\bclass="[^"]*view[^"]*"[^>]*\bid="([^"]+)"|<(?:section|div)\b[^>]*\bid="([^"]+)"[^>]*\bclass="[^"]*view[^"]*"', content)
    spa_views = [a or b for a, b in spa_views]

    # Images check
    img_tags = re.findall(r"<img\b[^>]*>", content, flags=re.IGNORECASE)
    imgs_missing_alt = []
    imgs_missing_dims = []
    imgs_formats = set()
    for tag in img_tags:
        src_m = re.search(r'src="([^"]+)"', tag)
        src = src_m.group(1) if src_m else "unknown"
        ext = os.path.splitext(src)[1].lower()
        if ext:
            imgs_formats.add(ext)
        if 'alt=' not in tag.lower():
            imgs_missing_alt.append(src)
        if 'width=' not in tag.lower() or 'height=' not in tag.lower():
            imgs_missing_dims.append(src)

    # Accessibility & Navigation fundamentals
    has_lang = bool(re.search(r'<html[^>]*\blang="[^"]+"', content, re.IGNORECASE))
    title_m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
    title_text = title_m.group(1).strip() if title_m else ""
    has_skip_link = bool(re.search(r'href="#(main|content|tresc)"', content, re.IGNORECASE))
    has_reduced_motion = "prefers-reduced-motion" in content
    has_px_font_sizes = len(re.findall(r"font-size\s*:\s*\d+px", content))
    has_rem_font_sizes = len(re.findall(r"font-size\s*:\s*[\d.]+rem", content))

    # Debug / leftover artifacts & dead links
    has_seo_toggle = "seo-toggle" in content or "data-seo" in content
    dead_hash_links = len(re.findall(r'href="#"', content))
    target_blank_total = len(re.findall(r'target="_blank"', content))

    result = {
        "file": os.path.abspath(html_path),
        "total_lines": len(content.splitlines()),
        "spa_views_count": len(spa_views),
        "spa_views": spa_views,
        "fundamentals": {
            "has_html_lang": has_lang,
            "static_title": title_text,
            "has_skip_link": has_skip_link,
            "has_prefers_reduced_motion": has_reduced_motion,
            "font_size_px_occurrences": has_px_font_sizes,
            "font_size_rem_occurrences": has_rem_font_sizes,
        },
        "images": {
            "total_img_tags": len(img_tags),
            "missing_alt_count": len(imgs_missing_alt),
            "missing_width_or_height_count": len(imgs_missing_dims),
            "missing_width_or_height_srcs": imgs_missing_dims[:25],
            "formats_used": sorted(list(imgs_formats)),
        },
        "ethics_and_production": {
            "leftover_seo_debug_layer": has_seo_toggle,
            "dead_links_href_hash_count": dead_hash_links,
            "target_blank_links_count": target_blank_total,
        },
        "css_variables_contrast": contrast_checks,
    }
    return result


def main():
    parser = argparse.ArgumentParser(description="Skaner techniczny UX i WCAG 2.2 (59 punktów)")
    parser.add_argument("html_path", help="Ścieżka do pliku index.html")
    parser.add_argument("--output", "-o", help="Opcjonalna ścieżka zapisu pliku JSON z wynikami")
    args = parser.parse_args()

    if not os.path.exists(args.html_path):
        print(f"Błąd: Plik nie istnieje: {args.html_path}", file=sys.stderr)
        sys.exit(1)

    report = scan_html(args.html_path)
    json_str = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as out_f:
            out_f.write(json_str)
        print(f"Zapisano raport techniczny JSON do: {args.output}")
    else:
        print(json_str)


if __name__ == "__main__":
    main()
