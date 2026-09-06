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
- **Data:** 299-09-11 ranek · lato (298)
- **Miejsce:** Winterfell - serce Polnocy, siedziba Starkow / dwor Krola Robba (wesele Robb-Roslin za dni)
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 100 · Sytosc 78 · Zmeczenie 20**

## KASA (1 jelen=100 mied · 1 smok=200 jel)
- **Wolne:** 2 smokow + 95 jeleni + 1 mied
- **Dzien Bilansu:** 1. dnia miesiaca · nastepny 299-10-01

## UMIEJETNOSCI
pismo 8 · rachunki 10 · prawo 9 · retoryka 8 · jezyki 8 · spryt_uliczny 8 · kondycja 7 · rzemioslo 1 · handel 8 · walka 6 · geometria 5 · czytanie_ludzi 10 · organizacja 9 · audyt 9 · finanse 9 · wlodarstwo 8 · historia 6 · wiedza_o_swiecie 7 · polityka 10
**Reputacja:** port 38 · schody_zamkowe 40 · cech_pisarzy -6 · wiara 96 · zamek 24 · cech_kolodziejow 42

## LUDZIE NA SCENIE
- **Luwin** (`maester_luwin`) — maester Winterfell (dwór Starków) — uczony, rządzi skła… · nast ZYCZLIWY -> PROFESJONALNY PODZIW/ZAUFANIE ROBOCZE (0813): po arcyrachunku zapasow (nat.100) Luwin uznaje Symona za rownego-lub-lepszego w rachunkach; trust glęboki
- **Roggen** (`szafarz_roggen`) — starszy szafarz zachodnich składów Winterfell (sługa od… · nast nieznane (nie kontaktowani; Symon obserwuje z boku)
- **Ser Rodrik Cassel** (`rodrik_cassel`) —  · nast ?
- **Medger Cerwyn** (`lord_medger_cerwyn`) — lord rodu Cerwyn (zamek na goscincu ~pol dnia pod Winte… · nast cieply -> PRZYJACIEL (07-10): uklad przybity + Symon spytal 'jak mu sie zyje', Medger sie otworzyl
- **Arya Stark** (`arya_stark`) —  · nast ?
- **mistrz Beron** (`notariusz_beron`) —  · nast ?
- **Bran Stark** (`bran_stark`) — syn Neda, sparalizowany po upadku z wiezy (~10l); bystr… · nast cieply/wdzieczny (Symon dal mu przyszlosc po upadku - nie litosc lecz droga umyslu)
- **Sansa Stark** (`sansa_stark`) — lady, przezyla lata w klatce Cersei/Joffreya (widziala … · nast czujna/wyuczona nieufnosc (kazdy w KP czegos chcial) - ale Symon rozbroil pierwsza szczeline nie chcac od niej NICZEGO ('dziekuje ze nie klamiecie ladniej')
- **Rickon Stark** (`rickon_stark`) — dziki po stratach (ojciec/wojna/rozdzielenie); wilkor K… · nast dziki/nieufny jak zwierze; Symon nie napieral/nie balo sie -> Kudlacz przestal warczec, 'ty jesteś ten co pisze' (poczatek, nie oswojenie)
- **mistrz Gawen (Skarbnik Korony)** (`gawen_skarbnik`) —  · nast ?
- **mistrz Rodwell (Dyrektor Domu Starkow)** (`rodwell_dyrektor_domu_starkow`) —  · nast ?
- **Ser Alyn** (`ser_alyn_zastepca`) —  · nast ?
- **Stara Niania** (`stara_niania`) —  · nast ?

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

## WATKI OTWARTE (555; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
- `czy_przesmyk_podlega_wezwaniu_korony_299_09` [otwarte_do_polozenia_przed_krolem] Czy Przesmyk podlega wezwaniu Korony - pytanie do Krola
- `standard_traktu_polnocy_i_liczba_dla_krola_299_09` [gotowe_do_polozenia_przed_krolem] Standard traktu Polnocy - cena mili zamiast sumy, dla Krola
- `pomiar_wyjsciowy_myta_fosy_przed_robotami_299_09` [do_wykonania_gawen_garth] Pomiar i ogloszenie wyjsciowego poziomu myta Fosy - przed pierwszym palem
- `finansowanie_traktu_pod_myto_299_09` [do_polozenia_przed_krolem] Sfinansowac trakt pod myto zamiast budowac z oszczednosci - zdolnosc kredytowa Polnocy
- `taryfa_celna_polnocy_299_09` [projekt_do_polozenia_przed_krolem] Taryfa celna wolnej Polnocy - cztery klasy przywozu, trzy wywozu
- `pomiar_przesmyku_reka_krannogow_299_09` [rozkaz_wydany_czeka_na_pogode] Pomiar Przesmyku - wlasnymi silami (Glebokorzen + Fosa), zima 299/300
- `ustroj_miast_polnocy_299_09` [wykladnia_przyjeta] Ustroj i rejestr miast Polnocy - miasta panskie, nie wolne
- `grunt_przystani_wilka_trzy_strony_299_09` [domkniete_z_cerwynem_czeka_na_manderly_i_krola] Przystan Wilka - miasto o udzialach: Korona 1/2, Cerwyn 1/4, Manderly 1/4
- `karta_cailin_pisana_zawczasu_299_09` [do_napisania] Karta Cailin - pisac teraz, gdy miasto male i wdzieczne
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

## OSTATNIE WPISY DZIENNIKA
- [297-02-07] `septon_torren`: 297-02-07 (rzut 54): Symon pytal o forum i litere na powstrzymanie Harwina. Torren dal mape z ostroznoscia: FORUM = formalna skarga do RADY, ujeta jako obrona porzadku miasta przed urzedniki…
- [297-02-08] `septon_torren`: 297-02-08: Symon poprosil o zahartowanie pozycji prawnej przed odwetem Harwina/Rymana. Z Torrenem uczynil zelaznymi: obywatelstwo, tytul kamieniczki, kluczowe papiery (swiadkowane/skopiowane…
- [297-03-11] `septon_torren`: 297-03-11 (rzut 66): UKLAD MENTORSTWA - Torren (septon-jurysta) bedzie uczyl Symona PRAWA w zamian za pomoc pisarska przy sprawach prawnych/majatkowych Septy (zapisy/nadania/wlasnosc kosciel…
- [297-03-21] `septon_torren`: 297-03-21 (rzut 19): sesja nauki prawa - uklad mentorski dziala (Symon pomogl przy majatkowych sprawach Septy, Torren uczyl), relacja sie grzeje. ALE nauka plytka: (1) prawo Symona juz wysok…
- [297-03-24] `septon_torren`: 297-03-24 POPOL (rzut 78): praca nad REALNYMI sprawami prawnymi Septy (sporny zapis, granica, zawilosc w nadaniu) - nie dryl. Symon dal Sepcie wartosc (zapisy uporzadkowane, pulapka w nadani…
- [297-04-16] `septon_torren`: 297-04-16 (rzut 68): sesja prawa - pogłebione prawo umow handlowych+arbitrazu (co czyni umowe egzekwowalna, mechanizm sporu, waga udokumentowanego arbitrazu). Podklada formalny grunt pod to,…
- [297-05-26] `septon_torren`: 297-05-26 WIECZOR (rzut 25): reconnect po miesiacu, ale wieczorem krotko - Torren zajety obowiazkami (pora). Zdawkowa wymiana o punkcie prawnym, bez glebszej sesji. Relacja durable trzyma i …
- [297-06-22] `septon_torren`: 297-06-22 (rzut 3, slepy zaulek bez dramatu): Symon przyszedl po tekst charteru. Torren ZATRZYMAL sie z rozmyslem - charteru cechu nie wyciaga sie z polki: oficjalny wglad = formalne zapytan…
- [297-06-24] `septon_torren`: 297-06-24 WIECZOR (rzut 38): Symon przyszedl wieczorem NIE dumpowac swoich 2 spraw na zmeczonego, lecz POMOC - odciazyl Torrena przy zaleglych sprawach Septy (zapisy/nadania/majatkowe, wasza…
- [297-06-25] `septon_torren`: 297-06-25 (rzut 58): sformalizowal OBIE sprawy. FIRMA: forma prawna szkielet gotowy (usluga kupiecko-faktorska, jawnie nie-skrybowska, poza cechem z natury, fundament obywatelstwo-kupca; umo…
- [297-10-09] `septon_torren`: 297-10-09: Symon przyszedl spisac umowe malzenska (4 dni przed slubem). Torren zredagowal wedle dom.md: osobne grunty + korytarz 50/50 + wzajemne dziedziczenie, wazne wobec miasta i Wiary. Z…
- [297-10-15] `septon_torren`: 297-10-15 POPOLUDNIE (bez rzutu - cieple kompetentne zaangazowanie): Symon wpadl pomoc Torrenowi z prawno-majatkowymi sprawami Sepy (rejestry wlasnosci koscielnej/zapisy/nadania). Jego rachu…
