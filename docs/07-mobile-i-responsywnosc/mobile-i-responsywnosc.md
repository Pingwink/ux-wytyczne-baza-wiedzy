# 07. Urządzenia mobilne i responsywność

> **Zakres:** projektowanie responsywne, obszary dotyku, ergonomia ekranów dotykowych.
> **Prefiks ID:** `MOB`

[← Powrót do README](../../README.md)

---

## MOB-01 Poprawny meta viewport
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
Nie blokuj powiększania (`user-scalable=no`, `maximum-scale=1`) – narusza to potrzeby osób słabowidzących (WCAG 1.4.4) i jest zgłaszane przez Lighthouse.

**Źródła:** MDN, *Viewport meta tag* – https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag ; Chrome Developers, *Lighthouse: user-scalable="no" is used...* – https://developer.chrome.com/docs/lighthouse/accessibility/meta-viewport

## MOB-02 Projektowanie responsywne i mobile-first
- Jedna treść, układ dostosowany do szerokości (siatki płynne, `flex`/`grid`, zapytania medialne i kontenerowe).
- Punkty przełamania dobieraj do treści, nie do konkretnych urządzeń.
- Zachowaj parytet treści i funkcji między wersjami – Google stosuje indeksowanie mobile-first (wersja mobilna jest podstawą indeksowania).
- Strona musi działać przy szerokości 320 px CSS (WCAG 1.4.10, DOST-20).

**Źródła:** web.dev, *Learn Responsive Design* – https://web.dev/learn/design ; Google Search Central, *Mobile-first indexing best practices* – https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing ; L. Wroblewski (2011), *Mobile First*, A Book Apart

## MOB-03 Rozmiar obszarów dotyku
| Źródło | Minimalny rozmiar |
|---|---|
| WCAG 2.2 SC 2.5.8 (AA) – wymóg | 24 × 24 px CSS (lub odpowiedni odstęp) |
| WCAG 2.2 SC 2.5.5 (AAA) | 44 × 44 px CSS |
| Apple Human Interface Guidelines | 44 × 44 pt |
| Material Design (Google) | 48 × 48 dp (ok. 9 mm), odstęp min. 8 dp |

**Rekomendacja bazy:** projektuj główne elementy dotykowe na **co najmniej 44–48 px**, a 24 px traktuj jako twarde minimum zgodności. Obszar dotyku może być większy niż widoczna ikona (padding).

**Źródła:** WCAG – https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; Apple HIG, *Accessibility* – https://developer.apple.com/design/human-interface-guidelines/accessibility ; Material Design 3, *Accessibility – Structure (Touch and pointer targets)* – https://m3.material.io/foundations/designing/structure ; Material Design (M2), *Accessibility – Layout and typography* – https://m2.material.io/design/usability/accessibility.html#layout-and-typography ; Material Design (M2), *Touch targets* – https://m2.material.io/develop/web/supporting/touch-target

## MOB-04 Strefy kciuka i sposób trzymania telefonu
Badanie obserwacyjne S. Hoobera (1333 obserwacje, 2013) wykazało, że użytkownicy trzymają telefon na różne sposoby: ok. 49% jedną ręką, 36% oburącz z kciukiem jednej ręki (cradled), 15% oburącz z dwoma kciukami – i często zmieniają chwyt. Środek ekranu jest najłatwiej dostępny i najdokładniej trafiany; rogi – najtrudniej. **Wniosek:** kluczowe akcje umieszczaj w łatwo dostępnych strefach (dolna/środkowa część), destrukcyjne akcje – z dala od częstych akcji.

**Źródła:** S. Hoober (2013), *How Do Users Really Hold Mobile Devices?*, UXmatters – https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php ; S. Hoober (2017), *Design for Fingers, Touch, and People, Part 1*, UXmatters – https://www.uxmatters.com/mt/archives/2017/03/design-for-fingers-touch-and-people-part-1.php

## MOB-05 Hover nie istnieje na dotyku
Nie ukrywaj kluczowych informacji ani akcji wyłącznie za stanem `:hover`. Używaj zapytań `@media (hover: hover)` i `(pointer: coarse)` do dostosowania interakcji.

**Źródła:** MDN, *@media hover* – https://developer.mozilla.org/en-US/docs/Web/CSS/@media/hover ; MDN, *@media pointer* – https://developer.mozilla.org/en-US/docs/Web/CSS/@media/pointer

## MOB-06 Natrętne okna na mobile
Pełnoekranowe interstitiale i pop-upy zasłaniające treść zaraz po wejściu z wyszukiwarki pogarszają doświadczenie; Google wskazuje je jako negatywny sygnał doświadczenia strony. Wyjątki: wymagane prawnie (np. weryfikacja wieku, zgoda na cookies) i rozsądnie małe banery.

**Źródło:** Google Search Central, *Avoid intrusive interstitials and dialogs* – https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials

## MOB-07 Orientacja i bezpieczne obszary
Obsługuj obie orientacje (WCAG 1.3.4); w urządzeniach z wycięciami ekranu stosuj `env(safe-area-inset-*)` i `viewport-fit=cover`, by treść nie była zasłaniana.

**Źródła:** WCAG SC 1.3.4 – https://www.w3.org/WAI/WCAG22/Understanding/orientation.html ; MDN, *env()* – https://developer.mozilla.org/en-US/docs/Web/CSS/env

