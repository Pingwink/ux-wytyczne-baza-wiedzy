---
name: ux-audit-checklista
description: >-
  Przeprowadza kompleksowy audyt UX i dostępności (WCAG 2.2 AA) strony internetowej
  lub aplikacji webowej jedną komendą na podstawie 59-punktowej checklisty i bazy
  175 wytycznych. Tworzy personę, planuje ścieżkę użytkownika pokrywającą 100%
  widoków, wykonuje automatyczny skan HTML/CSS/JS, robi zrzuty ekranu każdego
  etapu, ocenia wszystkie 59 punktów checklisty, nadaje błędom wagi (1–4) wraz z
  gotowymi fixami i generuje spójny raport (Markdown, edytowalny HTML oraz DOCX
  gotowy do Canva Docs). Użyj tego skilla, gdy użytkownik prosi o audyt UX,
  sprawdzenie strony z checklistą, raport dostępności WCAG lub test ścieżki persony
  (np. komendą /ux-audit-checklista).
---

# Autorski Skill: Audyt UX i Dostępności WCAG 2.2 (59-punktowa Checklista)

Ten skill automatyzuje pełny proces audytu UX i dostępności strony internetowej **jedną komendą** (np. `/ux-audit-checklista <ścieżka_lub_URL> [opis_persony]`).

Łączy automatyczny skaner kodu HTML/CSS/JS z przejściem poznawczym (Cognitive Walkthrough) dopasowanej persony oraz pełną weryfikacją [59-punktowej checklisty](./references/checklista-59-kryteriow.md).

---

## Kiedy uruchomić ten skill

Aktywuj ten skill natychmiast, gdy użytkownik:
- wpisze komendę `/ux-audit-checklista` lub poprosi o uruchomienie skilla audytu UX,
- powie: *„sprawdź tę stronę z naszą checklistą”*, *„zrób audyt UX tej strony”*, *„przetestuj stronę personą i wygeneruj raport”*, *„oceń dostępność WCAG i błędy UX”*.

---

## Procedura wykonania audytu (Krok po kroku – „Jedna Komenda”)

Gdy użytkownik wywoła audyt, wykonaj poniższe 6 kroków bez przerywania pracy (chyba że brakuje ścieżki/URL do badanej strony):

### Krok 1: Identyfikacja celu badania i Persony
1. Ustal lokalizację badanej strony:
   - Jeśli podano archiwum `.zip`, rozpakuj je poleceniem `tar -xf <plik.zip> -C <folder_docelowy>`.
   - Jeśli podano folder lub plik `.html`, zlokalizuj główny plik `index.html` oraz powiązane arkusze CSS, skrypty JS i obrazy.
   - Jeśli podano żywy adres URL, użyj subagenta `browser` do inspekcji DOM i zrzutów ekranu.
2. Ustal profil **Persony badawczej**:
   - Jeśli użytkownik podał opis persony (np. *„pracownik wytwórni muzycznej zamawiający ramy i passe-partout”*), zbuduj pełny profil dopasowany do tego opisu.
   - Jeśli użytkownik nie podał persony, wygeneruj realistyczną personę główną (Primary Persona) dopasowaną do branży badanej strony (cele, częstotliwość wizyt, urządzenia, obawy i typowe zadania).

### Krok 2: Uruchomienie automatycznego skanera technicznego (59 punktów)
Uruchom skrypt pomocniczy [audit_scanner.py](./scripts/audit_scanner.py) na badanym pliku lub katalogu HTML:

```powershell
python .agents/skills/ux-audit-checklista/scripts/audit_scanner.py "<ścieżka_do_index.html>" --output "<ścieżka_do_wynikow.json>"
```

Skrypt automatycznie wykrywa i mierzy m.in.:
- wszystkie widoki SPA (`section.view`, podstrony, routery `#hash`), formularze, tabele i okna modalne,
- **dokładne współczynniki kontrastu WCAG 2.2** dla par kolorów zdefiniowanych w CSS (próg `4,5:1` dla tekstu, `3,0:1` dla dużego tekstu, obramowań kontrolek i `:focus-visible`),
- obecność `<html lang>`, `<title>`, `<meta name="viewport">`, linku „Przejdź do treści” (skip-link), regionów landmark (`<header>`, `<nav>`, `<main>`, `<footer>`),
- atrybuty `alt`, `width`, `height`, `loading="lazy"` i `fetchpriority="high"` na wszystkich znacznikach `<img>`,
- powiązanie pól formularzy z `<label>`, obecność `autocomplete`, `aria-live`, `aria-expanded`, `aria-current`,
- pozostawione na produkcji narzędzia deweloperskie / debuggerskie (np. `#seo-toggle`, `data-seo`) oraz martwe linki (`href="#"`, `target="_blank"` bez ostrzeżenia).

### Krok 3: Zaplanowanie ścieżki użytkownika (100% pokrycia widoków) i zrzuty ekranu
1. Na podstawie listy widoków zwróconej przez skaner zaplanuj logiczną **ścieżkę użytkownika (8–12 etapów)** tak, aby persona odwiedziła **każdy widok/ekran** oraz przetestowała kluczowe interakcje (nawigację, wyszukiwarkę, tabele porównawcze, konfiguratory/formularze, stany błędów walidacji oraz widok mobilny RWD `375 px`).
2. Dla każdego etapu wykonaj zrzut ekranu (`screenshots/etap_01.png` .. `etap_XX.png`):
   - Użyj subagenta `browser` (jeśli dostępny) lub generatora wizualnych makiet ekranów w Pythonie (`Pillow` + zasoby strony), oznaczając na zrzutach badany etap i kluczowe obserwacje audytowe.

### Krok 4: Weryfikacja każdego z 59 punktów checklisty
Otwórz plik referencyjny [checklista-59-kryteriow.md](./references/checklista-59-kryteriow.md) i oceń **każdy z 59 punktów** w 9 obszarach:
1. Dostępność – fundamenty (16 pkt)
2. Nawigacja i architektura informacji (9 pkt)
3. Formularze i konfiguratory (9 pkt)
4. Treść i typografia (5 pkt)
5. Wydajność – Core Web Vitals (4 pkt)
6. Mobile i responsywność (4 pkt)
7. Interakcje i komponenty (5 pkt)
8. Etyka, prywatność i zaufanie (4 pkt)
9. Badania i testowanie (3 pkt)

Każdemu punktowi przypisz status:
- `✅ Spełnione` – pełna zgodność z wytyczną,
- `⚠️ Częściowo` – wdrożone niepełnie lub z drobnymi uchybieniami,
- `❌ Niespełnione` – brak realizacji lub naruszenie progu WCAG / UX.

### Krok 5: Klasyfikacja błędów według wagi (Severity 1–4) i opracowanie Fixów
Dla każdego wykrytego problemu utwórz kartę błędu (`BŁĄD-01`, `BŁĄD-02`, ...) zgodnie ze skalą Nielsena (NN/g) i WCAG 2.2:
- **🔴 Waga 4/4 (Krytyczny / Bloker):** Uniemożliwia realizację celu biznesowego/zakupowego, psuje kluczowy wariant produktu, narusza twardy próg kontrastu kontrolek (`< 3:1`) lub ujawnia warstwy deweloperskie na produkcji.
- **🟠 Waga 3/4 (Poważny):** Znacząco utrudnia korzystanie ze strony (brak skip-linku, kontrast tekstu `< 4,5:1`, brak stanu pustego w wyszukiwarce, brak zarządzania fokusem w SPA, przedwczesna walidacja `on input`).
- **🟡 Waga 2/4 (Średni):** Powoduje frustrację lub obniża zaufanie (brak orientacyjnych widełek cenowych, niespójne dane w stopce, brak lightboxa mimo efektu zoomu, martwy link polityki prywatności).
- **🟢 Waga 1/4 (Drobny):** Kosmetyka i optymalizacja techniczna (brak `width`/`height` na części obrazów, brak WebP/AVIF, `px` zamiast `rem`).

**Każdy błąd MUSI zawierać:**
1. Identyfikator naruszonej wytycznej (np. `DOST-17`, `FORM-10`),
2. Dokładne miejsce w kodzie (selektor CSS / linia HTML / funkcja JS),
3. Konkretny, gotowy do wklejenia **Proponowany Fix** (fragment kodu HTML, CSS lub JS).

### Krok 6: Wygenerowanie spójnego pakietu raportów (MD + HTML + DOCX do Canvy)
Korzystając ze wzorca w [szablon-raportu.md](./references/szablon-raportu.md), wygeneruj dla użytkownika:
1. **`RAPORT_UX_<NAZWA>.md`** – pełny raport w Markdownie z osadzonymi ścieżkami do zrzutów ekranu.
2. **`RAPORT_UX_<NAZWA>.html`** – interaktywny, atrakcyjny wizualnie raport HTML z podglądem na żywo, osadzonymi screenami, trybem edycji tekstu i przyciskiem kopiowania Rich Text do Canva Docs.
3. **`RAPORT_UX_<NAZWA>_CANVA.docx`** – natywny dokument Word (`.docx`) z osadzonymi w treści wszystkimi zrzutami ekranu (`word/media/etap_XX.png`), gotowy do zaimportowania jednym kliknięciem w Canvie (**Utwórz projekt → Importuj plik**).
4. *(Opcjonalnie, jeśli użytkownik poprosi o bezpośredni zapis na koncie Canva)* – utwórz projekt przez narzędzie MCP `canva_canva:create-design` i zwróć bezpośredni link do edycji.

