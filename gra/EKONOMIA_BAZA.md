# EKONOMIA — BAZA USTALONA. 300-03-11.
### To jest jedyne źródło liczb pieniężnych. Nie wyprowadza się ich na nowo, nie „doprecyzowuje" i nie audytuje w trakcie gry.
### Zmienia je wyłącznie ZDARZENIE W GRZE (decyzja gracza, rzut, wojna, zima), nigdy ponowne liczenie.

---

## ⚠ KOREKTA, KTÓRA ZAMYKA WCZORAJSZY WĄTEK

Rozbicie Białego Portu i Fosy HQ na linie (765 / 515 / 325 / 195 oraz 555 / 360 / 330) **było moją alokacją, nie zapisem.** Więc „luka 150 smoków miesięcznie, której nie widzi Kasa 2" **nie jest odkryciem — jest artefaktem mojego własnego podziału.** Skasowana.

**Zostaje z tego jedno prawdziwe pytanie i jest warte zadania:** *czy lenno dostaje za swój towar monetę, czy rozliczenie.* To jedna pozycja, nie trzy.

---

# ⚑ KOREKTA SKALI 300-04-26 — ROZSTRZYGNIĘCIE GRACZA (ma moc zapisu, zasada 43)

> „Stare bilanse nie są aktualne — mocno podkręcić, wyliczyć razy 2–3 i dodać to, co nieuwzględniane. Dochód Korony też 2–3 razy, bo sytuacja się stabilizuje i Północ zaczyna się pieniężyć."

- **Od 300-04-01 przychody Kas 1, 2 i 3 liczą się ×2 (dół widełek) do ×3 (góra).** Dotyczy także zysku pięciu placówek z modelu. **Koszty, obrót informacyjny, zdarzenia jednorazowe i pozycje `bez_skali` — bez zmian.** Silnik: `_korekta_skali` w `ekonomia.json`, funkcja `skala()` w `kasa.py`.
- **Nowe linie (dotąd poza bilansem):** atelier Miry (bez bursztynu) · wędzarnia · Dom Audytowy Tally · placówka Braavos (kantor Nesty) · placówka Pentos (Obaro) · drukarnia i skryptorium Fosy (koszt V–VI) → Wydawnictwo Domu Tally (od VII) · ekstra zysk z towaru Korony (IV–VI, poza skalą) · szkoła Fosy (wpisowe, praktykanci) · lecznica (leki przez filię).
- **W świecie:** wojna skończona, trakty i grobla otwarte, Wilk przyjmowany po nominale, jedna brama w komorach, Kompania Północ–Dorzecze, Essos przez Nestę, wiosna. To, co szło w naturze, zaczyna iść w monecie.

| piętro (po korekcie) | miesięcznie IV/300 | rocznie (rząd) |
|---|---|---|
| **Kasa 1 — Dom Handlowy Tally** | ~1 070 – 2 590 | ~13 000 – 31 000 |
| **Kasa 2 — lenno Fosy Cailin** | ~115 – 485 | ~1 400 – 5 800 |
| **Kasa 3 — Skarb Północy (Korona)** | ~615 – 1 010 | ~7 400 – 12 100 |

⚠ **Skutek — z poprawką gracza 300-04-26 („jest jeszcze Manderly, znacznie bogatszy”):** górna krawędź Domu Tally zbliża się do osobistego dochodu Pana Winterfell (25–40 tys. przed korektą), **ale Symon NIE jest drugą sakiewką Północy.** **MANDERLY JEST ZNACZNIE BOGATSZY** — od Domu Tally i w monecie także od osobistej sakiewki Winterfell: jedyny prawdziwy port Północy, własne myto (pobiera je sam — list 300-04-26), flota, bednarnie, stocznie, srebro z handlu morskiego. Monetyzacja Północy podnosi także wielkie domy — **Manderly zyskuje na niej najwięcej, bo przez jego port przechodzi moneta.** Porządek w monecie: **MANDERLY ≫ WINTERFELL (osobiście) > DOM TALLY > reszta lordów.** **MANDERLY: 40 000 – 60 000 smoków rocznie** (rozstrzygnięcie gracza 300-04-26, moc zapisu) — wobec Winterfell 25 000 – 40 000 osobiście i Domu Tally ~13 000 – 31 000 po korekcie skali. Tabela „CZTERY PIĘTRA” niżej opisuje stan sprzed 300-04 i zostaje jako historia.

---

# CZTERY PIĘTRA, NIE TRZY KASY

Trzy kasy to **porządek rachunkowy Symona**. Skala świata ma cztery piętra i mieszanie ich było moim błędem.

| piętro | rocznie | co to jest |
|---|---|---|
| **① WIELKIE DOMY — majątek osobisty pana** | **Winterfell 25 000 – 40 000 · MANDERLY 40 000 – 60 000** (gracz, 300-04-26) | dochód osobisty Pana Winterfell; Manderly znacznie bogatszy, największy na Północy, bo ma jedyny prawdziwy port |
| **② KASA 1 — Dom Handlowy Tally** | **~3400 netto** | duży dom handlowy; **jakaś dziesiąta część osobistego dochodu Starka** |
| **③ KASA 3 — Skarb Północy, w monecie** | **~3500** | **nowy fisk królewski**, nie majątek Północy |
| **④ KASA 2 — lenno Fosy Cailin** | **~550** | małe lordostwo; stąd danina 20-40, czyli 4-7% |

---

## ⚠ RZECZ, KTÓRA TŁUMACZY CAŁĄ RESZTĘ: KRÓL JEST BOGATY, A KRÓLESTWO BIEDNE — I TO NIE JEST TA SAMA SAKIEWKA

**Robb Stark jest jednocześnie Panem Winterfell i Królem Północy, ale to dwie różne kieszenie.**

Jego **osobisty** dochód to 25-40 tysięcy. Jego **królewska** kasa — Skarb Północy, urząd stworzony przed niespełna rokiem, w trakcie wojny, w kraju, który daniny płaci zbożem, ludźmi i robocizną — bierze w monecie jakieś **3500**. Winterfell nie płaci sam sobie daniny.

**Stąd wszystko, co dzieje się w tej grze od miesięcy:**
- dlaczego Gawen uznaje 695 i nie może zapłacić — **to piąta część całego rocznego srebra Korony**, a nie ułamek majątku Starków;
- dlaczego Korona chce płacić **przywilejem** — przywileje ma, srebra nie;
- dlaczego zapłacenie Symona z sakiewki Winterfell byłoby czymś zupełnie innym niż zapłacenie ze Skarbu — **król spłacałby dług królestwa własnym majątkiem**, a to precedens, którego żaden król nie ustanawia dwa razy;
- dlaczego sto smoków oddane Skarbowi w marcu jest realną ulgą.

## I CO TO ZNACZY O SYMONIE — bo to też trzeba powiedzieć wprost

**Dom Handlowy Tally zarabia jakąś dziesiątą część tego, co Stark bierze osobiście.** Symon nie jest bogaty miarą lordów. Jest **średnim lordem z nadzwyczaj dobrym interesem** — a jego siła nie leży w wielkości majątku, tylko w tym, że kontroluje **przepływ monety w królestwie, którego król monety nie ma.**

Północ nie jest biedna. Północ jest **niezmonetyzowana**: czynsze tłuste w naturze, daniny w zbożu i ludziach, świadczenia w naturze pięć do dziesięciu razy większe od pieniężnych. Srebro przecieka przez to cienką strużką — i to jest ta strużka, przy której siedzi Dom Tally.

---

## KASA 1 — DOM HANDLOWY TALLY

**Obrót:** kwartał zimowy 6655. Zima to dno roku; trakty stoją, brokerka zamiera.
**Zysk kwartału zimowego:** 915 (placówki) + 54 (udziały) − 261 (aparat 87/mies.) = **708**.
**Skrzynia:** ~95, a po wykupie 340 — przy zerze. Odbudowa z pozostałych ~650 towaru Korony przez wiosnę.

**Linie, które zarabiają:** łańcuch konserwacji (sól, ryba solona, beczki — jedyna rosnąca zimą) · przewóz i tranzyt · kontrakty dworskie i koronne · brokerka · składy · arteria · młyny · gospoda na Rozdrożu · warstwa kredytowa.
**Linie, które jeszcze nie zarabiają:** papiernia (siedzi w koszcie) · bursztyn (+4 jelenie/mies.) · ubezpieczenia frachtu (50 rezerwy).

## KASA 2 — LENNO FOSY CAILIN

**Dochód:** czynsze · myto, waga, targ, brama · regale torfowe · prawo składu · **sprzedaż produkcji włości przez placówki Domu**.
**Wytwarza:** torf · ryba · trzcina · futra · żelazo bagienne · warzywo ze szklarni · zioła i mech · mąka z młyna w śluzie.
**Obciążenia:** garnizon 22/mies. · szkoła 9/mies. · danina do Korony 20-40/rok · budowy · od 300-03-11 żołd koronnego garnizonu w Cailin.
**Twarde ograniczenie:** zwyczaj zabrania podnoszenia czynszów. **Cały wzrost musi pochodzić z rzeczy nowych.**

## KASA 3 — SKARB PÓŁNOCY

**~3500 w monecie rocznie.** Winna Domowi 695 (spłacane w towarze). Gawen uznał całość; zwłoka ma jedną przyczynę i jest podana wprost: nie ma czym.

---

## JAK TO SIĘ ZMIENIA W GRZE

Rosną: **ruch** (trakt, grobla, brama, myto, waga) · **nowe rzeczy** (przewłoka, Starkport, Przystań Wilka, komora wodna) · **linie odwieszone** (papiernia — bo królestwo zaczęło pisać; bursztyn — bo wojna się skończyła; ubezpieczenia — bo brakuje im rachmistrza, nie rynku).
Spadają: zima · wojna · zajęcie zdolności domu cudzą robotą bez zysku.

**Nie rosną ani nie spadają przez ponowne przeliczenie.**

---

# RACHUNEK DOMU — CZTERY LICZBY (rozstrzygnięcie gracza 300-05-05, moc zapisu)

> „Skala powinna zwalniać większą liczbę gotówki. Dom obraca towarem i operacjami o wartości X, przychód to X, zysk to X, wolna gotówka to X. Sytuacja, że wszystko rośnie, a nigdy nie ma gotówki, nie jest realna. Warsztaty rozdzielone oddzielnie, nie zmniejszane i nie wsadzane w obrót.” (gracz, 300-05-05)

Liczy `python3 gra/kasa.py miesiac|rok` (blok **RACHUNEK DOMU**) i `python3 gra/kasa.py wolne` (skrzynia).

| poziom | co to jest | IV/300 (smoki/mies.) | V/300 |
|---|---|---|---|
| **1. OBRÓT** | wszystko, co przechodzi przez Dom: przychód + papier w obiegu + fracht kryty + tranzyt Kompanii; **dźwignia ×2–7** na kapitale własnym 4–6 tys. | ~11 200 – 29 500 | ~11 300 – 29 900 |
| **2. PRZYCHÓD** | sprzedaż towaru placówek (Westeros i Essos), sprzedaż warsztatów, prowizje, odsetki, udziały | ~6 100 – 12 500 | ~6 200 – 12 700 |
| **3. ZYSK** | wynik operacyjny po kosztach (kasa.py) | ~1 080 – 2 590 | ~1 100 – 2 640 |
| **4. WOLNA GOTÓWKA** | zysk minus reinwestycja 25–35%; bufor Hala 1000 napełniony w IV i stoi | 0 – 945 (po buforze) | **~720 – 1 980** |

- **Towar włości płacony monetą (40–90/mies.) to KAPITAŁ OBROTOWY**, nie odpływ: wraca przy sprzedaży w marży placówek.
- **Warsztaty i zakłady — każdy osobno** (sprzedaż i zysk): jubilerski (bursztyn Marra), papiernia, warzelnia i solarnia, bednarnia, atelier Miry, wędzarnia, dom audytowy, wydawnictwo (od VII); w lennie: zielarnia, szkoła, lecznica. Sprzedaż = zysk / marża warsztatu.
- **Parametry (E — szacunek GM, do korekty przez gracza):** marże warsztatów 20–70% wg rodzaju; Essos 12–16%; papier 2–3%/mies., ubezpieczenie 1,5–2,5%, prowizja Kompanii 3–5%; reinwestycja 25–35%.
- Rocznie 300 (I–III bez korekty skali): zysk ~12 300 – 28 700, **wolna gotówka ~7 000 – 20 500**. Porządek zostaje: MANDERLY ≫ WINTERFELL (osobiście) > DOM TALLY.
- Stara „synteza 299-09” (zysk 200–300, wolna 80–120/mies.) — **HISTORIA, nieaktualna**.
