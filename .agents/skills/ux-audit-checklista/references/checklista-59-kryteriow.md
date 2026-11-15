# Pełna matryca 59 kryteriów kontrolnych UX i dostępności WCAG 2.2 AA

Poniższa matryca stanowi bazę referencyjną dla skilla `ux-audit-checklista`. Każdy z 59 punktów musi zostać zweryfikowany w raporcie ze statusem `✅ Spełnione`, `⚠️ Częściowo` lub `❌ Niespełnione`.

Legenda priorytetów:
- 🔴 **Wymóg prawny / WCAG 2.2 A–AA** (Europejski Akt o Dostępności EAA / PAD / RODO)
- 🟡 **Silna rekomendacja badawcza** (NN/g, Baymard Institute, W3C COGA, Google Web.dev)
- 🟢 **Dobra praktyka branżowa**

---

## 1. Dostępność – fundamenty (16 punktów)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 1 | 🔴 | Obrazy informacyjne mają `alt` opisujący treść/funkcję, dekoracyjne `alt=""` | `DOST-10` | Sprawdź wszystkie `<img>`, `<svg>` i grafiki w przyciskach (WCAG 1.1.1 A). |
| 2 | 🔴 | Wideo ma napisy; nagrania audio – transkrypcję | `DOST-11` | Sprawdź `<video>` (`<track kind="captions">`) i `<audio>` (WCAG 1.2.1–1.2.5). |
| 3 | 🔴 | Struktura w kodzie: nagłówki `h1`–`h6`, listy, regiony landmark, tabele z `<th scope>` | `DOST-13`, `ARIA-07` | Sprawdź hierarchię nagłówków, `<header>`, `<nav>`, `<main>`, `<footer>`, `<th>` (WCAG 1.3.1 A). |
| 4 | 🔴 | Kontrast tekstu ≥ 4,5:1 (duży ≥ 3:1), kontrolek, obramowań pól i ikon ≥ 3:1 | `DOST-17`, `DOST-18` | Policz kontrast luminancji dla tekstu, `:hover`, obramowań `input` i chipów (WCAG 1.4.3 / 1.4.11 AA). |
| 5 | 🔴 | Informacja nie jest przekazywana wyłącznie kolorem | `DOST-16` | Sprawdź linki w tekście, stany aktywne, próbki kolorów i błędy formularzy (WCAG 1.4.1 A). |
| 6 | 🔴 | Zoom 200% bez utraty treści; brak przewijania poziomego przy szerokości 320 px | `DOST-19`, `DOST-20` | Sprawdź użycie `rem` zamiast `px` dla `font-size` i responsywność przy 320 CSS px (WCAG 1.4.4 / 1.4.10 AA). |
| 7 | 🔴 | Cała obsługa możliwa z klawiatury, bez pułapek klawiaturowych | `DOST-24`, `DOST-22` | Sprawdź nawigację `Tab`, `Shift+Tab`, `Enter`, `Space` oraz zamykanie `Esc` (WCAG 2.1.1 / 2.1.2 / 1.4.13). |
| 8 | 🔴 | Link „Przejdź do treści” (Skip link) jako pierwszy element fokusowalny | `DOST-25` | Sprawdź obecność `<a href="#main" class="skip-link">` na początku `<body>` (WCAG 2.4.1 A). |
| 9 | 🔴 | Widoczny i niezasłonięty wskaźnik fokusu (`≥ 3:1`); logiczna kolejność i fokus w SPA | `DOST-26`, `DOST-27` | Sprawdź styl `:focus-visible`, `scroll-margin-top` przy sticky headerze i przenoszenie fokusu po zmianie widoku SPA (WCAG 2.4.3 / 2.4.7 / 2.4.11). |
| 10 | 🔴 | Ruchome treści > 5 s można zatrzymać; brak błysków > 3 razy na sekundę | `DOST-30`, `DOST-31` | Sprawdź karuzele, autoodtwarzane wideo i animacje (WCAG 2.2.2 / 2.3.1 A). |
| 11 | 🔴 | Unikalny, opisowy `<title>` na każdym widoku; zadeklarowany `lang="pl"` | `DOST-33`, `DOST-43` | Sprawdź statyczny `<title>` w `<head>`, aktualizację `document.title` w SPA oraz `<html lang="pl">` (WCAG 2.4.2 / 3.1.1 A). |
| 12 | 🔴 | Cele dotyku i kliknięcia ≥ 24×24 px CSS (zalecane 44×44 – 48×48 px) | `DOST-39`, `MOB-03` | Zmierz wysokość/szerokość przycisków, linków, próbek i kontrolek (WCAG 2.5.8 AA). |
| 13 | 🔴 | Natywne elementy HTML zamiast `div` z ARIA; każda kontrolka ma nazwę dostępną | `ARIA-01`, `ARIA-05` | Sprawdź użycie `<button>`, `<a>`, `<fieldset>`, `<details>` oraz `aria-hidden="true"` na dekoracyjnych SVG (WCAG 4.1.2 A). |
| 14 | 🔴 | Komunikaty statusu, wyników wyszukiwania i błędów ogłaszane czytnikom (`aria-live`) | `DOST-47` | Sprawdź `role="status"`, `role="alert"` lub `aria-live="polite"` na dynamicznych komunikatach (WCAG 4.1.3 AA). |
| 15 | 🟡 | Brak „nakładek dostępności” (accessibility overlays / widgetów) | `DOST-06` | Upewnij się, że strona nie ładuje skryptów typu AccessiBe/UserWay. |
| 16 | 🔴/🟢 | Deklaracja dostępności cyfrowej i informacja o dostępności architektonicznej | `PRAW-02`, `PRAW-07` | Sprawdź obecność deklaracji dostępności oraz opisu wejścia/schodów/parkingu dla punktów stacjonarnych. |

---

## 2. Nawigacja i architektura informacji (9 punktów)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 17 | 🟡 | Etykiety menu zrozumiałe dla użytkownika, bez żargonu i fałszywych obietnic | `NAW-02` | Sprawdź czy nazwy pozycji menu i kart odpowiadają rzeczywistej zawartości podstron docelowych. |
| 18 | 🟡 | Na desktopie pełne menu widoczne (nie ukryte wyłącznie pod ikoną hamburgera) | `NAW-04` | Sprawdź widoczność głównej nawigacji powyżej 900–1024 px. |
| 19 | 🟡 | Oznaczona bieżąca lokalizacja w menu i okruszkach (`aria-current="page"`) | `NAW-05` | Sprawdź czy aktywna podstrona/sekcja ma wizualne wyróżnienie oraz atrybut `aria-current="page"`. |
| 20 | 🟢 | Logo po lewej stronie (lub czytelnie w nagłówku), prowadzi do strony głównej | `NAW-06` | Sprawdź czy logo jest linkiem do strony głównej i ma tekst alternatywny. |
| 21 | 🟡 | Okruszki (breadcrumbs) na podstronach w serwisach wielopoziomowych | `NAW-08` | Sprawdź `<nav aria-label="Okruszki"><ol>...</ol></nav>` na wszystkich podstronach oferty/kategorii. |
| 22 | 🔴 | Więcej niż jeden sposób dotarcia do podstron (menu + wyszukiwarka + kafelki/mapa) | `DOST-35` | Sprawdź minimum 2 niezależne mechanizmy nawigacji (WCAG 2.4.5 AA). |
| 23 | 🟡 | Funkcjonalna wyszukiwarka przeszukująca treści i obsługująca stan „Brak wyników” | `NAW-10` | Przetestuj wyszukiwarkę na hasłach z oferty oraz hasłach z treści podstron; sprawdź stan pusty. |
| 24 | 🔴 | Opisowe teksty linków (bez „kliknij tutaj”, „więcej”) i ostrzeżenie przy `target="_blank"` | `DOST-34`, `NAW-11`, `NAW-12` | Sprawdź teksty linków oraz czy linki otwierające nowe okno informują o tym użytkownika (WCAG 2.4.4 A). |
| 25 | 🟢 | Pomocna strona 404 (lub obsługa nieznanego adresu `#hash` w routerze SPA) | `NAW-13` | Sprawdź co dzieje się po wpisaniu nieistniejącego adresu podstrony lub błędnego `#hash`. |

---

## 3. Formularze i konfiguratory (9 punktów)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 26 | 🟡 | Tylko niezbędne pola; czytelny układ jednokolumnowy krok po kroku | `FORM-01`, `FORM-02` | Sprawdź liczbę pól i czy grupy opcji układają się w jedną logiczną ścieżkę pionową. |
| 27 | 🔴 | Widoczne etykiety `<label>` powiązane z polami; `placeholder` nie zastępuje etykiety | `FORM-04` | Sprawdź czy każde pole (w tym drugie pole w parach szerokość × wysokość) ma widoczną etykietę i jednostkę (WCAG 3.3.2 A). |
| 28 | 🟡 | Wyraźnie oznaczone pola wymagane i opcjonalne | `FORM-05` | Sprawdź oznaczenia `(opcjonalnie)` lub `(wymagane)`. |
| 29 | 🔴 | Atrybuty `autocomplete`, właściwe `inputmode` i brak przypadkowej zmiany `type="number"` scrollem | `DOST-15`, `FORM-07` | Sprawdź pola danych użytkownika oraz zabezpieczenie pól liczbowych przed przypadkowym przewinięciem kółkiem myszy (WCAG 1.3.5 AA). |
| 30 | 🔴 | Błędy opisane tekstem przy polu, z sugestią poprawki i `aria-invalid="true"` | `FORM-09`, `DOST-44` | Wpisz błędną wartość (np. za mały margines) i sprawdź treść komunikatu, `aria-invalid` i `aria-describedby` (WCAG 3.3.1 / 3.3.3). |
| 31 | 🟡 | Walidacja po opuszczeniu pola (`on blur`), a nie w trakcie pisania pierwszej cyfry (`on input`) | `FORM-10`, `FORM-11` | Sprawdź czy komunikat błędu nie pojawia się przedwcześnie, zanim użytkownik dokończy wpisywanie liczby. |
| 32 | 🔴 | Możliwość wklejania haseł/kodów/wymiarów (`paste`); brak niedostępnej CAPTCHA | `DOST-45`, `FORM-13`, `FORM-14` | Sprawdź brak blokad `onpaste` i brak zagadek obrazkowych bez alternatywy (WCAG 3.3.8 AA). |
| 33 | 🟡 | Brak przymusu zakładania konta; orientacyjne koszty/widełki pokazane wcześnie | `FORM-16`, `FORM-17` | Sprawdź możliwość zamówienia/zapytania bez rejestracji oraz dostępność orientacyjnych cen („od X zł”) i listy wielopozycyjnej dla zamówień B2B. |
| 34 | 🔴 | Kompletne i dokładne podsumowanie wszystkich wariantów przed złożeniem zamówienia | `FORM-18` | Sprawdź czy podsumowanie uwzględnia wszystkie wybrane warianty (np. wszystkie 3 warstwy w wariancie potrójnym) (WCAG 3.3.4 AA). |

---

## 4. Treść i typografia (5 punktów)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 35 | 🟡 | Zasada odwróconej piramidy; opisowe śródtytuły, krótkie akapity, listy i tabele | `TRE-02`, `TRE-03` | Sprawdź skanowalność tekstu (chunking) na stronie głównej i podstronach oferty. |
| 36 | 🟡 | Prosty język (Plain Language – ISO 24495-1), wyjaśnienie pojęć technicznych | `TRE-04` | Sprawdź czy specjalistyczne pojęcia (np. fazowanie 45°, karton muzealny, szkło muzealne) są wyjaśnione prostym językiem. |
| 37 | 🟢 | Przyciski CTA opisują akcję czasownikiem (np. „Zadzwoń”, „Wybierz wymiary”) | `TRE-05` | Sprawdź wszystkie przyciski `.btn` (czy nie zawierają samego numeru telefonu bez czasownika). |
| 38 | 🟡 | Tekst główny ≥ 16 px zdefiniowany w `rem`; długość wiersza 50–75 znaków (`ch`); interlinia ≥ 1,5 | `TYP-01`, `TYP-02`, `TYP-03` | Sprawdź `font-size`, `line-height` oraz `max-width` kolumny tekstu w CSS. |
| 39 | 🟢 | Tekst wyrównany do lewej (`text-align: left`), bez obustronnego wyjustowania | `TYP-04` | Sprawdź brak `text-align: justify` w arkuszu stylów. |

---

## 5. Wydajność – Core Web Vitals (4 punkty)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 40 | 🟡 | Architektura sprzyjająca LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 | `WYD-01` | Sprawdź wielkość DOM, brak ciężkich bibliotek blokujących główny wątek i stabilność układu. |
| 41 | 🟡 | Element LCP (Hero) bez `loading="lazy"`, z `<link rel="preload">` / `fetchpriority="high"` | `WYD-04` | Sprawdź sposób ładowania obrazu Hero i pierwszego obrazu nad linią zgięcia. |
| 42 | 🟡 | Jawnie zadeklarowane atrybuty `width` i `height` dla wszystkich obrazów `<img>` i `<iframe>` | `WYD-06` | Sprawdź czy każdy znacznik `<img>` posiada atrybuty `width` i `height` zapobiegające przesunięciom CLS. |
| 43 | 🟢 | Nowoczesne formaty obrazów (`AVIF` / `WebP`) oraz responsywne `srcset` / `<picture>` | `WYD-07` | Sprawdź formaty plików graficznych i obecność `srcset`. |

---

## 6. Mobile i responsywność (4 punkty)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 44 | 🔴 | Poprawny `<meta name="viewport">` bez `maximum-scale=1` i `user-scalable=no` | `MOB-01` | Sprawdź tag `<meta name="viewport">` w `<head>`. |
| 45 | 🔴 | Pełna obsługa obu orientacji ekranu (pionowej i poziomej) | `DOST-14` | Sprawdź brak blokad orientacji w CSS/JS (WCAG 1.3.4 AA). |
| 46 | 🟡 | Kluczowe informacje i nawigacja nie są dostępne wyłącznie po najechaniu myszą (`:hover`) | `MOB-05` | Sprawdź działanie menu mobilnego i kart na ekranach dotykowych (np. 375 px). |
| 47 | 🟡 | Brak natrętnych pełnoekranowych pop-upów i elementów zasłaniających treść na mobile | `MOB-06` | Sprawdź czy żadne pływające przyciski (np. `#seo-toggle`) nie zasłaniają treści na wąskim ekranie. |

---

## 7. Interakcje i komponenty (5 punktów)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 48 | 🟡 | Wyraźna sygnalizacja klikalności (affordance) i brak fałszywych sygnalizatorów | `INT-01`, `INT-02`, `WIZ-05` | Sprawdź czy elementy wyglądające na klikalne (np. zdjęcia z efektem zoomu na hover) faktycznie reagują na kliknięcie (np. otwierają lightbox). |
| 49 | 🟡 | Komplet stanów komponentów (`default`, `hover`, `focus-visible`, `active`, `disabled`, `error`, `empty`) | `INT-03`, `INT-12` | Sprawdź stany przycisków, pól formularza i stan pusty („Brak wyników”) w wyszukiwarce. |
| 50 | 🟡 | Panele rozwijane i modale obsługują klawisz `Esc` oraz zarządzają fokusem | `INT-06`, `DOST-22` | Sprawdź zamykanie podmenu, wyszukiwarki i paneli klawiszem `Escape`. |
| 51 | 🟡 | Brak automatycznie przewijanych karuzel bez przycisku pauzy | `INT-07` | Sprawdź brak agresywnych sliderów. |
| 52 | 🔴 | Poszanowanie preferencji systemowej `@media (prefers-reduced-motion: reduce)` | `DOST-32`, `INT-10` | Sprawdź regułę `@media (prefers-reduced-motion: reduce)` w CSS. |

---

## 8. Etyka, prywatność i zaufanie (4 punkty)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 53 | 🔴 | Zgodność z RODO/ePrivacy: polityka prywatności oraz ładowanie zewnętrznych `<iframe>` (np. Google Maps) po zgodzie / kliknięciu | `ETY-05`, `PRAW-08` | Sprawdź czy link „Polityka prywatności” działa (nie prowadzi do `href="#"`) i czy zewnętrzne mapy nie ładują ciasteczek śledzących bez interakcji. |
| 54 | 🔴 | Brak wzorców manipulacyjnych (Dark Patterns – fałszywe liczniki, ukryte opłaty, presja) | `ETY-03` | Sprawdź uczciwość komunikatów w całym serwisie. |
| 55 | 🔴 | Brak wymuszonych subskrypcji i utrudnień w rezygnacji | `ETY-04` | Sprawdź brak pułapek subskrypcyjnych. |
| 56 | 🟡 | Pełne dane rejestrowe firmy (NIP/KRS), spójne godziny otwarcia/kontakt i brak warstw deweloperskich na produkcji | `ETY-01`, `ETY-02`, `POD-10` | Sprawdź spójność danych w sekcji kontaktu, stopce i JSON-LD, obecność NIP/KRS oraz brak roboczych przycisków deweloperskich (`#seo-toggle`). |

---

## 9. Badania i testowanie (3 punkty)

| Lp. | Priorytet | Kryterium kontrolne | ID wytycznej | Jak weryfikować (w kodzie i UI) |
| :--- | :---: | :--- | :--- | :--- |
| 57 | 🟡 | Weryfikacja ścieżki zadaniowej na realistycznej personie (Cognitive Walkthrough) | `BAD-02` | Przejdź pełną ścieżkę zadaniową persony przez 100% ekranów. |
| 58 | 🟡 | Połączenie skanu automatycznego z ręcznym testem klawiatury i analizą semantyki | `BAD-08`, `BAD-10` | Wykonaj skan skryptem `audit_scanner.py` oraz ręczną inspekcję klawiaturą i kontrastu. |
| 59 | 🟢 | Rekomendacja wdrożenia automatycznych testów dostępności (`axe-core` / Playwright) w CI/CD | `BAD-10` | Dołącz w podsumowaniu gotową instrukcję uruchomienia testów regresji dostępności. |

