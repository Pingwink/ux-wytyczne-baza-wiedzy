# 02a. Dostępność: przegląd WCAG 2.2

> **Zakres:** struktura standardu WCAG, poziomy zgodności, nowe kryteria w wersji 2.2, dane o skali problemu.
> **Prefiks ID:** `DOST`

[← Powrót do README](../../README.md) · Dalej: [Kryteria szczegółowe](wcag-kryteria-szczegolowe.md) · [Prawo PL/UE](prawo-pl-ue.md) · [Semantyka i ARIA](semantyka-html-aria.md)

---

## DOST-01 Czym jest WCAG
*Web Content Accessibility Guidelines* (WCAG) to standard W3C (Web Accessibility Initiative). Aktualna wersja **WCAG 2.2** została opublikowana jako Rekomendacja W3C **5 października 2023 r.** WCAG 2.2 jest wstecznie zgodny: treść spełniająca 2.2 spełnia też 2.1 i 2.0. WCAG 2.2 zostało również zatwierdzone jako norma ISO/IEC 40500:2025.

**Źródła:**
- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* – https://www.w3.org/TR/WCAG22/
- W3C WAI, *What's New in WCAG 2.2* – https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- W3C WAI, *WCAG 2 Overview* – https://www.w3.org/WAI/standards-guidelines/wcag/

## DOST-02 Cztery zasady (POUR)
1. **Postrzegalność (Perceivable)** – informacje i komponenty muszą być prezentowane w sposób, który użytkownik może postrzec (np. tekst alternatywny, napisy, kontrast).
2. **Funkcjonalność (Operable)** – komponenty i nawigacja muszą być obsługiwalne (np. klawiatura, wystarczający czas, brak wywoływania napadów).
3. **Zrozumiałość (Understandable)** – informacje i obsługa interfejsu muszą być zrozumiałe (język, przewidywalność, pomoc przy błędach).
4. **Solidność (Robust)** – treść musi być interpretowana przez różne programy użytkownika, w tym technologie asystujące.

Zasady dzielą się na **13 wytycznych**, a te na testowalne **kryteria sukcesu**.

**Źródło:** https://www.w3.org/TR/WCAG22/#principles ; W3C WAI, *WCAG 2 at a Glance* – https://www.w3.org/WAI/standards-guidelines/wcag/glance/

## DOST-03 Poziomy zgodności A / AA / AAA
- **A** – minimum; bez tego część użytkowników w ogóle nie skorzysta z treści.
- **AA** – poziom wymagany przez prawo w UE/Polsce (przez normę EN 301 549) i najczęściej przyjmowany jako cel.
- **AAA** – najwyższy; W3C **nie zaleca** wymagania AAA dla całych serwisów, bo dla niektórych treści nie da się go spełnić.

Zgodność dotyczy **całych stron** (nie fragmentów) i **kompletnych procesów** (np. wszystkie kroki zakupu).

**Źródło:** https://www.w3.org/TR/WCAG22/#conformance ; W3C, *Understanding Conformance* – https://www.w3.org/WAI/WCAG22/Understanding/conformance

> [!IMPORTANT]
> **Rekomendacja bazy:** celem minimalnym każdej strony powinien być **WCAG 2.2 poziom AA**. W prawie PL/UE normą zharmonizowaną przywołaną w Dz.U. UE jest EN 301 549 V3.2.1 (WCAG 2.1 AA), przy czym we wrześniu 2026 r. ETSI opublikowało wersję **EN 301 549 V4.1.1** opartą już na **WCAG 2.2 AA** (oczekującą na publikację odniesienia w Dz.U. UE).

## DOST-04 Nowe kryteria sukcesu w WCAG 2.2
WCAG 2.2 dodało 9 kryteriów:

| Nr | Nazwa (EN) | Poziom | Istota |
|----|-----------|--------|--------|
| 2.4.11 | Focus Not Obscured (Minimum) | AA | Element z fokusem nie może być całkowicie zasłonięty przez treść autora (np. przyklejony nagłówek, baner cookies). |
| 2.4.12 | Focus Not Obscured (Enhanced) | AAA | Żadna część elementu z fokusem nie jest zasłonięta. |
| 2.4.13 | Focus Appearance | AAA | Wskaźnik fokusu ma określony minimalny obszar i kontrast 3:1 między stanem z fokusem i bez. |
| 2.5.7 | Dragging Movements | AA | Każdą funkcję wymagającą przeciągania da się wykonać pojedynczym wskazaniem (np. kliknięciem), chyba że przeciąganie jest niezbędne. |
| 2.5.8 | Target Size (Minimum) | AA | Cele dotykowe/kliknięcia mają co najmniej 24×24 px CSS (z wyjątkami, m.in. dotyczącymi odstępu). |
| 3.2.6 | Consistent Help | A | Mechanizmy pomocy (kontakt, czat, FAQ) występują w tej samej względnej kolejności na stronach. |
| 3.3.7 | Redundant Entry | A | Nie wymagaj ponownego wpisywania informacji podanej wcześniej w tym samym procesie (autouzupełnij lub pozwól wybrać). |
| 3.3.8 | Accessible Authentication (Minimum) | AA | Logowanie nie może wymagać testu funkcji poznawczych (zapamiętanie, przepisanie, rozwiązanie zagadki) bez alternatywy lub wsparcia (np. wklejanie, menedżer haseł). |
| 3.3.9 | Accessible Authentication (Enhanced) | AAA | Jak wyżej, bez wyjątków dla rozpoznawania obiektów i treści dostarczonych przez użytkownika. |

Ponadto kryterium **4.1.1 Parsing** zostało w WCAG 2.2 oznaczone jako przestarzałe i usunięte.

**Źródło:** W3C WAI, *What's New in WCAG 2.2* – https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

## DOST-05 Skala problemu – dane
- Według WHO ok. **1,3 mld osób (ok. 16% populacji świata)** doświadcza znaczącej niepełnosprawności.
- Raport **WebAIM Million** (automatyczna analiza 1 mln stron głównych): w edycji **2025** wykryto błędy WCAG na **94,8%** stron (średnio **51** błędów na stronę, niski kontrast na **79,1%** stron), a w edycji **2026** na **95,9%** stron (średnio **56,1** błędu na stronę). Najczęstsze problemy: niski kontrast tekstu (**83,9%** stron w 2026 r., **79,1%** w 2025 r.), brak tekstu alternatywnego obrazów, puste linki, brak etykiet formularzy, puste przyciski, brak deklaracji języka dokumentu.

> [!NOTE]
> Narzędzia automatyczne wykrywają tylko część problemów – brak błędów w teście automatycznym **nie oznacza** zgodności z WCAG (zob. [BAD-08](../11-badania-i-testowanie/badania-i-testowanie.md)).

**Źródła:**
- WHO, *Disability* (fact sheet, 2023) – https://www.who.int/news-room/fact-sheets/detail/disability-and-health
- WebAIM, *The WebAIM Million* – https://webaim.org/projects/million/

## DOST-06 Unikaj „nakładek dostępności” (overlays)
Nakładki (widżety JS obiecujące automatyczną zgodność z WCAG) nie naprawiają problemów w kodzie źródłowym, mogą kolidować z technologiami asystującymi użytkowników, a ich stosowanie nie gwarantuje zgodności. W 2025 r. amerykańska Federal Trade Commission (FTC) nałożyła na dostawcę nakładki accessiBe karę **1 mln USD** za wprowadzające w błąd twierdzenia, że narzędzie AI automatycznie zapewnia zgodność stron z WCAG. Dostępność należy wbudować w kod i treść.

**Źródła:**
- *Overlay Fact Sheet* (podpisany przez ponad 800 ekspertów) – https://overlayfactsheet.com/
- FTC, sprawa accessiBe (komunikat z 3.01.2025 i decyzja końcowa z 22.04.2025) – https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-order-requires-online-marketer-pay-1-million-deceptive-claims-its-ai-product-could-make-websites ; https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-approves-final-order-requiring-accessibe-pay-1-million

