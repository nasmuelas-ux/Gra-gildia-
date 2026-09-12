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
- **Data:** 300-02-25 wieczor · zima (300)
- **Miejsce:** FOSA CAILIN - wlasne lenno. Przyjazd po czterech miesiacach. Cerwyn przyjezdza 2.-5. III na trzy dni.
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 85 · Sytosc 64 · Zmeczenie 58**

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
| Symon | odpowiedź **burmistrzowi**: TERMIN, nie łaska | **SPÓŹNIONE — 3 miesiące** | 299-11 |
| Symon → Theonowi | „będę ci mówił" | **BEZ TERMINU** | 300-02-18 |
| Gawen | **liczący** — sześć wierszy, ilu ludzi przy której robocie | **BEZ DATY** ⚠️ | 300-02-20 |
| Cerwyn | wezwanie szafarza demeny + wyrok Hobba | **88 DNI PO TERMINIE** | 300-02-20 |
| **Starkport / Cypel** | ### PUSTY | ekipa dopiero zbierana |
| **Trakt: Bliźniaki · Riverrun · Fosa–Cerwyn–Winterfell** | ### PUSTY | policzone, niezaczęte |
| **Mennica Wilk** | ### PUSTY | dała mniej, niż kosztował stempel |
| Stannis — Mur, czerwona kapłanka | Wyman / Davos | bez terminu | 299-12-29 |
| **Daenerys** | Nesta | III/300 | ### ani jednej drogi |

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

## WATKI OTWARTE (660; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
- `maester_willam_stary_zamek_299_11` [otwarty] 
- `aemon_rivers_skrzynia_299_11` [otwarty] 
- `ZYCIE_PRYWATNE` [otwarty] 
- `lista_wymian_jencow_korony_299_11` [otwarty] 
- `przeprawa_zimowa_do_braavos_299_12` [otwarty] 
- `ilario_wagowy_braavos_299_12` [otwarty] 
- `sukcesja_morskiego_pana_braavos_299_12` [otwarty] 
- `zelazny_bank_negocjacje_299_12` [otwarty] 
- `handel_polnocnym_drewnem_braavos_299_12` [otwarty] 
- `werbunek_dla_fosy_w_braavos_299_12` [otwarty] 
- `dom_prestayn_braavos_299_12` [otwarty] 
- `korespondencja_braavos_299_12` [otwarty] 
- `budowniczy_projekt_cailin_299_12` [otwarty] 
- `dom_antaryon_braavos_299_12` [otwarty] 
- `jak_obalic_polnoc_model_zagrozenia_299_12` [otwarty] 
- `strategia_krolestwa_polnocy_299_12` [otwarty] 
- `kamieniczka_schody_zamkowe` [otwarty] 
- `bilans_domu_tally_300_01` [otwarty] 
- `dom_audytowy_tally_300_01` [otwarty] 
- `kto_pyta_o_polnocne_zboze_300_01` [otwarty] 
- `relief_domu_tally_299_05` [otwarty] 
- `podroz_bialy_port_winterfell_300_02` [otwarty] 
- `rejestr_rozwoju_polnocy_300_02` [otwarty] 
- `przystanie_ladunkowe_wschodu_300_02` [otwarty] 
- `spichlerz_polnocy_dwa_etapy_300_02` [otwarty] 
- `zakaz_wylacznosci_faktora_i_porty_jako_komory_300_02` [otwarty] 
- `wielka_rada_porzadek_obrad_300_04` [otwarty] 
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

## OSTATNIE WPISY DZIENNIKA
- [300-02-25] `deficyt_zywnosci_fosy_zima_299_06`: ### CENTRALIZACJA ZIARNA NA FOSIE - PRZYJETE PRZEZ GRACZA: 'A od jutra, C + D do siodmego'. ### A - JEDNA KARTA, DWIE RECE, OD 300-02-26. Nic sie nie zwozi, nic nie zmienia wlasciciela. CO D…
- [300-02-25] `deficyt_zywnosci_fosy_zima_299_06`: ### VOID (GM) - W TEJ SAMEJ ROZMOWIE: napisalem 'ziarno siewne trzeba rozgrodzic, zanim gospodarze przestana moc zmienic zdanie co do siewu; ten dzien nazwaliscie sami, Warryn odpisal wam go…
- [300-02-25] `spichlerz_polnocy_mistrz_zapasow_zimowych_300_02`: ### CENTRALIZACJA ZIARNA NA FOSIE - PRZYJETE PRZEZ GRACZA: 'A od jutra, C + D do siodmego'. ### A - JEDNA KARTA, DWIE RECE, OD 300-02-26. Nic sie nie zwozi, nic nie zmienia wlasciciela. CO D…
- [300-02-25] `spichlerz_polnocy_mistrz_zapasow_zimowych_300_02`: ### VOID (GM) - W TEJ SAMEJ ROZMOWIE: napisalem 'ziarno siewne trzeba rozgrodzic, zanim gospodarze przestana moc zmienic zdanie co do siewu; ten dzien nazwaliscie sami, Warryn odpisal wam go…
- [300-02-25] `soltysi_i_samorzad_lenna_299_08`: ### VOID (GM) - W TEJ SAMEJ ROZMOWIE: napisalem 'ziarno siewne trzeba rozgrodzic, zanim gospodarze przestana moc zmienic zdanie co do siewu; ten dzien nazwaliscie sami, Warryn odpisal wam go…
- [300-02-25] `rzadca_warryn`: ### DWA ZASTRZEZENIA WARRYNA PRZYJETE DO WIADOMOSCI, NIEROZSTRZYGNIETE: ### (1) KWIT PRZY BRAMIE: 'podpis, ktory ma byc PRZY BRAMIE, nie jest podpisem, ktory mozna dac Z ZAMKU'. Warryn siedz…
- [300-02-25] `lenno/WARRYN`: ### DWA ZASTRZEZENIA WARRYNA PRZYJETE DO WIADOMOSCI, NIEROZSTRZYGNIETE: ### (1) KWIT PRZY BRAMIE: 'podpis, ktory ma byc PRZY BRAMIE, nie jest podpisem, ktory mozna dac Z ZAMKU'. Warryn siedz…
- [300-02-25] `lenno/ORLAND KORZEC`: ### CENTRALIZACJA ZIARNA NA FOSIE - PRZYJETE PRZEZ GRACZA: 'A od jutra, C + D do siodmego'. ### A - JEDNA KARTA, DWIE RECE, OD 300-02-26. Nic sie nie zwozi, nic nie zmienia wlasciciela. CO D…
- [300-02-25] `soltysi_i_samorzad_lenna_299_08`: ### PYTANIE GRACZA: 'panszczyzna zniesiona dla nowych - jaki to efekt daje?'. ODPOWIADA WARRYN, bez rzutu (wlasny, oplacany czlowiek melduje z wykonania wlasnej reformy - zasada 7). Reforma …
- [300-02-25] `rzadca_warryn`: ### PYTANIE GRACZA: 'panszczyzna zniesiona dla nowych - jaki to efekt daje?'. ODPOWIADA WARRYN, bez rzutu (wlasny, oplacany czlowiek melduje z wykonania wlasnej reformy - zasada 7). Reforma …
- [300-02-25] `lenno_fosa_cailin_administracja_299_05`: ### PYTANIE GRACZA: 'panszczyzna zniesiona dla nowych - jaki to efekt daje?'. ODPOWIADA WARRYN, bez rzutu (wlasny, oplacany czlowiek melduje z wykonania wlasnej reformy - zasada 7). Reforma …
- [300-02-25] `lenno/WARRYN`: ### PYTANIE GRACZA: 'panszczyzna zniesiona dla nowych - jaki to efekt daje?'. ODPOWIADA WARRYN, bez rzutu (wlasny, oplacany czlowiek melduje z wykonania wlasnej reformy - zasada 7). Reforma …
