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
- **Data:** 300-02-07 ranek · zima (300)
- **Miejsce:** WINTERFELL. O switu wyszly dwa kruki: do marszalka Osrica (tlumacz z Kasy III, rozmowa z Rayderem, poslaniec, linijka o …
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 83 · Sytosc 30 · Zmeczenie 15**

## KASA (1 jelen=100 mied · 1 smok=200 jel)
- **Wolne:** 2 smokow + 95 jeleni + 1 mied
- **Dzien Bilansu:** 1. dnia miesiaca · nastepny 300-03-01

## UMIEJETNOSCI
pismo 8 · rachunki 10 · prawo 9 · retoryka 8 · jezyki 8 · spryt_uliczny 8 · kondycja 7 · rzemioslo 1 · handel 8 · walka 6 · geometria 5 · czytanie_ludzi 10 · organizacja 9 · audyt 9 · finanse 9 · wlodarstwo 8 · historia 6 · wiedza_o_swiecie 7 · polityka 10
**Reputacja:** port 38 · schody_zamkowe 40 · cech_pisarzy -6 · wiara 96 · zamek 24 · cech_kolodziejow 42

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

## WATKI OTWARTE (637; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
- `granice_poselstwa_namiestnik_za_morzem_299_09` [otwarty] 
- `kto_jest_namiestnikiem_gdy_nie_ma_namiestnika_299_09` [otwarty] 
- `kanon_nauki_rodu_starkow_299_09` [otwarty] 
- `kancelaria_namiestnika_299_09` [otwarty] 
- `list_warunkowy_obrony_korony_299_09` [otwarty] 
- `rozproszone_sklady_korony_299_09` [otwarty] 
- `relief_i_cena_zboza_jako_sonda_299_09` [otwarty] 
- `moratorium_na_nowe_reguly_299_09` [otwarty] 
- `mur_trzech_kas_i_wladza_ponad_procedura_299_09` [otwarty] 
- `dlug_korony_wobec_domu_tally_299_10` [otwarty] 
- `lenno_fosy_rozliczenie_299_10` [otwarty] 
- `woz_w_lodzie_przy_brodzie_299_09` [otwarty] 
- `audyt_fosy_299_10` [otwarty] 
- `willa_prospekt_wywiad` [otwarty] 
- `danina_karholdu_299_10` [otwarty] 
- `migracja_wschodniego_wybrzeza_299_10` [otwarty] 
- `raport_osrica_z_muru_299_10` [otwarty] 
- `harrion_karstark_poszukiwanie_299_11` [otwarty] 
- `napad_w_borze_hornwood_299_11` [otwarty] 
- `sad_w_hornwood_299_11_15` [otwarty] 
- `palenie_zmarlych_polnoc_299_10` [otwarty] 
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

## OSTATNIE WPISY DZIENNIKA
- [300-02-06] `objazd_wschodu_jako_pierwszy_objazd_poborowy_299_09`: ### SPRAWOZDANIE Z OBJAZDU ZLOZONE KROLOWI - SZESC BRAM, DOM PO DOMU. Winterfell, 300-02-06, przy dziennym swietle, z pisarzem i arkuszami. Bez rzutow (sprawozdanie Namiestnika przed Krolem)…
- [300-02-06] `objazd_wschodu_jako_pierwszy_objazd_poborowy_299_09`: ### SPRAWOZDANIE Z OBJAZDU ZLOZONE KROLOWI - SZESC BRAM, IMIONA I OSTRZEZENIA. Winterfell, 300-02-06, przy dziennym swietle, z pisarzem. Bez rzutow. ### == REJESTR POLEGLYCH KORONY POLNOCY (…
- [300-02-06] `projekt_cailin_trakt_forteca_miasto_299_09`: ### PAKT DUSTINPORT I CZESC CZWARTA POLOZONE PRZED KROLEM. Winterfell, 300-02-06. Bez rzutow. ### == DUSTINPORT - CO ISTNIEJE I DLACZEGO NIE ODPOWIADA NA TEN KRYZYS == Lady Barbrey Dustin od…
- [300-02-06] `spotkanie_ze_stannisem_w_pentos_299_09`: ### SKRZYNIA Z PENTOS OTWARTA PRZED KROLEM. Winterfell, wieczor 300-02-06, drzwi zamkniete. Bez rzutow. ### ### TRZECIEJ RELACJI NIE MA. Rozdzielono je na dwa kadluby; trzecia wiezie CZLOWIE…
- [300-02-07] `zbior_swiadectw_dlugiej_nocy_299_09`: ### DZIEWIEC ODPOWIEDZI MAESTEROW ZESTAWIONE Z WYKAZEM KAPLANKI - RZUT 6 (krytycznie nisko). Winterfell, wieczor 300-02-06 i caly 300-02-07, izba archiwum. ROBOTA WYKONANA BEZ BLEDU; MATERIA…
- [300-02-07] `_dziennik_300_02_07`: 300-02-07, WINTERFELL - dzien pochloniety przez robote nad listami maesterow (patrz zbior_swiadectw_dlugiej_nocy_299_09). Pogoda: snieg drobny i rowny, bezwietrznie, mroz lzejszy. INBOUND rz…
- [300-02-06] `poprawki`: ### VOID - PROWADZACY PRZESKOCZYL DZIEN (drugi raz w tej sesji, na wskazanie gracza). ### SKRESLONE W CALOSCI: (a) ze robota nad listami maesterow trwala 'do pozna, potem drugi dzien' i poch…
- [300-02-06] `harrion_karstark_poszukiwanie_299_11`: ### WYMIANA - ROZSTRZYGNIETA Z KROLEM, WIECZOR 300-02-06, WINTERFELL. Bez rzutow. ### SUGESTIA SYMONA: SPROBOWAC WYMIENIC HARRIONA. Krol przyjal jako sugestie, nie wniosek ('za to ostateczni…
- [300-02-06] `mur_mance_rayder_i_lud_za_murem_299_09`: ### ROZKAZ DO MARSZALKA OSRICA - ODPOWIEDZ NA PROSBE Z MELDUNKU SZOSTEGO I OTWARCIE KANALU DO MANCE'A RAYDERA. Winterfell, wieczor 300-02-06, uzgodnione z Krolem. Bez rzutow. Kruk poczta Kor…
- [300-02-06] `czym_ma_byc_bran_stark_299_08`: ### REJESTR SWIADKOW KORONY POLNOCY - ZALOZONY, PROWADZI BRANDON STARK. Winterfell, izba archiwum, wieczor 300-02-06. Bez rzutow. ### KONTEKST: Bran (11 lat) w jeden wieczor zestawil dziewie…
- [300-02-07] `_dziennik_ranek_300_02_07`: RANEK 300-02-07, WINTERFELL. Pogoda rzut 41: szaro, snieg drobny i rowny, mroz umiarkowany, bez wiatru. Trakty przejezdne, nic sie nie zmienia. INBOUND rzut 18: CISZA - z zewnatrz nie przysz…
- [300-02-07] `soltysi_i_samorzad_lenna_299_08`: ### RANEK 300-02-07, WINTERFELL - CZTERY PISMA. Bez rzutow. ### == I. DO BURMISTRZA MIASTA CAILIN == Gratulacje (glosowalo 8 palenisk na 10, u starych i u osadnikow; w piatej wsi glosowalo n…
