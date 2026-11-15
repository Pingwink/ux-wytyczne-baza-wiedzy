# ✅ Checklista UX i dostępności strony WWW

Skrócona lista kontrolna. Każdy punkt odsyła do pełnej wytycznej (z uzasadnieniem i źródłem). Skopiuj do zadania/issue i odhaczaj.

[← Powrót do README](README.md)

Legenda: 🔴 wymóg prawny/WCAG A–AA · 🟡 silna rekomendacja (badania) · 🟢 dobra praktyka

---

## Dostępność – fundamenty
- [ ] 🔴 Obrazy informacyjne mają `alt` opisujący treść/funkcję, dekoracyjne `alt=""` – [DOST-10](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Wideo ma napisy; nagrania audio – transkrypcję – [DOST-11](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Struktura w kodzie: nagłówki, listy, regiony, tabele z `<th>` – [DOST-13](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [ARIA-07](docs/02-dostepnosc/semantyka-html-aria.md)
- [ ] 🔴 Kontrast tekstu ≥ 4,5:1 (duży ≥ 3:1), kontrolek i ikon ≥ 3:1 – [DOST-17](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [DOST-18](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Informacja nie jest przekazywana wyłącznie kolorem – [DOST-16](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Zoom 200% bez utraty treści; brak przewijania poziomego przy 320 px – [DOST-19](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [DOST-20](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Cała obsługa możliwa z klawiatury, bez pułapek – [DOST-24](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Link „Przejdź do treści” – [DOST-25](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Widoczny i niezasłonięty wskaźnik fokusu; logiczna kolejność – [DOST-26](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [DOST-27](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Ruchome treści > 5 s można zatrzymać; brak błysków > 3/s – [DOST-30](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [DOST-31](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Unikalny, opisowy `<title>`; `lang="pl"` – [DOST-33](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [DOST-43](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🔴 Cele dotyku ≥ 24×24 px CSS (zalecane 44–48) – [DOST-39](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [MOB-03](docs/07-mobile-i-responsywnosc/mobile-i-responsywnosc.md)
- [ ] 🔴 Natywne elementy HTML zamiast `div` z ARIA; każda kontrolka ma nazwę dostępną – [ARIA-01](docs/02-dostepnosc/semantyka-html-aria.md), [ARIA-05](docs/02-dostepnosc/semantyka-html-aria.md)
- [ ] 🔴 Komunikaty statusu ogłaszane czytnikom (`role="status"`) – [DOST-47](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🟡 Brak „nakładek dostępności” – [DOST-06](docs/02-dostepnosc/wcag-2-2-przeglad.md)
- [ ] 🔴/🟢 Deklaracja dostępności (obowiązkowa dla podmiotów publicznych) – [PRAW-02](docs/02-dostepnosc/prawo-pl-ue.md), [PRAW-07](docs/02-dostepnosc/prawo-pl-ue.md)

## Nawigacja
- [ ] 🟡 Etykiety menu zrozumiałe dla użytkownika, bez żargonu – [NAW-02](docs/03-nawigacja-i-architektura-informacji/nawigacja-i-ia.md)
- [ ] 🟡 Na desktopie menu widoczne (nie tylko hamburger) – [NAW-04](docs/03-nawigacja-i-architektura-informacji/nawigacja-i-ia.md)
- [ ] 🟡 Oznaczona bieżąca lokalizacja (`aria-current`) – [NAW-05](docs/03-nawigacja-i-architektura-informacji/nawigacja-i-ia.md)
- [ ] 🟢 Logo po lewej, prowadzi do strony głównej – [NAW-06](docs/03-nawigacja-i-architektura-informacji/nawigacja-i-ia.md)
- [ ] 🟡 Okruszki w serwisach o głębokiej strukturze – [NAW-08](docs/03-nawigacja-i-architektura-informacji/nawigacja-i-ia.md)
- [ ] 🔴 Więcej niż jeden sposób dotarcia do stron (menu + wyszukiwarka/mapa) – [DOST-35](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🟡 Widoczne pole wyszukiwania w serwisach z dużą ilością treści – [NAW-10](docs/03-nawigacja-i-architektura-informacji/nawigacja-i-ia.md)
- [ ] 🔴 Opisowe teksty linków (bez „kliknij tutaj”) – [DOST-34](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [NAW-11](docs/03-nawigacja-i-architektura-informacji/nawigacja-i-ia.md)
- [ ] 🟢 Pomocna strona 404 z kodem HTTP 404 – [NAW-13](docs/03-nawigacja-i-architektura-informacji/nawigacja-i-ia.md)

## Formularze
- [ ] 🟡 Tylko niezbędne pola; układ jednokolumnowy – [FORM-01](docs/04-formularze/formularze.md), [FORM-02](docs/04-formularze/formularze.md)
- [ ] 🔴 Widoczne etykiety powiązane z polami; placeholder nie zastępuje etykiety – [FORM-04](docs/04-formularze/formularze.md)
- [ ] 🟡 Oznaczone pola wymagane/opcjonalne – [FORM-05](docs/04-formularze/formularze.md)
- [ ] 🔴 `autocomplete` i właściwe typy pól – [DOST-15](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [FORM-07](docs/04-formularze/formularze.md)
- [ ] 🔴 Błędy opisane tekstem przy polu, z sugestią poprawki – [FORM-09](docs/04-formularze/formularze.md), [DOST-44](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🟡 Walidacja po opuszczeniu pola, podsumowanie błędów po wysłaniu – [FORM-10](docs/04-formularze/formularze.md), [FORM-11](docs/04-formularze/formularze.md)
- [ ] 🔴 Można wklejać hasła/kody; brak niedostępnej CAPTCHA – [DOST-45](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [FORM-13](docs/04-formularze/formularze.md), [FORM-14](docs/04-formularze/formularze.md)
- [ ] 🟡 Zakup jako gość; pełne koszty pokazane wcześnie – [FORM-16](docs/04-formularze/formularze.md), [FORM-17](docs/04-formularze/formularze.md)
- [ ] 🔴 Podsumowanie przed złożeniem zamówienia/transakcji – [FORM-18](docs/04-formularze/formularze.md)

## Treść i typografia
- [ ] 🟡 Najważniejsze informacje na początku; opisowe śródtytuły, krótkie akapity – [TRE-02](docs/05-tresc-i-typografia/tresc-i-typografia.md), [TRE-03](docs/05-tresc-i-typografia/tresc-i-typografia.md)
- [ ] 🟡 Prosty język – [TRE-04](docs/05-tresc-i-typografia/tresc-i-typografia.md)
- [ ] 🟢 Przyciski opisują akcję czasownikiem – [TRE-05](docs/05-tresc-i-typografia/tresc-i-typografia.md)
- [ ] 🟡 Tekst treści ≥ 16 px w `rem`; wiersz 50–75 znaków; interlinia ≥ 1,5 – [TYP-01](docs/05-tresc-i-typografia/tresc-i-typografia.md), [TYP-02](docs/05-tresc-i-typografia/tresc-i-typografia.md), [TYP-03](docs/05-tresc-i-typografia/tresc-i-typografia.md)
- [ ] 🟢 Tekst wyrównany do lewej, bez justowania – [TYP-04](docs/05-tresc-i-typografia/tresc-i-typografia.md)

## Wydajność
- [ ] 🟡 LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 (75. percentyl, dane terenowe) – [WYD-01](docs/06-wydajnosc/wydajnosc-core-web-vitals.md)
- [ ] 🟡 Element LCP bez lazy-load, z `fetchpriority="high"` – [WYD-04](docs/06-wydajnosc/wydajnosc-core-web-vitals.md)
- [ ] 🟡 Wymiary podane dla obrazów i embedów – [WYD-06](docs/06-wydajnosc/wydajnosc-core-web-vitals.md)
- [ ] 🟢 Obrazy AVIF/WebP, responsywne `srcset` – [WYD-07](docs/06-wydajnosc/wydajnosc-core-web-vitals.md)

## Mobile
- [ ] 🔴 Meta viewport bez blokady zoomu – [MOB-01](docs/07-mobile-i-responsywnosc/mobile-i-responsywnosc.md)
- [ ] 🔴 Obie orientacje ekranu działają – [DOST-14](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md)
- [ ] 🟡 Kluczowe informacje nie tylko pod `:hover` – [MOB-05](docs/07-mobile-i-responsywnosc/mobile-i-responsywnosc.md)
- [ ] 🟡 Brak natrętnych pełnoekranowych pop-upów – [MOB-06](docs/07-mobile-i-responsywnosc/mobile-i-responsywnosc.md)

## Interakcje
- [ ] 🟡 Elementy klikalne wyglądają na klikalne; jedna główna akcja – [INT-01](docs/08-interakcje-i-komponenty/interakcje-i-komponenty.md), [INT-02](docs/08-interakcje-i-komponenty/interakcje-i-komponenty.md)
- [ ] 🟡 Komplet stanów komponentów (w tym fokus, błąd, ładowanie) – [INT-03](docs/08-interakcje-i-komponenty/interakcje-i-komponenty.md)
- [ ] 🟡 Modale: Esc, zarządzanie fokusem, brak modali bez akcji użytkownika – [INT-06](docs/08-interakcje-i-komponenty/interakcje-i-komponenty.md)
- [ ] 🟡 Brak autoprzewijanych karuzel (lub pauza) – [INT-07](docs/08-interakcje-i-komponenty/interakcje-i-komponenty.md)
- [ ] 🔴 Animacje respektują `prefers-reduced-motion` – [DOST-32](docs/02-dostepnosc/wcag-kryteria-szczegolowe.md), [INT-10](docs/08-interakcje-i-komponenty/interakcje-i-komponenty.md)

## Etyka i prywatność
- [ ] 🔴 Baner cookies: „Odrzuć” równorzędne z „Akceptuj”, brak zaznaczonych domyślnie zgód – [ETY-05](docs/10-etyka-i-zaufanie/etyka-i-zaufanie.md)
- [ ] 🔴 Brak wzorców manipulacyjnych – [ETY-03](docs/10-etyka-i-zaufanie/etyka-i-zaufanie.md)
- [ ] 🔴 Rezygnacja/wycofanie zgody równie łatwe jak zapis – [ETY-04](docs/10-etyka-i-zaufanie/etyka-i-zaufanie.md)
- [ ] 🟡 Widoczne dane firmy, kontakt, warunki – [ETY-01](docs/10-etyka-i-zaufanie/etyka-i-zaufanie.md), [ETY-02](docs/10-etyka-i-zaufanie/etyka-i-zaufanie.md)

## Badania i testy
- [ ] 🟡 Testy z użytkownikami (rundy po ok. 5 osób) przed i po wdrożeniu – [BAD-02](docs/11-badania-i-testowanie/badania-i-testowanie.md)
- [ ] 🟡 Testy dostępności: automat + klawiatura + czytnik ekranu – [BAD-08](docs/11-badania-i-testowanie/badania-i-testowanie.md)
- [ ] 🟢 Automatyczne testy dostępności w CI – [BAD-10](docs/11-badania-i-testowanie/badania-i-testowanie.md)

