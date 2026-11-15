# 02b. Dostępność: kluczowe kryteria WCAG 2.2 w praktyce

> **Zakres:** najważniejsze kryteria sukcesu (A i AA) z dokładnymi wartościami progowymi, pogrupowane tematycznie.
> **Prefiks ID:** `DOST`
> **Format:** każdy punkt zawiera numer kryterium, poziom, wymaganie, sposób sprawdzenia i link do dokumentu *Understanding* W3C.

[← Powrót do README](../../README.md) · [Przegląd WCAG](wcag-2-2-przeglad.md)

Wspólne źródło normatywne: W3C, *WCAG 2.2* – https://www.w3.org/TR/WCAG22/ ; *Understanding WCAG 2.2* – https://www.w3.org/WAI/WCAG22/Understanding/ ; *How to Meet WCAG (Quick Reference)* – https://www.w3.org/WAI/WCAG22/quickref/

---

## A. Treści nietekstowe i multimedia

### DOST-10 Tekst alternatywny – SC 1.1.1 Non-text Content (A)
Każda treść nietekstowa ma tekstowy odpowiednik pełniący tę samą funkcję.
- Obraz informacyjny → `alt` opisujący treść/funkcję („Wykres: sprzedaż wzrosła o 20% w 2024”).
- Obraz będący linkiem/przyciskiem → `alt` opisuje **cel**, nie wygląd („Strona główna”, nie „logo”).
- Obraz dekoracyjny → pusty `alt=""` (lub tło CSS), aby czytnik ekranu go pominął.
- Złożone grafiki (wykresy, infografiki) → krótki `alt` + pełny opis w tekście obok.
- CAPTCHA → opis celu + alternatywa w innej modalności.

**Jak sprawdzić:** przejrzyj wszystkie `<img>`, `<svg>`, ikony-przyciski; wyłącz obrazy i sprawdź, czy treść jest kompletna.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html ; W3C WAI, *Images Tutorial* (drzewo decyzyjne alt) – https://www.w3.org/WAI/tutorials/images/decision-tree/

### DOST-11 Napisy i audiodeskrypcja – SC 1.2.2 (A), 1.2.4 (AA), 1.2.5 (AA)
- **1.2.2 Napisy (nagrane), A** – nagrane wideo z dźwiękiem ma napisy (dialogi + istotne dźwięki, identyfikacja mówiących).
- **1.2.4 Napisy (na żywo), AA** – transmisje na żywo mają napisy.
- **1.2.5 Audiodeskrypcja (nagrane), AA** – istotne informacje wizualne niedostępne w ścieżce dźwiękowej są opisane audiodeskrypcją.
- **1.2.1 (A)** – dla nagrań tylko audio – transkrypcja; dla tylko wideo – transkrypcja lub ścieżka audio.

**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded.html ; https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html ; https://www.w3.org/WAI/WCAG22/Understanding/captions-live.html ; https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html ; W3C WAI, *Making Audio and Video Media Accessible* – https://www.w3.org/WAI/media/av/

### DOST-12 Kontrola dźwięku – SC 1.4.2 Audio Control (A)
Jeśli dźwięk odtwarza się automatycznie dłużej niż **3 sekundy**, musi istnieć mechanizm jego zatrzymania/wyciszenia niezależny od głośności systemowej. **Zalecenie:** nie odtwarzaj dźwięku automatycznie.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/audio-control.html

---

## B. Struktura i prezentacja

### DOST-13 Informacje i relacje – SC 1.3.1 Info and Relationships (A)
Struktura widoczna wizualnie musi być zapisana w kodzie: nagłówki `<h1>`–`<h6>`, listy `<ul>/<ol>`, tabele danych z `<th>` i `scope`, etykiety pól `<label>`, grupy `<fieldset>/<legend>`, regiony `<header>`, `<nav>`, `<main>`, `<footer>`.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html

### DOST-14 Orientacja – SC 1.3.4 Orientation (AA)
Treść nie może być ograniczona do jednej orientacji ekranu (pion/poziom), chyba że jest to niezbędne (np. czek bankowy, pianino).
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/orientation.html

### DOST-15 Cel pola formularza – SC 1.3.5 Identify Input Purpose (AA)
Pola zbierające dane o użytkowniku mają programowo określony cel – w HTML przez atrybut `autocomplete` (np. `name`, `email`, `tel`, `street-address`, `postal-code`, `cc-number`).
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html ; lista wartości: WCAG 2.2 sekcja 7 – https://www.w3.org/TR/WCAG22/#input-purposes

### DOST-16 Nie tylko kolor – SC 1.4.1 Use of Color (A)
Kolor nie może być jedynym sposobem przekazania informacji (np. błąd pola = czerwona ramka **+** ikona **+** tekst; linki w treści odróżnione nie tylko kolorem – np. podkreśleniem – lub kontrastem min. 3:1 względem otaczającego tekstu oraz dodatkowym wyróżnieniem przy hover/focus).
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html ; technika G183 – https://www.w3.org/WAI/WCAG22/Techniques/general/G183

---

## C. Kontrast i skalowanie (wartości progowe)

### DOST-17 Kontrast tekstu – SC 1.4.3 Contrast (Minimum) (AA)
| Rodzaj tekstu | Minimalny współczynnik |
|---|---|
| Tekst zwykły | **4,5 : 1** |
| Tekst duży: ≥ 18 pt (ok. 24 px CSS) lub ≥ 14 pt pogrubiony (ok. 18,66 px CSS) | **3 : 1** |
| Logotypy, tekst dekoracyjny, nieaktywne elementy | brak wymogu |

Poziom AAA (SC 1.4.6): **7 : 1** dla tekstu zwykłego i **4,5 : 1** dla dużego.

**Jak sprawdzić:** WebAIM Contrast Checker, DevTools przeglądarki, Colour Contrast Analyser (TPGi). Wartości nie zaokrągla się w górę (4,49:1 nie spełnia 4,5:1).
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html ; https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced.html ; https://webaim.org/resources/contrastchecker/

### DOST-18 Kontrast elementów nietekstowych – SC 1.4.11 Non-text Contrast (AA)
Minimum **3 : 1** względem sąsiednich kolorów dla: granic pól formularzy i kontrolek potrzebnych do ich identyfikacji, stanów (np. zaznaczony checkbox, wskaźnik fokusu), elementów grafik niezbędnych do zrozumienia treści (linie wykresu, ikony bez etykiety).
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html

### DOST-19 Powiększanie tekstu – SC 1.4.4 Resize Text (AA)
Tekst można powiększyć do **200%** bez technologii asystujących i bez utraty treści lub funkcji. Stosuj jednostki względne (`rem`, `em`), nie blokuj zoomu (`user-scalable=no`, `maximum-scale=1` w meta viewport są błędem).
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html

### DOST-20 Dopasowanie do szerokości (reflow) – SC 1.4.10 Reflow (AA)
Treść wyświetla się bez przewijania w dwóch wymiarach przy szerokości **320 px CSS** (przewijanie pionowe) lub wysokości **256 px CSS** (przewijanie poziome) – odpowiada to powiększeniu 400% przy oknie 1280 px. Wyjątki: mapy, tabele danych, diagramy, gry.
**Jak sprawdzić:** okno 1280 px szerokości, zoom 400% – brak poziomego paska przewijania dla tekstu.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/reflow.html

### DOST-21 Odstępy w tekście – SC 1.4.12 Text Spacing (AA)
Brak utraty treści/funkcji, gdy użytkownik ustawi: wysokość linii **1,5×** rozmiaru czcionki, odstęp po akapicie **2×** rozmiaru czcionki, odstęp między literami **0,12×**, odstęp między słowami **0,16×**. Nie ustawiaj sztywnych wysokości kontenerów z tekstem.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html

### DOST-22 Treść pojawiająca się po najechaniu/fokusie – SC 1.4.13 (AA)
Tooltipy, rozwijane podpowiedzi itp. muszą być: **odrzucalne** (np. klawisz Esc bez przesuwania fokusu), **najeżdżalne** (można przesunąć kursor na pojawiającą się treść), **trwałe** (pozostają, dopóki użytkownik ich nie zamknie lub nie przeniesie fokusu/kursora).
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html

### DOST-23 Obrazy tekstu – SC 1.4.5 Images of Text (AA)
Używaj prawdziwego tekstu zamiast tekstu w grafice (wyjątek: logotypy, gdy prezentacja jest niezbędna).
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html

---

## D. Obsługa klawiaturą i fokus

### DOST-24 Klawiatura – SC 2.1.1 Keyboard (A) i 2.1.2 No Keyboard Trap (A)
Cała funkcjonalność dostępna z klawiatury (Tab, Shift+Tab, Enter, Spacja, strzałki, Esc) bez wymagań czasowych. Fokus nie może utknąć w komponencie (np. w osadzonym odtwarzaczu); jeśli wyjście wymaga niestandardowego klawisza – poinformuj o tym.
**Jak sprawdzić:** odłóż mysz i przejdź całą ścieżkę (menu, formularz, modal, koszyk) samą klawiaturą.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html ; https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html

### DOST-25 Pomijanie bloków – SC 2.4.1 Bypass Blocks (A)
Zapewnij mechanizm pominięcia powtarzających się bloków – np. link „Przejdź do treści” jako pierwszy element fokusowalny oraz poprawne regiony (`<main>`, `<nav>`) i nagłówki.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html

### DOST-26 Kolejność fokusu – SC 2.4.3 Focus Order (A)
Kolejność przechodzenia fokusem zachowuje sens i obsługiwalność – zwykle zgodna z kolejnością wizualną. Unikaj dodatnich wartości `tabindex`. Po otwarciu modala przenieś do niego fokus, a po zamknięciu przywróć do elementu wywołującego.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html ; WAI-ARIA APG, *Dialog (Modal) Pattern* – https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

### DOST-27 Widoczny fokus – SC 2.4.7 Focus Visible (AA) i 2.4.11 Focus Not Obscured (AA)
Wskaźnik fokusu klawiatury musi być widoczny (nie usuwaj `outline` bez zamiennika; używaj `:focus-visible`) i nie może być całkowicie zasłonięty przez przyklejone nagłówki, banery cookies, czaty (pomaga `scroll-padding-top`). Zalecenie (AAA 2.4.13): obrys co najmniej 2 px CSS o kontraście 3:1.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html ; https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html ; https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html

### DOST-28 Skróty jednoznakowe – SC 2.1.4 Character Key Shortcuts (A)
Skróty klawiszowe z jednym znakiem (litera, cyfra, znak) muszą dać się wyłączyć, przemapować albo działać tylko przy fokusie na komponencie.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/character-key-shortcuts.html

---

## E. Czas, ruch i bezpieczeństwo

### DOST-29 Regulowany czas – SC 2.2.1 Timing Adjustable (A)
Dla limitów czasu użytkownik może je wyłączyć, dostosować (min. 10× domyślnego) lub przedłużyć – z ostrzeżeniem co najmniej **20 sekund** przed upływem i możliwością przedłużenia prostą akcją (co najmniej 10 razy). Wyjątki: zdarzenia w czasie rzeczywistym, limity niezbędne, limity dłuższe niż 20 godzin.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html

### DOST-30 Pauza, zatrzymanie, ukrycie – SC 2.2.2 Pause, Stop, Hide (A)
Ruchome, migające lub przewijane treści, które startują automatycznie, trwają dłużej niż **5 sekund** i są wyświetlane obok innej treści (karuzele, animowane banery, tickery) – muszą mieć mechanizm pauzy/zatrzymania/ukrycia. Automatycznie aktualizowane treści – mechanizm pauzy, zatrzymania, ukrycia lub kontroli częstotliwości.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html

### DOST-31 Błyski – SC 2.3.1 Three Flashes or Below Threshold (A)
Nic nie błyska więcej niż **3 razy w ciągu sekundy**, chyba że błyski mieszczą się poniżej progów ogólnego i czerwonego błysku. Ryzyko napadów padaczki fotogennej.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html

### DOST-32 Animacje wywołane interakcją – SC 2.3.3 (AAA) i `prefers-reduced-motion`
Animacje ruchu wywołane interakcją (paralaksa, zoom, przewijanie z efektami) muszą dać się wyłączyć. Praktyka: respektuj preferencję systemową przez zapytanie medialne `@media (prefers-reduced-motion: reduce)`.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html ; technika C39 – https://www.w3.org/WAI/WCAG22/Techniques/css/C39 ; MDN – https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion

---

## F. Nawigacja i orientacja

### DOST-33 Tytuł strony – SC 2.4.2 Page Titled (A)
Każda strona ma unikalny, opisowy `<title>`; zalecany wzorzec: „Treść strony – Sekcja – Nazwa serwisu” (najbardziej specyficzna informacja na początku). Przy błędzie formularza warto dodać „Błąd:” na początku tytułu.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html ; GOV.UK Design System, *Page template / Error summary* – https://design-system.service.gov.uk/components/error-summary/

### DOST-34 Cel linku – SC 2.4.4 Link Purpose (In Context) (A)
Cel linku zrozumiały z jego tekstu (lub tekstu wraz z kontekstem programowym). Unikaj „kliknij tutaj”, „więcej”, „czytaj dalej” bez doprecyzowania.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html

### DOST-35 Wiele sposobów – SC 2.4.5 Multiple Ways (AA)
Do strony w zbiorze stron prowadzi więcej niż jedna droga (np. menu + wyszukiwarka, mapa strony, spis treści) – z wyjątkiem stron będących krokiem procesu.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/multiple-ways.html

### DOST-36 Nagłówki i etykiety – SC 2.4.6 Headings and Labels (AA)
Nagłówki i etykiety opisują temat lub cel. Praktyka: jeden `<h1>` z tematem strony, hierarchia bez przeskakiwania poziomów (zalecenie dobrych praktyk, nie wymóg WCAG).
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html ; W3C WAI, *Headings Tutorial* – https://www.w3.org/WAI/tutorials/page-structure/headings/

### DOST-37 Spójna nawigacja i identyfikacja – SC 3.2.3 (AA), 3.2.4 (AA), 3.2.6 (A)
Powtarzające się menu w tej samej względnej kolejności; komponenty o tej samej funkcji tak samo nazwane (np. ikona lupy zawsze „Szukaj”); mechanizmy pomocy w tym samym miejscu względem innych treści.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation.html ; https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification.html ; https://www.w3.org/WAI/WCAG22/Understanding/consistent-help.html

### DOST-38 Brak niespodziewanej zmiany kontekstu – SC 3.2.1 On Focus (A), 3.2.2 On Input (A)
Samo ustawienie fokusu ani zmiana wartości pola nie może automatycznie zmienić kontekstu (przekierować, wysłać formularza, otworzyć nowego okna) bez uprzedzenia. Np. lista wyboru kraju nie przeładowuje strony – użyj przycisku „Zastosuj”.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/on-focus.html ; https://www.w3.org/WAI/WCAG22/Understanding/on-input.html

---

## G. Wskaźnik i dotyk

### DOST-39 Rozmiar celu – SC 2.5.8 Target Size (Minimum) (AA)
Cel wskazania ma co najmniej **24×24 px CSS**, lub – jeśli mniejszy (wyjątek *Spacing*) – okrąg o średnicy 24 px CSS wyśrodkowany na jego obrysie (bounding box) nie nachodzi na żaden inny cel ani na okrąg innego pomniejszonego celu. Pozostałe wyjątki: odpowiednik spełniający wymóg na tej samej stronie (*Equivalent*), cel w wierszu tekstu ograniczony wysokością linii (*Inline*), rozmiar określony przez przeglądarkę (*User Agent Control*), prezentacja niezbędna lub prawnie wymagana (*Essential*). AAA (SC 2.5.5): **44×44 px CSS**. Zob. też [MOB-03](../07-mobile-i-responsywnosc/mobile-i-responsywnosc.md).
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html

### DOST-40 Gesty i przeciąganie – SC 2.5.1 (A), 2.5.2 (A), 2.5.7 (AA)
- **2.5.1 Pointer Gestures** – funkcje wymagające gestów wielopunktowych (szczypanie) lub ścieżkowych (przesunięcie po określonej trajektorii) dostępne też pojedynczym wskazaniem (np. przyciski +/− przy mapie).
- **2.5.2 Pointer Cancellation** – akcja wykonywana na zdarzenie „w górę” (puszczenie przycisku), z możliwością przerwania przez odsunięcie wskaźnika.
- **2.5.7 Dragging Movements** – alternatywa dla przeciągania (np. przyciski „w górę/w dół” przy sortowaniu, kliknięcie na suwaku).

**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/pointer-gestures.html ; https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation.html ; https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html

### DOST-41 Etykieta w nazwie – SC 2.5.3 Label in Name (A)
Nazwa dostępna komponentu zawiera widoczny tekst jego etykiety (najlepiej na początku). Np. przycisk „Wyślij” nie może mieć `aria-label="Prześlij formularz"` – użytkownicy sterowania głosem powiedzą „kliknij Wyślij”.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html

### DOST-42 Aktywacja ruchem – SC 2.5.4 Motion Actuation (A)
Funkcje uruchamiane ruchem urządzenia (potrząśnięcie, przechylenie) dostępne też przez komponenty UI i możliwe do wyłączenia.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/motion-actuation.html

---

## H. Język, błędy, kompatybilność

### DOST-43 Język strony i części – SC 3.1.1 (A), 3.1.2 (AA)
`<html lang="pl">`; fragmenty w innym języku oznaczone `lang` (np. `<span lang="en">`). Umożliwia poprawną wymowę czytnikom ekranu.
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html ; https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts.html

### DOST-44 Błędy w formularzach – SC 3.3.1 (A), 3.3.2 (A), 3.3.3 (AA), 3.3.4 (AA)
- **3.3.1 Identyfikacja błędu** – błąd wykryty automatycznie jest wskazany, a jego opis podany tekstem.
- **3.3.2 Etykiety lub instrukcje** – pola wymagające danych mają etykiety/instrukcje (w tym format, np. „DD.MM.RRRR”).
- **3.3.3 Sugestia korekty** – jeśli znana jest poprawka, zasugeruj ją (o ile nie narusza to bezpieczeństwa).
- **3.3.4 Zapobieganie błędom (prawne, finansowe, dane)** – transakcje są odwracalne, sprawdzane lub potwierdzane przed ostatecznym wysłaniem.

Szczegóły projektowe: [04 Formularze](../04-formularze/formularze.md).
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html ; https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html ; https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html ; https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html

### DOST-45 Uwierzytelnianie i powtórne wpisywanie – SC 3.3.7 (A), 3.3.8 (AA)
Pozwól na wklejanie haseł i kodów oraz na menedżery haseł; nie wymagaj przepisywania znaków z obrazka bez alternatywy; nie każ ponownie wpisywać danych podanych wcześniej w procesie (np. „adres do faktury taki sam jak dostawy”).
**Źródła:** https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html ; https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html

### DOST-46 Nazwa, rola, wartość – SC 4.1.2 Name, Role, Value (A)
Dla wszystkich komponentów UI nazwa i rola są programowo określone, a stany/wartości mogą być ustawiane i ogłaszane technologiom asystującym. Natywne elementy HTML (`<button>`, `<a href>`, `<input>`) zapewniają to automatycznie; własne widżety wymagają ARIA – zob. [Semantyka i ARIA](semantyka-html-aria.md).
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html

### DOST-47 Komunikaty o stanie – SC 4.1.3 Status Messages (AA)
Komunikaty o statusie bez przenoszenia fokusu („Dodano do koszyka”, „Znaleziono 12 wyników”) są ogłaszane technologiom asystującym – np. przez `role="status"` / `aria-live="polite"` lub `role="alert"` dla pilnych.
**Źródło:** https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html

