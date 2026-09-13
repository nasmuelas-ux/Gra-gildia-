# STAN GRY — indeks (regenerowany z JSON+JSONL, NIE edytuj recznie)
_Zrodlo prawdy: gra/*.json + gra/db/wpisy.jsonl. Szczegoly: `python3 gra/db.py pokaz <klucz>` / `szukaj <fraza>` / `dzien <data>`._

## ⚠️ 38 ZASAD SILNIKA — `gra/PROWADZENIE.md`, sekcja od "TRZYDZIESCI PIEC ZASAD"
**PRZECZYTAJ JE PO KAZDYM KOMPAKTOWANIU.** Przy sprzecznosci z czymkolwiek innym — tamte wygrywaja.
Skrot najczesciej lamanych: **1** nie twierdze, nie sprawdziwszy · **3** blad GM nie przechodzi na gracza (VOID znaczy VOID) ·
**7** moja cisza nie jest zastojem (rzecz zlecona i obsadzona idzie sama) · **8** postep rodzi problemy, nie wstazki ·
**12** kryterium to OBSADZENIE, nie nazwisko · **22** prerogatywa nie idzie pod glosy · **27** jeden rzut na sprawe albo zero ·
**31** nie pisze mysli gracza, nie zamieniam rozmowy w akt, nie posuwam czasu w rozmowie · **34** bez kanalu nie ma wiadomosci.
### **36 - DWA POZIOMY:** SPRAWA zyje latami i NIE ma sie zamykac (filar) · OPERACJA ma dzien, cel i spust, i MUSI sie zamknac.
Test: czy to moze sie skonczyc konkretnego dnia? Meldunek idzie z poziomu OPERACJI - filary stoja, melduje sie to, co sie pod nimi rusza.
**ALARM: sprawa zywa, pod ktora nie ma ANI JEDNEJ otwartej operacji** - to nie brak postepu, to ja nie otworzylem nastepnego kroku.
### **37 - SZUKA SIE W DWOCH KSIEGACH, NIGDY W JEDNEJ** (stala, 300-03-03).
Przed obsadzeniem KAZDEGO krzesla i przed powiedzeniem, ze kogos NIE MA, czyta sie OBA spisy Fosy:
**(1) SPIS MIESZKANCOW 299-06 - 640 dusz IMIENNIE**, zawod = co umie rekami, trzy osobne rubryki CZYTA/PISZE/LICZY,
dzieci z imienia, wiekiem i rodzicem (takze dziewczeta) - obejmuje ludnosc SPRZED przybycia czterystu;
**(2) REJESTR DNIOWEK MELLI od 300-02-28** - czterystu przybyszow, kolumna CO UMIE, wpis imieniem ALBO znakiem,
plus ksiega bramy od 02-12. **Zaden nie pokrywa calosci - dlatego zawsze oba.**
### **38 - OBSADY I TERMINOW NIE PODAJE SIE Z PAMIECI** (stala, 300-03-03).
Sa DANYMI: `gra/obsada.json` i `gra/terminy.json`, oba renderowane nizej w tym pliku.
**Kazde nadanie, kazdy wakat i kazdy termin dopisuje sie TAM w tej samej turze, w ktorej padl.**
**Termin bez zapisanego ZAMKNIECIA nie jest terminem - tylko data, ktora minie.**

## 📅 TERMINY — `gra/terminy.json` (JEDYNE ZRODLO; kalendarz ranka generuj STAD, nie z pamieci)
_Kazda pozycja: co · kto · czym sie ZAMYKA. Termin bez zamkniecia tylko mija._

- **300-03-03 lub WCZESNIEJ** — ROZWIAZANIE MIRY, Bialy Port. RHONA: 'to nie bedzie trzeci dzien trzeciego miesiaca - dziecko stoi NIZEJ, niz powinno, a DRUGIE przychodzi predzej niz pierwsze' · _kto:_ **RHONA, WENNA, ELNA; Lyra u Elny** · _zamyka:_ wiadomosc z Bialego Portu (kruk 2 dni, jezdziec 6-8) **⚠ OTWARTE - MOZE JUZ SIE STALO**
- **300-03-05** — Cerwyn wyjezdza; odpis urzadzen Fosy ma byc gotowy · _kto:_ **dwaj pisarze** · _zamyka:_ odpis wreczony
- **300-03-06** — czlowiek Wymana na Fosie - pomiar przewloki pod dwie pieczecie · _kto:_ **Weylin + Orbelo + czlowiek Wymana** · _zamyka:_ wspolne przejscie sznurem
- **300-03-06..08** — odpowiedz Krola na pismo z 300-02-19 (rejestry Locke'ow, pochodzenie, jency) · _kto:_ **GARRICK rozdziela** · _zamyka:_ czesc koronna w bieg, czesc prywatna zapieczetowana do ksiegi Domu
- **300-03-07** — WYJAZD SYMONA z Fosy · _kto:_ **Symon + przyboczna (Sten)** · _zamyka:_ wyjazd
- **300-03-07** — pierwsza KARTA ZYWNOSCIOWA (geby, korce, na ile dni) · _kto:_ **Orland + Warryn** · _zamyka:_ karta na stole
- **300-03-07** — ODBICI BEZ DOMU - ilu Fosa bierze; limit z karty, nie z uznania · _kto:_ **Symon** · _zamyka:_ liczba wpisana
- **300-03-07** — pytania proby wstepnej dla lawy · _kto:_ **MELLA** · _zamyka:_ pytania oddane lawie
- **300-03-07** — KARTA ODHACZEN GARRICKA - czwarta kolumna (idzie / stoi / pyta kancelarie) przy kazdym wierszu · _kto:_ **GARRICK** · _zamyka:_ karta wypelniona
- **300-03-07** — przywilej bagienny - szesc rzemiosl na slup; zegar pana · _kto:_ **WARRYN + lawa** · _zamyka:_ slup
- **300-03-09** — WARRYN ZAMYKA RACHUNEK ETAPU I (dwa niepoliczone otwory: kamien z zewnatrz, szesc pozycji Kasy 2) · _kto:_ **WARRYN** · _zamyka:_ liczba
- **po 300-03-09** — najwczesniejsza uczciwa data papieru dluznego lenna (8,5 prosty, 5 lat, odnawialny) · _kto:_ **Symon + Hal** · _zamyka:_ suma emisji i srodek wierzyciela
- **300-03-10** — CICHY KUPIEC rusza (sol, ksiega Domu, sfera Dreadfortu) · _kto:_ **WILLA** · _zamyka:_ wyjazd
- **~300-03-13** — BIALY PORT - WYMAN: podpis Ujscia z reki do reki, splawnosc Samotnych Wzgorz, udzial w drewnie, Medrick, dwa nowe porty · _kto:_ **Symon** · _zamyka:_ podpis
- **~300-03-13** — BIALY PORT - HAL: placowki (Braavos, Pentos, Gulltown, Highgarden), obrot przez rece cechowe, forma zwrotu 695, POCHODZENIE ziarna, suma emisji · _kto:_ **Symon + Hal** · _zamyka:_ rozmowa w oczy
- **~300-03-13** — koniec przewagi NIEOGLOSZONEGO STATUTU - do podpisu Wymana · _kto:_ **-** · _zamyka:_ podpis albo utrata przewagi
- **300-03-29** — CZTERNASCIE KART DO KWATER - dwie kolumny: NAD TYM GLOSUJECIE / TO OGLOSZONO; plus druga prosba do domow · _kto:_ **kancelaria** · _zamyka:_ karty zaniesione
- **300-03-30** — WIELKA RADA. 0. MUR (meldunek + aklamacja) - I. ZIEMIA BEZ PANA (pod glosy sama PROBA) - II. WODA - III. CHLEB + REWIZJA - IV. HANDEL · _kto:_ **Symon, Cerwyn, Wyman** · _zamyka:_ cztery glosowania i aklamacja
- **300-04-01** — ZALEGLOSC KARHOLDU 148/160 - dwanascie · _kto:_ **Korona** · _zamyka:_ zaplata albo zaleglosc
- **przed 300-04-01** — RAMSAY - wezwanie do czterdziestu domow; meldunek MA PASC TAKZE, JESLI NIE PRZYJEDZIE · _kto:_ **kancelaria -> Symon (Bialy Port do ~20.III, potem Winterfell)** · _zamyka:_ meldunek o przyjezdzie ALBO o niestawieniu sie
- **300-04-01** — BRACTWO RZEMIOSLA WOLNEGO - miasto wykonuje statut · _kto:_ **miasto Cailin** · _zamyka:_ wykonanie
- **ten tydzien** — FEVER polowa (a): ile tygodni rzeka stoi - kanal Warryna do krannogmenow + przewoznicy z brodu · _kto:_ **WARRYN** · _zamyka:_ odpowiedz
- **ten tydzien** — NARYBEK do stawow + ROSLINY JADALNE - tym samym jezdzcem co Fever · _kto:_ **WARRYN** · _zamyka:_ odpowiedz
- **tygodnie - PRZED SIEWEM** — ZRODLO NASIENIA owsa i jeczmienia NA TEN SIEW · _kto:_ **Symon / Hal / Harl** · _zamyka:_ ziarno w skladzie **⚠ OTWARTE - NAJPILNIEJSZE**
- **~300-03-13** — WILLA: druga droga na poludnie - dwie kolumny rejestru; czyta MELLA, wynik do Willi szyfrem · _kto:_ **MELLA -> HARROL -> WILLA** · _zamyka:_ odczyt kolumn
- **V/300** — NESTA: kolumna dziesieciu przystani zachodnich (fracht) + pytanie o DAENERYS · _kto:_ **NESTA** · _zamyka:_ odpowiedz z Braavos
- **jesien 300** — ZYTO OZIME - siew; odpowiedz OSRICA o Darze pod to, nie pod wiosne · _kto:_ **Symon / Osric** · _zamyka:_ siew
- **koniec VI/300** — DRUGA RATYFIKACJA traktatu z Dorzeczem; zakaz zaliczek przed ratyfikacja · _kto:_ **Catelyn / Lucan** · _zamyka:_ ratyfikacja
- **bez daty - CISZA** — MELDUNEK VII OSRICA (Mur) - zalegly; doszlo mu pytanie o Dar · _kto:_ **OSRIC** · _zamyka:_ meldunek
- **bez daty - CISZA** — PRZYSTAN WILKA - status budowy; pyta CERWYN jako wspolwlasciciel cwiartki; podanie nazwiska budowniczego jest czescia odpowiedzi · _kto:_ **CERWYN** · _zamyka:_ meldunek z nazwiskiem
- **bez daty - CISZA** — DONNEL OBROK (Dustinport, budowa) - pytanie pod pieczecia, jezdziec eskadry · _kto:_ **DONNEL** · _zamyka:_ meldunek w formie osmiu rubryk
- **bez daty** — GARTH: liczba miesieczna dziury w komorach wodnych - zmierzona 299-10-01 i NIE ZMIERZONA PONOWNIE · _kto:_ **GARTH** · _zamyka:_ nowa liczba
- **bez daty** — BERON: wszystko, co przyszlo od BRYNDENA TULLY'EGO od 299-07, z datami; potem list do Blackfisha (poludniowa sciana, nie traktat) · _kto:_ **BERON** · _zamyka:_ wykaz
- **bez daty** — THEOMORE: gdzie kolebka, ile kosztuje PIERWSZY ROK, kogo wzialbys jako pierwszego ucznia; spis flory jako pierwszy zbior (w reke na Radzie) · _kto:_ **THEOMORE** · _zamyka:_ odpowiedz
- **300-03-04** — URBARZ ZALOZONY - cztery kolumny KTO / Z CZEGO / ILE / KIEDY; pierwszy wpis to szesc tygodni niepobranego czynszu (od 300-02-07) · _kto:_ **SARRA OD KRESKI + INGA LICZYDLO** · _zamyka:_ ksiega otwarta z pierwsza strona
- **300-03-04** — LAWA MIASTA SADZA KOWALA (Brusk od Miecha, wskazala Mella) - kuznia idzie pierwsza albo nie idzie nic · _kto:_ **lawa burmistrza** · _zamyka:_ posadzenie
- **300-03-05** — CERWYN WYJEZDZA - ma zostawic TOMMARDA KOSE jako lustratora Fosy na rok · _kto:_ **CERWYN** · _zamyka:_ czlowiek zostaje, kiedy pan odjezdza
- **ten tydzien** — SOLTYSI: ktore wsie wybraly, kiedy i kogo - pytanie zadane dawno, odpowiedzi nie bylo · _kto:_ **WARRYN** · _zamyka:_ lista wsi z nazwiskami i datami
- **300-03-30** — AKADEMIA WOJSKOWA: data po Radzie, platnik Kasa 3, baszta w Przystani Wilka; pierwszy mistrz BRYNDEN TULLY, zapasowo zbrojmistrz Fosy · _kto:_ **Symon / Brynden** · _zamyka:_ odpowiedz Blackfisha
- **wyslane 300-02-27 - CISZA** — PRZYPOMNIENIE O REJESTRATORZE KORONY. Jedno zdanie, bez nazwiska, spisane przez Garricka pod dyktando: 'KRZESLO REJESTRATORA KORONY STOI PUSTE CZWARTY MIESIAC. NAZWISKA NIE PODAJE, BO ZASTRZEGLISCIE JE SOBIE. PODAJE DATE.' Ten sam goniec co prosba o zwyczaj, OSOBNA KARTA - zeby nie zamienic tamtej w upomnienie. UWAGA: UCHO KORONY I REJESTRATOR KORONY TO JEDNO KRZESLO (odkryte 300-02-27) - puste jest wieksze, niz wyglada. · _kto:_ **SYMON -> ROBB STARK** · _zamyka:_ NAZWISKO OD KROLA. A jesli do Rady 300-03-30 nie przyjdzie - ZAMYKA TO MILCZENIE: przestaje byc prosba bez odpowiedzi, a staje sie faktem, ktory Namiestnik moze wypowiedziec na Radzie. Drugi raz sie nie prosi. **⚠ OTWARTE - LIST POSZEDL 300-02-27, ODPOWIEDZI NIE BYLO**
- **PRZED Rada 300-03-30 - WARUNKOWE** — SPRAWA CAILIN (prawo skladu + garnizon). KROL OBIECAL 300-02-07: rozstrzygnie PRZED Rada, ale DOPIERO GDY PRZYJDZIE PISMO MIASTA, NIE NAMIESTNIKA. Prosba miasta o piec dni targowych stoi na slupie od 300-03-03 - ALE NA SLUPIE, NIE W WINTERFELL. Dopoki lawa nie wysle wlasnego pisma, zegar Krola nie ruszyl. ROZSTRZYGNIECIE GRACZA 300-03-03: lawa wysyla wlasne pismo 300-03-04, krukiem. · _kto:_ **LAWA MIASTA CAILIN / HERWIN SZALA** · _zamyka:_ pismo MIASTA w Winterfell - ono uruchamia obietnice Krola **⚠ WARUNEK SPELNIANY - LAWA WYSYLA PISMO MIASTA 300-03-04 KRUKIEM**
- **300-03-04** — PISMO MIASTA CAILIN DO KORONY - wlasna pieczec miasta, podpisy lawy, krukiem z Fosy (2 dni). TRESC: TYLKO sprawa Cailin (przymus skladu piec dni targowych + garnizon). NIE laczyc z ustrojem miast - tamto Krol przyjmie tylko OD WSZYSTKICH NARAZ i pismo Cailin utknie za czternastoma innymi. WARUNEK FORMY: Symon nie dyktuje ani slowa; podaje Herwinowi TYLKO to, ze warunek Krola istnieje. · _kto:_ **LAWA MIASTA / HERWIN SZALA** · _zamyka:_ kruk w powietrzu
- **~300-03-06** — PISMO MIASTA W WINTERFELL - od tej chwili biegnie obietnica Krola z 300-02-07: rozstrzygnie PRZED Rada · _kto:_ **kancelaria Korony (BERON)** · _zamyka:_ rozstrzygniecie Krola w sprawie skladu i garnizonu Cailin

_Zamkniete ostatnio:_ cena minimalna z iloscia + cena dzisiejsza + oferta kupna na (zrobione 300-03-03)

## 👤 OBSADA — `gra/obsada.json` (NIE PODAWAC OBSADY Z PAMIECI — CZYTAC STAD)
### LENNO — _Kasa 2 (lenno), o ile nie zaznaczono inaczej_
- **RZADCA:** WARRYN _(11 lat na tej ziemi; ROZSTRZYGA BUDOWY (300-03-01), Garrick konsultuje)_
- **KANCLERZ OSOBISTY:** GARRICK _(pelnomocnictwo notarialne na Fose 300-03-01; sprawy panstwowe -> kancelaria Winterfell)_
- **MARSZALEK FORTECY / KAPITAN DOMU TALLY:** HENDRY _(~50 druzyna + obrona Fosy; pismo o granicach urzedu 300-02-28)_
- **DOWODCA PRZYBOCZNEJ:** STEN _(pod nim DAGON i HARL; przyboczna jedzie z Symonem 300-03-07)_
- **DZIESIETNIK (Dustinport):** HARL _(prowadzi dziesieciu z Theonem; swita przy wjezdzie, straz kilka dni, powrot)_
- **ZBROJMISTRZ:** stary zbrojmistrz (imie nie pada w zapisie) _(bron, cwiczenie, chlopcy; arsenal i zapasy zbrojne (OSOBNO od prowiantu garnizonu))_
- **MAESTER:** WYSTAN _(srebro, czarne zelazo, miedz, OLOW (trucizny); trzeci odczyt ziarna na Fosie)_
- **SEDZIA - SAD GRODZKI:** RODERYK _(umowy od rownowartosci 30 korcy; orzeka 'jedna sakiewka' (300-03-03))_
- **MAJORDOM FOSY:** ALYS _(dom, izby, goscie, SPIZARNIA I KLUCZE. Majordomat Fosy od 299-07 to ALYS I BRAN RAZEM: ona dom, on roboty.)_
- **MAJORDOM ROBOT:** BRAN _(roboty; UWAGA: to NIE jest Bran Stark z Winterfell - dwie rozne osoby o tym imieniu. Od 300-03-01 trakt do Dorzecza.)_
- **ZIELARKA WLOSCI:** NINA _(lecznica + apteka bagna)_
- **UCZENNICA ZIELARKI:** GYTHA KADZIEL _(z czterystu przybyszow, podpisuje sie znakiem; opatrywala w barakach po nocach)_
- **REJESTR DNIOWEK:** MELLA _(kolumna CO UMIE; imie ALBO znak w tym samym rzedzie; czyta tez kolumny Willi)_
- **SKLAD:** ORLAND KORZEC _(cztery przegrody; karta A na 300-03-07)_
- **SZKLARNIE:** WERRAN _(MIRA jako druga reka - nieobecna; szklarnia ma byc matecznikiem)_
- **WODA I SLUZA:** WEYLIN _(INZYNIER ZAMKOWY - 'urzad na pokolenia', 3 z 20 wiez; woda, dreny, sluzy. TO JEST 'szef architektow'. Gniazdo na wal przed zamknieciem komory; stawy do rysunku.)_
- **KAMIEN I BUDOWA:** ORBELO _(syn palownika; kafar odrysowany z podlogi Terysa)_
- **PISARZ PRZY BRAMIE:** jeden z trzech pisarzy Nesty (ten, ktory nie siedzi nad cena mchu) _(od 300-03-03 CIAGNIE LOS 1 na 12 przed otwarciem bramy)_
- **PISARZE DWORU:** dwaj z trojki Nesty _(trzeci poszedl na brame; przepisuja urzadzenia dla Cerwyna)_
- **SPIZARNIA DOMOWA / KLUCZE:** ALYS _(majordomat; przy przeliczeniu spichlerza ONA szla przy liczbach, Bran przy robotach - wydawanie z domu nigdy nie bylo puste)_
- **SZKOLA I NAUKA:** dwaj uczacy, pod WARRYNEM _(szkola + posilek przy szkole; pierwsza szkola powszechna Polnocy. Ochmistrza nauki NIE MA - nikt nie odpowiada za nauke z nazwy.)_
- **KLUCZNIK LOCHU:** DOREN KLAMRA _(REJESTR MELLI. Trzymany w Harrenhal cztery miesiace - wie, co to trzymanie. Podpisuje sie ZNAKIEM; kwit odbioru wiezionego podpisuje PISARZ GRODZKI (jak przy Rowanie). NIE JEST JASTRZEBIEM - kto chwyta, ten nie trzyma.)_
- **PROWIANTMISTRZ GARNIZONU:** ARNO SUCHAR _(REJESTR MELLI, wskazal HENDRY (jego drabina). Karmil kolumne marszowa; liczy, liter nie sklada. OSOBNO od skladu (Orland) i od spizarni (Alys).)_
- **KUCHARZ:** NELDA OD KOTLA _(REJESTR MELLI. Gotowala w barakach od przyjazdu i nikt jej za to nie placil - jak Gytha, ktora opatrywala po nocach. Wegorz jej nie przeraza.)_
- **MIERNICZY TORFU:** JORREN LUT _(REJESTR MELLI. Brat HARROLA, ten sam fach - stad umiejetnosc nie wymaga sprawdzania. Wakat po Harrolu (poszedl na szyfratora 300-03-02) zamkniety tego samego tygodnia.)_
- **PIWNICZY:** OTTO BECZKA _(REJESTR MELLI.)_
- **LOWCZY:** HAKON OD JASZCZURA _(SPIS 299-06, NIE rejestr Melli - lowczy bagna musi znac bagno, a przybysz jest tu trzy tygodnie. Ryba, ptactwo wodne, jaszczurolw. Bez niego kanon jadla byl lista.)_
- **LESNICZY:** SIGURD OLCHA _(SPIS 299-06. Regale lesne; olcha na lodzie Jastrzebi szla dotad z wlasnego lasu BEZ EWIDENCJI - od dzis idzie przez niego.)_
- **KONIUSZY:** TORGIL WOZNICA _(SPIS 299-06. Konie, wozy, zaprzegi, woly na trasie Cailin-Bialy Port.)_
- **POBORCA CZYNSZOW:** INGA LICZYDLO _(SPIS 299-06, rubryka LICZY. Zasada przy nadaniu: NIE POBIERA WE WLASNEJ WSI. Czynsz istnieje od 300-02-07, poborcy nie bylo szesc tygodni.)_
- **MLYNARZ:** TOBEN OD ZARNA _(WSKAZALI WARRYN I KESSEL WSPOLNIE (tryb z 300-02-27) - mlyn siedzi w sluzie, a sluza to brama wodna twierdzy, wiec musial przejsc przez rzadce I przez dowodce strazy.)_
- **ZASTEPCA PRZY GROBLI:** KORM PALIK _(WSKAZAL BRAN, z 48. Ma stac, zanim kafar pierwszy raz wejdzie w grunt.)_
- **NASIENNIK:** HELWA STRACZEK _(WSKAZAL WERRAN. Bez niego szklarnia byla szkolka jednorazowa; z nim jest matecznik.)_
- **OCHMISTRZ SZKOLY I NAUKI:** MABEL SIWA _(SPIS 299-06, wszystkie trzy rubryki. Nie uczy - ODPOWIADA: czy dzieci przychodza, czy jedza, czy ktos zniknal z listy. Dwaj uczacy zostaja pod Warrynem.)_
- **GLOWNY ARCHIWISTA:** HALDOR OD SKRZYN _(SPIS 299-06, najdluzej na tej ziemi z czytajacych. ZABEZPIECZENIE W SAMYM URZEDZIE: ARCHIWISTA NIE PISZE. Przyjmuje i wydaje ZA KWITEM, a KATALOG JEST JAWNY - kazdy widzi, czego brakuje. Kto katalogue, ten nie redaguje (ta sama zasada co ksiega Jastrzebi u pisarza grodzkiego).)_
- **SKARBNIK LENNA (Kasa 2):** GERRIK RACHUBA _(SPIS 299-06, rubryka LICZY. ROZDZIELENIE, KTORE BYLO CALYM PROBLEMEM: SKARBNIK LICZY I NIE WYDAJE. Wydaje RZADCA - ale na kwit skarbnika. Dwie reki na jednej monecie, po raz pierwszy w Kasie 2.)_
- **PISARZ PODATKOWY / URBARZ:** SARRA OD KRESKI _(REJESTR MELLI, pisze i liczy. Zaklada URBARZ od 300-03-04: cztery kolumny KTO / Z CZEGO / ILE / KIEDY. Pierwszy wpis - szesc tygodni czynszu, ktorego nikt nie pobral.)_
- **LUSTRATOR (rewident objazdowy):** TOMMARD KOSA - CZLOWIEK CERWYNA _(NIE Z ZADNEJ KSIEGI FOSY, I TO JEST CALY SENS. Wypozyczony przez Justycjariusza na rok; objazd i kontrola to wlasny fach Cerwyna. CENA JEST PRAWDZIWA: czlowiek Justycjariusza siedzi w ksiegach Namiestnika. To wlasnie czyni krzeslo wiarygodnym.)_

### MCHOWE JASTRZEBIE - STRAZ LENNA — _KASA SYMONA (nie lenna)_
_20 ludzi. Lodzie plaskodenne na tyczkach, kusze. Nazwa od 299-09-05. Powolana do pomocy celnikom 300-02-25. NIE PODLEGA HENDRY'EMU - dowodca podlega BEZPOSREDNIO SYMONOWI. ZAKAZ NACZELNY: KTO CHWYTA, TEN NIE SADZI. Ksiega Jastrzebi u PISARZA GRODZKIEGO (kto dowodzi, nie spisuje sam)._
- **DOWODCA:** KESSEL BRODATY _(jedyne nazwisko, ktore padlo u Hendry'ego i Warryna osobno; wybiera mlynarza wspolnie z Warrynem)_
- **ZASTEPCA:** ODD MOKRADLO _(ksiegi nie tyka)_
- **PRZY BRAMIE:** ROWAN POLUCHO _(nie czyta - kwit przy bramie podpisuje kto inny (dziura mala i realna))_

### MIASTO CAILIN — _miasto; lord nadaje, miasto sadza_
- **BURMISTRZ:** HERWIN SZALA _(dawny wagowy, 12 lat przy wadze; autor poprawki o znaku normy; uczony odczytu ziarna 300-03-02)_
- **WAGOWY:** BENNIS OD WAGI _(15 lat, liter nie zna; wybrany przez lawe; wage trzyma i placi rada; PIERWSZY ODCZYT STANU ZIARNA)_
- **LAWA:** lawa burmistrza _(proba wstepna, losowanie dzialek, przywilej bagienny; ustalila 5 dni targowych (300-03-03, niejednoglosnie))_
- **KOWAL:** BRUSK OD MIECHA - wskazala MELLA _(REJESTR MELLI. Mella pisala rachunki W KUZNI za meza, zanim tu przyszla, i wyrabia gwozdzie we wsi pod grobla - wie, kogo szukac. LORD NADAJE KUZNIE, LAWA SADZA KOWALA.)_

### DOM HANDLOWY TALLY — _Kasa 1_
- **DYREKTOR:** HAL SIEROTA _(Bialy Port; forma zwrotu 695 w towarze - jego sprawa)_
- **SIATKA / UCHO:** WILLA _(kartka zgodnosci; dwie kolumny drugiej drogi)_
- **SZYFRATOR DOMOWY:** HARROL LUT _(mierniczy torfu; liczby tak, liter nie sklada; matryce zapieczetowane z dniem na wierzchu)_
- **ODSLUCHIWACZKA RYNKOW:** MAEGA KOSZYK _(zbieraczka; osoba, nie rubryka - da sie ja poslac)_
- **KURIER PRZY MAEDZE:** WYLL SZUWAR _(bez tytulu i bez zmiany; nikt go nie pamieta)_
- **NOTARIUSZ DOMU:** imie do potwierdzenia _(SIEDZIBA FOSA CAILIN, operacje Bialy Port; NIE Winterfell, NIE Beron)_
- **CICHY KUPIEC:** bez imienia _(towar: SOL; ksiega DOMU; cel: sfera Dreadfortu)_
- **BRAAVOS:** NESTA _(2,5 miesiaca w jedna strone)_
- **DORZECZE:** LUCAN _(zboze, weksle 420/80/340)_
- **PRAWA REKA / KWATERMISTRZ:** ERROLD _(przyzwoity kwatermistrz, przeszedl do Symona; jedno dowodztwo, wspolny rachunek)_
- **KANTOR - INSTRUMENTY:** TAM i WICK _(spisali instrumenty w nocy przed pieczecia; WICK na pensji, liter wyuczony przez Symona i Hala)_
- **WARZELNIA I SOLARNIA (Bialy Port):** HAL _(solona ryba w skladzie Domu; 6-8 dni od Fosy)_

### KORONA — _Kasa 3 - Skarb Polnocy_
- **NAMIESTNIK:** SYMON TALLY _(lord Fosy Cailin)_
- **JUSTYCJARIUSZ:** lord MEDGER CERWYN _(objazd; tryb Rady; corka JONELLE prowadzi Zamek Cerwyn; zona nie zyje)_
- **SKARBNIK:** GAWEN _(uznal 695 w calosci; chce placic przywilejem - odrzucone 300-03-02)_
- **KANCELARIA WINTERFELL:** BERON _(karta 7-dniowa; od 300-03-03 nowa rubryka: co przyszlo do Korony, a czego Namiestnik nie widzial)_
- **CELNIK / KOMORA:** GARTH _(URZEDNIK KORONY - nie przyjmuje polecen Symona w sprawach cla; ksiega bramy od 300-02-12; psiarze)_
- **PIERWSZY ADMIRAL:** TORREN SOLNY _(lowborn z Kamienistego Brzegu, wies spalili zelazni; osiem rubryk przyslal 300-03-02)_
- **MARSZALEK CHORAGWI:** OSRIC KAMIEN _(posel do Muru; MELDUNEK VII ZALEGLY, adres Winterfell)_
- **GLEBOKORZEN:** THEOMORE _(pierwszy mistrz; budowy NIKT nie prowadzi; spis flory jako pierwszy zbior)_
- **DORADCA W DUSTINPORCIE:** THEON GREYJOY _(kadluby + nauka admirala; jedzie z pismem do Torrena)_
- **REJESTRATOR KORONY:** ### PUSTE _(PUSTE OD ~299-11. Nazwisko zastrzegl sobie Krol; przypomnienie 300-02-27)_
- **TRZECI ODCZYT ZIARNA POZA FOSA:** ORIN WAGA i THELL SITO - szkoli WYSTAN _(Maester jest jeden i zostaje na Fosie. Odczyt poza Fosa NIE POTRZEBUJE maestera - potrzebuje wyuczonego oka, a maszyna do uczenia juz stoi (Wystan uczyl Herwina i Bennisa 300-03-02/03). Dwoch na objazd, nie jeden - bo odczyt sporny ma miec dwie reke.)_
- **CZLOWIEK OD FEVER:** JONN BRODOWY _(przewoznik z brodu - niesie OBIE polowy naraz: (a) ile tygodni rzeka stoi, kanalem Warryna do krannogmenow, (b) to, co czekalo na Weylina.)_
- **BUDOWA GLEBOKORZENIA:** VARD KILOF - czlowiek ORBELA _(jedzie ZE ZWIADEM KAMIENIA na Goracy Port (pozycja od 300-02-27) - jedna wyprawa, dwa rachunki, trzeci cel. Miejsce ma byc obejrzane, zanim Theomore stanie na Radzie 300-03-30.)_
- **AKADEMIA WOJSKOWA:** PIERWSZY MISTRZ: BRYNDEN TULLY (pismo w drodze) _(DATA: po Wielkiej Radzie. PLATNIK: Kasa 3. MIEJSCE: baszta w Przystani Wilka. Brynden mial szkolic wojsko i budowac zabezpieczenia juz przy doktrynie antyzelaznej 298-11-13 - to nie nowa prosba, to ta sama. JESLI ODMOWI: akademia otwiera sie z ZBROJMISTRZEM FOSY, bo on i tak juz uczy chlopcow.)_
- **OCHMISTRZ WYCHOWANKOW:** KASZTELAN WINTERFELL (scalone, nie powielone) _(prowadzi rejestr zamku od 300-02-17 i ma wytypowac 3-4 miejsca dla wychowankow - to JEST ten urzad, tylko nienazwany. Raport Gawena idzie do niego, nie obok niego.)_

### WINTERFELL — _Korona (Kasa 3) + dom Starkow_
_Rada 299-09-07 w skladzie: Cerwyn, Gawen, Rodwell, ser Alyn, Luwin, Catelyn._
- **KROL:** ROBB STARK _(list z prosba o godzine poszedl 300-03-01)_
- **KANCELARIA KORONY:** BERON _(karta 7-dniowa; nowa rubryka od 300-03-03)_
- **SKARBNIK:** GAWEN _(siedzi w Winterfell; sprawozdania zostawia na stole, nie krukiem)_
- **MAESTER WINTERFELL:** LUWIN _(agronomia chlodu 299-08-15; licencja nauczania; szkola Winterfell; przez niego idzie kruk z listem jencow)_
- **TRZYMA WINTERFELL:** ser ALYN _(czlowiek domu Starkow, szkolony przez Rodrika Cassela; NIE do zabrania przez Namiestnika)_
- **STOPIEN I - drugie nazwisko:** ser RODRIK CASSEL _(dopisany obok ser Alyna)_
- **RADA 299-09-07 - takze:** RODWELL _(zasiadal w radzie)_
- **KASZTELAN WINTERFELL:** kasztelan (imie do potwierdzenia) _(prowadzi rejestr zamku od 300-02-17; ma wytypowac 3-4 miejsca dla wychowankow i przeslac spis dzieci)_
- **ROLKA MUSZTRY:** pisarz Osrica w Winterfell _(odpis co miesiac; dziura na pln-wschodzie zostaje dziura)_
- **POLNOCNA CYTADELA / GLEBOKORZEN:** THEOMORE _(w Winterfell PRZY REJESTRZE, nie przy budowie)_
- **OCHMISTRZ WYCHOWANKOW:** ### PUSTE _(PUSTE; raport zamowiony u Gawena)_

### DOM PRYWATNY - BIALY PORT — _Kasa 1_
_Mira w Bialym Porcie; rozwiazanie. RHONA: 'to nie bedzie trzeci dzien trzeciego miesiaca - dziecko stoi NIZEJ, niz powinno na osmy miesiac, a DRUGIE PRZYCHODZI PREDZEJ NIZ PIERWSZE'._
- **ZONA:** MIRA _(slub przez Owena, umowa u Torrena)_
- **CORKA:** LYRA _(na czas rozwiazania idzie do ELNY)_
- **PRZY MIRZE:** RHONA, WENNA, ELNA _(Owen za rogiem; ludzie Wylisa przy bramie)_

### 🏛️ PIEC DEPARTAMENTOW (schemat dworu — urzad → kto go faktycznie robi)
**I. KANCELARIA (administracja centralna)**
- **KANCLERZ DOMENY** — GARRICK - kanclerz osobisty od 299-09; pelnomocnictwo notarialne na Fose od 300-03-01, pieczec lenna. ISTNIEJE.
- **GLOWNY ARCHIWISTA (kustosz ksiag)** — WAKAT - PILNY. Ksiegi sa i sa rozproszone: spis mieszkancow 299-06 (Warryn), rejestr dniowek (Mella), ksiega bramy (Garth - KORONA, nie lenno), ksiega Jastrzebi (pisarz grodzki), rejestr zamku (Winterfell). NIKT NIE TRZYMA CALOSCI I NIKT NIE WIE, CO W KTOREJ STOI.
- **PROTOKOLANT DWORSKI** — CZESCIOWO - PISARZE DWORU (dwaj z trojki Nesty) przepisuja akty, ale NARAD NIKT NIE PROTOKOLUJE. Narada budowlana 300-03-01 (dziewieciu naraz) nie ma protokolu. To funkcja do dopisania pisarzom, nie nowy urzad.
**II. SKARB I KONTROLA**
- **SKARBNIK LENNA (Kasa 2)** — WAKAT - PILNY. Kase 2 liczy i wydaje TA SAMA REKA: WARRYN (rachunek Etapu I na 300-03-09). Skarbnik GAWEN to Kasa 3 (Korona), HAL to Kasa 1 (Dom). Lenno nie ma wlasnego skarbnika.
- **LUSTRATOR (rewident objazdowy)** — WAKAT. Na poziomie krolestwa stoi juz wakat MISTRZ DOMU AUDYTOWEGO ('poza cechem nie ma mistrzow rewizji'). Na Fosie audyt robil dotad SAM SYMON (Dreadfort 299-10-21).
- **PISARZ PODATKOWY / URBARZ** — WAKAT - PILNY I NAJSTARSZY. OCZYNSZOWANIE weszlo 300-02-07 ('nowy winien grosz, a nie dni') - a KSIEGI PARCEL Z PRZYPISANYM CZYNSZEM NIE MA. Spis 299-06 liczy dusze i umiejetnosci, rejestr dniowek liczy dniowki, losowanie dzialek prowadzi lawa miasta. Nikt nie ma kolumny: kto, z czego, ile, kiedy.
- **_trzy_krzesla_kontroli** — OBSADZONE 300-03-03 wieczorem, z rozwiazaniem problemu wpisanym W SAME URZEDY, nie w termin: ARCHIWISTA nie pisze (przyjmuje za kwitem, katalog jawny). SKARBNIK liczy i nie wydaje (wydaje rzadca na jego kwit). LUSTRATOR nie pochodzi z zadnej ksiegi Fosy (czlowiek Cerwyna). Trzy krzesla, trzy rozne zrodla - i zadne nie sprawdza samo siebie.
**III. ADMINISTRACJA TERENOWA**
- **RZADCA KLUCZA** — WARRYN - rzadca calego lenna, 11 lat na tej ziemi. Posredniego szczebla (kilka wsi na jednego urzednika) NIE MA - i przy 640 duszach plus czterystu przybyszach Warryn jest juz waskim gardlem.
- **SOLTYSI (szczebel ponizej rzadcy)** — USTROJ ISTNIEJE OD 299-08: jedno palenisko = jeden glos, soltysa WYBIERAJA mieszkancy przy rzadcy, przysiega calej Fosie, rzadzi z lawa przysieglych majaca oba glosy (starzy z bagna I osadnicy). ALE: KTORE WSIE WYBRALY, KIEDY I KOGO - PYTANIE ZADANE I BEZ ODPOWIEDZI.
- **POBORCA CZYNSZOW** — WAKAT. Czynsz jest, poborcy nie ma. GARTH to celnik KORONY - nie przyjmuje polecen Symona i nie zbiera czynszow lenna.
- **MAGAZYNIER PROWIANTOWY** — ORLAND KORZEC - sklad, cztery przegrody, karta zywnosciowa na 300-03-07. ISTNIEJE. Osobno: SPIZARNIA DOMOWA = ALYS (klucze), a PROWIANTMISTRZ GARNIZONU = WAKAT (drabina Hendry'ego). Trzy rozne brzuchy, trzy rozne rece.
- **LESNICZY PRZYSIEGLY** — WAKAT - juz zapisany. Regale lesne zaprojektowane, nieobsadzone; olcha na lodzie Jastrzebi idzie z wlasnego lasu bez ewidencji.
**IV. SPRAWIEDLIWOSC I BEZPIECZENSTWO**
- **SEDZIA PATRYMONIALNY** — RODERYK - sad grodzki; umowy od rownowartosci 30 korcy; od 300-03-03 orzeka 'jedna sakiewka' (poprawka Cerwyna). ISTNIEJE.
- **PISARZ SADOWY** — PISARZ GRODZKI - trzyma ksiege Mchowych Jastrzebi (kto dowodzi, ten nie spisuje). ISTNIEJE.
- **NACZELNIK STRAZY** — DWOCH, I TAK MA BYC: HENDRY marszalek fortecy (zamek, ~50 druzyny) i KESSEL BRODATY, dowodca Mchowych Jastrzebi (20 ludzi, drogi i woda, pomoc celnikom). KESSEL PODLEGA BEZPOSREDNIO SYMONOWI, NIE HENDRY'EMU.
- **KLUCZNIK LOCHU (komisarz wiezienny)** — WAKAT. Zakaz naczelny Jastrzebi brzmi KTO CHWYTA, TEN NIE SADZI - ale KTO TRZYMA MIEDZY CHWYCENIEM A SADEM, nie zostalo powiedziane nigdy. Wiaze sie z otwarta sprawa jencow (Cerwyn).
**V. TECHNIKA I INFRASTRUKTURA**
- **MAGISTER INZYNIERII** — TRZECH, PODZIELENI RZECZOWO: WEYLIN - inzynier zamkowy (woda, dreny, sluzy, 'urzad na pokolenia'); ORBELO - kamien i budowa; BRAN - majordom robot (grobla, trakt). ISTNIEJE, i jest to najlepiej obsadzony departament lenna.
- **URZEDNIK MIAR I WAG** — BENNIS OD WAGI - wagowy miasta od 300-03-03, wage trzyma i placi RADA MIASTA, nie zamek. Nad nim HERWIN SZALA, burmistrz, 12 lat przy wadze, autor poprawki o ZNAKU NORMY. ISTNIEJE - ale jako urzad MIASTA. Lenno swojej wagi nie ma i miec nie powinno: lord nadaje regule, miasto sadzi.

### 🔴 WAKATY (3)
- **REJESTRATOR KORONY** _(KORONA)_ **POZA REKA SYMONA** — NIE DO OBSADZENIA PRZEZ NAMIESTNIKA - KROL ZASTRZEGL SOBIE NAZWISKO (zasada 22: prerogatywa nie idzie pod glosy ani pod nadanie). Piaty miesiac. Jedyne, co wolno: przypominac.
- **MISTRZ DOMU AUDYTOWEGO** _(KORONA)_ — PIERWSZEGO TRZEBA ZROBIC, NIE ZNALEZC - poza cechem mistrzow rewizji nie ma. TOMMARD KOSA (lustrator Fosy od 300-03-03) jest nasieniem tego urzedu, nie jego zaprzeczeniem.
- **SOLTYSI - ILE WSI WYBRALO** _(LENNO)_ **PYTANIE BEZ ODPOWIEDZI** — ustroj od 299-08 (jedno palenisko jeden glos, lawa z oboma glosami); Symon pytal, ktore wsie wybraly - odpowiedzi nie dostal.

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
- **300-03-03 lub WCZESNIEJ** — ROZWIAZANIE MIRY, Bialy Port. RHONA: 'to nie bedzie trzeci dzien trzeciego miesiaca - dziecko stoi NIZEJ, niz powinno, a DRUGIE przychodzi predzej niz pierwsze'
- **300-03-05** — Cerwyn wyjezdza; odpis urzadzen Fosy ma byc gotowy
- **300-03-06** — czlowiek Wymana na Fosie - pomiar przewloki pod dwie pieczecie
- **300-03-06..08** — odpowiedz Krola na pismo z 300-02-19 (rejestry Locke'ow, pochodzenie, jency)
- **300-03-07** — WYJAZD SYMONA z Fosy
- **300-03-07** — pierwsza KARTA ZYWNOSCIOWA (geby, korce, na ile dni)
- **300-03-07** — ODBICI BEZ DOMU - ilu Fosa bierze; limit z karty, nie z uznania
- **300-03-07** — pytania proby wstepnej dla lawy
- **300-03-07** — KARTA ODHACZEN GARRICKA - czwarta kolumna (idzie / stoi / pyta kancelarie) przy kazdym wierszu
- **300-03-07** — przywilej bagienny - szesc rzemiosl na slup; zegar pana
- **300-03-07** — cena minimalna z iloscia + cena dzisiejsza + oferta kupna nasienia na slup
- **300-03-09** — WARRYN ZAMYKA RACHUNEK ETAPU I (dwa niepoliczone otwory: kamien z zewnatrz, szesc pozycji Kasy 2)
- **po 300-03-09** — najwczesniejsza uczciwa data papieru dluznego lenna (8,5 prosty, 5 lat, odnawialny)
- **300-03-10** — CICHY KUPIEC rusza (sol, ksiega Domu, sfera Dreadfortu)
- **~300-03-13** — BIALY PORT - WYMAN: podpis Ujscia z reki do reki, splawnosc Samotnych Wzgorz, udzial w drewnie, Medrick, dwa nowe porty
- **~300-03-13** — BIALY PORT - HAL: placowki (Braavos, Pentos, Gulltown, Highgarden), obrot przez rece cechowe, forma zwrotu 695, POCHODZENIE ziarna, suma emisji
- **~300-03-13** — koniec przewagi NIEOGLOSZONEGO STATUTU - do podpisu Wymana
- **300-03-29** — CZTERNASCIE KART DO KWATER - dwie kolumny: NAD TYM GLOSUJECIE / TO OGLOSZONO; plus druga prosba do domow
- **300-03-30** — WIELKA RADA. 0. MUR (meldunek + aklamacja) - I. ZIEMIA BEZ PANA (pod glosy sama PROBA) - II. WODA - III. CHLEB + REWIZJA - IV. HANDEL
- **300-04-01** — ZALEGLOSC KARHOLDU 148/160 - dwanascie
- **przed 300-04-01** — RAMSAY - wezwanie do czterdziestu domow; meldunek MA PASC TAKZE, JESLI NIE PRZYJEDZIE
- **300-04-01** — BRACTWO RZEMIOSLA WOLNEGO - miasto wykonuje statut
- **ten tydzien** — FEVER polowa (a): ile tygodni rzeka stoi - kanal Warryna do krannogmenow + przewoznicy z brodu
- **ten tydzien** — NARYBEK do stawow + ROSLINY JADALNE - tym samym jezdzcem co Fever
- **tygodnie - PRZED SIEWEM** — ZRODLO NASIENIA owsa i jeczmienia NA TEN SIEW
- **~300-03-13** — WILLA: druga droga na poludnie - dwie kolumny rejestru; czyta MELLA, wynik do Willi szyfrem
- **V/300** — NESTA: kolumna dziesieciu przystani zachodnich (fracht) + pytanie o DAENERYS
- **jesien 300** — ZYTO OZIME - siew; odpowiedz OSRICA o Darze pod to, nie pod wiosne
- **koniec VI/300** — DRUGA RATYFIKACJA traktatu z Dorzeczem; zakaz zaliczek przed ratyfikacja
- **bez daty - CISZA** — MELDUNEK VII OSRICA (Mur) - zalegly; doszlo mu pytanie o Dar
- **bez daty - CISZA** — PRZYSTAN WILKA - status budowy; pyta CERWYN jako wspolwlasciciel cwiartki; podanie nazwiska budowniczego jest czescia odpowiedzi
- **bez daty - CISZA** — DONNEL OBROK (Dustinport, budowa) - pytanie pod pieczecia, jezdziec eskadry
- **bez daty** — GARTH: liczba miesieczna dziury w komorach wodnych - zmierzona 299-10-01 i NIE ZMIERZONA PONOWNIE
- **bez daty** — BERON: wszystko, co przyszlo od BRYNDENA TULLY'EGO od 299-07, z datami; potem list do Blackfisha (poludniowa sciana, nie traktat)
- **bez daty** — THEOMORE: gdzie kolebka, ile kosztuje PIERWSZY ROK, kogo wzialbys jako pierwszego ucznia; spis flory jako pierwszy zbior (w reke na Radzie)
- **300-03-04** — URBARZ ZALOZONY - cztery kolumny KTO / Z CZEGO / ILE / KIEDY; pierwszy wpis to szesc tygodni niepobranego czynszu (od 300-02-07)
- **300-03-04** — LAWA MIASTA SADZA KOWALA (Brusk od Miecha, wskazala Mella) - kuznia idzie pierwsza albo nie idzie nic
- **300-03-05** — CERWYN WYJEZDZA - ma zostawic TOMMARDA KOSE jako lustratora Fosy na rok
- **ten tydzien** — SOLTYSI: ktore wsie wybraly, kiedy i kogo - pytanie zadane dawno, odpowiedzi nie bylo
- **300-03-30** — AKADEMIA WOJSKOWA: data po Radzie, platnik Kasa 3, baszta w Przystani Wilka; pierwszy mistrz BRYNDEN TULLY, zapasowo zbrojmistrz Fosy
- **wyslane 300-02-27 - CISZA** — PRZYPOMNIENIE O REJESTRATORZE KORONY. Jedno zdanie, bez nazwiska, spisane przez Garricka pod dyktando: 'KRZESLO REJESTRATORA KORONY STOI PUSTE CZWARTY MIESIAC. NAZWISKA NIE PODAJE, BO ZASTRZEGLISCIE JE SOBIE. PODAJE DATE.' Ten sam goniec co prosba o zwyczaj, OSOBNA KARTA - zeby nie zamienic tamtej w upomnienie. UWAGA: UCHO KORONY I REJESTRATOR KORONY TO JEDNO KRZESLO (odkryte 300-02-27) - puste jest wieksze, niz wyglada.
- **PRZED Rada 300-03-30 - WARUNKOWE** — SPRAWA CAILIN (prawo skladu + garnizon). KROL OBIECAL 300-02-07: rozstrzygnie PRZED Rada, ale DOPIERO GDY PRZYJDZIE PISMO MIASTA, NIE NAMIESTNIKA. Prosba miasta o piec dni targowych stoi na slupie od 300-03-03 - ALE NA SLUPIE, NIE W WINTERFELL. Dopoki lawa nie wysle wlasnego pisma, zegar Krola nie ruszyl. ROZSTRZYGNIECIE GRACZA 300-03-03: lawa wysyla wlasne pismo 300-03-04, krukiem.
- **300-03-04** — PISMO MIASTA CAILIN DO KORONY - wlasna pieczec miasta, podpisy lawy, krukiem z Fosy (2 dni). TRESC: TYLKO sprawa Cailin (przymus skladu piec dni targowych + garnizon). NIE laczyc z ustrojem miast - tamto Krol przyjmie tylko OD WSZYSTKICH NARAZ i pismo Cailin utknie za czternastoma innymi. WARUNEK FORMY: Symon nie dyktuje ani slowa; podaje Herwinowi TYLKO to, ze warunek Krola istnieje.
- **~300-03-06** — PISMO MIASTA W WINTERFELL - od tej chwili biegnie obietnica Krola z 300-02-07: rozstrzygnie PRZED Rada

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
- [300-03-03] `lenno/MELLA`: ### RESZTA KRZESEL OBSADZONA - 300-03-03, pozny wieczor. Rozkaz gracza: 'natychmiast o pozostale osoby'. Bez rzutow. PO TYM WIECZORZE LENNO FOSY CAILIN NIE MA ANI JEDNEGO WAKATU. Pierwszy ra…
- [300-03-03] `kancelaria_namiestnika_299_09`: ### KOREKTA REJESTRU TERMINOW - 300-03-03, wskazanie gracza: 'ja juz przypominalem krolowi i wyslalem mu list, czy masz go w terminach'. MA RACJE - NIE MIALEM. LIST ISTNIEJE W ZAPISIE I NIE …
- [300-03-03] `ustroj_urzedow`: ### KOREKTA REJESTRU TERMINOW - 300-03-03, wskazanie gracza: 'ja juz przypominalem krolowi i wyslalem mu list, czy masz go w terminach'. MA RACJE - NIE MIALEM. LIST ISTNIEJE W ZAPISIE I NIE …
- [300-03-03] `ucho_korony`: ### KOREKTA REJESTRU TERMINOW - 300-03-03, wskazanie gracza: 'ja juz przypominalem krolowi i wyslalem mu list, czy masz go w terminach'. MA RACJE - NIE MIALEM. LIST ISTNIEJE W ZAPISIE I NIE …
- [300-03-03] `prawo_o_skladach_zboza_299_09`: ### KOREKTA REJESTRU TERMINOW - 300-03-03, wskazanie gracza: 'ja juz przypominalem krolowi i wyslalem mu list, czy masz go w terminach'. MA RACJE - NIE MIALEM. LIST ISTNIEJE W ZAPISIE I NIE …
- [300-03-03] `polnoc/robb_stark`: ### KOREKTA REJESTRU TERMINOW - 300-03-03, wskazanie gracza: 'ja juz przypominalem krolowi i wyslalem mu list, czy masz go w terminach'. MA RACJE - NIE MIALEM. LIST ISTNIEJE W ZAPISIE I NIE …
- [300-03-03] `lenno/HERWIN`: ### KOREKTA REJESTRU TERMINOW - 300-03-03, wskazanie gracza: 'ja juz przypominalem krolowi i wyslalem mu list, czy masz go w terminach'. MA RACJE - NIE MIALEM. LIST ISTNIEJE W ZAPISIE I NIE …
- [300-03-03] `prawo_o_skladach_zboza_299_09`: ### LAWA MIASTA WYSYLA WLASNE PISMO DO KORONY - rozstrzygniecie gracza 300-03-03, wykonanie 300-03-04, krukiem. Bez rzutu (wlasny urzad miasta robi swoja robote, zasada 27). ZEGAR KROLA RUSZ…
- [300-03-03] `projekt_cailin`: ### LAWA MIASTA WYSYLA WLASNE PISMO DO KORONY - rozstrzygniecie gracza 300-03-03, wykonanie 300-03-04, krukiem. Bez rzutu (wlasny urzad miasta robi swoja robote, zasada 27). ZEGAR KROLA RUSZ…
- [300-03-03] `ustroj_urzedow`: ### LAWA MIASTA WYSYLA WLASNE PISMO DO KORONY - rozstrzygniecie gracza 300-03-03, wykonanie 300-03-04, krukiem. Bez rzutu (wlasny urzad miasta robi swoja robote, zasada 27). ZEGAR KROLA RUSZ…
- [300-03-03] `lenno/HERWIN`: ### LAWA MIASTA WYSYLA WLASNE PISMO DO KORONY - rozstrzygniecie gracza 300-03-03, wykonanie 300-03-04, krukiem. Bez rzutu (wlasny urzad miasta robi swoja robote, zasada 27). ZEGAR KROLA RUSZ…
- [300-03-03] `polnoc/robb_stark`: ### LAWA MIASTA WYSYLA WLASNE PISMO DO KORONY - rozstrzygniecie gracza 300-03-03, wykonanie 300-03-04, krukiem. Bez rzutu (wlasny urzad miasta robi swoja robote, zasada 27). ZEGAR KROLA RUSZ…
