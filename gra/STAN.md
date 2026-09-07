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
- **Data:** 299-09-15 ranek · lato (298)
- **Miejsce:** Winterfell - serce Polnocy, siedziba Starkow / dwor Krola Robba; od 299-09-14 KROL WROCIL Z BLIZNIAKOW ZONATY, z krolowa…
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 96 · Sytosc 44 · Zmeczenie 4**

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

## WATKI OTWARTE (572; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
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
- `nastepstwo_i_ciaglosc_korony_299_09` [otwarty] 
- `polityczna_polowa_wiadomosci_o_neda_299_09` [otwarty] 
- `clo_bialego_portu_czyja_linia_299_09` [otwarty] 
- `zsumowanie_myta_i_cla_na_fosie_299_09` [otwarty] 
- `sansa_opiekunka_krolowej_roslin_299_08` [otwarty] 
- `zwiazac_nastepce_freya_299_09` [otwarty] 
- `stannis_odpowiedz_299_09` [otwarty] 
- `spotkanie_ze_stannisem_w_pentos_299_09` [otwarty] 

## OSTATNIE WPISY DZIENNIKA
- [299-09-14] `robb_stark`: 299-09-14 wieczor, ciag dalszy - DWIE RZECZY PODANE KROLOWI O SIOSTRACH. Bez rzutu. || I. ARYA I BRAAVIJSKI MISTRZ WODNEGO TANCA - to jest DOKLADNIE ta rozmowa, ktora zostala odlozona 299-08…
- [299-09-14] `arya_stark`: 299-09-14: BRAMA OTWARTA PO STRONIE KROLA. Oferta z 299-08-18 (nauka u braavijskiego mistrza wodnego tanca z druzyny Fosy) przedlozona Robbowi po jego powrocie, zgodnie z tym, co wtedy ustal…
- [299-09-14] `robb_stark`: 299-09-14 noc - ROZMOWA O FREYACH. Bez rzutu. Pierwsza taka rozmowa po weselu i po powrocie z Blizniakow. || CO SYMON POLOZYL NA STOLE - CZTERY RZECZY, WSZYSTKIE Z KSIEGI, ZADNEJ ZGADYWANEJ:…
- [299-09-14] `zwiazac_nastepce_freya_299_09`: 299-09-14 NOWY WATEK, POSTAWIONY NA PODSTAWIE OSTRZEZENIA SAMEGO WALDERA FREYA (299-07-02): 'wiazecie MNIE, nie Blizniaki; martwego slowo to kosc - ZWIAZCIE NASTEPCE'. Malzenstwo z Roslin wi…
- [299-09-14] `robb_stark`: 299-09-14 noc, koniec rozmowy - SYMON PYTA KROLA O ROSLIN. Bez rzutu. Pytanie zadane godzine po tym, jak Robb postawil granice ('nie pilnujcie mojej zony') - i Symon nazwal to pierwszy: 'Pyt…
- [299-09-14] `roslin_frey`: 299-09-14 - PIERWSZY OBRAZ KROLOWEJ, z ust Krola: lagodna, stara sie za bardzo, NIE BOI SIE OKRUCIENSTWA - BOI SIE, ZE ZAWIEDZIE. PRZEPRASZA BEZ PRZERWY, za wszystko. Robb: 'Jestem dla niej …
- [299-09-14] `lady_catelyn_stark`: 299-09-14 pozna noc - SYMON PRZYSZEDL DO LADY CATELYN. Bez rzutu. Przyszedl JAKO JEDYNY TEGO DNIA, KTORY NICZEGO OD NIEJ NIE CHCIAL na wejsciu - i ona to zauwazyla. || I. DOTRZYMANIE POWIERZ…
- [299-09-15] `swiat`: 299-09-15 ranek - POGODA (rzut 99, wyjatkowa): DZIEN NIE NA TE PORE ROKU. Bezwietrznie, niebo bez chmury, slonce grzeje jak w sierpniu; bloto obeschlo w jedna noc, trakty twarde i rowne. Sta…
- [299-09-15] `stannis_odpowiedz_299_09`: 299-09-15 rano - ODPOWIEDZ DLA STANNISA NAPISANA. Bez rzutu (redakcja; wynik przyjdzie z jego odpowiedzia). FORMA: pismo KROL DO KROLA. Symon UKLADA, PODPISUJE I PIECZETUJE ROBB - odpowiedz …
- [299-09-15] `stannis_odpowiedz_299_09`: 299-09-15 - UZUPELNIENIE PO UWADZE GRACZA. SPRAWDZONE W KSIEDZE: podstawa dla SPOTKANIA ze Stannisem ISTNIEJE i jest z 299-09-07, z referatu wywiadowczego przed Rada, czyli DOKLADNIE jako po…
- [299-09-15] `spotkanie_ze_stannisem_w_pentos_299_09`: 299-09-15 WATEK USTANOWIONY (podstawa: 299-09-07, zbieznosc pieciu zrodel; potwierdzone przez gracza jako zamiar ustalony po liscie Aemona). RZECZ, KTORA MA TRAFIC DO KROLA I DO LISTU DLA ST…
- [299-09-15] `lord_wyman_manderly`: 299-09-15 UZUPELNIENIE ZAPISU (luka w dzienniku zalatana na wskazanie gracza): NA PROSBE Z 299-08-23 WYMAN SIE ZGODZIL - DAJE OKRET na poselstwo do Braavos i Pentos i POSYLA WLASNEGO PRZEDST…
