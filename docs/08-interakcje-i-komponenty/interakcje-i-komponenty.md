# 08. Interakcje, komponenty i informacja zwrotna

> **Zakres:** przyciski, stany komponentów, modale, karuzele, powiadomienia, animacje, potwierdzenia.
> **Prefiks ID:** `INT`

[← Powrót do README](../../README.md)

---

## INT-01 Przyciski wyglądają na klikalne
Elementy interaktywne muszą mieć wyraźne wskazówki afordancji (kształt przycisku, kontrast, podkreślenie linku). Płaskie interfejsy bez takich wskazówek wydłużają czas wykonania zadań i zwiększają niepewność użytkowników (badanie NN/g: „flat” linki/przyciski wymagały więcej czasu i fiksacji wzroku).

**Źródła:** NN/g, *Flat UI Elements Attract Less Attention and Cause Uncertainty* – https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/ ; NN/g, *Beyond Blue Links: Making Clickable Elements Recognizable* – https://www.nngroup.com/articles/clickable-elements/

## INT-02 Hierarchia przycisków
Na ekranie/sekcji jedna główna akcja (przycisk wypełniony, kontrastowy), akcje drugorzędne mniej wyróżnione (obrys/tekst). Nie stosuj kilku równorzędnie wyróżnionych przycisków obok siebie.

**Źródła:** Material Design 3, *Buttons – Choosing buttons* – https://m3.material.io/components/all-buttons ; GOV.UK Design System, *Button – secondary buttons* – https://design-system.service.gov.uk/components/button/

## INT-03 Kompletne stany komponentów
Każdy element interaktywny ma zaprojektowane stany: domyślny, hover, fokus (widoczny!), aktywny/wciśnięty, nieaktywny, ładowanie, błąd, sukces. Stan nie może być sygnalizowany wyłącznie kolorem (DOST-16), a kontrast stanów ≥ 3:1 (DOST-18).

**Źródła:** Material Design 3, *States* – https://m3.material.io/foundations/interaction/states/overview ; WCAG SC 1.4.11 – https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html

## INT-04 Natychmiastowa informacja zwrotna
Każda akcja użytkownika otrzymuje reakcję: zmiana stanu przycisku po kliknięciu, potwierdzenie dodania do koszyka, licznik koszyka. Komunikaty statusu dostępne dla czytników ekranu (DOST-47). Zob. progi czasu POD-17 i POD-18.

**Źródła:** NN/g, *Visibility of System Status* – https://www.nngroup.com/articles/visibility-system-status/ ; WCAG SC 4.1.3 – https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html

## INT-05 Potwierdzaj tylko akcje destrukcyjne – lub oferuj „Cofnij”
Okna potwierdzenia stosuj oszczędnie, tylko dla akcji poważnych i nieodwracalnych (inaczej użytkownicy klikają je odruchowo). Lepszą alternatywą jest często możliwość cofnięcia (np. „Usunięto wiadomość. Cofnij”).

**Źródło:** NN/g, *Confirmation Dialogs Can Prevent User Errors (If Not Overused)* – https://www.nngroup.com/articles/confirmation-dialog/

## INT-06 Okna modalne – używaj z umiarem i poprawnie
- Stosuj modale do krótkich, ważnych zadań wymagających uwagi; nie do treści, którą użytkownik chce porównać ze stroną.
- Nie otwieraj modali bez akcji użytkownika (np. zaraz po wejściu).
- Zawsze widoczny przycisk zamknięcia, zamknięcie klawiszem Esc, fokus przenoszony do modala i uwięziony w nim do czasu zamknięcia, potem przywracany (DOST-26). Natywny `<dialog>` + `showModal()` zapewnia większość zachowań.

**Źródła:** NN/g, *Modal & Nonmodal Dialogs: When (& When Not) to Use Them* – https://www.nngroup.com/articles/modal-nonmodal-dialog/ ; WAI-ARIA APG, *Dialog (Modal) Pattern* – https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

## INT-07 Karuzele – unikaj automatycznego przewijania
Automatycznie przewijane karuzele: użytkownicy często je ignorują („ślepota banerowa”), slajdy zmieniają się zanim zostaną przeczytane, a ruch rozprasza. Jeśli karuzela jest konieczna: brak autoodtwarzania (lub przycisk pauzy – wymóg WCAG 2.2.2 dla ruchu > 5 s), widoczne kontrolki, wskaźnik liczby slajdów, obsługa klawiatury, najważniejsza treść na pierwszym slajdzie.

**Źródła:** NN/g, *Auto-Forwarding Carousels and Accordions Annoy Users and Reduce Visibility* – https://www.nngroup.com/articles/auto-forwarding/ ; W3C WAI, *Carousels Tutorial* – https://www.w3.org/WAI/tutorials/carousels/ ; WAI-ARIA APG, *Carousel Pattern* – https://www.w3.org/WAI/ARIA/apg/patterns/carousel/

## INT-08 Akordeony i ujawnianie progresywne
Ujawnianie progresywne (progressive disclosure): pokazuj najważniejsze opcje, zaawansowane – na żądanie. Akordeony są dobre dla długich treści referencyjnych na mobile (FAQ), ale nie ukrywaj w nich treści, której potrzebuje większość użytkowników. Przycisk nagłówka z `aria-expanded`.

**Źródła:** NN/g, *Progressive Disclosure* – https://www.nngroup.com/articles/progressive-disclosure/ ; NN/g, *Accordions on Desktop: When and How to Use* – https://www.nngroup.com/articles/accordions-on-desktop/ ; WAI-ARIA APG, *Accordion Pattern* – https://www.w3.org/WAI/ARIA/apg/patterns/accordion/

## INT-09 Powiadomienia typu toast/snackbar
Krótkie, niekrytyczne komunikaty; nie umieszczaj w nich jedynej drogi do ważnej akcji ani informacji o błędach wymagających działania. Jeśli zawierają akcję – nie znikają automatycznie zbyt szybko (WCAG 2.2.1), ogłaszane przez `role="status"`.

**Źródła:** Material Design 3, *Snackbar* – https://m3.material.io/components/snackbar/guidelines ; WCAG SC 2.2.1 – https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html ; SC 4.1.3 – https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html

## INT-10 Animacje: funkcjonalne, krótkie, wyłączalne
- Animacja powinna mieć cel (wyjaśnia zmianę stanu, kierunek, relację), a nie tylko ozdabiać.
- Typowe czasy mikrointerakcji: ok. 100–500 ms (NN/g: zwykle 200–500 ms dla przejść interfejsu; krótsze dla małych elementów).
- Respektuj `prefers-reduced-motion` (DOST-32), unikaj błysków (DOST-31).

**Źródła:** NN/g, *Executing UX Animations: Duration and Motion Characteristics* – https://www.nngroup.com/articles/animation-duration/ ; Material Design 3, *Motion – Easing and duration* – https://m3.material.io/styles/motion/easing-and-duration/applying-easing-and-duration

## INT-11 Ikony z etykietami tekstowymi
Poza nielicznymi uniwersalnymi ikonami (lupa, dom, drukarka) znaczenie ikon jest niejednoznaczne – dodawaj widoczne etykiety tekstowe. Ikony bez tekstu wymagają nazwy dostępnej (ARIA-05) i najlepiej podpowiedzi.

**Źródło:** NN/g, *Icon Usability* – https://www.nngroup.com/articles/icon-usability/

## INT-12 Stany puste
Pusty koszyk, brak wyników, brak danych w panelu – wyjaśnij, dlaczego jest pusto, i zaproponuj następny krok (CTA, sugestie). Nie zostawiaj pustego ekranu.

**Źródło:** NN/g, *Designing Empty States in Complex Applications: 3 Guidelines* – https://www.nngroup.com/articles/empty-state-interface-design/

