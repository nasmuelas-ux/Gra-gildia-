# STAN GRY — indeks (regenerowany z JSON+JSONL, NIE edytuj recznie)
_Zrodlo prawdy: gra/*.json + gra/db/wpisy.jsonl. Szczegoly: `python3 gra/db.py pokaz <klucz>` / `szukaj <fraza>` / `dzien <data>`._

## ⚠️ OBOWIAZKOWA RAMA RANKA (nie pomijac po kompaktowaniu!)
Kazdy RANEK renderuj W TEJ KOLEJNOSCI, ZAWSZE:
1. Naglowek daty + pogoda/zdarzenie
2. Kalendarz (targ/swieto/clo)
3. **📬 WIADOMOSCI / KORESPONDENCJA** — osobna ramka: kto sie odezwal/przyslal poslanca/jaka wiesc/co dojrzalo (rzut na inbound); jak nic → napisz "cisza". TO NIE JEST NA ZADANIE — renderuj SAM co ranek.
4. STATUS: jedzenie (sytosc/zmeczenie/zdrowie) + hajs (wolne + skrot)
5. Watki w toku → pytanie "co robisz" (bez listy opcji)

## ⚠️ ZAPIS STANU — NOWY TRYB (od 299-09-11)
NIE przepisuj wielkich JSON-ow. Dopisuj JEDNA LINIE do dziennika:
```
python3 -c "import sys; sys.path.insert(0,'gra'); import db; db.dopisz('watki','<klucz>','RRR-MM-DD','<tresc>')"
```
Zrodla: `watki` · `npc` (klucz = `sekcja/id`) · `swiat` · `postac`. Metadane (status, termin, kasa, sytosc) edytuje sie w JSON jak dotad.

## TERAZ
- **Data:** 300-02-25 wieczor · zima (300)
- **Miejsce:** WINTERFELL - komnata Namiestnika. Dwa dni do wyjazdu kolumny na Fose.
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 85 · Sytosc 64 · Zmeczenie 58**

## KASA (1 jelen=100 mied · 1 smok=200 jel)
- **Wolne:** 2 smokow + 55 jeleni + 1 mied
- **Dzien Bilansu:** 1. dnia miesiaca · nastepny 300-03-01

## UMIEJETNOSCI
pismo 8 · rachunki 10 · prawo 9 · retoryka 8 · jezyki 8 · spryt_uliczny 8 · kondycja 7 · rzemioslo 1 · handel 8 · walka 6 · geometria 5 · czytanie_ludzi 10 · organizacja 9 · audyt 9 · finanse 9 · wlodarstwo 8 · historia 6 · wiedza_o_swiecie 7 · polityka 10
**Reputacja:** port 38 · schody_zamkowe 40 · cech_pisarzy -6 · wiara 96 · zamek 24 · cech_kolodziejow 42

## ⚠️ TRZY PUDELKA — SPRAWDZ PRZED KAZDA SCENA Z NPC
_TRZY PUDELKA. Ani jeden czlowiek nie sluzy w dwoch. Przed kazda scena z NPC: sprawdz, CZYJ jest, GDZIE siedzi i CO DO NIEGO NIE TRAFIA. Jesli NPC mialby zaraportowac cos spoza swojego pudelka - to znaczy, ze watki sie pomieszaly._

**DOM TALLY** (Kasa 1) — handel, filie, papiernia, warzelnia, bursztyn, weksle, siatka prywatna, koordynacja dom<->lenno
  - ### NIE TU: korespondencja Korony, porzadek obrad Rady, rejestr przedsiewziec Korony, poczta Korony, sprawy urzedow koronnych
  - **GARRICK** — Kanclerz Kancelarii Namiestnika (dom+lenno) · _FOSA CAILIN_ · raport: Symon
  - **WILLA** — kanclerz-archiwista, siatka/wywiad domu · _w terenie_ · raport: Symon
  - **HAL** — dyrektor Domu Handlowego · _BIALY PORT_ · raport: Symon
  - **NESTA** — wspolniczka, Braavos · _BRAAVOS_ · raport: Symon (partnerka, nie podwladna)
  - **LUCAN** — czlowiek domu na poludniu · _DORZECZE_ · raport: Symon
  - **MARR** — szlifierz bursztynu · _?_

**LENNO FOSY** (Kasa 2) — grobla i roboty, myto, spis mieszkancow, solectwa, sad grodzki, Mchowe Jastrzebie, miasteczko Cailin (ma WLASNA kase miejska)
  - ### NIE TU: clo Korony (to Kasa 3, tylko pobierane reka lenna)
  - **ALYS** — majordom przy liczbach · _FOSA_ · raport: Symon/Garrick
  - **BRAN** — majordom robot (NIE Brandon Stark) · _FOSA_ · raport: Symon/Garrick
  - **HENDRY** — marszalek/druzyna lenna · _FOSA_
  - **RZADCA** — rzadca lenna · _FOSA_
  - **BURMISTRZ (wagowy)** — burmistrz miasta Cailin z wyboru 299-11-01 · _MIASTECZKO CAILIN_ · raport: rada miejska, NIE Symon  ⚠️ pisze do KORONY bezposrednio w sprawie prawa skladu - tak zadal Symon

**KORONA** (Kasa 3) — kancelaria Korony, poczta Korony, rejestr przedsiewziec, porzadek obrad Rady, clo, daniny, sady, eskadra, Mur
  - **BERON** — SEKRETARZ KANCELARII KORONY · _WINTERFELL_ · raport: KROL  ⚠️ tu trafia wszystko koronne; przysiega Krolowi, placi Kasa 3, zostaje gdy Namiestnik odchodzi
  - **GAWEN** — Skarbnik Korony · _WINTERFELL_ · raport: KROL
  - **MEDGER CERWYN** — Justycjariusz Polnocy · _ZAMEK CERWYN + objazd_ · raport: KROL
  - **TORREN SOLNY** — Pierwszy Admiral Korony · _DUSTINPORT_ · raport: KROL  ⚠️ NIE dostal pisma o granicach urzedu - dlug Symona
  - **OSRIC** — marszalek / oddzial pod Murem · _MUR/w drodze_
  - **RODRIK CASSEL** — mistrz nad bronia Winterfell · _WINTERFELL_
  - **LUWIN** — maester Winterfell · _WINTERFELL_
  - **MYLES** — wybrany przez KROLA na glos przy lordach, X/299 · _WINTERFELL (przyjechal 300-02-19)_
  - **THEOMORE** — maester, pomiar Przesmyku · _WINTERFELL (przyjechal 300-02-19)_
  - **KASZTELAN WINTERFELL** — rejestr zamku · _WINTERFELL_
  - ### SZEW: **GARTH** — czlowiek LENNA stojacy przy komorze celnej KORONY - pobiera clo Kasy 3 reka lenna. Jedyny prawdziwy szew Fosy. Nie dostal pisma o granicach urzedu (obiecane przed przyjazdem Cerwyna).
  - ### SZEW: **POCZTA KORONY** — przelozony poczty odpowiada Beronowi w Winterfell, ale Garrick nia dysponuje, bo jest na miejscu. Chodzi na zdrowy rozsadek i kiedys przestanie.

## 🧩 SPRAWY SIE PRZEPLATAJA — CZYSTE MA BYC ROZSTRZYGNIECIE, NIE SPRAWA
_LUDZIE maja jedno pudelko. SPRAWY maja ich kilka i tak ma byc. Czyste musi byc nie to, kogo sprawa DOTYKA, tylko: KTO ROZSTRZYGA (jeden), Z CZYJEJ KASY (jedna), KTO PISZE, KTO CZYTA, i KTO NIE MOZE TEGO TKNAC._
### SYMON JEST JEDNOCZESNIE: Namiestnikiem Korony, panem lenna Fosy i wlascicielem Domu Tally. KAZDA sprawa na Fosie przechodzi przez wszystkie trzy jego role naraz. To nie jest wada swiata - to jest osnowa calej gry.
- **PRAWO SKLADU DLA MIASTA CAILIN** — dotyka: Korona, Lenno Fosy, Miasto Cailin, Dom Tally · **rozstrzyga: JUSTYCJARIUSZ CERWYN - bo Symon jest strona**
- **KOMORA CELNA FOSY** — dotyka: Korona, Lenno Fosy · **rozstrzyga: KORONA (Kasa 3)**
- **GROBLA I PRZENIOSKA** — dotyka: Korona, Lenno Fosy, Dom Tally · **rozstrzyga: ?**
- **SPIS MIESZKANCOW MIASTECZKA** — dotyka: Lenno Fosy, Miasto Cailin · **rozstrzyga: ?**
**Zamiast odsylac NPC, GM pyta:** Ktora CZESC tej sprawy jest twoja? · Kto to ROZSTRZYGA i czy ja jestem strona? · Z ktorej kasy to idzie? · Kto tego NIE MOZE tknac i dlaczego?

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

## WATKI OTWARTE (658; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
- `zamarznieta_zatoka_wschod_299_11` [otwarty] 
- `stary_zamek_locke_299_11` [otwarty] 
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

## OSTATNIE WPISY DZIENNIKA
- [300-02-18] `poprawki`: ### VOID (GM) - SPRAWA THEONA NIE IDZIE POD GLOSOWANIE RADY. Poprawka gracza, druga tego samego rodzaju. ### BLAD: dwukrotnie wlozone w usta zdanie 'jesli Rada powie, ze ma zostac zakladniki…
- [300-02-18] `rickon_stark`: ### POZEGNANIE Z RICKONEM - NOC PRZED WYJAZDEM. Bez rzutu. ### KIJ: JEDENASCIE NACIEC, ciete krzywo ale rowno, po jednym, od 300-02-07. ### PYTANIE DZIECKA, KTOREGO SYMON NIE PRZEWIDZIAL: 'A…
- [300-02-18] `bran_stark`: ### POZEGNANIE Z BRANEM - I DWIE RZECZY, KTORE ON POLOZYL PIERWSZY. Pozna noc 300-02-18. Bez rzutu. ### ### PIERWSZE ZDANIE BRANA, ZAMIAST POWITANIA: 'ZMIENILISCIE RUBRYKE D I DOWIEDZIALEM S…
- [300-02-18] `sansa_stark`: ### POZEGNANIE Z SANSA - NOC PRZED WYJAZDEM. Bez rzutu. ### OTWARCIE JEJ: 'Wszyscy dzis chodza po zamku i sie zegnaja - slychac drzwi. Byliscie juz u Rickona i u Brana. Wiem, w jakiej kolejn…
- [300-02-19] `sprawa_rymana_justycjariusz_299_08`: ### WIECZOR PRZY OGNIU U CERWYNA - SYMON PRZYZNAL SIE DO ODWOLANEGO ROZKAZU. Zamek Cerwyn, 300-02-19. Bez rzutu na wyznanie; RZUT 30 na to, czy slad czlowieka Garricka zostal zauwazony w Sta…
- [300-02-19] `lista_jencow_korony_polnocy_299_11`: ### NOC U CERWYNA - WYMIANA JENCOW POSTAWIONA NA NOGI. Zamek Cerwyn, 300-02-19. Bez rzutu (wlasny urzednik, rzecz lezaca od 21 miesiecy). ### SPROSTOWANIE CERWYNA CO DO WLASNYCH SLOW: 'Nie p…
- [300-02-20] `kasztelan_winterfell`: (patrz medger_cerwyn 300-02-20 - wyrok niewykonany przeciw demenie Korony, szafarz demeny wezwany do wyjasnienia)
- [300-02-20] `medger_cerwyn`: ### RANEK U CERWYNA - DWIE SPRAWY ROZSTRZYGNIETE. Zamek Cerwyn, 300-02-20. Bez rzutow (wlasny urzednik, praca wlasna). ### == I. SPRAWA, KTORA POLOZYL SAM: WYROK NIEWYKONANY == WYROK Z 299-1…
- [300-02-20] `wielka_rada_porzadek_obrad_300_04`: ### PISANIE PRZED RADA - STAN I PRAWDZIWY TERMIN. Zamek Cerwyn, 300-02-20. Bez rzutu. ### CO JEST NAPISANE: KODEKS GOTOWY (czystopis pelny) - ALE LEZY W DWOCH TEKACH I OBIE SA CERWYNA. 'Praw…
- [300-02-20] `standard_traktu_polnocy_299_09`: ### PROGRAM DROGOWY POSTAWIONY JAKO JEDNA RZECZ - i rozstrzygniecie, KTO TO KOORDYNUJE. Zamek Cerwyn, 300-02-20. Bez rzutu. ### RAMA GRACZA: plan Fosy to plan na wiele lat; lenno ma PRZYCIAG…
- [300-02-25] `dziennik`: ### DROGA ZAMEK CERWYN -> FOSA CAILIN, 20.-25. dnia II Miesiaca (rzut 56 - droga jak droga, bez przygod i bez laski). ### DZIEN I: Theon milczal pol dnia, potem podjechal i powiedzial jedno …
- [300-02-25] `projekt_cailin`: ### CZTERY MELDUNKI NA DZIEDZINCU FOSY, 300-02-25 wieczor. Bez rzutow (raporty wlasnych, oplacanych ludzi). Alys: 'Cztery rzeczy czekaja i ZADNA NIE JEST ZLA.' ### == (1) ALYS - SPIS MIESZKA…
