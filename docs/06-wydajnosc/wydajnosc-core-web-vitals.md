# 06. Wydajność i Core Web Vitals

> **Zakres:** metryki wydajności postrzeganej przez użytkownika, progi, techniki optymalizacji.
> **Prefiks ID:** `WYD`

[← Powrót do README](../../README.md)

---

## WYD-01 Core Web Vitals – metryki i progi
Google definiuje trzy główne metryki doświadczenia ładowania, interaktywności i stabilności wizualnej:

| Metryka | Co mierzy | Dobrze | Wymaga poprawy | Słabo |
|---|---|---|---|---|
| **LCP** – Largest Contentful Paint | czas wyrenderowania największego elementu treści w widoku | ≤ 2,5 s | 2,5–4,0 s | > 4,0 s |
| **INP** – Interaction to Next Paint | opóźnienie reakcji na interakcje (kliknięcia, dotyk, klawisze) w trakcie całej wizyty | ≤ 200 ms | 200–500 ms | > 500 ms |
| **CLS** – Cumulative Layout Shift | nieoczekiwane przesunięcia układu | ≤ 0,1 | 0,1–0,25 | > 0,25 |

- Ocena dla strony: wartość **75. percentyla** wizyt, oddzielnie dla urządzeń mobilnych i desktopowych.
- **INP zastąpił FID** (First Input Delay) jako Core Web Vital **12 marca 2024 r.**

**Źródła:** web.dev, *Web Vitals* – https://web.dev/articles/vitals ; *LCP* – https://web.dev/articles/lcp ; *INP* – https://web.dev/articles/inp ; *CLS* – https://web.dev/articles/cls ; *Defining the Core Web Vitals metrics thresholds* – https://web.dev/articles/defining-core-web-vitals-thresholds ; *INP becomes a Core Web Vital on March 12* – https://web.dev/blog/inp-cwv-march-12

## WYD-02 Mierz na danych rzeczywistych (field) i laboratoryjnych (lab)
- **Dane terenowe (RUM):** Chrome UX Report (CrUX), PageSpeed Insights (sekcja danych rzeczywistych), Search Console – raport Podstawowe wskaźniki internetowe, biblioteka `web-vitals` JS.
- **Dane laboratoryjne:** Lighthouse, WebPageTest, panel Performance w DevTools – do diagnozy, ale nie odzwierciedlają realnych użytkowników (INP nie da się zmierzyć w lab – zastępczo używa się TBT).

**Źródła:** web.dev, *Lab and field data* – https://web.dev/articles/lab-and-field-data-differences ; https://pagespeed.web.dev/ ; https://github.com/GoogleChrome/web-vitals

## WYD-03 Wpływ wydajności na zachowanie użytkowników
- Progi percepcji czasu: 0,1 s / 1 s / 10 s (zob. [POD-17](../01-podstawy/heurystyki-i-prawa-ux.md)).
- Wielokrotnie cytowana statystyka Google (2016): **53% wizyt mobilnych jest porzucanych, gdy ładowanie trwa dłużej niż 3 s**. Traktuj ją jako orientacyjną (dane z jednego badania Google/SOASTA).
- Studia przypadków na web.dev dokumentują związek poprawy Core Web Vitals ze wskaźnikami biznesowymi (np. konwersje, współczynnik odrzuceń).

**Źródła:** Think with Google, *Find out how you stack up to new industry benchmarks for mobile page speed* (2017) – https://www.thinkwithgoogle.com/marketing-strategies/app-and-mobile/mobile-page-speed-new-industry-benchmarks/ ; web.dev, *Case studies* – https://web.dev/case-studies

## WYD-04 Optymalizacja LCP
- Element LCP (zwykle obraz bohatera lub nagłówek) musi być odkrywalny w HTML – **nie** ładuj go leniwie (`loading="lazy"`) ani przez JS; dodaj `fetchpriority="high"`.
- Skróć TTFB (cache, CDN), usuń zasoby blokujące renderowanie (krytyczny CSS inline, `defer` dla skryptów).
- Kompresuj i skaluj obrazy (AVIF/WebP, `srcset`/`sizes`).

**Źródło:** web.dev, *Optimize Largest Contentful Paint* – https://web.dev/articles/optimize-lcp

## WYD-05 Optymalizacja INP
- Dziel długie zadania JS (> 50 ms) i oddawaj wątek główny (`scheduler.yield()`, `setTimeout`).
- Natychmiast pokaż wizualną reakcję na interakcję, a cięższą pracę wykonaj później.
- Ogranicz rozmiar DOM i kosztowne przeliczenia układu; ogranicz skrypty firm trzecich.

**Źródła:** web.dev, *Optimize Interaction to Next Paint* – https://web.dev/articles/optimize-inp ; web.dev, *Optimize long tasks* – https://web.dev/articles/optimize-long-tasks

## WYD-06 Optymalizacja CLS
- Zawsze podawaj wymiary (`width`/`height` lub `aspect-ratio`) obrazów, wideo, iframe’ów, reklam.
- Rezerwuj miejsce na treści ładowane dynamicznie (banery, embedy, reklamy); nie wstawiaj treści nad istniejącą, chyba że w odpowiedzi na akcję użytkownika.
- Animuj właściwości `transform`/`opacity`, nie `top`/`height`.
- Ogranicz przesunięcia wywołane fontami (TYP-06).

**Źródło:** web.dev, *Optimize Cumulative Layout Shift* – https://web.dev/articles/optimize-cls

## WYD-07 Obrazy
- Nowoczesne formaty (AVIF, WebP) z fallbackiem przez `<picture>`.
- Obrazy responsywne (`srcset`, `sizes`) – nie wysyłaj 2000 px na ekran 400 px.
- `loading="lazy"` dla obrazów poniżej pierwszego ekranu (nigdy dla elementu LCP).

**Źródła:** web.dev, *Learn Images* – https://web.dev/learn/images ; web.dev, *Browser-level image lazy loading* – https://web.dev/articles/browser-level-image-lazy-loading

## WYD-08 Wydajność postrzegana: stany ładowania
- Dla operacji 1–10 s: wskaźnik nieokreślony (spinner) lub szkielet treści (skeleton screen) dla ładowania całych widoków.
- Dla operacji > 10 s: wskaźnik postępu z procentem/czasem i możliwością anulowania.
- Nie pokazuj spinnera dla operacji < 1 s (powoduje „migotanie”).

**Źródło:** NN/g, *Progress Indicators Make a Slow System Less Insufferable* – https://www.nngroup.com/articles/progress-indicators/ ; NN/g, *Skeleton Screens 101* – https://www.nngroup.com/articles/skeleton-screens/

