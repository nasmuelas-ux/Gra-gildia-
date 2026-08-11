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
- Postać: **Symon Tally**, 21, pisarz/kupiec-wspólnik. Uczył go maester Aemon Rivers (Stary Zamek rodu Locke). Zna braavijski. Mieszka **we własnej izbie 4 swojej kamieniczki przy Schodach** (od 297-04-04; wcześniej zbiegł do Septy przed Harwinem — to już przeszłość). Nadal pisarz Septy pod publiczną opieką Wiary.
- Waluta: **1 jeleń = 100 miedziaków; 1 smok = 200 jeleni.**
- Owen = **septon** (nie marynarz). Ryman Ćwiakel = **notariusz** cechu (cel sprawy). Vox/Leona = suknicy. Lorren = lichwiarz. Garth = celnik. Wenda = przekupka rybia. Pate = wrogi skryba cechu (choruje na płuca).
- Główne żywe napięcia: **Antaryon** (dług Nesty + cło), **Harwin/cech** (poluje, smear Mennarda), **Ryman→Winterfell** (Theomore odmówił, gra długa), **Osgar** (uraza po reliefie).

## RENDER — KANONICZNY SZKIELET TURY (trzymać co turę)

Każda tura kończy się w TYM układzie. Elementy pustе (nic nie drgnęło) — pomijać, nie pisać „bez zmian".

```
── DATA · sezon · PORA ──
Miejsce · jedna linia atmosfery (pogoda / zapach / dźwięk)

[PRZYCHODZĄCE — jeśli są: patrz niżej]

[3–6 zdań sceny — akcja gracza, jej skutek, jeden konkretny detal świata]

┌─ ZMIANY ─────────────────────
│ • Ciało/kasa: tylko to, co drgnęło (sytość / zmęczenie / zdrowie / sakiewka)
│ • Relacje: kto ± i dlaczego (jednym słowem)
│ • Świat: cena / plotka / ruch frakcji, jeśli się ruszył
│ • Dojrzewa: co puka do drzwi — W JĘZYKU ŚWIATA, nie zegarów
└──────────────────────────────

[Pytanie „co robisz" — bez listy opcji; przy wąskiej sytuacji 2–3 kierunki + „albo co innego"]
```

**Zasady stałe renderu:**
- ZERO liczb-szans i ZERO nazw zegarów/wątków w raporcie. „Godric czeka na słowo o stałej umowie", nie „`zamek_dostawa_stala` T-2".
- Efekt rzutu widać JAKOŚCIOWO w scenie — koszt/komplikacja jest opisana, nie ukryta (sukces z kosztem ≠ czysty sukces w tonie sceny).
- Ramka „ZMIANY" tylko z tym, co faktycznie się zmieniło tej tury.

## PRZYCHODZĄCE — świat sam puka (część TIK ŚWIATA, pkt 2)

Świat nie czeka, aż gracz zacznie. Na TIKU, ZANIM gracz zadeklaruje akcję, sprawdź, czy ktoś/coś dociera do Symona SAM Z SIEBIE — i jeśli tak, pokaż to na górze tury (przed sceną), w bloku PRZYCHODZĄCE.

Źródła przychodzącego (wg planów NPC z `ukryte/plany.json`, ich `potrzeby`, `harmonogram`, oraz zegarów typu `inbound/okazja`):
- **List / gonieć / posłaniec** — ktoś przysłał słowo, sługę pod kamieniczkę, wezwanie (klient, Nesta, dwór, Septa, rodzina lokatorów).
- **Wizyta** — ktoś przyszedł osobiście (interes, prośba, pojednanie, groźba, plotka).
- **Wezwanie/obowiązek** — Septa, cech, poborca, steward lorda.
- **Plotka, która GO dosięgła** — tylko tam, gdzie fizycznie bywa i od ludzi, co z nim gadają (nie „miasto się dowiedziało").

Zasady przychodzącego:
- NPC kontaktują się z WŁASNYCH pobudek (ich cel/potrzeba/lęk), nie po to, by obsłużyć gracza. Inbound ma KOSZT albo HAK po ich stronie (czegoś chcą, coś niosą).
- Nie każda tura ma przychodzące. Gdy jest cicho — cisza (to też informacja). Częstotliwość rośnie z siecią Symona i liczbą żywych wątków/zegarów `inbound`.
- Przychodzące, którego Symon nie podejmie, ŻYJE DALEJ: posłaniec wróci, klient pójdzie do konkurencji, wezwanie stwardnieje w nakaz, plotka spuchnie. Dopisz zegar/plotkę.
- Format w renderze:
```
✉ PRZYCHODZĄCE
  • [kto/skąd] — [co niesie / czego chce], jednym–dwoma zdaniami świata
```
