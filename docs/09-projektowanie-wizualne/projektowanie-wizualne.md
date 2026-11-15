# 09. Projektowanie wizualne

> **Zakres:** hierarchia wizualna, kolor, białe przestrzenie, układ, obrazy, spójność (design system).
> **Prefiks ID:** `WIZ`

[← Powrót do README](../../README.md)

---

## WIZ-01 Wyraźna hierarchia wizualna
Najważniejsze elementy wyróżniaj rozmiarem, kontrastem, kolorem i położeniem; ograniczaj liczbę poziomów wyróżnienia. Test: patrząc na stronę przez kilka sekund (lub rozmywając ją – „blur test”), użytkownik powinien wskazać główny cel i główną akcję.

**Źródło:** NN/g, *Visual Hierarchy in UX: Definition* – https://www.nngroup.com/articles/visual-hierarchy-ux-definition/

## WIZ-02 Białe przestrzenie i grupowanie
Odstępy grupują powiązane elementy i oddzielają niepowiązane (zasada bliskości, POD-20). Stosuj spójną skalę odstępów (np. wielokrotności 4 lub 8 px), zwiększaj odstęp między grupami bardziej niż wewnątrz grup.

**Źródła:** NN/g, *Proximity Principle in Visual Design* – https://www.nngroup.com/articles/gestalt-proximity/ ; Material Design 3, *Layout – Spacing* – https://m3.material.io/foundations/layout/understanding-layout/spacing

## WIZ-03 Kolor: kontrast, znaczenie, daltonizm
- Spełnij progi kontrastu (DOST-17, DOST-18).
- Nie przekazuj znaczenia tylko kolorem (DOST-16) – ok. **8% mężczyzn i 0,5% kobiet** pochodzenia północnoeuropejskiego ma zaburzenia widzenia barw (najczęściej czerwono-zielone).
- Używaj kolorów semantycznych konsekwentnie (np. czerwony = błąd/destrukcja, zielony = sukces) i z dodatkowymi oznaczeniami (ikona, tekst).
- Testuj symulatorem daltonizmu (np. DevTools → Rendering → Emulate vision deficiencies).

**Źródła:** National Eye Institute, *Color Blindness* – https://www.nei.nih.gov/learn-about-eye-health/eye-conditions-and-diseases/color-blindness ; Chrome DevTools, *Emulate vision deficiencies* – https://developer.chrome.com/docs/devtools/rendering/apply-effects#emulate_vision_deficiencies

## WIZ-04 Tryb ciemny jako opcja
Jeśli oferujesz tryb ciemny: respektuj `prefers-color-scheme`, pozwól też przełączyć ręcznie, sprawdź kontrast w obu motywach (wymagania WCAG obowiązują w każdym), unikaj czystej bieli na czystej czerni dla dużych bloków tekstu (zalecenia platform sugerują ciemnoszare tła).

**Źródła:** MDN, *prefers-color-scheme* – https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme ; Material Design 2, *Dark theme* – https://m2.material.io/design/color/dark-theme.html ; NN/g, *Dark Mode vs. Light Mode: Which Is Better?* – https://www.nngroup.com/articles/dark-mode/

## WIZ-05 Obrazy: informacyjne, nie ozdobne „stocki”
Użytkownicy zwracają uwagę na obrazy niosące informację (zdjęcia produktów, prawdziwych ludzi z zespołu), a ignorują zdjęcia czysto dekoracyjne, typowo stockowe. Zdjęcia produktów: wiele ujęć, możliwość powiększenia, kontekst skali.

**Źródła:** J. Nielsen (2010), *Photos as Web Content* – https://www.nngroup.com/articles/photos-as-web-content/ ; Baymard Institute, *Product Page UX – Images* – https://baymard.com/blog/ensure-sufficient-image-resolution-and-zoom

## WIZ-06 Ślepota banerowa
Użytkownicy ignorują elementy wyglądające jak reklamy lub umieszczone w typowych miejscach reklam (np. prawa kolumna, górny baner) – nie umieszczaj tam kluczowej treści i nie stylizuj ważnych informacji na reklamy.

**Źródło:** K. Pernice (2018), *Banner Blindness Revisited: Users Dodge Ads on Mobile and Desktop* – https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/

## WIZ-07 Spójność dzięki systemowi projektowemu
Utrzymuj bibliotekę komponentów i tokenów (kolory, typografia, odstępy) z dokumentacją użycia i dostępności. Zwiększa spójność (heurystyka POD-06) i przyspiesza pracę. Wzorce: GOV.UK Design System, Material Design, Carbon (IBM), a w Polsce np. komponenty serwisu gov.pl.

**Źródła:** NN/g, *Design Systems 101* – https://www.nngroup.com/articles/design-systems-101/ ; GOV.UK Design System – https://design-system.service.gov.uk/ ; IBM Carbon – https://carbondesignsystem.com/

## WIZ-08 Treść „above the fold” i przewijanie
Użytkownicy przewijają, ale uwaga jest nierówno rozłożona: badania eyetrackingowe NN/g wykazały, że ok. 57% czasu oglądania przypada na pierwszy ekran (a 74% na pierwsze dwa ekrany). **Wniosek:** najważniejsze informacje i propozycja wartości na górze, ale bez upychania wszystkiego; unikaj „fałszywego dna” (wizualnego sygnału, że strona się kończy).

**Źródło:** NN/g, *Scrolling and Attention* (2018) – https://www.nngroup.com/articles/scrolling-and-attention/

