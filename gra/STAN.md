# STAN GRY — indeks (regenerowany z JSON+JSONL, NIE edytuj recznie)
_Zrodlo prawdy: gra/*.json + gra/db/wpisy.jsonl. Szczegoly: `python3 gra/db.py pokaz <klucz>` / `szukaj <fraza>` / `dzien <data>`._

## ⚠️ 36 ZASAD SILNIKA — `gra/PROWADZENIE.md`, sekcja od "TRZYDZIESCI PIEC ZASAD"
**PRZECZYTAJ JE PO KAZDYM KOMPAKTOWANIU.** Przy sprzecznosci z czymkolwiek innym — tamte wygrywaja.
Skrot najczesciej lamanych: **1** nie twierdze, nie sprawdziwszy · **3** blad GM nie przechodzi na gracza (VOID znaczy VOID) ·
**7** moja cisza nie jest zastojem (rzecz zlecona i obsadzona idzie sama) · **8** postep rodzi problemy, nie wstazki ·
**12** kryterium to OBSADZENIE, nie nazwisko · **22** prerogatywa nie idzie pod glosy · **27** jeden rzut na sprawe albo zero ·
**31** nie pisze mysli gracza, nie zamieniam rozmowy w akt, nie posuwam czasu w rozmowie · **34** bez kanalu nie ma wiadomosci.
### **36 - DWA POZIOMY:** SPRAWA zyje latami i NIE ma sie zamykac (filar) · OPERACJA ma dzien, cel i spust, i MUSI sie zamknac.
Test: czy to moze sie skonczyc konkretnego dnia? Meldunek idzie z poziomu OPERACJI - filary stoja, melduje sie to, co sie pod nimi rusza.
**ALARM: sprawa zywa, pod ktora nie ma ANI JEDNEJ otwartej operacji** - to nie brak postepu, to ja nie otworzylem nastepnego kroku.

## ⚠️ OBOWIAZKOWA RAMA RANKA (nie pomijac po kompaktowaniu!)
Kazdy RANEK renderuj W TEJ KOLEJNOSCI, ZAWSZE:
1. **DATA + POGODA** — pogoda ma niesc skutek, nie ozdobe.
2. **KALENDARZ** — najblizsze terminy (patrz blok TERMINY nizej).
3. **📬 KORESPONDENCJA — TRZY RZECZY**, renderuj SAM, nie na zadanie:
   - CO PRZYSZLO Z ZEWNATRZ — rzut na inbound, losowany **Z LISTY "CO SLEDZIMY"** (gra/KSIEGA_ZOBOWIAZAN.md, sekcja III), NIE z powietrza. Podaj KANAL (zasada 34).
   - CO SAMO DOJRZALO — meldunki ludzi i urzedow, ktorym cos zlecono. **BEZ RZUTU** (zasada 7). Forma z zasady 8: co zrobione / na czym utknal / ile kosztowalo / czego chce ode mnie.
   - CISZA JEST PRAWDZIWA W DRODZE (zasada 11). Jak nic nie przyszlo → napisz "cisza".
4. **STATUS** — sytosc/zmeczenie/zdrowie + kasa (wolne + skrot).
5. **🧵 WATKI — MAKSIMUM TRZY LINIE, TYLKO WYJATKI:** ZAPADA DZIS · SPOZNIONE (ile dni) · BEZ TERMINU albo PUSTE KRZESLO.
   Potem "co robisz?" — bez listy opcji.

**DZIEN BILANSU (1. dnia miesiaca)** ma stala zawartosc: kasa · daniny · **MELDUNKI BUDOW wedle zasady 33**
(ile stoi · ilu ludzi · co ich zatrzymuje · czego potrzebuja z zewnatrz), po jednym akapicie z kazdego miejsca.

## ⚠️ ZAPIS STANU — NOWY TRYB (od 299-09-11)
NIE przepisuj wielkich JSON-ow. Dopisuj JEDNA LINIE do dziennika:
```
python3 -c "import sys; sys.path.insert(0,'gra'); import db; db.dopisz('watki','<klucz>','RRR-MM-DD','<tresc>')"
```
Zrodla: `watki` · `npc` (klucz = `sekcja/id`) · `swiat` · `postac`. Metadane (status, termin, kasa, sytosc) edytuje sie w JSON jak dotad.

## TERAZ
- **Data:** 300-03-03 ranek · zima (300)
- **Miejsce:** FOSA CAILIN. Cerwyn 2.-5. III. Wyjazd 300-03-07.
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 78 · Sytosc 72 · Zmeczenie 38**

## KASA (1 jelen=100 mied · 1 smok=200 jel)
- **Wolne:** 2 smokow + 55 jeleni + 1 mied
- **Dzien Bilansu:** 1. dnia miesiaca · nastepny 300-03-01

## UMIEJETNOSCI
pismo 8 · rachunki 10 · prawo 9 · retoryka 8 · jezyki 8 · spryt_uliczny 8 · kondycja 7 · rzemioslo 1 · handel 8 · walka 6 · geometria 5 · czytanie_ludzi 10 · organizacja 9 · audyt 9 · finanse 9 · wlodarstwo 8 · historia 6 · wiedza_o_swiecie 7 · polityka 10
**Reputacja:** port 38 · schody_zamkowe 40 · cech_pisarzy -6 · wiara 96 · zamek 24 · cech_kolodziejow 42

## ⚠️ PUDELKA — pelna tabela w gra/ludzie.json; tu tylko WYJATKI
- ### `?` NIEPEWNE — NIE WKLADAC W USTA, PYTAC: MARR (DOM_TALLY)
- ### SZEW: **GARTH** — czlowiek LENNA stojacy przy komorze celnej KORONY - pobiera clo Kasy 3 reka lenna. Jedyny prawdziwy szew Fosy. Nie dostal pisma o granicach urzedu (ob…
- ### SZEW: **POCZTA KORONY** — przelozony poczty odpowiada Beronowi w Winterfell, ale Garrick nia dysponuje, bo jest na miejscu. Chodzi na zdrowy rozsadek i kiedys przestanie.

## 🧩 SPRAWY SIE PRZEPLATAJA — CZYSTE MA BYC ROZSTRZYGNIECIE, NIE SPRAWA
_LUDZIE maja jedno pudelko. SPRAWY maja ich kilka i tak ma byc. Czyste musi byc nie to, kogo sprawa DOTYKA, tylko: KTO ROZSTRZYGA (jeden), Z CZYJEJ KASY (jedna), KTO PISZE, KTO CZYTA, i KTO NIE MOZE TEGO TKNAC._
### SYMON JEST JEDNOCZESNIE: Namiestnikiem Korony, panem lenna Fosy i wlascicielem Domu Tally. KAZDA sprawa na Fosie przechodzi przez wszystkie trzy jego role naraz. To nie jest wada swiata - to jest osnowa calej gry.
**Zamiast odsylac NPC, GM pyta:** Ktora CZESC tej sprawy jest twoja? · Kto to ROZSTRZYGA i czy ja jestem strona? · Z ktorej kasy to idzie? · Kto tego NIE MOZE tknac i dlaczego?
_(pelna lista spraw: gra/sprawy.json)_

## 🧵 KSIEGA ZOBOWIAZAN — SAME WYJATKI (pelna: gra/KSIEGA_ZOBOWIAZAN.md)
| ### Hendry | ### **PISARZ PRZY BRAMIE — NADAL PUSTY.** Mella odmówiła sama: *„brama to jedyne miejsce, przez które przechodzi każdy obcy"* | ### **przed 300-03-02** | 300-02-28 |
| ### **PIERWSZA ROBOTA BRANA NIE JEST KOPANIEM** | **Przejść i zmierzyć** — standard z punktu 10: *„żaden odcinek bez nazwiska i bez daty"*. Ręce z rejestru dniówek *(kolumna „co umie")*, ten sam mechanizm co przy przewłoce, drugi raz | — | 300-03-01 |
| ### **ZASTĘPCA PRZY GROBLI — data, której nikt nie zna** | **Nie jest potrzebny dziś** *(grobla stoi, 48 idzie z Branem)* — **jest potrzebny w dniu, w którym kafar znów wchodzi w grunt.** ### Termin bez daty nie jest terminem, więc data brzmi: **„przed pierwszym dniem, w którym kafar wchodzi w grunt"** — ### **a jedynym, który ten dzień rozpozna, jest BRAN. Nazwisko musi paść, ZANIM Bran wyjdzie na trakt** | **przed wyjściem Brana** | 300-03-01 |
| ### ✅ **BRAN wskazuje przodownika spośród 48 — przed wyjściem na trakt** | Data: **przed pierwszym dniem, w którym kafar wchodzi w grunt**. Wiersz w części E przestaje być pusty | **przed wyjściem** | 300-03-01 |
| **projekt Cailin** | **PUNKT 10 — PRACE POSZCZEGÓLNE** dopisany: odcinek po odcinku, klasa gruntu, obiekty od sztuki, cena ze standardu. ### *Żaden odcinek bez nazwiska i bez daty* | `gra/projekt_cailin.md` | 300-02-27 |
| **Symon → Nesta** | **co słyszała o DAENERYS TARGARYEN** — pierwsza próba ruszenia białej plamy, przy której stoi *„ani jednej drogi"* | wysłane 300-02-27 | 300-02-27 |
| ### **Symon → Nesta** | ### **ZBADAĆ BRAAVIJSKIE DOMY HANDLOWE** — sprawdzone: **nie było zlecone nigdzie**. Nowe zlecenie, nie przypomnienie | ### bez terminu | 300-02-27 |
| ### ✅ **CZYTANIE ZIARNA — (a) i (c) ROZSTRZYGNIĘTE 300-03-02** | ### **(a) PIERWSZY ODCZYT ROBI WAGOWY** — lord dopisuje **powinność do urzędu**, nie wskazuje człowieka *(„lord nazywa CO, nie JAK")*. ### **(c) WYSTAN UCZY JEDNEGO, TEN JEDEN UCZY PRZY WADZE** — kanał już istnieje i stoi w zapisie: *Bennis od wagi „uczył się rachunku od Herwina"*. **Maester nie musi jechać do czternastu miast.** ### **(b) trzeci, sporny odczyt — NADAL PUSTY**, a jest jedynym zabezpieczeniem znaku | ### **(b) puste** | 300-03-02 |
| ### ⚡ **PYTANIE (c) NIE JEST SPISEM — JEST AMUNICJĄ NA PIERWSZE GŁOSOWANIE** | **Z jakich wsi ich wzięto, z nazwy — i które z tych wsi stoją puste.** ### *„Ziemia bez pana" dowodzona w powietrzu brzmi jak zabór.* ### **Ta sama rzecz dowodzona nazwami pustych wsi i imionami ludzi, których z nich wzięto — a którzy siedzą żywi na przyczółku — jest ratunkiem, który się spóźnił.** ### **Torren MA te imiona, przysłał je w rubryce (7). Brakuje drugiej kolumny obok nich** | ### **300-03-30** | 300-03-02 |
| ### ⚡ **SZKLARNIA TO NIE OGRÓD — TO MATECZNIK** | Szklarnia karmiąca lenno musiałaby być dziesięć razy większa. **Szklarnia produkująca ROZSADĘ obsługuje dziesięć razy więcej ziemi, niż sama zajmuje.** Rozsada kapusty i rzepy, cebula, czosnek, zioła, zielenina dla chorych i dzieci | ### **300-03-07** | 300-03-02 |
| ### ⚠ **KOREKTA SKALI 300-03-02: CENA MINIMALNA NIE JEST KIEROWNICĄ PÓŁNOCY** | ### **Dno wymaga KUPUJĄCEGO** — kto ogłasza dno, obiecuje kupić po tym dnie. ### **Kasa 3: 3000–6000 w monecie na rok, winna 695, termin minął 03-01 bez odpowiedzi.** ### **Korona nie może być kupującym ostatniej instancji dla całej Północy** — dno ogłoszone przez pusty skarbiec to dokładnie to, przed czym Symon bronił się przy kursie: *„sufit to obietnica, którą Korona złamie w pierwszym prawdziwym kryzysie"* | — | 300-03-02 |
| ### ⚡⚡ **KIEROWNICĄ PÓŁNOCY JEST ⑥ PODATEK W ZIARNIE — „najtańsze z dziewięciu, bo nie kosztuje nic"** | ### **Nie trzeba kupować, żeby kierować. Wystarczy powiedzieć, CZEGO SIĘ NIE ODMÓWI W DANINIE.** ### **Człowiek, który może zapłacić powinność żytem, posieje żyto. Człowiek, który musi sprzedać żyto, by kupić monetę na daninę, posieje to, co się lepiej sprzedaje.** ### **DLA LENNA KIEROWNICĄ JEST CENA. DLA KRÓLESTWA — DANINA. I to jedyna, która działa przy pustym skarbcu** | ### **ogłoszenie, nie głosowanie** | 300-03-02 |
| ### ⚠ **TRZECI KLUCZ NIE MA RĘKI** | Pisarzy Korony nie ma tylu, ilu okręgów — cała nadwyżka to **sześciu Nesty na Fosie**, a Gawen stracił dwóch. ### Pierwszy rok: gdzie nie ma pisarza, drugim kluczem **dwaj z ławy przysięgłych**. ### **Wpisać jawnie jako stan przejściowy Z DATĄ** — *„stopniowo" bez daty trwało raz trzy tygodnie, a ktoś w tym czasie oferował 12 smoków za trzy wozy* | ### **data wymagana** | 300-02-28 |
| ### **Garrick** *(nie Korona)* | ### **REJESTRY LOCKE'ÓW + POCHODZENIE** — **rozdzielone z listu do Króla.** Dwie własne ręce, **Kasa 1**, wpisane jawnie jako **sprawa prywatna Namiestnika** *(jak stoi od 299-09-11: „ni jeden człowiek Korony")*. Żadnego kruka Korony | **bez terminu** | 300-02-28 |

## ⏳ TERMINY Z DATA
- **300-03-01** — OCHMISTRZ WYCHOWANKOW - ogloszenie nazwiska  _(Winterfell)_
- **300-03-01** — DZIEN BILANSU
- **300-03-02..05** — CERWYN NA FOSIE - trzy dni pisania, pisarz Skarbnika przy stole  _(Fosa Cailin)_
- **300-03-03** — ROZWIAZANIE LADY MIRY  _(Bialy Port)_
- **300-03-07** — Symon opuszcza Fose; jesli nie ma odpowiedzi Torrena - Theon wraca z nim
- **300-03-pol** — CZTERDZIESCIORO DZIECI wjezdza do Winterfell
- **300-03** — WEKSLE LUCANA - 340 zapada
- **300-03** — ZBOZE Z DORZECZA rusza, gdy trakty puszcza
- **300-03-30** — WSZYSTKO NAPISANE + 168 odpisow do kwater lordow
- **300-04-01** — WIELKA RADA  _(Winterfell)_
- **300-04-01** — ROZSTRZYGNIECIE O THEONIE - ma zapasc PRZED tym dniem (prerogatywa Krola)
- **300-04-01** — KANCELARIA KORONY - data ustanowienia
- **300-04-05** — brat Gorren wyjezdza z Winterfell (rubryka C rejestru)
- **300-06-koniec** — TRAKTAT Z DORZECZEM - termin klauzuli ratyfikacyjnej

## LUDZIE NA SCENIE
- **Luwin** (`maester_luwin`) — maester Winterfell (dwór Starków) — uczony, rządzi skła… · nast ZYCZLIWY -> PROFESJONALNY PODZIW/ZAUFANIE ROBOCZE (0813): po arcyrachunku zapasow (nat.100) Luwin uznaje Symona za rownego-lub-lepszego w rachunkach; trust glęboki
- **Roggen** (`szafarz_roggen`) — starszy szafarz zachodnich składów Winterfell (sługa od… · nast nieznane (nie kontaktowani; Symon obserwuje z boku)
- **Medger Cerwyn** (`lord_medger_cerwyn`) — lord rodu Cerwyn (zamek na goscincu ~pol dnia pod Winte… · nast cieply -> PRZYJACIEL (07-10): uklad przybity + Symon spytal 'jak mu sie zyje', Medger sie otworzyl
- **Arya Stark** (`arya_stark`) —  · nast ?
- **mistrz Beron** (`notariusz_beron`) —  · nast ?
- **Bran Stark** (`bran_stark`) — syn Neda, sparalizowany po upadku z wiezy (~10l); bystr… · nast cieply/wdzieczny (Symon dal mu przyszlosc po upadku - nie litosc lecz droga umyslu)
- **Sansa Stark** (`sansa_stark`) — lady, przezyla lata w klatce Cersei/Joffreya (widziala … · nast czujna/wyuczona nieufnosc (kazdy w KP czegos chcial) - ale Symon rozbroil pierwsza szczeline nie chcac od niej NICZEGO ('dziekuje ze nie klamiecie ladniej')
- **Rickon Stark** (`rickon_stark`) — dziki po stratach (ojciec/wojna/rozdzielenie); wilkor K… · nast dziki/nieufny jak zwierze; Symon nie napieral/nie balo sie -> Kudlacz przestal warczec, 'ty jesteś ten co pisze' (poczatek, nie oswojenie)
- **mistrz Gawen (Skarbnik Korony)** (`gawen_skarbnik`) —  · nast ?
- **mistrz Rodwell (Dyrektor Domu Starkow)** (`rodwell_dyrektor_domu_starkow`) —  · nast ?
- **Ser Alyn** (`ser_alyn_zastepca`) — zastepca ser Rodrika Cassela; garnizon Winterfell · nast szacunek zawodowy, mocno w gore (299-09-11) - uczy ciecia sadowego
- **Stara Niania** (`stara_niania`) —  · nast ?
- **Orwyl** (`orwyl_zbrojmistrz`) —  · nast ?
- **Oswyn Miarka** (`oswyn_miarka`) — miernik/urzednik miejski Zimowego Miasta - spichlerz mi… · nast rzeczowy, uparty; woli sie spoznic niz przyniesc niepewna liczbe
- **Robb Stark** (`robb_stark`) — dziedzic Winterfell, l.15 - TRZYMA grod jako p.o. pana … · nast UFA gleboko + od 09-30 CZLOWIEK RADY (chce Symona przy swojej radzie dla umyslu, nie tylko taboru)
- **Ser Rodrik Cassel** (`rodrik_cassel`) —  · nast ?
- **Roslin Frey (kandydatka - lagodny standout)** (`roslin_frey`) — KROLOWA POLNOCY (od wesela w Blizniakach, sierpien/wrze… · nast ?

## ZEGARY
- ◆ `?` draw_nesta: Miesieczny draw wspolnika ze spolki Nesty (6 jel) -> depozyt. || 297-02-19: ODPALIL - draw wspo…
- ◆ `?` polnoc_halvard_wiesci: Stan polnocnego kanalu (drewno/futra) niepewny: sroga zima w glebi Polnocy, Halvard (faktor Tor…
- ◆ `?` canary_szept_przeciek: 298-10-26 noc: WNYK (canary) zastawiony z Blackfishem - dwie zatrute przynety: (A) falszywy det…
- ◆ `?` oko_blizniaki_frey: 298-10-27: Willa zaklada OKO NA BLIZNIAKACH (stały nasluch Freya - hedżowanie/kontakt Frey<->Ty…
- ◆ `?` front_zelaznych_greyjoy: 298-10-29: BALON GREYJOY oglosil sie Krolem Wysp Zelaznych; longshipy bija w ZACHODNI brzeg Pol…
- ◆ `?` theon_przechylenie_wiernosc: 298-10-29: Symon PRZECHYLA Theona ku wiernosci - lek na rane (glod przynaleznosci): prawdziwe u…
- ◆ `?` amfibie_rozbudowa: 298-10-31 (rzut 61): rozbudowa floty amfibii/plaskodennych - mandatem prowiantmistrza drewno+ci…
- ◆ `?` agenda_szachownica: 298-10-31 TEMATY DO ROZEGRANIA (z doktryny 5 krolow): (1) RENLY-SONDA - dyplomatyczna sonda ku …
- ◆ `?` jaime_dzwignia_tywin: 298-11-01 (rzut 58): Jaime=najciezsza karta na Tywina, wart TRZYMANY nie wydany. Robb pojal: (a…
- ◆ `NIEAKTUALNY — Renly nie zyje (stan_poludnia_zelazny_tron_299_07); do rozstrzygniecia, czy sonda idzie ku samym Tyrellom` renly_sonda: 298-11-01 (rzut 48): cichy feeler ku Renly'emu/Tyrellom siatka Symona (deniable, low-commitment…

## WATKI OTWARTE (687; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
- `traktat_handlowy_z_dorzeczem_300_02` [otwarty] 
- `cztery_puste_miejsca_na_nazwiska_300_02` [otwarty] 
- `cztery_listy_przedpoludnia_300_02_07` [otwarty] 
- `rachunek_drogi_i_liczba_dla_rickona_300_02` [otwarty] 
- `objazd_korony_300_02` [otwarty] 
- `zeszyt_sansy_kto_komu_ustepuje_300_02` [otwarty] 
- `znajdowanie_ludzi_ktorzy_umieja_liczyc_300_02` [otwarty] 
- `szkola_tallych_300_02` [otwarty] 
- `mchowe_jastrzebie_straz_lenna_300_02` [otwarty] 
- `spichlerz_polnocy_mistrz_zapasow_zimowych_300_02` [otwarty] 
- `wychowankowie_winterfell_300_02` [otwarty] 
- `DANINA_LENNA_299_09_04` [otwarty] 
- `zelazne_wyspy_theon_300_02` [otwarty] 
- `lista_jencow_korony_polnocy_299_11` [otwarty] 
- `standard_traktu_polnocy_299_09` [otwarty] 
- `projekt_cailin` [otwarty] 
- `poprawki` [otwarty] 
- `rzadca_warryn` [otwarty] 
- `nina_zielarka_fosy` [otwarty] 
- `maester_wystan_fosy` [otwarty] 
- `rozdroze_placowka_domu_tally` [otwarty] 
- `kto_skupuje_zboze_w_dorzeczu` [otwarty] 
- `catelyn_stark` [otwarty] 
- `roose_bolton` [otwarty] 
- `gawen_skarbnik` [otwarty] 
- `system_danin` [otwarty] 
- `theon_greyjoy` [otwarty] 
- `program_okretow_modelowe_kadluby_299_12` [otwarty] 
- `ucho_korony` [otwarty] 
- `kanal_olenna` [otwarty] 
- `wyman_manderly` [otwarty] 
- `pochodzenie_symona_299_09` [otwarty] 
- `maester_aemon` [otwarty] 
- `theomore_mistrz_nauki` [otwarty] 
- `illyrio_mopatis` [otwarty] 
- `torren_solny` [otwarty] 
- `nesta_braavijka` [otwarty] 
- `ustroj_urzedow` [otwarty] 
- `bractwo_rzemiosla_wolnego` [otwarty] 
- `howland_reed` [otwarty] 
- `spis_flory_przesmyku_299_09` [otwarty] 
- `maester_luwin` [otwarty] 
- `obrona_fosy_garnizon` [otwarty] 
- `lecznica_fosy_nina_299_06` [otwarty] 
- `przywilej_bagienny_fosa_300_02` [otwarty] 

## OSTATNIE WPISY DZIENNIKA
- [300-03-03] `ustroj_urzedow`: ### WIECZOR Z CERWYNEM - O KROLESTWIE I O JEGO WLASNYM LENNIE. 300-03-03. Bez rzutow (rozmowa z czlowiekiem, z ktorym juz siedzialo sie przy ogniu 300-02-19). || ## O KROLESTWIE - DIAGNOZA C…
- [300-03-03] `system_oswiaty_polnocy_struktura_299_06`: ### WIECZOR Z CERWYNEM - O KROLESTWIE I O JEGO WLASNYM LENNIE. 300-03-03. Bez rzutow (rozmowa z czlowiekiem, z ktorym juz siedzialo sie przy ogniu 300-02-19). || ## O KROLESTWIE - DIAGNOZA C…
- [300-03-03] `projekt_cailin`: ### WIECZOR Z CERWYNEM - O KROLESTWIE I O JEGO WLASNYM LENNIE. 300-03-03. Bez rzutow (rozmowa z czlowiekiem, z ktorym juz siedzialo sie przy ogniu 300-02-19). || ## O KROLESTWIE - DIAGNOZA C…
- [300-03-03] `korona/CERWYN`: ### WIECZOR Z CERWYNEM - O KROLESTWIE I O JEGO WLASNYM LENNIE. 300-03-03. Bez rzutow (rozmowa z czlowiekiem, z ktorym juz siedzialo sie przy ogniu 300-02-19). || ## O KROLESTWIE - DIAGNOZA C…
- [300-03-03] `projekt_cailin`: ### ODPIS URZADZEN FOSY DLA CERWYNA - zgoda, 300-03-03. Bez rzutow. || CO IDZIE: rejestr dniowek z kolumna CO UMIE (i dwa rodzaje wpisu w jednym rzedzie - imie albo znak) - proba wstepna prz…
- [300-03-03] `wielka_rada_porzadek_obrad_300_04`: ### ODPIS URZADZEN FOSY DLA CERWYNA - zgoda, 300-03-03. Bez rzutow. || CO IDZIE: rejestr dniowek z kolumna CO UMIE (i dwa rodzaje wpisu w jednym rzedzie - imie albo znak) - proba wstepna prz…
- [300-03-03] `spis_mieszkancow_fosy_299_06`: ### ODPIS URZADZEN FOSY DLA CERWYNA - zgoda, 300-03-03. Bez rzutow. || CO IDZIE: rejestr dniowek z kolumna CO UMIE (i dwa rodzaje wpisu w jednym rzedzie - imie albo znak) - proba wstepna prz…
- [300-03-03] `korona/CERWYN`: ### ODPIS URZADZEN FOSY DLA CERWYNA - zgoda, 300-03-03. Bez rzutow. || CO IDZIE: rejestr dniowek z kolumna CO UMIE (i dwa rodzaje wpisu w jednym rzedzie - imie albo znak) - proba wstepna prz…
- [300-03-03] `wielka_rada_porzadek_obrad_300_04`: ### PRZEGLAD PORZADKU OBRAD Z CERWYNEM - 300-03-03. Bez rzutow (jego fach: on ten tryb ulozyl). || ## ⚡ ZNALAZL ZMIANE, KTOREJ NIKT NIE ZAUWAZYL, BO ZASZLA WCZORAJ ## ### PIERWSZE GLOSOWANIE…
- [300-03-03] `mur_mance_rayder_i_lud_za_murem_299_09`: ### PRZEGLAD PORZADKU OBRAD Z CERWYNEM - 300-03-03. Bez rzutow (jego fach: on ten tryb ulozyl). || ## ⚡ ZNALAZL ZMIANE, KTOREJ NIKT NIE ZAUWAZYL, BO ZASZLA WCZORAJ ## ### PIERWSZE GLOSOWANIE…
- [300-03-03] `spichlerz_polnocy_mistrz_zapasow_zimowych_300_02`: ### PRZEGLAD PORZADKU OBRAD Z CERWYNEM - 300-03-03. Bez rzutow (jego fach: on ten tryb ulozyl). || ## ⚡ ZNALAZL ZMIANE, KTOREJ NIKT NIE ZAUWAZYL, BO ZASZLA WCZORAJ ## ### PIERWSZE GLOSOWANIE…
- [300-03-03] `korona/CERWYN`: ### PRZEGLAD PORZADKU OBRAD Z CERWYNEM - 300-03-03. Bez rzutow (jego fach: on ten tryb ulozyl). || ## ⚡ ZNALAZL ZMIANE, KTOREJ NIKT NIE ZAUWAZYL, BO ZASZLA WCZORAJ ## ### PIERWSZE GLOSOWANIE…
