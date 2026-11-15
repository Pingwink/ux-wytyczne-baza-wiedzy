# 01. Podstawy: heurystyki, normy i prawa UX

> **Zakres:** fundamenty teoretyczne, na których opierają się wytyczne z pozostałych rozdziałów.
> **Prefiks ID:** `POD`

[← Powrót do README](../../README.md)

---

## Definicje bazowe

### POD-01 Definicja użyteczności (ISO 9241-11)
Użyteczność to *„stopień, w jakim system, produkt lub usługa mogą być używane przez określonych użytkowników do osiągnięcia określonych celów ze skutecznością, efektywnością i satysfakcją w określonym kontekście użycia”*.

- **Skuteczność** – czy użytkownik osiąga cel (np. odsetek ukończonych zadań).
- **Efektywność** – zasoby zużyte do osiągnięcia celu (czas, liczba kroków).
- **Satysfakcja** – subiektywna ocena (np. kwestionariusz SUS).

**Źródło:** ISO 9241-11:2018 *Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts* – https://www.iso.org/standard/63500.html

### POD-02 Projektowanie zorientowane na człowieka (ISO 9241-210)
Norma opisuje cykl: (1) zrozumienie i określenie kontekstu użycia, (2) określenie wymagań użytkowników, (3) tworzenie rozwiązań projektowych, (4) ewaluacja rozwiązań względem wymagań – powtarzany iteracyjnie. Zasady: projekt oparty na jawnym zrozumieniu użytkowników, zadań i środowisk; angażowanie użytkowników przez cały proces; projekt napędzany i doskonalony ewaluacją; iteracyjność; uwzględnianie całego doświadczenia użytkownika; interdyscyplinarny zespół.

**Źródło:** ISO 9241-210:2019 *Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems* – https://www.iso.org/standard/77520.html

---

## 10 heurystyk użyteczności Jakoba Nielsena

Heurystyki opublikowane przez J. Nielsena w 1994 r. (opis zaktualizowany przez Nielsen Norman Group w 2020 r.; same zasady się nie zmieniły). Stosowane m.in. w ocenie heurystycznej (zob. [BAD-03](../11-badania-i-testowanie/badania-i-testowanie.md)).

**Źródło dla całej sekcji:** J. Nielsen, *10 Usability Heuristics for User Interface Design*, Nielsen Norman Group – https://www.nngroup.com/articles/ten-usability-heuristics/

| ID | Heurystyka | Co oznacza w praktyce na stronie WWW |
|----|-----------|--------------------------------------|
| POD-03 | **Widoczność stanu systemu** | Informuj o tym, co się dzieje: wskaźniki ładowania, potwierdzenie dodania do koszyka, oznaczenie aktywnej pozycji menu, postęp w wieloetapowym formularzu. |
| POD-04 | **Zgodność systemu z rzeczywistością** | Mów językiem użytkownika, nie żargonem firmowym; stosuj znane konwencje i logiczną kolejność informacji. |
| POD-05 | **Kontrola i swoboda użytkownika** | Zapewnij „wyjście awaryjne”: cofnij, anuluj, zamknij modal, edytuj zamówienie przed zatwierdzeniem. |
| POD-06 | **Spójność i standardy** | Spójność wewnętrzna (te same elementy wyglądają i działają tak samo) i zewnętrzna (konwencje branżowe, np. logo w lewym górnym rogu prowadzi do strony głównej). |
| POD-07 | **Zapobieganie błędom** | Lepiej zapobiegać niż komunikować błędy: ograniczenia w polach, wartości domyślne, potwierdzenie przed nieodwracalnymi akcjami. |
| POD-08 | **Rozpoznawanie zamiast przypominania** | Minimalizuj obciążenie pamięci: widoczne opcje, podpowiedzi, historia wyszukiwań, etykiety zawsze widoczne. |
| POD-09 | **Elastyczność i efektywność** | Skróty dla zaawansowanych (np. skróty klawiszowe, filtry zapisane), bez komplikowania ścieżki dla nowicjuszy. |
| POD-10 | **Estetyka i minimalizm** | Interfejs nie powinien zawierać informacji nieistotnych lub rzadko potrzebnych – każda dodatkowa informacja konkuruje z istotnymi. |
| POD-11 | **Pomoc w rozpoznawaniu, diagnozowaniu i naprawie błędów** | Komunikaty błędów prostym językiem, precyzyjnie wskazujące problem i konstruktywnie sugerujące rozwiązanie (zob. [FORM-09](../04-formularze/formularze.md)). |
| POD-12 | **Pomoc i dokumentacja** | Najlepiej, by system nie wymagał dokumentacji; jeśli jest potrzebna – łatwa do przeszukania, kontekstowa, zorientowana na zadania. |

---

## Prawa i zjawiska psychologiczne stosowane w UX

### POD-13 Prawo Fittsa
Czas potrzebny do wskazania celu zależy od odległości do celu i jego rozmiaru. **Wniosek:** ważne elementy interaktywne (główne CTA) powinny być duże i łatwo osiągalne; związane akcje umieszczaj blisko siebie.

**Źródła:**
- P. M. Fitts (1954), *The information capacity of the human motor system in controlling the amplitude of movement*, Journal of Experimental Psychology, 47(6), 381–391. https://doi.org/10.1037/h0055392
- Laws of UX – https://lawsofux.com/fittss-law/

### POD-14 Prawo Hicka (Hicka–Hymana)
Czas podejmowania decyzji rośnie (logarytmicznie) wraz z liczbą i złożonością dostępnych opcji. **Wniosek:** ograniczaj liczbę równorzędnych wyborów, dziel złożone procesy na kroki, wyróżniaj opcję rekomendowaną. Nie stosuj prawa mechanicznie do menu z dobrze uporządkowanymi pozycjami – użytkownicy skanują listy, a nie rozważają każdej opcji.

**Źródła:**
- W. E. Hick (1952), *On the rate of gain of information*, Quarterly Journal of Experimental Psychology, 4(1), 11–26. https://doi.org/10.1080/17470215208416600
- Laws of UX – https://lawsofux.com/hicks-law/

### POD-15 Prawo Jakoba
Użytkownicy spędzają większość czasu na *innych* stronach, więc oczekują, że Twoja strona będzie działać tak samo jak te, które już znają. **Wniosek:** stosuj ugruntowane wzorce (koszyk w prawym górnym rogu, logo → strona główna, podkreślone linki w treści).

**Źródło:** J. Nielsen, *End of Web Design* (2000) – https://www.nngroup.com/articles/end-of-web-design/ ; Laws of UX – https://lawsofux.com/jakobs-law/

### POD-16 Ograniczona pojemność pamięci roboczej
G. Miller (1956) opisał „magiczną liczbę 7±2” elementów; nowsze badania (Cowan, 2001) wskazują na ok. 4 porcje (chunks). **Wniosek:** nie wymagaj od użytkownika zapamiętywania informacji między ekranami; grupuj dane (np. numer telefonu w blokach). **Uwaga:** reguła NIE oznacza, że menu musi mieć maksymalnie 7 pozycji – to częste nadużycie.

**Źródła:**
- G. A. Miller (1956), *The magical number seven, plus or minus two*, Psychological Review, 63(2), 81–97. https://doi.org/10.1037/h0043158
- N. Cowan (2001), *The magical number 4 in short-term memory*, Behavioral and Brain Sciences, 24(1), 87–114. https://doi.org/10.1017/S0140525X01003922
- Laws of UX – https://lawsofux.com/millers-law/

### POD-17 Progi czasu odpowiedzi
- **0,1 s** – użytkownik odczuwa reakcję jako natychmiastową.
- **1 s** – granica zachowania ciągłości myśli; opóźnienie jest zauważalne, ale nie wymaga dodatkowej informacji zwrotnej.
- **10 s** – granica utrzymania uwagi; przy dłuższych operacjach pokaż wskaźnik postępu i szacowany czas.

**Źródło:** J. Nielsen (1993), *Response Times: The 3 Important Limits* – https://www.nngroup.com/articles/response-times-3-important-limits/ (na podstawie: R. B. Miller, 1968, *Response time in man-computer conversational transactions*).

### POD-18 Próg Doherty’ego
Produktywność rośnie, gdy system i użytkownik reagują w czasie poniżej ok. **400 ms**. **Wniosek:** stosuj natychmiastową informację zwrotną (optymistyczne UI, skeleton screens), nawet gdy operacja trwa dłużej.

**Źródło:** W. J. Doherty, A. J. Thadani (1982), *The Economic Value of Rapid Response Time*, IBM Report GE20-0752-0; Laws of UX – https://lawsofux.com/doherty-threshold/

### POD-19 Efekt estetyki-użyteczności
Użytkownicy często postrzegają estetyczne interfejsy jako bardziej użyteczne i są bardziej tolerancyjni wobec drobnych problemów. **Wniosek:** estetyka ma znaczenie, ale może maskować problemy w testach – obserwuj zachowanie, nie tylko deklaracje.

**Źródła:** M. Kurosu, K. Kashimura (1995), *Apparent usability vs. inherent usability*, CHI ’95 Conference Companion, 292–293. https://doi.org/10.1145/223355.223680 ; NN/g – https://www.nngroup.com/articles/aesthetic-usability-effect/

### POD-20 Zasady Gestalt (bliskość, podobieństwo, wspólny region)
Elementy położone blisko siebie, podobne wizualnie lub zamknięte we wspólnym obszarze są postrzegane jako grupa. **Wniosek:** etykieta powinna być bliżej swojego pola niż pola sąsiedniego; powiązane opcje grupuj odstępem lub ramką.

**Źródło:** NN/g, *Proximity Principle in Visual Design* – https://www.nngroup.com/articles/gestalt-proximity/ ; Laws of UX – https://lawsofux.com/law-of-proximity/

