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
- **Data:** 299-09-14 ranek · lato (298)
- **Miejsce:** Winterfell - serce Polnocy, siedziba Starkow / dwor Krola Robba; od 299-09-14 KROL WROCIL Z BLIZNIAKOW ZONATY, z krolowa…
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 94 · Sytosc 28 · Zmeczenie 6**

## KASA (1 jelen=100 mied · 1 smok=200 jel)
- **Wolne:** 2 smokow + 95 jeleni + 1 mied
- **Dzien Bilansu:** 1. dnia miesiaca · nastepny 299-10-01

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

## WATKI OTWARTE (564; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
- `lista_z_rozwidlenia_299_09_09` [otwarta_do_sprawdzenia] Lista imion z rozwidlenia - kola i osie, barka na czczo, nazwisko ktore nie padlo
- `spis_przedsiewziec_korony_299_09_10` [gotowy_przed_krola] Spis przedsiewziec Korony - kto prowadzi, ile kosztuje, czego brakuje
- `eskadra_ktora_lowi_koszt_floty_299_09` [do_rozstrzygniecia_przez_krola] Koszt pierwszej eskadry i pytanie, czy wolno im lowic
- `przedsiewziecia_bez_nazwiska_299_09` [obsadzone_2_z_3_starkport_do_opisania] Trzy przedsiewziecia Korony bez czlowieka odpowiedzialnego
- `kancelaria_namiestnika_299_09_10` [stoi_jako_po_do_potwierdzenia_przez_krola] Kancelaria Namiestnika - urzad, ktory ma przetrwac urzednika
- `poczta_korony_stala_linia_299_09` [ustanowiona_do_uruchomienia] Poczta Korony - stala linia Winterfell-Fosa-Bialy Port
- `misja_do_dorzecza_catelyn_299_09` [list_goni_Catelyn_w_drodze] Misja do Dorzecza - Catelyn, Rodwell na wiosne, rachmistrz odbiorczy
- `rymowanka_do_osmiu_299_09_10` [stos_drugi_co_mowi_tylko_jeden] Rymowanka do osmiu - nie uczy liczyc, uczy co robic
- `siec_maesterow_wzajemnosc_299_09` [pierwszy_znak] Siec maesterow - odpis calosci za wklad
- `ustroj_urzedow_redundancja_299_09_10` [projekt_narada_dzis_rada_po_powrocie_krola] Ustroj urzedow i KADRY Korony - p.o. niesie robote, nie obejmuje urzedu
- `kadry_korony_ilu_umie_czytac_299_09_10` [do_polozenia_przed_krolem_pierwszym_zdaniem] Kadry Korony - 40-60 rak potrzeba, dwadziescia jest, polowa u Tallych
- `stypendium_korony_uczniowie_299_09_10` [projekt] Stypendium Korony - dwa lata nauki za cztery lata sluzby
- `praktykanci_w_winterfell_299_09_10` [szkic_do_poprawy] Praktykanci na dworze Krola - chlopcy i dziewczeta, cztery bramy naboru
- `dwor_czy_panstwo_urzedy_ktore_zostaja_299_09_10` [szkic_do_poprawy] Dwor czy panstwo - ktore urzedy jada z Krolem, a ktore zostaja
- `trzy_narzedzia_panstwa_wzory_rachunek_objazd_299_09` [szkic_do_poprawy] Wzory pism, rachunek skladany dwa razy do roku, staly objazd
- `proba_urzednicza_otwarta_299_09_10` [szkic_srodek_ciezkosci_reformy] Proba urzednicza - otwarta dla kazdego, jedzie z objazdem
- `rewizja_szosty_pion_jeden_na_dziesiec_299_09_10` [szkic_domyka_stara_luke] Rewizja - szosty pion, jeden woz na dziesiec wybrany losem przy woznicy
- `heroldowie_korony_299_09_10` [szkic] Heroldowie Korony - glos prawa, poselstwo, ksiega herbow, pierwszenstwo
- `piec_dziur_z_narady_299_09_10` [odpowiedziane_projekt_zetapowany] Piec dziur z narady - kto placi rewizje, sedziowie, Cytadela, Rodwell, eskorta objazdu
- `etapy_budowy_administracji_299_09_10` [przyjete_na_naradzie] Cztery etapy budowy administracji - etap I: kancelarie, pisarze, redundancja
- `oswyn_miarka_burmistrz_handlarz_zbozem_299_09_10` [otwarty_do_rozegrania] Oswyn Miarka - pierwszy burmistrz Polnocy, handlarz zbozem w zimie prawa o skladach
- `miejski_spichlerz_zimowego_miasta_299_09` [wisi_na_jutro] Miejski spichlerz - pierwsza prosba burmistrza, czwarty gracz przy tym samym zbozu
- `szmaty_waskie_gardlo_papieru_299_09_10` [otwarte] Szmaty - wąskie gardlo papieru, a wiec i calego panstwa na papierze
- `kto_placi_mierzacemu_299_09_10` [rozwiazanie_korony_do_przelozenia_na_dom] Kto placi temu, kto mierzy - ta sama dziura u Korony i u domu, znaleziona tego samego dnia
- `skup_scinkow_ogloszona_cena_299_09_10` [list_wyslany] Ogloszona cena skupu scinkow - Mira i Leona, papier dla panstwa
- `sansa_chce_roboty_nie_opieki_299_09_10` [otwarte_do_rozegrania] Sansa: dwie siostry, dwa rozne domy - i jedyna osoba w Winterfell, ktora tam byla
- `relacja_sansy_z_czerwonej_twierdzy_299_09_10` [przerwana_pytaniem_komu_to_powtorzycie] Relacja Sansy - Joffrey, Cersei, Tyrion; stracenie Neda bylo kaprysem, nie planem
- `wyznal_bo_mnie_zobaczyl_299_09_10` [nazwana_i_sprostowana_nie_zamknieta] Rana Sansy - wierzy, ze ojciec sklamal i umarl w hanbie z jej powodu
- `powiedziec_robbowi_dlaczego_ojciec_sie_przyznal_299_09` [do_wykonania_po_powrocie_krola] Powiedziec Krolowi, dlaczego Ned sie przyznal - prosba Sansy
- `jeyne_poole_w_rekach_belisha_299_09` [otwarty] 
- `kto_oplacal_dontosa_299_09` [otwarty] 
- `sansa_jako_zrodlo_dworskie_299_09` [otwarty] 
- `ucho_korony_druga_siatka_299_09` [otwarty] 
- `rozbudowa_siatki_domu_garrick_299_09` [otwarty] 
- `list_do_willi_o_przecieciu_urzedu_299_09` [otwarty] 
- `precedens_wlasciwosci_lord_przed_krolem_299_09` [otwarty] 
- `kalendarz_terminow_korony_299_09` [otwarty] 
- `nauka_ciecia_sadowego_299_09` [otwarty] 
- `kronika_dlugiej_nocy_spisywanie_299_09` [otwarty] 
- `korzenie_symona_299_09` [otwarty] 
- `p_o_rodwella_dwie_polowy_299_09` [otwarty] 
- `spichlerz_miejski_oswyn_299_09` [otwarty] 
- `komory_wodne_dziura_w_poborze_299_09` [otwarty] 
- `zestawienie_dni_barka_komora_299_09` [otwarty] 
- `uklad_celny_pobor_lenna_299_09` [otwarty] 

## OSTATNIE WPISY DZIENNIKA
- [299-09-13] `lord_medger_cerwyn`: 299-09-13: oddal czystopis prawa o skladach w dwoch tekstach, gotowy do pieczeci - pierwszy raz od tygodnia bez nowej dziury. Zamiast dziury przyniosl pytanie sedziego: KTO BEDZIE PIERWSZY. …
- [299-09-13] `oswyn_miarka`: 299-09-13 rano, Winterfell - OSWYN MIARKA PRZYSZEDL Z DRUGIM LICZENIEM. Bez rzutu (urzednik miejski, sam sie zglosil, przynosi wlasna robote). || CO USTALIL: ZBOZE JEST. Nikt nie ukradl. Spi…
- [299-09-13] `prawo_o_skladach_zboza_299_09`: 299-09-13 - PIATE ROZSTRZYGNIECIE, DOPISANE W PRZEDDZIEN PIECZECI (zrodlo: Oswyn Miarka, miernik Zimowego Miasta). PROBLEM: zboze schnie, siada i ubywa go w sposob naturalny i staly; prawo k…
- [299-09-13] `postac`: 299-09-13 - PIERWSZY KWADRANS WEDLE PRZEPISANEGO RYTMU (rzut 56, zwyczajnie - i o to chodzilo). Dziedziniec po odwilzy: BLOTO. Alyn nie odwolal cwiczenia, tylko kazal ZASTOSOWAC wczorajsza n…
- [299-09-13] `postac`: 299-09-13 - TRENING KONDYCYJNY ZARAZ PO KWADRANSIE (rzut 10, nisko). BLAD WLASNY, NIE PECH LOSU. Alyn zgodzil sie, bo kondycja to co innego niz ciecie: 'Ciecie to nawyk i ma byc kwadrans. Ci…
- [299-09-13] `maester_luwin`: 299-09-13 poludnie, wieza maestera - LUWIN OPATRUJE DLONIE SYMONA. Bez rzutu (opieka wlasnego maestera, rutyna). ROBOTA LEKARSKA: przemyl gotowanym winem, MIOD na otwarte miejsca, czyste plo…
- [299-09-13] `swiat`: 299-09-13 popoludnie/wieczor - TEKA NAMIESTNIKA ZLOZONA NA POWROT KROLA (gra/teka_namiestnika_299_09_14.md). Bez rzutu (praca wlasna). SPOSOB: Symon NIE MOGL PISAC (dlonie w opatrunku, zakaz…
- [299-09-13] `notariusz_beron`: 299-09-13: PIERWSZA PRAWDZIWA ROBOTA KANCELARYJNA, wykonana zanim kancelaria formalnie istnieje. Symon nie mogl pisac (dlonie), wiec DYKTOWAL Beronowi cala teke na powrot Krola - kilkanascie…
- [299-09-13] `postac`: 299-09-13 wieczor - ODPOCZYNEK PO ZLOZENIU TEKI. Bez rzutu. Dlonie pulsuja pod opatrunkiem, bok daje o sobie znac przy kazdym obrocie. Symon nie czytal, nie pisal i nikogo nie przyjmowal - s…
- [299-09-14] `swiat`: 299-09-14 - DZIEN POWROTU KROLA. POGODA (rzut 46): szaro, mokro, bez mrozu; bloto po wczorajszej odwilzy nie obeschlo, dziedziniec rozjezdzony. Nic zlego, nic pieknego - dzien do jazdy, nie …
- [299-09-14] `swiat`: 299-09-14 - VOID PROWADZACEGO (ROZSZERZENIE IV). BLAD: napisalem, ze wesele Robb-Roslin DOPIERO NADCHODZI ('terminy sie ustalaja, Blizniaki czekaja'). ZRODLO BLEDU: nieaktualne pole swiat.js…
- [299-09-14] `roslin_frey`: 299-09-14: PRZYJECHALA DO WINTERFELL JAKO KROLOWA POLNOCY. Wesele w Blizniakach odbylo sie; Krol wrocil z nia i z calym hostem. Wchodzi dokladnie w to polozenie, ktorego bal sie jej brat Per…
