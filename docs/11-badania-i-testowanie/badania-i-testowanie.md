# 11. Badania i testowanie UX

> **Zakres:** metody badawcze, testy użyteczności, metryki, testy dostępności.
> **Prefiks ID:** `BAD`

[← Powrót do README](../../README.md)

---

## Dobór metod

### BAD-01 Dobieraj metodę do pytania badawczego
Metody różnią się w trzech wymiarach: **postawy vs. zachowania** (co ludzie mówią vs. co robią), **jakościowe vs. ilościowe** (dlaczego vs. ile), **kontekst użycia**. Przykładowo: wywiady i ankiety → postawy; testy użyteczności, analityka, testy A/B → zachowania.

**Źródło:** C. Rohrer, *When to Use Which User-Experience Research Methods*, NN/g – https://www.nngroup.com/articles/which-ux-research-methods/

### BAD-02 Testy użyteczności – małe, częste, iteracyjne
Badania jakościowe: ok. **5 uczestników** z danej grupy użytkowników pozwala wykryć większość (wg modelu ok. 85%) problemów – lepiej przeprowadzić kilka rund po 5 osób między iteracjami niż jedną dużą. Zasada **nie dotyczy** badań ilościowych (benchmarki, metryki – zwykle min. ok. 40 uczestników) ani sytuacji z kilkoma odrębnymi grupami użytkowników.

**Źródła:** J. Nielsen (2000), *Why You Only Need to Test with 5 Users* – https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ ; J. Nielsen, T. K. Landauer (1993), *A mathematical model of the finding of usability problems*, INTERCHI ’93, 206–213. https://doi.org/10.1145/169059.169166 ; NN/g, *How Many Participants for Quantitative Usability Studies* – https://www.nngroup.com/articles/summary-quant-sample-sizes/

### BAD-03 Ocena heurystyczna
3–5 ewaluatorów niezależnie ocenia interfejs wg heurystyk (POD-03–POD-12), potem wyniki są łączone i oceniane pod kątem dotkliwości. Jeden ewaluator wykrywa średnio ok. 35% problemów. Ocena ekspercka **uzupełnia**, ale nie zastępuje testów z użytkownikami.

**Źródło:** J. Nielsen, *How to Conduct a Heuristic Evaluation* – https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/

### BAD-04 Zasady prowadzenia testu
Realistyczne scenariusze zadań bez podpowiadania słów z interfejsu; metoda głośnego myślenia (think-aloud); moderator nie pomaga i nie ocenia; obserwuj zachowanie, a nie tylko opinie; rekrutuj uczestników reprezentatywnych – w tym osoby z niepełnosprawnościami.

**Źródła:** NN/g, *Thinking Aloud: The #1 Usability Tool* – https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/ ; NN/g, *Write Better Qualitative Usability Tasks: Top 10 Mistakes to Avoid* – https://www.nngroup.com/articles/better-usability-tasks/ ; W3C WAI, *Involving Users in Evaluating Web Accessibility* – https://www.w3.org/WAI/test-evaluate/involving-users/

---

## Metryki

### BAD-05 Metryki użyteczności
- **Skuteczność:** odsetek ukończonych zadań, liczba błędów.
- **Efektywność:** czas wykonania zadania, liczba kroków.
- **Satysfakcja:** SUS, SEQ (Single Ease Question – 7-stopniowa skala po każdym zadaniu).
(Zgodnie z definicją ISO 9241-11 – POD-01.)

**Źródła:** ISO 9241-11:2018 – https://www.iso.org/standard/63500.html ; J. Sauro, *10 Things to Know About the Single Ease Question (SEQ)*, MeasuringU – https://measuringu.com/seq10/

### BAD-06 System Usability Scale (SUS)
Kwestionariusz 10 pytań (skala 1–5, pytania naprzemiennie pozytywne i negatywne) opracowany przez J. Brooke’a (1986). Wynik 0–100 (to **nie** procent). Średni wynik w benchmarkach wynosi ok. **68**; wynik powyżej 68 oznacza użyteczność powyżej przeciętnej.

**Źródła:** J. Brooke (1996), *SUS: A „quick and dirty” usability scale*, w: Usability Evaluation in Industry, Taylor & Francis ; J. Brooke (2013), *SUS: A Retrospective*, Journal of Usability Studies 8(2), 29–40 – https://uxpajournal.org/sus-a-retrospective/ ; J. Sauro, *Measuring Usability with the System Usability Scale (SUS)*, MeasuringU – https://measuringu.com/sus/

### BAD-07 Testy A/B – zasady wiarygodności
Ustal hipotezę i metrykę główną przed startem; oblicz wymaganą wielkość próby; nie kończ testu przy pierwszym „istotnym” wyniku (problem podglądania – *peeking*); testuj pełne cykle tygodniowe; uważaj na wielokrotne porównania. Testy A/B mówią **co** działa, nie **dlaczego** – łącz z badaniami jakościowymi.

**Źródła:** R. Kohavi, D. Tang, Y. Xu (2020), *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*, Cambridge University Press. https://doi.org/10.1017/9781108653985 ; NN/g, *A/B Testing 101* – https://www.nngroup.com/articles/ab-testing/

---

## Testowanie dostępności

### BAD-08 Łącz testy automatyczne, ręczne i z użytkownikami
- **Automatyczne** (axe DevTools, WAVE, Lighthouse, Pa11y) – szybkie, ale wykrywają tylko część problemów (badanie GDS na stronie z celowo wprowadzonymi błędami: najlepsze narzędzie wykryło ok. 40% błędów; Deque szacuje, że automaty wykrywają ok. 57% *wystąpień* problemów w typowych audytach).
- **Ręczne:** obsługa klawiaturą, zoom 200%/400%, czytniki ekranu (NVDA, JAWS, VoiceOver, TalkBack), wyłączenie CSS/obrazów, sprawdzenie tekstów alternatywnych i kolejności czytania.
- **Z użytkownikami** z niepełnosprawnościami.

**Źródła:**
- GDS, *What we found when we tested tools on the world's least-accessible webpage* (2017) – https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/
- Deque, *Automated Testing Study Identifies 57 Percent of Digital Accessibility Issues* (2021) – https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues/
- W3C WAI, *Easy Checks – A First Review of Web Accessibility* – https://www.w3.org/WAI/test-evaluate/preliminary/
- W3C WAI, *Web Accessibility Evaluation Tools List* – https://www.w3.org/WAI/test-evaluate/tools/list/

### BAD-09 Metodologia audytu WCAG-EM
Formalna ocena zgodności: (1) określenie zakresu, (2) eksploracja serwisu, (3) wybór reprezentatywnej próbki stron (w tym kompletne procesy), (4) audyt próbki, (5) raport z wynikami. Narzędzie: WCAG-EM Report Tool.

**Źródła:** W3C, *Website Accessibility Conformance Evaluation Methodology (WCAG-EM) 1.0* – https://www.w3.org/TR/WCAG-EM/ ; *WCAG-EM Report Tool* – https://www.w3.org/WAI/eval/report-tool/

### BAD-10 Ciągłość: dostępność i UX w procesie, nie jednorazowo
Wbuduj kontrole w proces: kryteria akceptacji w zadaniach, testy automatyczne w CI (np. axe-core), przegląd projektu pod kątem dostępności przed wdrożeniem, regularne audyty po zmianach.

**Źródła:** W3C WAI, *Planning and Managing Web Accessibility* – https://www.w3.org/WAI/planning-and-managing/ ; Deque, *axe-core* – https://github.com/dequelabs/axe-core

