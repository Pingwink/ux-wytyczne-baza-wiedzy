# Szablon Raportu z Audytu UX i Dostępności WCAG 2.2 AA

Użyj poniższego układu podczas generowania raportu końcowego (`RAPORT_UX_<NAZWA>.md`, `.html` oraz `_CANVA.docx`):

```markdown
# 📋 Audyt UX i Dostępności (WCAG 2.2 AA): [Nazwa Strony] – Raport z Wędrówki Persony

## 1. Streszczenie zarządcze (Executive Summary)
- **Badany serwis:** [Nazwa i liczba przebadanych widoków / ekranów – 100% pokrycia]
- **Wynik weryfikacji 59-punktowej checklisty:**
  - ✅ Spełnione: X / 59 (X%)
  - ⚠️ Częściowo spełnione: Y / 59 (Y%)
  - ❌ Niespełnione: Z / 59 (Z%)
- **Rozkład wykrytych błędów wg wagi (Severity 1–4):**
  - 🔴 Waga 4/4 (Krytyczne / Blokery): ...
  - 🟠 Waga 3/4 (Poważne): ...
  - 🟡 Waga 2/4 (Średnie): ...
  - 🟢 Waga 1/4 (Drobne): ...

---

## 2. Persona badawcza
- **Imię, wiek, stanowisko i branża:** ...
- **Kontekst i częstotliwość zamówień / wizyt:** ...
- **Kluczowe cele i potrzeby (Jobs-to-be-Done):** ...
- **Główne punkty bólu (Frustrations) wykryte na stronie:** ...

---

## 3. Ścieżka użytkownika (Etapy 1..N – 100% pokrycia ekranów) ze zrzutami ekranu
Dla każdego etapu:
### Etap X: [Tytuł etapu i identyfikator widoku]
- **Działanie Persony:** ...
- **Pokryte elementy interfejsu:** ...
- **Wynik audytu na tym etapie (✅ / ⚠️ / ❌):** ...
> **📸 ZRZUT EKRANU ETAPU #0X**
> ![Zrzut ekranu Etap 0X](screenshots/etap_0X.png)

---

## 4. Sprawdzenie każdego aspektu z 59-punktowej checklisty (Tabela 59 wierszy w 9 obszarach)
| Lp. | Obszar | Priorytet | Kryterium z CHECKLISTA.md (ID) | Status (`✅`/`⚠️`/`❌`) | Szczegółowa ocena i dowód w kodzie |
| :--- | :--- | :---: | :--- | :---: | :--- |
| 1..59 | ... | ... | ... | ... | ... |

---

## 5. Pełna lista błędów z wagami (Severity 1–4) i proponowanymi Fixami
Dla każdego błędu:
#### 🔴/🟠/🟡/🟢 BŁĄD-XX (Waga X/4): [Tytuł błędu]
- **Naruszone wytyczne:** `[ID-WYTYCZNEJ]`
- **Lokalizacja w kodzie:** `[plik / linia / selektor]`
- **Opis problemu i wpływ na Personę:** ...
- **🔧 Proponowany Fix (gotowy kod HTML/CSS/JS):**
  ```html/css/js
  ...
  ```

---

## 6. Plan naprawczy (Priorytety wdrożeniowe)
1. **Sprint 1 (Pilne – Waga 4/4):** ...
2. **Sprint 2 (Ważne – Waga 3/4):** ...
3. **Sprint 3 (Usprawnienia UX i SEO/CWV – Waga 2/4 i 1/4):** ...
```

