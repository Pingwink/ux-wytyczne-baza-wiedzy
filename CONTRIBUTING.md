# 🤝 Zasady współtworzenia bazy

[← Powrót do README](README.md)

## Wymagania dla każdej wytycznej

1. **ID** w formacie `PREFIKS-NN` (zob. [system identyfikatorów](README.md#-system-identyfikatorów)). Nowe wytyczne dostają kolejny wolny numer; ID usuniętych wytycznych nie są ponownie używane.
2. **Konkret** – reguła sformułowana tak, by dało się ją sprawdzić (wartości progowe, warunki, przykłady), a nie ogólnik („strona powinna być przyjazna”).
3. **Co najmniej jedno źródło** z hierarchii w [ZRODLA.md](ZRODLA.md) – z pełnym tytułem i URL (dla publikacji naukowych: DOI).
4. **Rozróżnienie wymóg vs. zalecenie** – wymogi WCAG z numerem kryterium i poziomem, wymogi prawne z aktem i artykułem.
5. **Zastrzeżenia** przy danych z pojedynczych badań komercyjnych lub sprzecznych wynikach.

## Niedozwolone źródła

- Blogi i artykuły bez wskazania źródła danych, treści generowane przez AI bez weryfikacji, strony sprzedawców narzędzi jako jedyne źródło twierdzeń o skuteczności ich produktu, Wikipedia jako jedyne źródło.

## Proces zmian

1. Utwórz gałąź i wprowadź zmianę w odpowiednim pliku `docs/`.
2. Jeśli dodajesz wytyczną ważną dla wdrożeń – dodaj punkt w [CHECKLISTA.md](CHECKLISTA.md).
3. Nowe źródło dopisz do [ZRODLA.md](ZRODLA.md).
4. W Pull Requeście wskaż, co zweryfikowałeś(-aś) w źródle pierwotnym; recenzent sprawdza zgodność twierdzeń ze źródłem.
5. Zaktualizuj odpowiedni raport w [weryfikacja/](weryfikacja/) (status ✅/✏️/⚠️/❌ i data).

## Szablon wytycznej

```markdown
### PREFIKS-NN Krótka, sprawdzalna reguła
Opis: co, dlaczego, wartości progowe, przykład dobry/zły.

**Jak sprawdzić:** (opcjonalnie) metoda weryfikacji.
**Źródła:** [Tytuł źródła](URL) ; [Tytuł 2](URL)
```

## Przeglądy okresowe

Co najmniej raz w roku przejrzyj obszary zmienne: WCAG / EN 301 549, Core Web Vitals, przepisy PL/UE, coroczne raporty (WebAIM Million, Baymard), oraz sprawdź martwe linki (np. narzędziem `lychee` lub `markdown-link-check` w GitHub Actions).

