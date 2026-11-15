# 04. Formularze

> **Zakres:** projektowanie pól, etykiet, walidacji, komunikatów błędów, procesów wieloetapowych i checkoutu.
> **Prefiks ID:** `FORM`

[← Powrót do README](../../README.md) · Powiązane: [DOST-44, DOST-45](../02-dostepnosc/wcag-kryteria-szczegolowe.md)

---

## Struktura i zakres

### FORM-01 Pytaj tylko o niezbędne dane
Każde pole zwiększa wysiłek i ryzyko porzucenia. Usuń pola opcjonalne, których nie potrzebujesz; dane, które można wywnioskować (np. miasto z kodu pocztowego), uzupełniaj automatycznie. Badania Baymard pokazują, że przeciętny proces checkoutu zawiera znacznie więcej pól, niż potrzeba (można go skrócić o ok. 20–60%). Minimalizacja danych to też wymóg RODO (art. 5 ust. 1 lit. c).

**Źródła:** Baymard Institute, *Checkout Usability* – https://baymard.com/research/checkout-usability ; Baymard, *Checkout Optimization: Minimize Form Fields* – https://baymard.com/blog/checkout-flow-average-form-fields ; RODO art. 5 – https://eur-lex.europa.eu/eli/reg/2016/679/oj

### FORM-02 Układ jednokolumnowy
Układaj pola w jednej kolumnie – układ wielokolumnowy zaburza kolejność wypełniania i powoduje pomijanie pól. Wyjątek: krótkie, logicznie powiązane pola (np. kod pocztowy + miasto, data).

**Źródła:** Baymard Institute, *Avoid Multi-Column Forms* – https://baymard.com/blog/avoid-multi-column-forms ; CXL Institute, *Form Field Usability: Single Column vs. Multi-Column* – https://cxl.com/research-study/form-field-usability/

### FORM-03 Logiczne grupowanie
Grupuj powiązane pola (dane osobowe, adres, płatność) z nagłówkami sekcji; grupy przycisków radio i checkboxów otaczaj `<fieldset>` z `<legend>`.

**Źródła:** W3C WAI, *Forms Tutorial – Grouping Controls* – https://www.w3.org/WAI/tutorials/forms/grouping/

---

## Etykiety, podpowiedzi, placeholdery

### FORM-04 Każde pole ma widoczną, trwałą etykietę
Etykieta nad polem (najszybsze skanowanie, najlepsza na mobile) i powiązana programowo (`<label for="id">`). **Nie używaj placeholdera jako etykiety**: znika po rozpoczęciu pisania (obciążenie pamięci), ma zwykle zbyt niski kontrast, bywa mylony z wartością wypełnioną, utrudnia weryfikację przed wysłaniem.

**Źródła:** NN/g, *Placeholders in Form Fields Are Harmful* – https://www.nngroup.com/articles/form-design-placeholders/ ; W3C WAI, *Forms Tutorial – Labeling Controls* – https://www.w3.org/WAI/tutorials/forms/labels/ ; WCAG SC 3.3.2 – https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html ; M. Penzo (2006), *Label Placement in Forms*, UXmatters – https://www.uxmatters.com/mt/archives/2006/07/label-placement-in-forms.php

### FORM-05 Oznaczaj pola wymagane i opcjonalne
Wyraźnie oznacz pola – albo wymagane (np. gwiazdka z objaśnieniem legendy na początku formularza), albo opcjonalne („(opcjonalnie)”) gdy większość jest wymagana. Baymard zaleca oznaczanie **zarówno** pól wymaganych, jak i opcjonalnych. W kodzie: atrybut `required` lub `aria-required="true"`.

**Źródła:** Baymard Institute, *Mark Both Required and Optional Form Fields* – https://baymard.com/blog/required-optional-form-fields ; NN/g, *Marking Required Fields in Forms* – https://www.nngroup.com/articles/required-fields/

### FORM-06 Instrukcje formatu przed polem, nie w błędzie
Wymagany format (np. „DD.MM.RRRR”, wymagania hasła) podaj w tekście pomocniczym widocznym przed wypełnieniem, powiązanym z polem przez `aria-describedby`. Lepiej: akceptuj różne formaty (spacje w numerze karty, myślniki w telefonie) i normalizuj je po stronie systemu.

**Źródła:** GOV.UK Design System, *Text input – hint text* – https://design-system.service.gov.uk/components/text-input/ ; Baymard, *Allow Spaces in Credit Card Fields* – https://baymard.com/blog/credit-card-field-auto-format-spaces ; W3C WAI, *Forms Tutorial – Instructions* – https://www.w3.org/WAI/tutorials/forms/instructions/

---

## Typy pól i ułatwienia wprowadzania

### FORM-07 Właściwe typy pól, `inputmode` i `autocomplete`
- `type="email"`, `type="tel"`, `type="url"`, `type="search"` – odpowiednia klawiatura na mobile.
- `inputmode="numeric"` dla kodów i numerów, które nie są liczbami w sensie matematycznym (kod pocztowy, PIN, numer karty) – zamiast `type="number"` (który dodaje strzałki, może zmieniać wartość przy przewijaniu i usuwać wiodące zera).
- `autocomplete` z właściwymi tokenami (DOST-15) – umożliwia autouzupełnianie.
- Szerokość pola odpowiada długości oczekiwanej odpowiedzi (krótkie pole na kod pocztowy).

**Źródła:** MDN, *inputmode* – https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/inputmode ; GOV.UK Design System, *Text input – numbers* – https://design-system.service.gov.uk/components/text-input/#numbers ; web.dev, *Sign-up form best practices* – https://web.dev/articles/sign-up-form-best-practices ; Baymard Institute, *Form Field Usability: Matching User Expectations* – https://baymard.com/blog/form-field-usability-matching-user-expectations

### FORM-08 Dobór kontrolki do liczby opcji
- 2–5 wzajemnie wykluczających się opcji → przyciski radio (wszystkie opcje widoczne).
- Wiele opcji → lista wyboru `<select>` lub combobox z wyszukiwaniem (np. kraj).
- Wielokrotny wybór → checkboxy.
- Pojedyncze tak/nie, które działa natychmiast → przełącznik (switch); w formularzu wysyłanym przyciskiem → checkbox.
- Daty znane użytkownikowi (data urodzenia) → trzy pola tekstowe lub jedno z formatem zamiast kalendarza.

**Źródła:** NN/g, *Checkboxes vs. Radio Buttons* – https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/ ; NN/g, *Toggle-Switch Guidelines* – https://www.nngroup.com/articles/toggle-switch-guidelines/ ; GOV.UK Design System, *Date input* – https://design-system.service.gov.uk/components/date-input/

---

## Walidacja i błędy

### FORM-09 Treść komunikatów błędów
Komunikat błędu powinien: być widoczny i blisko pola, wyróżniony nie tylko kolorem (ikona + tekst), opisywać problem prostym językiem, wskazywać sposób naprawy, nie obwiniać użytkownika, zachowywać wpisane dane.
Przykład: zamiast „Nieprawidłowe dane” → „Wpisz kod pocztowy w formacie 00-000”.

**Źródła:** NN/g, *Error-Message Guidelines* – https://www.nngroup.com/articles/error-message-guidelines/ ; GOV.UK Design System, *Error message* – https://design-system.service.gov.uk/components/error-message/ ; WCAG SC 3.3.1, 3.3.3 – https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html

### FORM-10 Moment walidacji (inline)
Waliduj pole po jego opuszczeniu (on blur), nie w trakcie pisania (nie pokazuj błędu „za krótki e-mail” po pierwszym znaku). Po poprawieniu błędu usuwaj komunikat od razu (w trakcie pisania). Badania Baymard: walidacja inline poprawia doświadczenie, ale przedwczesne komunikaty frustrują.

**Źródła:** Baymard Institute, *Usability Testing of Inline Form Validation* – https://baymard.com/blog/inline-form-validation ; L. Wroblewski (2009), *Inline Validation in Web Forms*, A List Apart – https://alistapart.com/article/inline-validation-in-web-forms/

### FORM-11 Podsumowanie błędów po wysłaniu
Po wysłaniu formularza z błędami: pokaż na górze podsumowanie błędów z linkami do pól i przenieś do niego fokus; dodaj „Błąd:” na początku `<title>`; przy każdym polu komunikat powiązany przez `aria-describedby`; oznacz pole `aria-invalid="true"`.

**Źródła:** GOV.UK Design System, *Error summary* – https://design-system.service.gov.uk/components/error-summary/ ; W3C WAI, *Forms Tutorial – User Notifications* – https://www.w3.org/WAI/tutorials/forms/notifications/

### FORM-12 Nie blokuj przycisku wysyłania
Nieaktywny przycisk „Wyślij” nie mówi, co jest nie tak, a elementy `disabled` bywają niedostępne z klawiatury i mają niski kontrast. Lepiej pozwolić na wysłanie i pokazać konkretne błędy.

**Źródła:** GOV.UK Design System, *Button – disabled buttons* – https://design-system.service.gov.uk/components/button/#disabled-buttons ; Smashing Magazine, *Usability Pitfalls of Disabled Buttons* – https://www.smashingmagazine.com/2021/08/frustrating-design-patterns-disabled-buttons/

---

## Hasła, logowanie, CAPTCHA

### FORM-13 Przyjazne pola haseł
- Opcja „Pokaż hasło”.
- Zezwalaj na wklejanie i menedżery haseł (`autocomplete="current-password"` / `"new-password"`).
- Wymagania pokazuj z góry; NIST zaleca min. długość zamiast reguł złożoności (min. 8 znaków, a 15 gdy hasło jest jedynym czynnikiem – wg SP 800-63B rev. 4) i niewymuszanie okresowych zmian bez powodu.

**Źródła:** NIST SP 800-63B-4, *Digital Identity Guidelines: Authentication and Authenticator Management* – https://pages.nist.gov/800-63-4/sp800-63b/ (https://doi.org/10.6028/NIST.SP.800-63B-4) ; WCAG SC 3.3.8 – https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html ; web.dev, *Sign-in form best practices* – https://web.dev/articles/sign-in-form-best-practices

### FORM-14 Unikaj CAPTCHA lub zapewnij dostępne alternatywy
Tradycyjne CAPTCHA (zniekształcony tekst, wybór obrazków) wykluczają osoby z niepełnosprawnościami wzroku, poznawczymi i ruchowymi. Preferuj metody niewymagające interakcji (honeypot, analiza ryzyka po stronie serwera, limity prób); jeśli CAPTCHA jest konieczna – zapewnij co najmniej dwie modalności i spełnij SC 3.3.8.

**Źródło:** W3C, *Inaccessibility of CAPTCHA* (W3C Group Note) – https://www.w3.org/TR/turingtest/

---

## Procesy wieloetapowe i checkout

### FORM-15 Wskaźnik postępu w procesach wieloetapowych
Pokaż liczbę kroków i bieżący krok („Krok 2 z 4: Dostawa”), pozwól wrócić do poprzednich kroków bez utraty danych.

**Źródła:** NN/g, *Wizards: Definition and Design Recommendations* – https://www.nngroup.com/articles/wizards/ ; Baymard Institute, *Progress Indicators in Checkout* / *Accordion Style Checkouts* – https://baymard.com/blog/progress-indicators-for-ui-ux ; https://baymard.com/blog/accordion-style-checkout

### FORM-16 Zakup bez zakładania konta
Udostępnij zakup jako gość w widocznym miejscu. Wg badań Baymard wymóg założenia konta jest jedną z głównych przyczyn porzucenia koszyka (obok dodatkowych kosztów i zbyt długiego procesu); średni odsetek porzuconych koszyków wynosi ok. 70%.

**Źródła:** Baymard Institute, *Cart Abandonment Rate Statistics* – https://baymard.com/lists/cart-abandonment-rate ; Baymard, *Guest Checkout* – https://baymard.com/blog/delayed-account-creation

### FORM-17 Pełne koszty wcześnie
Pokaż całkowity koszt (wysyłka, podatki, opłaty) jak najwcześniej – nieoczekiwane dodatkowe koszty to najczęstsza przyczyna porzucenia koszyka w badaniach Baymard. Ukrywanie kosztów do ostatniego kroku to także wzorzec manipulacyjny (zob. ETY-03).

**Źródło:** Baymard Institute, *Cart Abandonment Rate Statistics* – https://baymard.com/lists/cart-abandonment-rate

### FORM-18 Potwierdzenie i możliwość korekty przed ostatecznym wysłaniem
Dla transakcji finansowych/prawnych pokaż ekran podsumowania z możliwością edycji (WCAG 3.3.4), a po wysłaniu – jasne potwierdzenie z numerem zamówienia i dalszymi krokami.

**Źródła:** WCAG SC 3.3.4 – https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html ; GOV.UK Design System, *Check answers* – https://design-system.service.gov.uk/patterns/check-answers/ ; GOV.UK Design System, *Confirmation pages* – https://design-system.service.gov.uk/patterns/confirmation-pages/

