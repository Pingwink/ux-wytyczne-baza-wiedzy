# 02d. Dostępność: semantyczny HTML i WAI-ARIA

> **Zakres:** zasady stosowania natywnej semantyki HTML i atrybutów ARIA przy budowie komponentów.
> **Prefiks ID:** `ARIA`

[← Powrót do README](../../README.md)

---

## ARIA-01 Pierwsza zasada ARIA: najpierw natywny HTML
Jeśli możesz użyć natywnego elementu HTML lub atrybutu z wbudowaną semantyką i zachowaniem – zrób to, zamiast nadawać rolę ARIA innemu elementowi. `<button>` zamiast `<div role="button" tabindex="0">`; `<a href>` dla nawigacji, `<button>` dla akcji.

**Źródło:** W3C, *Using ARIA* – „First Rule of ARIA Use” – https://www.w3.org/TR/using-aria/#rule1

## ARIA-02 Nie zmieniaj natywnej semantyki bez potrzeby
Nie nadpisuj ról natywnych elementów (np. `<h2 role="tab">` – lepiej `<div role="tab"><h2>…</h2></div>`).

**Źródło:** W3C, *Using ARIA* – Second Rule – https://www.w3.org/TR/using-aria/#2ndrule

## ARIA-03 Interaktywne kontrolki ARIA muszą działać z klawiatury
Każdy element z interaktywną rolą ARIA musi być fokusowalny i obsługiwalny klawiaturą zgodnie z wzorcem (np. Enter i Spacja dla przycisku).

**Źródło:** W3C, *Using ARIA* – Third Rule – https://www.w3.org/TR/using-aria/#3rdrule

## ARIA-04 Nie ukrywaj elementów fokusowalnych
Nie stosuj `role="presentation"` ani `aria-hidden="true"` na elementach, które mogą otrzymać fokus.

**Źródło:** W3C, *Using ARIA* – Fourth Rule – https://www.w3.org/TR/using-aria/#4thrule

## ARIA-05 Każdy element interaktywny ma nazwę dostępną
Np. przycisk-ikona: `<button aria-label="Zamknij">` lub ukryty wizualnie tekst. Pola formularzy: `<label for>`.

**Źródła:** W3C, *Using ARIA* – Fifth Rule – https://www.w3.org/TR/using-aria/#fifthrule ; *Accessible Name and Description Computation 1.2* – https://www.w3.org/TR/accname-1.2/

## ARIA-06 „Brak ARIA jest lepszy niż zła ARIA”
Błędnie użyta ARIA pogarsza dostępność. Dane WebAIM Million pokazują, że strony z ARIA mają średnio **więcej** wykrytych błędów niż strony bez ARIA (korelacja, nie przyczynowość – ARIA występuje częściej na złożonych stronach).

**Źródła:** W3C WAI-ARIA APG, *Read Me First* – https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/ ; WebAIM Million – https://webaim.org/projects/million/

## ARIA-07 Regiony (landmarks)
Używaj elementów `<header>`, `<nav>`, `<main>` (jeden na stronę), `<aside>`, `<footer>`, `<form>`/`<search>` z nazwą. Gdy ten sam typ regionu występuje wielokrotnie (np. dwa `<nav>`), nadaj im różne etykiety (`aria-label="Główne"`, `aria-label="Stopka"`). Cała treść powinna znajdować się w regionach.

**Źródło:** W3C WAI-ARIA APG, *Landmark Regions* – https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/

## ARIA-08 Wzorce komponentów (APG)
Dla złożonych widżetów (akordeon, zakładki, menu rozwijane, combobox, modal, karuzela, drzewo) stosuj role, stany i obsługę klawiatury opisaną w *ARIA Authoring Practices Guide*. Przykład – zakładki: `role="tablist"`, `role="tab"` z `aria-selected` i `aria-controls`, `role="tabpanel"`; strzałki przełączają zakładki, Tab przenosi do panelu.

> [!NOTE]
> Przykłady APG demonstrują wzorce, ale nie zawsze są testowane ze wszystkimi czytnikami ekranu – sprawdzaj tabelę wsparcia przy każdym wzorcu.

**Źródło:** W3C WAI-ARIA APG, *Patterns* – https://www.w3.org/WAI/ARIA/apg/patterns/

## ARIA-09 Elementy natywne warte użycia
- `<dialog>` z `showModal()` – natywny modal z obsługą Esc i zarządzaniem fokusem (`inert` dla tła).
- `<details>/<summary>` – natywny akordeon/ujawnianie.
- `<fieldset>/<legend>` – grupy przycisków radio i checkboxów.
- `<table>` z `<caption>`, `<th scope>` – tabele danych (nigdy do układu strony).

**Źródła:** MDN, `<dialog>` – https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog ; MDN, `<details>` – https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details ; W3C WAI, *Tables Tutorial* – https://www.w3.org/WAI/tutorials/tables/

