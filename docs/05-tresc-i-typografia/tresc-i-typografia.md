# 05. Treść, czytelność i typografia

> **Zakres:** pisanie dla sieci, prosty język, struktura tekstu, typografia (rozmiar, interlinia, długość wiersza).
> **Prefiks ID:** `TRE` (treść), `TYP` (typografia)

[← Powrót do README](../../README.md)

---

## Jak użytkownicy czytają w sieci

### TRE-01 Użytkownicy skanują, a nie czytają
Badania NN/g (1997) wykazały, że 79% badanych skanowało nowe strony, a tylko 16% czytało słowo po słowie. Badania eyetrackingowe pokazują wzorce skanowania (np. wzorzec F), które pojawiają się, gdy tekst nie ma wyraźnej struktury. **Wniosek:** projektuj tekst pod skanowanie (TRE-02–TRE-05).

**Źródła:** J. Nielsen (1997), *How Users Read on the Web* – https://www.nngroup.com/articles/how-users-read-on-the-web/ ; K. Pernice (2017), *F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant* – https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/

### TRE-02 Odwrócona piramida
Zaczynaj od najważniejszej informacji (wniosek, odpowiedź, akcja), potem szczegóły, na końcu tło. Pierwsze zdanie akapitu i pierwsze słowa nagłówka niosą kluczową treść.

**Źródło:** NN/g, *Inverted Pyramid: Writing for Comprehension* – https://www.nngroup.com/articles/inverted-pyramid/

### TRE-03 Struktura ułatwiająca skanowanie
- Opisowe nagłówki i śródtytuły (nie „Wstęp”, „Inne”).
- Krótkie akapity (jedna myśl na akapit).
- Listy punktowane dla wyliczeń, numerowane dla kroków.
- Pogrubienie wyłącznie kluczowych fraz (nadużycie niweluje efekt).
- Tabele dla danych porównawczych.

**Źródła:** NN/g, *How to Write for the Web* (seria) – https://www.nngroup.com/topic/writing-web/ ; GOV.UK, *Content design: planning, writing and managing content* – https://www.gov.uk/guidance/content-design/writing-for-gov-uk

---

## Prosty język

### TRE-04 Pisz prostym językiem
Norma ISO 24495-1:2023 definiuje prosty język przez cztery zasady: komunikat jest napisany prostym językiem, jeśli jego odbiorcy otrzymują informacje **trafne** (których potrzebują) oraz mogą łatwo **znaleźć** potrzebne informacje, **zrozumieć** je i **wykorzystać**. Praktyki:
- Krótkie zdania (wytyczne GOV.UK: średnio do ok. 25 słów; polskie poradniki prostego języka – do ok. 20 słów).
- Strona czynna zamiast biernej, czasowniki zamiast rzeczowników odczasownikowych („złóż wniosek” zamiast „dokonaj złożenia wniosku”).
- Zwracaj się bezpośrednio do odbiorcy („Ty”/„Pan/Pani” konsekwentnie).
- Wyjaśniaj lub unikaj żargonu, skrótów, terminów specjalistycznych.

**Źródła:**
- ISO 24495-1:2023 *Plain language — Part 1: Governing principles and guidelines* – https://www.iso.org/standard/78907.html
- GOV.UK, *Writing for GOV.UK* – https://www.gov.uk/guidance/content-design/writing-for-gov-uk
- Pracownia Prostej Polszczyzny, Uniwersytet Wrocławski – https://prostapolszczyzna.uwr.edu.pl/ (dawniej: http://www.ppp.uni.wroc.pl/)
- Służba Cywilna (gov.pl), *Prosty język w służbie cywilnej* – https://www.gov.pl/web/sluzbacywilna/prosty-jezyk ; Ministerstwo Funduszy i Polityki Regionalnej, *Prosty język* – https://www.funduszeeuropejskie.gov.pl/strony/o-funduszach/fundusze-europejskie-bez-barier/prosty-jezyk/

### TRE-05 Tekst przycisków i mikrocopy
Etykiety przycisków opisują akcję i jej wynik czasownikiem („Zapisz zmiany”, „Pobierz fakturę”), nie ogólnikami („OK”, „Wyślij” bez kontekstu). W oknach potwierdzenia przyciski powtarzają akcję („Usuń konto” / „Anuluj”), a nie „Tak/Nie”.

**Źródła:** NN/g, *OK–Cancel or Cancel–OK? The Trouble With Buttons* – https://www.nngroup.com/articles/ok-cancel-or-cancel-ok/ ; NN/g, *Confirmation Dialogs Can Prevent User Errors* – https://www.nngroup.com/articles/confirmation-dialog/ ; Material Design 3, *Dialogs* – https://m3.material.io/components/dialogs/guidelines

---

## Typografia

### TYP-01 Rozmiar tekstu podstawowego
- Ustaw domyślny rozmiar tekstu treści w jednostkach względnych (`rem`), bazując na ustawieniu przeglądarki (domyślnie 16 px) – nie nadpisuj go mniejszą wartością w px.
- Powszechna praktyka: tekst treści **nie mniejszy niż 16 px CSS**. Lighthouse oznacza problem, gdy ponad 40% tekstu ma rozmiar poniżej 12 px (audyt „Document doesn't use legible font sizes”).
- Na iOS pola formularzy z czcionką mniejszą niż 16 px powodują automatyczne powiększanie strony przy fokusie.

**Źródła:** Chrome Developers, *Lighthouse: Document doesn't use legible font sizes* – https://developer.chrome.com/docs/lighthouse/seo/font-size ; M. Butterick, *Practical Typography – Point size* – https://practicaltypography.com/point-size.html ; WCAG SC 1.4.4 – https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html

### TYP-02 Długość wiersza
- Optymalnie ok. **50–75 znaków** na wiersz (ze spacjami) dla tekstu ciągłego.
- WCAG SC 1.4.8 (AAA): szerokość bloku tekstu **nie więcej niż 80 znaków** (40 dla znaków CJK).
- W CSS: np. `max-width: 70ch` dla kontenera tekstu.

**Źródła:** Baymard Institute, *Readability: The Optimal Line Length* – https://baymard.com/blog/line-length-readability ; R. Bringhurst, *The Elements of Typographic Style* (45–75 znaków jako zakres zadowalający, 66 jako ideał) ; WCAG SC 1.4.8 – https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html

### TYP-03 Interlinia i odstępy
- Wysokość linii dla tekstu ciągłego: **co najmniej 1,5** (WCAG 1.4.8 AAA); nagłówki mogą mieć mniejszą (np. 1,1–1,3).
- Odstęp między akapitami większy niż interlinia (WCAG 1.4.8: co najmniej 1,5× odstępu między wierszami).
- Treść musi wytrzymać zwiększenie odstępów przez użytkownika (DOST-21).

**Źródło:** WCAG SC 1.4.8 Visual Presentation – https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html ; SC 1.4.12 – https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html

### TYP-04 Wyrównanie tekstu
Wyrównuj tekst ciągły do lewej (w językach LTR). **Unikaj justowania** – nierówne odstępy między słowami („rzeki”) utrudniają czytanie, zwłaszcza osobom z dysleksją (WCAG 1.4.8 AAA: tekst nie jest wyjustowany). Unikaj długich bloków tekstu wyśrodkowanego.

**Źródła:** WCAG SC 1.4.8 – https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html ; British Dyslexia Association, *Dyslexia Style Guide* – https://www.bdadyslexia.org.uk/advice/employers/creating-a-dyslexia-friendly-workplace/dyslexia-friendly-style-guide

### TYP-05 Hierarchia typograficzna
Zbuduj ograniczoną, spójną skalę rozmiarów (np. 5–7 stopni), różnicuj poziomy nagłówków rozmiarem i grubością tak, by hierarchia była czytelna bez czytania treści. Ogranicz liczbę krojów (zwykle 1–2 rodziny). Unikaj długich fragmentów WIELKIMI LITERAMI i kursywą.

**Źródła:** Material Design 3, *Typography – Type scale* – https://m3.material.io/styles/typography/type-scale-tokens ; British Dyslexia Association, *Dyslexia Style Guide* (j.w.) ; M. Butterick, *Practical Typography – All caps* – https://practicaltypography.com/all-caps.html

### TYP-06 Ładowanie fontów webowych
Stosuj `font-display: swap` (lub `optional`), ładuj tylko potrzebne odmiany i podzbiory znaków (w tym polskie znaki diakrytyczne!), preferuj format WOFF2, rozważ `preload` dla kluczowego fontu – zapobiega niewidocznemu tekstowi (FOIT) i przesunięciom układu.

**Źródło:** web.dev, *Best practices for fonts* – https://web.dev/articles/font-best-practices

