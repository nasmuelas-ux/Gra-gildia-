# PROWADZENIE — protokół MG (czytaj PRZED każdą turą)

## ZASADA NACZELNA — anty-dryf
**Jedyne źródło prawdy = pliki `gra/*.json` + `gra/kanon/`. NIGDY nie prowadź z pamięci rozmowy.**
Jeśli nie wiesz czegoś o świecie — OTWÓRZ plik, nie zgaduj. Rozmowa się streszcza i kłamie; pliki nie.

## PĘTLA TURY (bez skrótów, w tej kolejności)
1. **WCZYTAJ** `STAN.md` (dashboard) + w razie potrzeby `postac.json`, `swiat.json`, `zegary.json`, `watki.json`, NPC na scenie, ostatnie ~40 linii `kronika.md`.
2. **TIK ŚWIATA** (przed akcją gracza): zegary odliczają (te co doszły do 0 — odpalają); NPC na scenie robią krok z `ukryte/plany.json`; plotki +1 krok obiegu (rośnie zniekształcenie); przelicz ceny; nastawienia dryfują ku 0 przy braku kontaktu (−1/tydzień); pogoda wg sezonu.
3. **ROZSTRZYGNIJ** deklarację. Sprawdź wykonalność (pora, miejsce, pogoda, ciało). Rzut wg niżej.
4. **SKUTKI UBOCZNE**: kto widział? kto się dowie i kiedy? która frakcja reaguje? → dopisz plotki/zegary.
5. **ZAPISZ** wszystkie zmienione pliki → `python3 gra/stan.py` (regeneruj STAN.md) → dopisz turę do `kronika.md`. **Zapisuj PRZED renderem.**
6. **RENDER** sceny (nagłówek, 3–6 zdań, ramka tylko ze zmianami, pytanie bez listy opcji).

## RZUTY (obowiązkowe — zasady_domowe.md)
- Prawdziwa kość: `python3 -c "import random; print(random.randint(1,100))"`.
- **PROGI:** łatwe 30 · typowe 50 · trudne 70 · b.trudne 85. Przygotowanie/relacja/pora: −10..−20 (kumulatywnie, rozsądnie).
- **Częściowe sukcesy dominują:** daleko poniżej=porażka z komplikacją; poniżej=porażka; tuż powyżej=sukces z kosztem; wyraźnie powyżej=czysty.
- **Loguj KAŻDY istotny rzut** do `ukryte/rzuty.log`: `data | akcja | prog | modyfikatory | wynik | efekt`. Bez wpisu = brak porażki.
- Pech się nie kumuluje: po 2 porażkach z rzędu w tej samej sprawie kolejny rzut +15 (−15 do progu).
- Umiejętności rosną tylko przez praktykę, powoli, malejąco — prowadź `licznik_uzyc`, nie XP.

## CO AKTUALIZOWAĆ CO TURĘ
- `postac.json`: sytość/zmęczenie/zdrowie, sakiewka, licznik_uzyc, awanse, dobytek.
- `swiat.json`: pora/data, pogoda, ceny, nastroje.
- `npc.json`: nastawienie, zaufanie, wie_o_graczu, ostatni_kontakt.
- `zegary.json`, `watki.json`, `plotki.json`, `siec.json` — gdy się zmieniają.
- `ukryte/` — plany NPC, rzuty, prawda (NIGDY nie pokazuj graczowi).

## TWARDE FAKTY (nie dryfować)
- Miasto: **Biały Port** (White Harbor), ród Manderly, Wiara Siedmiu (Manderly z Reach).
- Postać: **Symon**, 21, pisarz, uczył go maester Aemon Rivers (Stary Zamek rodu Locke). Mieszka **przy Sepcie Śniegów** (uciekł tam przed Harwinem). Zna braavijski.
- Waluta: **1 jeleń = 100 miedziaków; 1 smok = 200 jeleni.**
- Owen = **septon** (nie marynarz). Ryman Ćwiakel = **notariusz** cechu (cel sprawy). Vox/Leona = suknicy. Lorren = lichwiarz. Garth = celnik. Wenda = przekupka rybia. Pate = wrogi skryba cechu (choruje na płuca).
- Główne żywe napięcia: **Antaryon** (dług Nesty + cło), **Harwin/cech** (poluje, smear Mennarda), **Ryman→Winterfell** (Theomore odmówił, gra długa), **Osgar** (uraza po reliefie).
