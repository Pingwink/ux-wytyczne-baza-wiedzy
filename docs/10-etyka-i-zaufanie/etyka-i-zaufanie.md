# 10. Etyka, zaufanie i prywatność

> **Zakres:** wiarygodność strony, wzorce manipulacyjne (dark patterns), banery zgód, prywatność w projektowaniu.
> **Prefiks ID:** `ETY`

[← Powrót do README](../../README.md) · Kontekst prawny: [PRAW-08](../02-dostepnosc/prawo-pl-ue.md)

---

## Wiarygodność

### ETY-01 Czynniki wiarygodności strony
Wytyczne Stanford Web Credibility Project (B. J. Fogg) wskazują m.in.: ułatwiaj weryfikację informacji (źródła, cytaty), pokaż, że za stroną stoi realna organizacja (adres, dane rejestrowe), eksponuj ekspertyzę i ludzi, ułatwiaj kontakt, dbaj o profesjonalny wygląd, aktualizuj treści, ograniczaj treści promocyjne, unikaj błędów (literówki, niedziałające linki).

**Źródła:** B. J. Fogg (2002), *Stanford Guidelines for Web Credibility*, Stanford Persuasive Technology Lab – https://credibility.stanford.edu/guidelines/index.html ; NN/g, *Trustworthiness in Web Design: 4 Credibility Factors* – https://www.nngroup.com/articles/trustworthy-design/

### ETY-02 Przejrzystość informacji kluczowych
Ceny (z kosztami dodatkowymi), warunki zwrotu, czas dostawy, dane kontaktowe i dane firmy łatwe do znalezienia. W UE przedsiębiorca e-commerce ma obowiązek podania określonych informacji przed zawarciem umowy na odległość (dyrektywa 2011/83/UE, w Polsce ustawa o prawach konsumenta).

**Źródła:** Dyrektywa 2011/83/UE (prawa konsumentów), art. 6 – https://eur-lex.europa.eu/eli/dir/2011/83/oj ; Ustawa z dnia 30 maja 2014 r. o prawach konsumenta – https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20140000827 ; NN/g, *Trustworthy design* (j.w.)

---

## Wzorce manipulacyjne (dark patterns / deceptive patterns)

### ETY-03 Nie stosuj wzorców manipulacyjnych
Termin „dark patterns” wprowadził H. Brignull (2010). Przykłady do unikania:

| Wzorzec | Opis |
|---|---|
| **Confirmshaming** | Zawstydzanie przy odmowie („Nie, wolę przepłacać”). |
| **Ukryte koszty (drip pricing)** | Dodatkowe opłaty ujawniane dopiero na końcu procesu. |
| **Utrudniona rezygnacja (roach motel / obstruction)** | Łatwo zapisać się na subskrypcję, trudno zrezygnować. |
| **Przemycanie do koszyka (sneaking)** | Automatyczne dodawanie produktów/ubezpieczeń. |
| **Fałszywa pilność / niedobór** | Fikcyjne liczniki czasu, „zostały 2 sztuki” bez pokrycia. |
| **Wstępnie zaznaczone zgody** | Domyślnie zaznaczone zgody marketingowe lub dodatki. |
| **Nagging** | Uporczywe ponawianie tej samej prośby. |
| **Ukryta reklama / disguised ads** | Reklamy udające treść lub nawigację. |
| **Podwójna negacja / trick questions** | Mylące sformułowania checkboxów. |

Wzorce te mogą naruszać prawo: dyrektywę 2005/29/WE o nieuczciwych praktykach handlowych, RODO (zgoda), DSA art. 25 (platformy).

**Źródła:**
- H. Brignull, *Deceptive Design* (dawniej darkpatterns.org) – https://www.deceptive.design/types
- A. Mathur i in. (2019), *Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites*, Proc. ACM HCI 3 (CSCW) – https://doi.org/10.1145/3359183
- Komisja Europejska (2022), *Behavioural study on unfair commercial practices in the digital environment: dark patterns and manipulative personalisation* – https://op.europa.eu/en/publication-detail/-/publication/606365bc-d58b-11ec-a95f-01aa75ed71a1/language-en
- EDPB (2023), *Guidelines 03/2022 on Deceptive design patterns in social media platform interfaces: how to recognise and avoid them* (ver. 2.0) – https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-032022-deceptive-design-patterns-social-media_en
- Dyrektywa 2005/29/WE – https://eur-lex.europa.eu/eli/dir/2005/29/oj

### ETY-04 Rezygnacja równie łatwa jak zapis
Anulowanie subskrypcji, wycofanie zgody, usunięcie konta – dostępne tym samym kanałem i z podobnym wysiłkiem jak zapis (RODO art. 7 ust. 3 dla zgód). Zmieniona dyrektywa 2011/83/UE (przez dyrektywę (UE) 2023/2673, art. 11a) wprowadza obowiązek „przycisku odstąpienia” (funkcji odstąpienia od umowy) dla umów zawieranych online.

**Źródła:** RODO art. 7 – https://eur-lex.europa.eu/eli/reg/2016/679/oj ; Dyrektywa (UE) 2023/2673 – https://eur-lex.europa.eu/eli/dir/2023/2673/oj

---

## Zgody na cookies

### ETY-05 Baner zgód zgodny z prawem i przyjazny
- Przycisk „Odrzuć wszystkie” na pierwszej warstwie, równie widoczny jak „Akceptuj wszystkie” (te same rozmiar, kontrast, poziom).
- Brak wstępnie zaznaczonych kategorii (poza niezbędnymi) – wyrok Planet49.
- Brak ładowania nieniezbędnych cookies/skryptów przed wyrażeniem zgody.
- Jasne, zwięzłe informacje o celach; łatwy, stały dostęp do zmiany ustawień (np. link w stopce).
- Baner dostępny z klawiatury i dla czytników ekranu; nie zasłania fokusu (WCAG 2.4.11).

**Źródła:**
- EDPB, *Report of the work undertaken by the Cookie Banner Taskforce* (2023) – https://www.edpb.europa.eu/our-work-tools/our-documents/report/report-work-undertaken-cookie-banner-taskforce_en
- EDPB, *Guidelines 05/2020 on consent under Regulation 2016/679* – https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-052020-consent-under-regulation-2016679_en
- TSUE C-673/17 Planet49 – https://curia.europa.eu/juris/liste.jsf?num=C-673/17
- CNIL, *Cookies et autres traceurs – lignes directrices et recommandation* – https://www.cnil.fr/fr/cookies-et-autres-traceurs

### ETY-06 Prywatność w fazie projektowania (privacy by design)
Uwzględniaj ochronę danych od początku projektu i domyślnie (RODO art. 25): minimalizacja danych w formularzach (FORM-01), domyślne ustawienia najbardziej chroniące prywatność, jasne wyjaśnienie „dlaczego pytamy” przy wrażliwych polach.

**Źródło:** RODO art. 25 – https://eur-lex.europa.eu/eli/reg/2016/679/oj ; EDPB, *Guidelines 4/2019 on Article 25 Data Protection by Design and by Default* – https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-42019-article-25-data-protection-design-and_en

