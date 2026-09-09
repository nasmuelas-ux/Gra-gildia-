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
- **Data:** 299-10-01 wieczor · lato (298)
- **Miejsce:** BRAAVOS - dzien drugi. Deklaracja w skladzie, adres w faktorii Manderlych. Ilario odnaleziony zywy (wagowy w Porcie Lach…
- **Postac:** Symon Tally, l.24 — Lord Symon Tally, Namiestnik Krola Polnocy (Hand of the King in the North)
- **Zdrowie 86 · Sytosc 60 · Zmeczenie 40**

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

## WATKI OTWARTE (620; ostatnie 45 — pelna lista: `python3 gra/db.py otwarte`)
- `wezel_zachodni_domu_i_biala_plama_korony_299_09` [otwarty] Wezel Domu na zachodnim wybrzezu = jedyne oczy tam, gdzie Korona ich nie ma. Symon zglasza sie jako strona Ska…
- `odpis_ksiegi_myta_do_skarbu_299_09` [otwarty] Odpis ksiegi myta do Skarbu co miesiac - Fosa robi to sama i niepytana od zaraz; nalozenie tego na innych lenn…
- `zjazd_choragwi_przysiega_na_korone_299_09` [otwarty] · termin 299-10-05 zjazd zimowy; 300-04-01 Wielka Rada ZJAZD OGLOSZONY: zimowy 299-10-05 (krolowa, przysiega na Korone, obwieszczenie nastepstwa), Wielka Rada 300-04…
- `powiedziec_branowi_i_catelyn_o_nastepstwie_299_09` [otwarty] Bran i Catelyn WIEDZA (09-16). Nie wiedza: Rickon, Sansa, Arya, trzej nazwani lordowie
- `rickon_drugie_ogniwo_linii_299_09` [otwarty] RICKON - liczba na kiju przestala byc prawdziwa (60-70 nocy -> realnie 100-120). Poprawic PRZED wyjazdem, nie …
- `zastepcy_do_krukow_i_ksiag_299_09` [otwarty] Czlowiek do krukow i ksiag zamiast maestera - dwa-trzy lata zamiast szesnastu (rachunek Luwina). Jedyna odpowi…
- `sansa_uczy_dziedziny_dziesiatej_299_09` [otwarty] Sansa uczy dziedziny X kanonu (mowa i sluchanie) - probnie. Rozstrzygniecie metodyczne: nie uczy sie widzenia,…
- `zbior_swiadectw_polnocy_299_09` [otwarty] Zbior swiadectw - 2 z 14 odpowiedzi. Ostatnie Ognisko: ZIMNO NAJPIERW (potwierdzenie niezalezne wniosku Brana)…
- `umber_ruszy_bez_rozkazu_299_09` [otwarty] Wielki Jon: "jak przyjdzie, nie bede czekal na wezwanie - i wiem, ile mnie to kosztowalo ostatnim razem". Najb…
- `przysiega_przed_drzewem_i_septonem_299_09` [otwarty] Przysiega na Korone w bozym gaju - SEPTON Z BIALEGO PORTU STAJE OBOK DRZEWA SERCA. Te same slowa, ten sam dzie…
- `krol_uczy_sie_czytac_ksiege_299_09` [otwarty] · termin 299-09-19/20, przed przyjazdem Wymana Godzina Krola z Gawenem nad ksiega celna Korony - trzy pytania zamiast nauki rachunku; krol uczy sie CZYTAC, n…
- `korona_bez_wlasnych_zbrojnych_299_09` [otwarty] DZIURA: Korona nie ma wlasnych ludzi do orszaku wlasnego Namiestnika. Zimowa Straz przy Krolu, Osric w drodze,…
- `wyman_manderly_przyjazd_299_09` [otwarty] 
- `rewizja_i_drugi_pisarz_dziura_299_09` [otwarty] 
- `prawo_orszaku_co_sie_dzieje_gdy_zle_299_09` [otwarty] 
- `hornwood_ziemia_bez_pana_299_09` [otwarty] 
- `rejestr_imion_lordow_polnocy_299_09` [otwarty] 
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

## OSTATNIE WPISY DZIENNIKA
- [299-11-30] `objazd_wschodu_jako_pierwszy_objazd_poborowy_299_09`: 299-11-30 SWIT - KONIEC OBJAZDU, POCZATEK POSELSTWA. Kolumna zeszla z siodel, poselstwo weszlo na poklad; jedna droga (Fosa -> wschod -> Bialy Port -> Braavos) domknieta zgodnie z zamyslem z…
- [299-11-30] `harrion_karstark_poszukiwanie_299_11`: 299-11-30, POKLAD, PRZED ODBICIEM LODZI PILOTA - DWA PISMA WYSLANE OSTATNIA POCZTA Z OKRETU (jedyne okno: pilot wyprowadza okrety za lod i rede, jego lodz wraca w ciagu godziny). == PISMO I …
- [299-11-30] `lista_wymian_jencow_korony_299_11`: WATEK USTANOWIONY - WLASNA LISTA WYMIAN JENCOW KORONY POLNOCY. Zrodlo: luka systemowa nazwana przez Wille 299-11-26 przy odnalezieniu Harriona ('KORONA NIE PROWADZI WLASNEJ LISTY WYMIAN JENC…
- [299-12-01] `poselstwo_wolne_miasta_braavos_pentos_299_08`: 299-12-01/02, POD POKLADEM - PAKIET WILLI OTWARTY. REKONESANS BRAAVOS I PENTOS, ZAMOWIONY 299-08-29, DORECZONY PO TRZYNASTU TYGODNIACH. Bez rzutu (raport wlasnego, oplacanego czlowieka - pre…
- [299-12-02] `nesta_braavijka`: ### DLACZEGO NESTA WYPLYNELA Z BRAAVOS - POWIEDZIANE NA WODZIE, JAK OBIECALA. ### Bez rzutu (partnerka wieloletnia, sama zaproponowala rozmowe 299-11-29: 'spytajcie mnie o to na wodzie, nie …
- [299-12-02] `poprawki`: DWIE POPRAWKI PROWADZACEGO NA RZECZ GRACZA (bez kosztu; gracz mial racje w obu i w obu przywolal zapisy, ktorych prowadzacy nie doczytal). (1) ### SYMON NIE JEST OBCYM WOBEC ZELAZNEGO BANKU.…
- [299-12-05] `przeprawa_zimowa_do_braavos_299_12`: ### SZTORM NA WASKIM MORZU - RZUT NA PRZEPRAWE 2 (bardzo zle). ### Wyjscie z Bialego Portu 299-11-30 przy pogodzie 24; szyper zapowiedzial 'liczcie szesc, a jak sie wzmoze, to i osiem'. PRZE…
- [299-12-05] `program_okretow_polnocy_299_08`: ### STYL POLNOCNY OKRESLONY - NORMA CZTERECH WZOROW, spisana na pokladzie po sztormie (299-12-05). Bez rzutu (praca konceptualna, nie proba). ### ROLA SYMONA NAZWANA UCZCIWIE: rzemioslo 1, g…
- [299-12-05] `program_okretow_polnocy_299_08`: ### WZORY NAZWANE - SZESC KADLUBOW, CZTERY RODZINY. Uzupelnienie normy z tego samego dnia; dodany trzeci wzor wojenny (wskazanie gracza: brakowalo okretu, KTORY WALCZY NA MORZU - Kra bije pr…
- [299-12-11] `poselstwo_wolne_miasta_braavos_pentos_299_08`: ### 299-12-11 SWIT - PRZYBYCIE DO BRAAVOS. Rzut na to, co zastaja w porcie: 39 (slabo). ### WEJSCIE: Tytan wychodzacy z mgly, ryk powietrza pchanego przez braz przy przejsciu miedzy nogami; …
- [299-12-11] `poselstwo_wolne_miasta_braavos_pentos_299_08`: 299-12-11 BRAAVOS, DZIEN PIERWSZY - CIAG DALSZY: DEKLARACJA, ADRES KORONY, DRUGI OKRET, RANNI. == I. DEKLARACJA ZLOZONA W URZEDZIE PORTOWYM (wykonanie rady celnika po rzucie 95) == TRESC, UL…
- [299-12-11] `jorven_marynarz`: JORVEN - marynarz Manderlych, 27 lat, na pokladach od jedenastego roku zycia. Zmiazdzona noga podczas przesztauowania ladunku w sztormie 299-12-03 (wykonywal decyzje Symona 'najpierw rece, p…
