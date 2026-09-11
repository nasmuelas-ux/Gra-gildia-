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
- **Data:** 300-02-16 poludnie · zima (300)
- **Miejsce:** WINTERFELL - komnata Namiestnika, ranek. Karta Wychowankow lezy spisana na stole.
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 84 · Sytosc 88 · Zmeczenie 48**

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

## WATKI OTWARTE (653; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
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

## OSTATNIE WPISY DZIENNIKA
- [300-02-16] `traktat_handlowy_z_dorzeczem_300_02`: ### TRAKTAT - AUTORZY, PODZIAL I TERMIN. Rozstrzygniecie gracza: CERWYN I SKARBNIK. ### || POWOD, DLA KTOREGO W OGOLE TERAZ: lady Catelyn wyjechala 299-10-05, a traktat postawiono 300-02-07 …
- [300-02-16] `gawen_skarbnik`: ### ROZKAZ DO SKARBNIKA, 300-02-16, przed wyjazdem Namiestnika (wyjazd 02-19). Bez rzutu. ### PIEC PUNKTOW: (I) OCHMISTRZ WYCHOWANKOW na 300-03-01, trzynascie dni, szuka Gawen - ZATWIERDZA K…
- [300-02-16] `gawen_skarbnik`: ### RUBRYKA KOSZTU POGODY - ZGODA UDZIELONA. ### Gawen prosil o nia 300-02-15 w sprawozdaniu ('cztery smoki piec jeleni za te odwilz, liczac konie; liczba mala i dlatego ja podaje - BO POGOD…
- [300-02-16] `robb_stark`: ### DEKLARACJA O ZARECZYNACH - ROZSTRZYGNIECIE GRACZA: NIE W DRUGIM KRUKU, TYLKO NA WIELKIEJ RADZIE, USTAMI KROLA, PRZY CZTERNASTU LORDACH. ### || POWODY PODANE PRZEZ KROLA: (1) 'Drugi kruk …
- [300-02-16] `bran_stark`: ### BRAN DRUGIM CZYTELNIKIEM REJESTRU - ROZSTRZYGNIECIE GRACZA. Wieza maestera, 300-02-16. Bez rzutu. ### ODRZUCONE NA GLOS PRZED WYBOREM: ZIMOWA STRAZ (Rodrik/Alyn) - 'oddac karte mistrzowi…
- [300-02-16] `ramsay_bastard_dreadfort_watch_299_08`: ### REJESTR ZAMKU ZALOZONY 300-02-16 - TEN SAM WZOR CO REJESTR ZIMOWEGO MIASTA, na pytanie Brana. Pelny tekst: gra/wzor_rejestru_zimowego_miasta_300_02.md (czesc druga). ### || PISZE KASZTEL…
- [300-02-16] `sansa_stark`: ### ZDANIE KROLA PODANE SANSIE CO DO SYLABY - popoludnie 300-02-16, kruzganek. Bez rzutu. ### TRESC: 'Dopoki ucza sie tu wasze dzieci, pod tym dachem nie zostana zawarte zadne zareczyny. Ani…
- [300-02-16] `jedzenie`: 300-02-16 POPOLUDNIE - pierwszy posilek od switu (grochowka na wedzonce, chleb, piwo; kuchnia wydala, co zostalo po poludniu). SYTOSC 62 -> 88. ZMECZENIE 44 -> 48 (popoludnie pracy: Krol dwa…
- [300-02-16] `catelyn_stark`: ### LIST DO LADY CATELYN - NAPISANY I ZAPIECZETOWANY 300-02-16, Winterfell. Wlasna reka, BEZ PIECZECI NAMIESTNIKA (pieczec zmienilaby to w rozkaz, a jej warunek z 299-09-19 brzmial: 'jade ja…
- [300-02-16] `rachunek_drogi_i_liczba_dla_rickona_300_02`: ### KOLUMNA NA FOSE - ZLOZONA 300-02-16. Wyjazd 02-19 o swicie. Bez rzutow. ### || ## I. ESKORTA - SZESCIU, LICZBA RODRIKA ## Symon oddal liczbe Rodrikowi ('Rodrik da') - PIATY RAZ TEGO DNIA…
- [300-02-16] `rachunek_drogi_i_liczba_dla_rickona_300_02`: ### KARTA SIEDMIODNIOWA WINTERFELL -> FOSA - POTWIERDZONA, IDZIE JAK SPISANA. ### POWOD: Namiestnik bedzie SZESC DNI DROGI od Winterfell przez DWADZIESCIA TRZY DNI, a w tym czasie dojrzeje: …
- [300-02-16] `wielka_rada_porzadek_obrad_300_04`: ### DO WIAZKI SZOSTEJ (USTROJ) WPISANE PYTANIE MISTRZA BRONI - ROZSTRZYGNIECIE GRACZA. ### PIERWSZA RZECZ DOLOZONA OD CZASU SCIECIA CZTERDZIESTU POZYCJI DO SZESCIU - I SYMON POWIEDZIAL TO NA…
