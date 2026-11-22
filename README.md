# Ukázkový squad — kontroly T8

Ukázkový repozitář pro guildu Git, CI/CD a governance (4IT433). Ukazuje, jak v repozitáři squadu fungují automatické kontroly Pull Requestů z `.github/workflows/pr-checks.yml`. Data ani notebooky nejsou skutečné.

## Stav

Repozitář slouží jen jako ukázka. Obsahuje jeden notebook ve složce `fabric/` a toto README podle šablony T7.

## Architektura

Struktura odpovídá týmovému repozitáři: Fabric workspace je propojený se složkou `fabric/` ve větvi `dev`, do `main` se dostává jen přes Pull Request.

## Konvence

Tabulky se jmenují malými písmeny s prefixem vrstvy, například `bronze_zastavky_demo` nebo `silver_zastavky_demo`.

## Datové zdroje a licence

Ukázkový notebook si data vytváří sám, žádný externí zdroj nepoužívá, takže se na něj nevztahuje žádná licence.

## Bronze – načtení

Notebook `nb_bronze_demo` zapíše tabulky `bronze_zastavky_demo`, `bronze_linky_demo` a `bronze_spoje_demo` se sloupcem `_loaded_at`.

### Kontrola počtů

| Tabulka | Zdroj | Bronze |
|---|---|---|
| bronze_zastavky_demo | 2 | 2 |

## Silver – pravidla čištění

Silver vrstva v ukázce zatím není, pravidla čištění se popíší u každé tabulky zvlášť.

## Kvalita dat a logování

Kvalita dat se v ukázce nehlídá. Ve skutečném projektu sem patří DQ pravidla, karanténa a tabulka běhů.

## Tým

Ukázku připravil squad 25 (David Malášek) pro guildu Git, CI/CD a governance.

## Použití AI

S přípravou ukázkového notebooku a README pomáhal Claude (Anthropic), výstup jsme zkontrolovali.
