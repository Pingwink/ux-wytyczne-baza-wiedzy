# 03. Architektura informacji i nawigacja

> **Zakres:** organizacja treści, menu, wyszukiwarka, okruszki, linki, strony błędów.
> **Prefiks ID:** `NAW`

[← Powrót do README](../../README.md)

---

## Architektura informacji

### NAW-01 Struktura oparta na modelu mentalnym użytkowników, nie organizacji
Grupuj i nazywaj treści tak, jak myślą o nich użytkownicy, a nie wg struktury działów firmy. Metody: sortowanie kart (card sorting) do tworzenia struktury, testy drzewa (tree testing) do jej weryfikacji.

**Źródła:** NN/g, *Card Sorting: Uncover Users' Mental Models* – https://www.nngroup.com/articles/card-sorting-definition/ ; NN/g, *Tree Testing* – https://www.nngroup.com/articles/tree-testing/

### NAW-02 Etykiety nawigacji: konkretne, rozpoznawalne, rozróżnialne
Używaj jasnych, znanych słów (np. „Cennik”, „Kontakt”), unikaj ogólników („Rozwiązania”, „Zasoby”) i pomysłowych nazw marketingowych. Najważniejsze słowo umieszczaj na początku etykiety (ułatwia skanowanie).

**Źródło:** NN/g, *Menu Design: Checklist of 15 UX Guidelines* – https://www.nngroup.com/articles/menu-design/

### NAW-03 Szerokość vs. głębokość
Badania wskazują, że płytsze i szersze hierarchie z dobrze pogrupowanymi pozycjami są zwykle efektywniejsze niż głębokie hierarchie z wieloma poziomami – każdy dodatkowy poziom to dodatkowa decyzja i ryzyko pomyłki.

**Źródła:** K. Larson, M. Czerwinski (1998), *Web page design: implications of memory, structure and scent for information retrieval*, CHI ’98, 25–32. https://doi.org/10.1145/274644.274649 ; NN/g, *Flat vs. Deep Website Hierarchies* – https://www.nngroup.com/articles/flat-vs-deep-hierarchy/

---

## Menu i nawigacja globalna

### NAW-04 Widoczna nawigacja na desktopie
Na szerokich ekranach pokazuj główne pozycje menu bezpośrednio – ukrycie ich za ikoną hamburgera obniża odkrywalność i wydłuża czas zadań. Na mobile ukryte menu jest akceptowalne, ale rozważ pokazanie 3–5 najważniejszych pozycji (np. dolny pasek kart).

**Źródła:** NN/g, *Hamburger Menus and Hidden Navigation Hurt UX Metrics* – https://www.nngroup.com/articles/hamburger-menus/ ; NN/g, *Beyond the Hamburger: What Makes Navigation Discoverable on Mobile* – https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/

### NAW-05 Wskazuj bieżącą lokalizację
Oznacz aktywną pozycję menu wizualnie (nie tylko kolorem – DOST-16) i programowo (`aria-current="page"`). Użytkownik zawsze powinien wiedzieć: gdzie jestem, gdzie mogę pójść, jak wrócić.

**Źródła:** NN/g, *Navigation: You Are Here* – https://www.nngroup.com/articles/navigation-you-are-here/ ; WAI-ARIA 1.2 `aria-current` – https://www.w3.org/TR/wai-aria-1.2/#aria-current

### NAW-06 Logo prowadzi do strony głównej
Umieść logo w lewym górnym rogu (w językach LTR) i podlinkuj je do strony głównej – to konwencja oczekiwana przez użytkowników. Badania NN/g wykazały, że użytkownicy znacznie częściej trafiają na stronę główną jednym kliknięciem, gdy logo jest po lewej stronie, niż gdy jest wyśrodkowane.

**Źródło:** NN/g, *Centered Logos Hurt Website Navigation* – https://www.nngroup.com/articles/centered-logos/

### NAW-07 Menu rozwijane i mega-menu
- Otwieraj po kliknięciu lub po krótkim opóźnieniu najechania (ok. 0,5 s), zamykaj z opóźnieniem – zapobiega przypadkowemu otwieraniu/zamykaniu.
- Mega-menu: grupuj pozycje z nagłówkami, unikaj przewijania wewnątrz menu.
- Obsługa klawiatury i ARIA: przycisk z `aria-expanded`; wzorzec *Disclosure Navigation* zamiast `role="menu"` dla nawigacji strony.

**Źródła:** NN/g, *Mega Menus Work Well for Site Navigation* – https://www.nngroup.com/articles/mega-menus-work-well/ ; NN/g, *Timing Guidelines for Exposing Hidden Content* – https://www.nngroup.com/articles/timing-exposing-content/ ; WAI-ARIA APG, *Disclosure Navigation Menu* – https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/examples/disclosure-navigation/

### NAW-08 Okruszki (breadcrumbs) w głębokich serwisach
Stosuj okruszki pokazujące hierarchię (nie historię przeglądania) w serwisach o więcej niż 2 poziomach; nie zastępują nawigacji głównej. Ostatni element (bieżąca strona) nie jest linkiem. Kod: `<nav aria-label="Okruszki">` + lista uporządkowana + `aria-current="page"`.

**Źródła:** NN/g, *Breadcrumbs: 11 Design Guidelines for Desktop and Mobile* – https://www.nngroup.com/articles/breadcrumbs/ ; WAI-ARIA APG, *Breadcrumb Pattern* – https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/

### NAW-09 Stopka jako nawigacja uzupełniająca
Stopka to miejsce, gdzie użytkownicy szukają informacji kontaktowych, prawnych (polityka prywatności, regulamin), dostępności, kariery. Zachowaj w niej spójny układ na wszystkich stronach.

**Źródło:** NN/g, *Footers 101: Design Patterns and When to Use Each* – https://www.nngroup.com/articles/footers/

---

## Wyszukiwanie

### NAW-10 Wyszukiwarka w serwisach z dużą ilością treści
- Pokaż pole wyszukiwania jako otwarte pole tekstowe (nie tylko ikonę) w nagłówku, na każdej stronie.
- Pole wystarczająco szerokie – NN/g zaleca, by pomieściło ok. 27 znaków.
- Ikona lupy jako przycisk wysyłania + obsługa Enter.
- Tolerancja literówek, synonimów, sugestie (autocomplete), czytelna strona braku wyników z podpowiedziami.

**Źródła:** NN/g, *Search: Visible and Simple* – https://www.nngroup.com/articles/search-visible-and-simple/ ; NN/g, *The Magnifying-Glass Icon in Search Design* – https://www.nngroup.com/articles/magnifying-glass-icon/ ; Baymard Institute, *E-Commerce Search Usability* – https://baymard.com/research/ecommerce-search

---

## Linki

### NAW-11 Linki rozpoznawalne i opisowe
- Linki w treści wyróżnione podkreśleniem (konwencja) i kolorem; odwiedzone linki mogą mieć inny kolor.
- Tekst linku opisuje cel (DOST-34); długość linku pozwala przewidzieć, dokąd prowadzi.
- Nie stosuj podkreślenia dla tekstu, który nie jest linkiem.

**Źródła:** NN/g, *Guidelines for Visualizing Links* – https://www.nngroup.com/articles/guidelines-for-visualizing-links/ ; WCAG SC 1.4.1 – https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html

### NAW-12 Linki do plików i otwieranie w nowym oknie
- Linki do plików wskazują typ i rozmiar: „Raport roczny (PDF, 2,4 MB)”.
- Domyślnie otwieraj linki w tym samym oknie; jeśli otwierasz nowe okno/kartę – uprzedź o tym (tekst lub ikona z alternatywą tekstową).

**Źródła:** NN/g, *Opening Links in New Browser Windows and Tabs* – https://www.nngroup.com/articles/new-browser-windows-and-tabs/ ; technika WCAG G201 – https://www.w3.org/WAI/WCAG22/Techniques/general/G201

---

## Strony błędów i stany puste

### NAW-13 Strona 404
Dobra strona 404: jasno komunikuje, że strony nie znaleziono (bez żargonu), zachowuje nagłówek i nawigację serwisu, oferuje wyszukiwarkę i linki do popularnych sekcji, zwraca poprawny kod HTTP 404 (nie „soft 404” z kodem 200).

**Źródła:** NN/g, *Improving the Dreaded 404 Error Message* – https://www.nngroup.com/articles/improving-dreaded-404-error-message/ ; Google Search Central, *Soft 404 errors* – https://developers.google.com/search/docs/crawling-indexing/http-network-errors#soft-404-errors

### NAW-14 Paginacja vs. nieskończone przewijanie vs. „Załaduj więcej”
- **Nieskończone przewijanie** – dobre dla treści do swobodnego przeglądania (feedy); złe, gdy użytkownik szuka konkretnej pozycji, porównuje lub potrzebuje stopki. Utrudnia powrót do pozycji i dostęp do stopki.
- **„Załaduj więcej”** – kompromis rekomendowany przez Baymard dla list produktów.
- **Paginacja** – dobra dla zadań zorientowanych na cel i wyników wyszukiwania.
Niezależnie od wzorca: zachowaj pozycję po powrocie przyciskiem „Wstecz”.

**Źródła:** NN/g, *Infinite Scrolling: When to Use It, When to Avoid It* – https://www.nngroup.com/articles/infinite-scrolling-tips/ ; Baymard Institute, *Product List UX* – https://baymard.com/blog/load-more-and-infinite-scrolling

