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

## ⏰ KOLEJKA INBOUND (zasada 40) — **poranny rzut ciagnie sie STAD, nie z pamieci**
**83 otwartych** · **6 PRZETERMINOWANYCH** · 2 wraca dzis

### 🔴 PRZETERMINOWANE — KAZDA MUSI DOSTAC ROZSTRZYGNIECIE W TEJ TURZE
_przyszlo · nie przyszlo I WIADOMO DLACZEGO · przyszlo co innego. Rzut nalezy sie sprawie zewnetrznej._
- **+92 dni** — LIST DO STANNISA BARATHEONA, redakcja II, z ZAPROSZENIEM DO PENTOS. Os odmowy udzialu w wojnie wyrzucona - sprawa miedzy koronami … · _kanal:_ morze na poludnie (Reach, Highgarden) · _zamyka:_ odpowiedz ze Smoczej Skaly
- **+22 dni** — LIST DO HALA: WYKUPIC WEKSEL DANY BOLTONOM. Podstawa: 299-10-20 Dreadfort, zamiec - postoj oplacony WEKSLEM NA DOM TALLY, Roose pr… · _kanal:_ kruk Fosa-Bialy Port · _zamyka:_ weksel w rekach Domu albo pisemna odmowa Roose'a
- **+22 dni** — LIST DO GAWENA: czlowiek do PRZYSTANI WILKA - 'czego szukac, nie kogo'. Zbiega sie z cisza o statusie budowy Przystani (pyta tez C… · _kanal:_ kruk Winterfell-Fosa · _zamyka:_ nazwisko albo opis czlowieka
- **+13 dni** — PRZYSTAN WILKA - status budowy; pyta CERWYN jako wspolwlasciciel cwiartki; podanie nazwiska budowniczego jest czescia odpowiedzi · _kanal:_ jezdziec Fosa-Dustinport · _zamyka:_ meldunek z nazwiskiem
- **+13 dni** — DONNEL OBROK (Dustinport, budowa) - pytanie pod pieczecia, jezdziec eskadry · _kanal:_ jezdziec Fosa-Dustinport · _zamyka:_ meldunek w formie osmiu rubryk
- **+2 dni** — POMIAR OSWYNA - zlecenie z 299-09-13: przez cala zime MIERZYC TEN SAM SKLAD przy zsypaniu i przy wysypaniu i spisywac roznice. W z… · _kanal:_ kruk Winterfell-Fosa · _zamyka:_ liczba roznicy zsyp/wysyp za zime

### 🟡 WRACA DZIS
- PRZYPOMNIENIE O REJESTRATORZE KORONY. Jedno zdanie, bez nazwiska, spisane przez Garricka pod dyktando: 'KRZESLO REJESTRATORA KORON… · _kanal:_ kruk Winterfell-Fosa
- ZLECENIE DLA WILLI - ZWEZENIE (300-01-27): PRZESTAC SZUKAC POSREDNIKA, ZAWEZIC DO PETYRA BAELISHA I DO KROLEWSKIEJ PRZYSTANI. Pods… · _kanal:_ siatka Willi

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
- **bez daty - CISZA** — MELDUNEK VII OSRICA (Mur) - zalegly. ⚠ TO NIE JEST ZALEGLOSC URZEDOWA: TEDY MA WROCIC ODPOWIEDZ OD MANCE'A RAYDERA. Poslaniec za Mur wyszedl 300-02-07; Osric jest jedynym kanalem, ktorym to moze przyjsc. Jego cisza i cisza zza Muru to JEDNA CISZA, nie dwie. · _kto:_ **OSRIC** · _zamyka:_ meldunek **⚠ ZAMKNIETE 300-03-03 - MELDUNEK VII WYDANY; SPOZNIONY, BO OSRIC CZEKAL, AZ BEDZIE MIAL CO NAPISAC O POSLANCU, I NIE DOCZEKAL SIE**
- **bez daty - CISZA** — PRZYSTAN WILKA - status budowy; pyta CERWYN jako wspolwlasciciel cwiartki; podanie nazwiska budowniczego jest czescia odpowiedzi · _kto:_ **CERWYN** · _zamyka:_ meldunek z nazwiskiem
- **bez daty - CISZA** — DONNEL OBROK (Dustinport, budowa) - pytanie pod pieczecia, jezdziec eskadry · _kto:_ **DONNEL** · _zamyka:_ meldunek w formie osmiu rubryk
- **bez daty** — GARTH: liczba miesieczna dziury w komorach wodnych - zmierzona 299-10-01 i NIE ZMIERZONA PONOWNIE · _kto:_ **GARTH** · _zamyka:_ nowa liczba
- **bez daty** — BERON: wszystko, co przyszlo od BRYNDENA TULLY'EGO od 299-07, z datami; potem list do Blackfisha (poludniowa sciana, nie traktat) · _kto:_ **BERON** · _zamyka:_ wykaz
- **bez daty** — THEOMORE - PYTANIA POPRAWIONE 300-03-03. STARE BYLY ZLE ZADANE: kolebka JEST USTALONA (Nowy Zamek w Bialym Porcie, dar Wymana 299-08-11), a pierwsza dziesiatka uczniow JEST WZIETA od 299-09-21. WLASCIWE PYTANIA: ILU Z DZIESIECIU ZOSTALO I CO SPISALI · ile kosztowal PIERWSZY ROK NAPRAWDE · kiedy gmach w Przystani Wilka bedzie gotowy przejac serce · i CZY DZIESIECIU WYSTARCZY, skoro Fosa ma teraz wlasna szkole i ochmistrza nauki. · _kto:_ **THEOMORE** · _zamyka:_ odpowiedz
- **300-03-04** — URBARZ ZALOZONY - cztery kolumny KTO / Z CZEGO / ILE / KIEDY; pierwszy wpis to szesc tygodni niepobranego czynszu (od 300-02-07) · _kto:_ **SARRA OD KRESKI + INGA LICZYDLO** · _zamyka:_ ksiega otwarta z pierwsza strona
- **300-03-04** — LAWA MIASTA SADZA KOWALA (Brusk od Miecha, wskazala Mella) - kuznia idzie pierwsza albo nie idzie nic · _kto:_ **lawa burmistrza** · _zamyka:_ posadzenie
- **300-03-05** — CERWYN WYJEZDZA - ma zostawic TOMMARDA KOSE jako lustratora Fosy na rok · _kto:_ **CERWYN** · _zamyka:_ czlowiek zostaje, kiedy pan odjezdza
- **ten tydzien** — SOLTYSI: ktore wsie wybraly, kiedy i kogo - pytanie zadane dawno, odpowiedzi nie bylo · _kto:_ **WARRYN** · _zamyka:_ lista wsi z nazwiskami i datami
- **300-03-30** — AKADEMIA WOJSKOWA: data po Radzie, platnik Kasa 3, baszta w Przystani Wilka; pierwszy mistrz BRYNDEN TULLY, zapasowo zbrojmistrz Fosy · _kto:_ **Symon / Brynden** · _zamyka:_ odpowiedz Blackfisha
- **wyslane 300-02-27 - CISZA** — PRZYPOMNIENIE O REJESTRATORZE KORONY. Jedno zdanie, bez nazwiska, spisane przez Garricka pod dyktando: 'KRZESLO REJESTRATORA KORONY STOI PUSTE CZWARTY MIESIAC. NAZWISKA NIE PODAJE, BO ZASTRZEGLISCIE JE SOBIE. PODAJE DATE.' Ten sam goniec co prosba o zwyczaj, OSOBNA KARTA - zeby nie zamienic tamtej w upomnienie. UWAGA: UCHO KORONY I REJESTRATOR KORONY TO JEDNO KRZESLO (odkryte 300-02-27) - puste jest wieksze, niz wyglada. · _kto:_ **SYMON -> ROBB STARK** · _zamyka:_ NAZWISKO OD KROLA. A jesli do Rady 300-03-30 nie przyjdzie - ZAMYKA TO MILCZENIE: przestaje byc prosba bez odpowiedzi, a staje sie faktem, ktory Namiestnik moze wypowiedziec na Radzie. Drugi raz sie nie prosi. **⚠ OTWARTE - LIST POSZEDL 300-02-27, ODPOWIEDZI NIE BYLO**
- **PRZED Rada 300-03-30 - WARUNKOWE** — SPRAWA CAILIN (prawo skladu + garnizon). KROL OBIECAL 300-02-07: rozstrzygnie PRZED Rada, ale DOPIERO GDY PRZYJDZIE PISMO MIASTA, NIE NAMIESTNIKA. Prosba miasta o piec dni targowych stoi na slupie od 300-03-03 - ALE NA SLUPIE, NIE W WINTERFELL. Dopoki lawa nie wysle wlasnego pisma, zegar Krola nie ruszyl. ROZSTRZYGNIECIE GRACZA 300-03-03: lawa wysyla wlasne pismo 300-03-04, krukiem. · _kto:_ **LAWA MIASTA CAILIN / HERWIN SZALA** · _zamyka:_ pismo MIASTA w Winterfell - ono uruchamia obietnice Krola **⚠ WARUNEK SPELNIONY 300-03-04 - PISMO MIASTA W DRODZE**
- **300-03-04 SWIT** — PISMO MIASTA CAILIN DO KORONY - wlasna pieczec miasta, podpisy lawy, krukiem z Fosy (2 dni). TRESC: TYLKO sprawa Cailin (przymus skladu piec dni targowych + garnizon). NIE laczyc z ustrojem miast - tamto Krol przyjmie tylko OD WSZYSTKICH NARAZ i pismo Cailin utknie za czternastoma innymi. WARUNEK FORMY: Symon nie dyktuje ani slowa; podaje Herwinowi TYLKO to, ze warunek Krola istnieje. · _kto:_ **LAWA MIASTA / HERWIN SZALA** · _zamyka:_ kruk w powietrzu **⚠ WYSLANE - PIECZEC MIASTA, PODPISY LAWY, KRUK O SWICIE**
- **~300-03-06** — PISMO MIASTA W WINTERFELL - od tej chwili biegnie obietnica Krola z 300-02-07: rozstrzygnie PRZED Rada · _kto:_ **kancelaria Korony (BERON)** · _zamyka:_ rozstrzygniecie Krola w sprawie skladu i garnizonu Cailin **⚠ OTWARTE - ZEGAR LICZY SIE OD 300-02-07, NIE OD WYSLANIA. ZWLOKA POWSTALA Z ZANIEDBANIA PROWADZACEGO (PISMO NIE BYLO W REJESTRZE) - NIE PRZECHODZI NA GRACZA: ROZSTRZYGNIECIE KROLA MA PACZC PRZED RADA, JAK OBIECAL.**
- **wyslany 300-02-27 - odpowiedz IV/300 najwczesniej** — LIST DO LADY OLENNY TYRELL. Tresc: Polnoc przezywa zime; Dom chce wejsc do Highgarden PO CICHU, zeby moc rozmawiac blizej. PIERWSZY WLASNY RUCH DOMU NA REACH - nie pismo Namiestnika, tylko Domu Handlowego (Kasa 1). PODSTAWA RELACJI: od 300-02-25 to nie jest 'tajny kanal', tylko RELACJA HANDLOWA Z DRUGIM SPICHLERZEM WESTEROS - obie strony maja powod, zeby jej nie zerwac, i zadna nie musi tlumaczyc, po co pisze. ZBIEGA SIE Z: placowka HIGHGARDEN na liscie do Hala (Bialy Port ~300-03-13) - TEN SAM CEL, DWIE DROGI. Nie wysylac trzeciej. ⚠ KOREKTA KANALU 300-03-03: poszedl KRUKIEM, nie droga morska Domu - wiec wraca TYGODNIE, nie miesiace. Koszt tej szybkosci: lancuch maesterski na poludnie idzie przez STARMIASTO, a pismo mialo byc 'po cichu'. · _kto:_ **SYMON / DOM HANDLOWY TALLY -> OLENNA TYRELL** · _zamyka:_ odpowiedz z Highgarden ALBO zgoda na cicha placowke. Droga: Fosa -> Bialy Port (6-8 dni) -> morzem na poludnie; tam i z powrotem to TYGODNIE, nie dni. **⚠ OTWARTE - W DRODZE, ZA WCZESNIE NA CISZE**
- **wyslany 300-02-07 - CISZA MIESIAC** — LIST DO HALA: WYKUPIC WEKSEL DANY BOLTONOM. Podstawa: 299-10-20 Dreadfort, zamiec - postoj oplacony WEKSLEM NA DOM TALLY, Roose przyjal papier bez pytania. Lezy piaty miesiac. NA DREADFORCIE LEZY PODPIS SYMONA - papier z jego nazwiskiem i CUDZA WOLA, platny na zadanie, ktory kladzie sie na stol wtedy, kiedy sie chce. PILNE PRZEZ TRZY ZBIEGI: cichy kupiec na Dreadfort 300-03-10, Ramsay wezwany przed 300-04-01, Rada 300-04-01 z Boltonami na sali. · _kto:_ **HAL SIEROTA** · _zamyka:_ weksel w rekach Domu albo pisemna odmowa Roose'a **⚠ OTWARTE - PILNE**
- **wyslany 300-02-27** — LIST DO ROOSE'A BOLTONA - nie czeka na spotkanie. Ta sama sprawa co weksel. · _kto:_ **ROOSE BOLTON** · _zamyka:_ odpowiedz ALBO milczenie do Rady 300-04-01 - i wtedy milczenie jest odpowiedzia
- **300-02-25 (ponowiony; pierwszy 299-09-08)** — LIST DO HOWLANDA REEDA. KANALU KRUCZEGO NIE MA - Greywater Watch PLYWA. Protokol: poslaniec jedzie na Przesmyk, staje w umowionym miejscu PRZY GROBLI i czeka, az krannogowie sami wyjda. MOZE DZIEN, MOZE DWA TYGODNIE - cisza tutaj NIE JEST cisza. · _kto:_ **poslaniec przy grobli** · _zamyka:_ krannogowie wychodza ALBO spotkanie z Howlandem **⚠ OTWARTE - BEZ ZEGARA Z NATURY KANALU**
- **wyslany 300-03-01, osobnym jezdzcem** — LIST DO SKARBNIKA GAWENA - PAKIET MONETARNY, PIEC POZYCJI. Podstawa liczbowa: dochod monetarny Korony w normalnym roku 8000-20000 smokow, DZIS 3000-6000. Mennica Wilk bije od 299. · _kto:_ **GAWEN** · _zamyka:_ odpowiedz na PIEC pozycji - nie na jedna
- **wyslany 300-02-07** — LIST DO GAWENA: czlowiek do PRZYSTANI WILKA - 'czego szukac, nie kogo'. Zbiega sie z cisza o statusie budowy Przystani (pyta tez Cerwyn jako wspolwlasciciel cwiartki). · _kto:_ **GAWEN** · _zamyka:_ nazwisko albo opis czlowieka
- **wyslany 300-03-01** — LIST DO KROLA - PROSBA O ROZMOWE O PORZADKU, NIE WYKLAD O NIM. Forma narzucona zasada, ktora Krol sam nalozyl na Symona przy Karcie Wychowankow: 'idzcie do niego DZIS. NIE Z KARTA - Z PYTANIEM'. List niesie prosbe i powod, nie argumentacje. OSOBNY od pisma z 02-19 i od przypomnienia o Rejestratorze. · _kto:_ **ROBB STARK** · _zamyka:_ WYZNACZONA GODZINA - przed Rada albo na Radzie
- **zlecone 300-03-02** — KANON JADLA POLNOCY - zadanie dla WYSTANA, trzy czesci: (1) dieta i dania z waloru miejscowego; (2) kanon potraw - co siac, co do szklarni, co hodowac, co lowic; (3) ruszyc ze szklarniami i szkolkami rolniczymi. OD 300-03-03 MA WYKONAWCE: LOWCZY HAKON OD JASZCZURA - wczesniej kanon byl lista bez rak. · _kto:_ **WYSTAN + WERRAN + HAKON** · _zamyka:_ kanon spisany i PIERWSZY POSILEK Z NIEGO PODANY - kanonu nie oglasza sie na slupie, kanon sie je
- **~300-03-15 (termin podany w samym liscie)** — ODPOWIEDZ MIRY - DZIESIEC DROBNYCH PYTAN O SZKOLE. Reka Symona, NIE rozkazem Korony (wskazowka Luwina: 'na rozkaz odpowie tez, ale na list odpowie PRAWDE O TYM, CO JEJ NIE WYCHODZI'). Zapisany bieg kruka: WRACA PRZED DRUGA POLOWA TRZECIEGO MIESIACA. ZDERZA SIE Z ROZWIAZANIEM - moze nie byc w stanie odpisac. · _kto:_ **MIRA** · _zamyka:_ odpowiedz na dziesiec pytan
- **wyslany 300-02-28** — LIST DO MIRY: 'kto nauczy tych dziesiecioro UCZYC' - druga sprawa szkolna, z powrotna. · _kto:_ **MIRA** · _zamyka:_ odpowiedz
- **RIVERRUN - jest na miejscu** — LADY CATELYN W RIVERRUN. Wyjechala z Winterfell 299-10-05; cel od poczatku: RIVERRUN, negocjowac w imieniu Polnocy. OKNO PRZEJAZDU PRZEZ FOSE (02-25..03-07) SIE ZAMKNELO - nie przejezdza, siedzi u brata. JEJ ROLA, nietknieta od 299-09-19: ONA OTWIERA DRZWI jako TULLY, w domu swojego ojca, do swojego brata. Korona przez nie wchodzi - ona nie podpisuje, nie ustepuje, nie negocjuje za Polnoc. LIST SYMONA do rak wlasnych (napisany 300-02-16, wlasna reka, BEZ pieczeci Namiestnika) idzie PRZEZ LUCANA od 300-02-27 - a Lucan siedzi w Dorzeczu, wiec kanal jest wlasciwy. KARTKA U WARRYNA NA FOSIE ZOSTAJE - na wypadek, gdyby wracala tedy. · _kto:_ **CATELYN w Riverrun / LUCAN doreczenie** · _zamyka:_ odpowiedz od niej ALBO ruch Edmure'a przy traktacie (druga ratyfikacja, koniec VI/300) **⚠ OTWARTE - POPRAWIONE WSKAZANIEM GRACZA 300-03-03: ONA SIEDZI W RIVERRUN**
- **wyslany 300-02-17** — NESTA - CZWARTE ZLECENIE: fracht na zachodnim morzu (nie okret - LADOWNIA; domy braavoskie maja kantory w Lannisporcie i Starym Miescie) + LUPACZ KAMIENIA. Kolejka wypisana wprost: (1) ksiega Antaryonow (2) karta cen (3) wschod i dziewczyna (4) to. 'Czwarta jest czwarta i ma nia zostac.' · _kto:_ **NESTA** · _zamyka:_ odpowiedz z Braavos - 2,5 miesiaca w jedna strone
- **wyslany 300-02-07** — NESTA - KADRY Z BRAAVOS (pozycja 2 kolejki). · _kto:_ **NESTA** · _zamyka:_ ludzie albo nazwiska
- **wyslany 300-03-01** — NESTA - ROZGLOSIC W BRAAVOS PRZYWILEJE FOSY; ludzie maja kierunek. ALE rozglaszanie ZACZYNA SIE PO PODPISIE, nie przed. · _kto:_ **NESTA** · _zamyka:_ podpis przywileju -> potem rozglos **⚠ OTWARTE - WARUNKOWE**
- **wyslany 300-03-03 o brzasku** — KRUK DO BIALEGO PORTU - pytanie o Mire. Poczta DOMU, pieczec DOMU, nie Korony. Dojdzie w dwa dni i tak czy inaczej PO FAKCIE - wysylany nie po to, zeby zdazyc, tylko zeby ktos tam wiedzial, ze pytano tego dnia. · _kto:_ **SYMON -> Bialy Port** · _zamyka:_ wiadomosc o rozwiazaniu
- **WIOSNA 300 - WYMAGALNE TERAZ** — POMIAR OSWYNA - zlecenie z 299-09-13: przez cala zime MIERZYC TEN SAM SKLAD przy zsypaniu i przy wysypaniu i spisywac roznice. W zleceniu stoi wprost: 'DO WIOSNY Skarbnik bedzie mial czym UZASADNIC ogloszona liczbe, zamiast ja wymyslic'. WIOSNA JEST TERAZ, A LICZBY NIKT NIE ZAZADAL. Ksiega spichlerza Zimowego Miasta miala byc WZOREM dla ksiag skladowych krolestwa - i cala dzisiejsza maszyna zbozowa (cena minimalna, rubryka stanu ziarna, przymus skladu) stoi bez tego pomiaru. · _kto:_ **OSWYN -> GAWEN** · _zamyka:_ liczba roznicy zsyp/wysyp za zime **⚠ OTWARTE - PRZETERMINOWANE**
- **PRZED ~300-03-13 (Bialy Port)** — ZLECENIE DLA GAWENA z 299-09-14: policzyc i OGLOSIC, ile placi JEDEN LADUNEK NA FOSIE RAZEM - myto lenna PLUS clo Korony, wedle rodzaju towaru. Warunek zapisany w zleceniu: 'ma byc gotowe i jawne ZANIM Wyman otworzy ksiegi Bialego Portu'. SYMON JEDZIE DO WYMANA ZA DZIESIEC DNI. Cel podwojny: dac Manderly'emu wzorzec i dowod dobrej wiary; sprawdzic, czy wlasna brama nie jest juz zaporowa - NIKT NIGDY NIE ZSUMOWAL OBU WARSTW. · _kto:_ **GAWEN + GARTH** · _zamyka:_ jedna liczba na slupie, jawna, przed Bialym Portem **⚠ ZAMKNIETE 300-03-03 - POLICZONE NA FOSIE, NIE W WINTERFELL. OBIE KSIEGI BYLY W MURACH.**
- **wyslany 299-09-15 - CISZA POL ROKU** — LIST DO MAESTERA AEMONA (Czarny Zamek). Pismo PRYWATNE - od czlowieka, ktory przysylal ziarno, nie od Namiestnika Krola; Aemon pisal do SYMONA, nie do Winterfell, i podal powod: 'to WY przysylaliscie ziarno; ludzie tutaj wiedza, czyje ono bylo'. DRUGA CISZA Z TEGO SAMEGO MIEJSCA - obok zaleglego meldunku VII Osrica. · _kto:_ **AEMON** · _zamyka:_ odpowiedz z Muru ALBO wiadomosc, ze nie zyje - a to tez jest odpowiedz **⚠ ZAMKNIETE - ODPOWIEDZ PRZYSZLA 299-09-18 I ZOSTALA PRZECZYTANA. NIE BYLO TU CISZY; JA JEJ NIE SPRAWDZILEM.**
- **wyslany 299-09-15 - CISZA POL ROKU** — LIST DO STANNISA BARATHEONA, redakcja II, z ZAPROSZENIEM DO PENTOS. Os odmowy udzialu w wojnie wyrzucona - sprawa miedzy koronami zamknieta od sierpnia 299 (Stannis PIERWSZY uznal niepodleglosc Polnocy na pismie). Zostaje zaproszenie i to, co po nim. · _kto:_ **STANNIS** · _zamyka:_ odpowiedz ze Smoczej Skaly
- **wyslane 299-12-18 - odpowiedz III/IV 300, NIE ZALEGLE** — PISMO DO CECHU PISARZY W SPRAWIE ILARIA. Dyktowane przez glowe domu, ktory juz nie utrzyma piora przez strone: ze oskarzenie, na ktorym cech oparl skreslenie, WYSZLO Z JEGO DOMU I BYLO FALSZYWE, i ze oswiadcza to WIEDZAC, ZE OSWIADCZA PRZECIW SOBIE. Jego wlasne ostrzezenie co do wartosci tego papieru zostalo zapisane razem z pismem. · _kto:_ **CECH PISARZY W BRAAVOS -> przez NESTE** · _zamyka:_ przywrocenie Ilaria na liste ALBO odmowa cechu na pismie **⚠ OTWARTE - CECH JEST W BRAAVOS, 2,5 MIESIACA W JEDNA STRONE; TERMIN JESZCZE NIE MINAL**
- **od 299-08-14 - STALE** — FOSA CAILIN JAKO KLIRINHAUS NOCNEJ STRAZY. List do WSZYSTKICH KROLESTW POLUDNIA: honorujcie Straz, slijcie chetnych; kazdy chetny z poludnia idzie do Fosy. Apel byl darmowy, ale NIGDY NIE POLICZONO, ILU PRZYSZLO. Miara istnieje od 300-02-12 (ksiega bramy) i od 300-02-28 (rejestr Melli) - wystarczy zapytac. · _kto:_ **GARTH (ksiega bramy) + MELLA** · _zamyka:_ liczba rekrutow z poludnia przez Fose **⚠ ODCZYTANE 300-03-03 - I ODCZYT JEST ZLY: KLIRINHAUS OGLOSZONO I NIGDY NIE URUCHOMIONO**
- **300-03-03 wieczor - WYSLANE** — ZADANIE POMIARU OSWYNA - kruk do Winterfell, do GAWENA i BERONA razem: przyslac liczbe roznicy zsyp/wysyp za cala zime, tak jak zlecono 299-09-13. Kruk 2 dni w kazda strone - LICZBA MOZE BYC NA FOSIE 300-03-07, w dniu wyjazdu, albo dogoni Symona w Bialym Porcie. · _kto:_ **OSWYN -> GAWEN/BERON -> SYMON** · _zamyka:_ liczba w rece **⚠ ZAMKNIETE 300-03-03 - LICZBA WYDANA (ZASADA 39A: ZWLOKA BYLA MOJA, NIE GRACZA)**
- **300-03-03 wieczor - WYSLANE** — KARTA DO BERONA: czy w kancelarii Korony lezy cokolwiek od STANNISA (od 299-09) oraz ODPOWIEDZ AEMONA NA PYTANIE O OBSYDIAN (kruk 299-09-22) - ta ostatnia BYLA ADRESOWANA DO WINTERFELL, NIE DO SYMONA, i on jej nigdy nie widzial. · _kto:_ **BERON** · _zamyka:_ wykaz albo puste - obie odpowiedzi sa odpowiedzia **⚠ OTWARTE - OD STANNISA NIC; ODPOWIEDZ AEMONA O OBSYDIANIE DO ODSZUKANIA W WINTERFELL**
- **PILNE - przed wyjazdem 300-03-07** — MYTO OD WARTOSCI - ROZSTRZYGNIECIE GRACZA 300-03-03. Plaskie 12 jeleni od wozu ZNIESIONE; myto lenna idzie 1/40 (2,5 proc.) wartosci, ta sama forma co clo Korony (1/20). PO ZMIANIE KAZDY LADUNEK PLACI 7,5 PROC. LACZNIE: torf spada z 15 na 7,5, owies stoi na 7,7 -> 7,5, futra i bursztyn rosna z 5,3 na 7,5. WYCENY NIE TRZEBA BUDOWAC - GARTH JUZ WYCENIA KAZDY WOZ, bo clo Korony od zawsze jest od wartosci. Myto jedzie na tej samej liczbie, zero nowego aparatu. MYTO TO REGALE LENNA (Kasa 2) - Krol niepotrzebny, oglasza sie na slupie. ⚠ KOREKTA 300-03-03: 2,7 proc. to NIE byla srednia, tylko woz ZBOZA. Plaskie myto 12 jeleni to bylo 10 proc. na torfie, 2,73 na owsie i 0,3 na futrach. STAWKI NEUTRALNEJ DLA SKARBU NIE DA SIE POLICZYC, DOPOKI NIKT NIE POLICZYL, CO PRZEZ TE BRAME JEDZIE. Ksiega bramy Gartha (od 300-02-12) jest tym, z czego to wyjdzie. 1/40 zostaje jako stawka wyjsciowa - ale jako DECYZJA, nie jako wyliczenie. · _kto:_ **SYMON (myto to jego regale) + GAWEN (clo to Korona)** · _zamyka:_ obwieszczenie na slupie w Cailin **⚠ ROZSTRZYGNIETE - NA SLUP 300-03-04**
- **PILNE** — JEDENASTU NA MUR - klirinhaus nigdy nie zadzialal. Ksiega bramy (od 300-02-12) notuje JEDENASTU, ktorzy przy wejsciu podali 'na Mur'. SIEDMIU Z NICH STOI DZIS W REJESTRZE MELLI jako dniowkowi na Fosie. Nikt ich dalej nie poslal, bo urzedu, ktory mial ich kierowac, nie bylo - byla tylko zapowiedz z 299-08-14. Fosa wchlonela rekrutow Muru. · _kto:_ **SYMON / HENDRY / MELLA** · _zamyka:_ decyzja: odeslac na Mur, zatrzymac jawnie, albo dac im wybor - i OSOBA, ktora odtad kieruje **⚠ OTWARTE - DO ROZSTRZYGNIECIA PRZEZ GRACZA**
- **300-03-04** — SLUP W CAILIN: MYTO 1/40 OD WARTOSCI zamiast 12 jeleni od wozu. Jedno zdanie, data na wierzchu. Idzie tym samym posiedzeniem lawy, co kowal i pismo miasta. · _kto:_ **HERWIN + GARTH (wycena juz istnieje)** · _zamyka:_ obwieszczenie
- **PILNE - do karty zywnosciowej 300-03-07** — UBYTEK SKLADOWY 7 PROC. - liczba Oswyna za zime (na 100 korcy zsypanych wysypalo sie 93). DNO CENY MUSI POKRYWAC UBYTEK, inaczej sklad traci na samym trzymaniu. Dno ustalone 300-03-03 (owies 3 jelenie 20, jeczmien 3 jelenie 60) LICZONO BEZ TEGO. Przeliczyc; sprawdzic tez cztery przegrody Fosy - NIGDY nie mierzone zsyp/wysyp. · _kto:_ **ORLAND KORZEC + GERRIK RACHUBA** · _zamyka:_ poprawione dno ceny i pierwszy pomiar przegrod Fosy **⚠ PRZELICZONE 300-03-03 - TRZY LICZBY NA SLUP 300-03-04**
- **300-03-04** — SLUP - TRZY LICZBY ZBOZOWE, PRZELICZONE POPRAWNIE 300-03-03: (1) NORMA UBYTKU 7 NA STO, ogloszona; w normie placi SKLADAJACY, ponad norme SKLAD. (2) NARZUT SKLADU 7,53 PROC. (nie 7 - zeby odzyskac 7 straconych, trzeba dolozyc 7,53): owies kupuje 11 / sprzedaje 11 jeleni 83; jeczmien 12 / 12 jeleni 90. (3) DNO SPRZEDAZY: owies 3 jelenie 44, jeczmien 3 jelenie 87. Dno KUPNA zostaje 3-20 i 3-60. · _kto:_ **HERWIN + ORLAND + BENNIS** · _zamyka:_ obwieszczenie
- **PILNE - do Rady 300-03-30** — LICZBA MURU - MA JUZ SZESC MIESIECY. List Aemona przyszedl i zostal przeczytany 299-09-18: MORMONT ZABITY PRZEZ WLASNYCH, OBJAZD WYBITY, MANCE PROWADZI CALY LUD, NIESPELNA SZESCIUSET LUDZI NA TRZYSTA MIL. Symon nazwal to wtedy: 'to nie jest wiadomosc, to jest zapalka' i NIE PODAL TRESCI UMBEROWI. PUNKT 0 WIELKIEJ RADY (MUR - meldunek i aklamacja) STOI DZIS NA TEJ SZESCIOMIESIECZNEJ LICZBIE, bo meldunek VII Osrica jest zalegly. NIC NOWEGO Z MURU NIE PRZYSZLO OD WRZESNIA. · _kto:_ **SYMON** · _zamyka:_ swiezy meldunek z Muru PRZED Rada 300-03-30 - od Osrica albo wprost z Czarnego Zamku **⚠ OTWARTE - PILNE, LICZBA SIE STARZEJE I TO ONA OTWIERA RADE**
- **PILNE - przed wyjazdem 300-03-07** — STRUKTURA RUCHU PRZEZ BRAME - z ksiegi Gartha od 300-02-12: ile wozow, jakiego towaru, o jakiej wartosci. BEZ TEJ LICZBY stawka myta 1/40 jest decyzja, a nie wyliczeniem, i nikt nie wie, czy Kasa 2 na zmianie zyskuje czy traci. · _kto:_ **GARTH (ksiega) + GERRIK RACHUBA (rachunek)** · _zamyka:_ rozklad wozow i wartosci za trzy tygodnie **⚠ OTWARTE - NOWE**
- **wyslany 299-09-22 - ODPOWIEDZ NIGDY NIE DOSZLA DO SYMONA** — PYTANIE O OBSYDIAN DO MAESTERA AEMONA. Pytanie wymyslil BRAN STARK 299-09-08: 'Pierwsi Ludzie mieli juz braz; po co lud, ktory zyl obok ludzi z metalem, trzymal sie nozy z kamienia - albo byli glupi, albo kamien robil cos, czego braz nie robil'. Kruk poszedl do najstarszego maestera w Westeros. ### W ZAPISIE STOI WPROST: 'ODPOWIEDZ PRZYJDZIE DO WINTERFELL, NIE DO SYMONA'. To ten sam ksztalt, co pismo Rejestratora - odpowiedz zaadresowana obok Namiestnika. ### SPRAWA NIE JEST DZIS CIEKAWOSTKA: Reed potwierdzil obsydian 299-10-04 (stare ostrza WYCHODZA Z TORFU, a torfiarnie Fosy tna ten sam torf), a 300-01-26 SYMON POWIEDZIAL WYMANOWI 'CZARNE SZKLO' i Wyman pierwszy raz tego wieczoru byl zaskoczony. ODPOWIEDZ AEMONA JEST JEDYNYM ZRODLEM ARCHIWALNYM, KTOREGO W TEJ SPRAWIE NIE ODCZYTANO. · _kto:_ **BERON - odszukac w kancelarii Winterfell** · _zamyka:_ odpowiedz Aemona w rece Symona ALBO potwierdzenie, ze nie dotarla
- **NIE WYSLANY - sprawdzone 300-03-03** — DAENERYS A AEMON: LISTU NIE BYLO. Przeszukane wszystkie wystapienia obu imion - w zadnym pismie do Czarnego Zamku nie ma Daenerys ani slowa 'Targaryen'. Pytanie o Daenerys poszlo JEDEN RAZ i nie tam: do NESTY, 300-03-02, i zapis mowi wprost, ze wczesniejsze listy do Nesty (299-09-19, 300-02-18) TEGO PYTANIA NIE NIOSLY. Odpowiedz realnie V/300. ### CO ISTNIEJE I JEST BLISKO: list do Aemona z 299-09-15, sekcja IV - o CZLOWIEKU, KTOREGO IMIENIA NIE PADA ANI RAZU, i o slowie, ktorego Aemon nie napisze, dopoki nie uslyszy go od tego, kogo dotyczy. TO JEST JON SNOW, NIE DAENERYS (watki jon_snow_krew_neda_na_murze_299_06, jon_snow_po_drugiej_stronie_299_09). ### I RZECZ, KTORA Z TEGO WYNIKA: przy Daenerys stoi 'ANI JEDNEJ DROGI', a najstarszy maester w Westeros koresponduje z Symonem PRYWATNIE od pol roku i ma archiwum Nocnej Strazy. TO JEST DROGA, KTOREJ NIKT NIE PROBOWAL - i jedyna, ktora nie wymaga czekania do maja. · _kto:_ **SYMON** · _zamyka:_ decyzja gracza: pytac Aemona czy nie **⚠ OTWARTE - DO ROZSTRZYGNIECIA**
- **WYSZEDL 300-02-07 - 25 DNI CISZY** — POSLANIEC ZA MUR DO MANCE'A RAYDERA - o DELEGACJE PRZED GLOWNA BRAME. Rozkaz wydany rano 300-02-07, zameldowany Krolowi tego samego dnia slowami: 'NIE MOWIE WAM, ZE SIE UDA. MOWIE, ZE WYSZLO'. RAZEM Z NIM: TLUMACZ ZATRZYMANY, PLATNY Z KASY 3 (zold pod Murem, biezaco, potwierdzony 300-02-15) - o co OSRIC PROSIL NA PISMIE I CZEKAL. PODSTAWA: stanowisko Symona przed Krolem 300-02-06 - 'poslac kogos za Mur do Mance'a Raydera PO ICH RELACJE i poprosic o DOWOD W POSTACI DOSTARCZENIA NIEUMARLYCH'. KANAL: nie ma kruka za Mur. Czlowiek wychodzi i wraca albo nie wraca. Odpowiedz wroci PRZEZ OSRICA - i dlatego jego zalegly meldunek VII jest dzis najwazniejsza cisza w grze. · _kto:_ **poslaniec -> MANCE RAYDER -> OSRIC -> SYMON** · _zamyka:_ delegacja przed glowna brama ALBO odmowa ALBO poslaniec, ktory nie wrocil - kazde z trzech jest odpowiedzia **⚠ ROZSTRZYGNIETE 300-03-03 (RZUT 20): POSLANIEC NIE WROCIL. PRZEWODNIK Z KLANOW WROCIL SAM PO DZIEWIECIU DNIACH.**
- **NIEODPOWIEDZIANE OD 300-02-06 - przed Rada 300-03-30** — TRZY WARUNKI KROLA PRZED OTWARCIEM BRAMY DZIKIM - postawione 300-02-06 i DO DZIS BEZ ODPOWIEDZI: (1) KTO IDZIE ZA MUR - 'nie wyslecie posla, POSEL TO JEST AKT; wyslecie kogos, kto umie tam wejsc i wyjsc'. (2) CO SIE ROBI Z DOWODEM - kto go niesie i przez ile mil, gdzie go trzymamy, kto przy nim stoi w nocy, CZYM GO ZABIJAMY, gdyby sie ruszyl: 'stal nie robi nic, ogien robi', a JEDYNE CZARNE SZKLO NA POLNOCY TO DWA OSTRZA W PLOTNIE. 'Jesli cos pojdzie nie tak, nie stracimy dowodu - STRACIMY WSZYSTKO, CO TEN DOWOD MIAL UDOWODNIC.' (3) CZYM ICH NAKARMIC - 20-40 TYSIECY, wiecej niz Bialy Port, w krolestwie, ktorego Krol policzyl JEDNA DZIESIATA spichlerzy. 'Nie mowie nie. Mowie, ze bez tej liczby otwarcie bramy jest WYROKIEM WYDANYM PRZEZ NIKOGO.' · _kto:_ **SYMON** · _zamyka:_ trzy odpowiedzi na pismie, przed punktem 0 Rady **⚠ OTWARTE - PILNE**
- **WIOSNA 300 - JEST TERAZ** — TLUMACZ SPOD MURU ODCHODZI NA WIOSNE. Zatrzymany za pieniadze od 300-02-07 (Kasa 3) - ale zatrzymanie bylo NA TE ZIME. Trzej dzicy zyja, JEDEN MOWI WIECEJ. To sa JEDYNE TRZY USTA, jakie Polnoc ma z tamtej strony, i jedyny czlowiek, ktory je rozumie. Krol powiedzial to wprost: 'chcecie rozmawiac z Mance'em Rayderem, a jeszcze nie odpisaliscie czlowiekowi, ktory pilnuje jedynych trzech ust, jakie mamy'. · _kto:_ **OSRIC / Kasa 3** · _zamyka:_ tlumacz zwiazany NA ROK, nie na zime - albo wyuczony drugi **⚠ ROZSTRZYGNIETE 300-03-03 (RZUT 29): ZOSTAL - ALE OSWIADCZYL, ZE ZA MUR DRUGI RAZ NIE POJDZIE.**
- **300-03-03 - WIADOMOSC JEST** — POSLANIEC ZA MUR NIE WROCIL (rzut 20). Wyszedl 300-02-07 z przewodnikiem z klanow gorskich - jedyna droga. PRZEWODNIK WROCIL SAM PO DZIEWIECIU DNIACH: rozstali sie w umowionym miejscu, poslaniec poszedl dalej Z LUDZMI, KTORYCH PRZEWODNIK NIE ZNAL. Nikt nie wie, czy dotarl do Mance'a. NIE MA CIALA, NIE MA ODMOWY, NIE MA DELEGACJI. · _kto:_ **-** · _zamyka:_ delegacja przed brama, poslaniec, albo wiadomosc o nim - dowolne z trzech **⚠ OTWARTE - AKT BEZ ODPOWIEDZI**
- **300-03-03 - WIADOMOSC JEST** — TLUMACZ ZOSTAL (rzut 29) - pieniadze z Kasy 3 doszly i przyjal. ALE OSWIADCZYL OSRICOWI, ZE ZA MUR DRUGI RAZ NIE POJDZIE. Kanal do trzech ust istnieje; PRZEWODNIKA DO MANCE'A NIE MA. Drugiego poslanca nie ma kto poprowadzic. · _kto:_ **OSRIC** · _zamyka:_ drugi przewodnik z klanow ALBO wyuczony drugi tlumacz **⚠ OTWARTE - NOWE WASKIE GARDLO**
- **wyslany 300-03-02 o brzasku** — WYMIANA LIST JENCOW - DO ZELAZNEGO TRONU. Kruk maestera, PODPIS CERWYNA JAKO JUSTYCJARIUSZA (nie Namiestnika - to akt sadowy, nie polityczny). DOKUMENT: 271 NAZWISK - 31 rangi + 240 prostych, dolozonych decyzja gracza, ZEBY DOKUMENT BYL NUDNY. HARRION KARSTARK stoi jako SIEDEMNASTY WIERSZ Z TRZYDZIESTU JEDNU, NA CZWARTEJ STRONIE, miedzy dwoma rycerzami z Zachodu, o ktorych nie wiemy nic. METODA: nie pytamy o Harriona, pytamy o CALA LISTE - 'czlowiek, o ktorego nikt nie pytal przez siedem miesiecy, jest tani; czlowiek, o ktorego pyta Namiestnik, ma cene'. ### TO JEST DRUGIE PISMO W TEJ SAMEJ SPRAWIE: pierwsze poszlo DO KROLA (status jencow, trzej dzicy, pieczec Namiestnika, od 300-02-19). Dwa pisma, dwaj adresaci, jedna sprawa. · _kto:_ **CERWYN (podpis) -> Zelazny Tron** · _zamyka:_ odpowiedz dworu ALBO milczenie - a milczenie tez rozstrzyga cene Harriona przed 300-04-01, gdy zapada zaleglosc Karholdu
- **300-03-05** — KAFARY NIE MAJA WLASCICIELA - jedyna rzecz realnie hamujaca groble, i NIKT NIE MA ROZKAZU JEJ USUNAC. Cerwyn 300-02-20 i Bran 300-02-25 powiedzieli to samo: 'nie brakuje nam pieniedzy, stoimy, bo mamy cztery kafary; kafary robi sie z DREWNA I Z ZELAZA, NIE Z MONETY, i trzeba je komus KAZAC zrobic'. Plac budowy BEZ MISTRZA, KUZNI I KAMIENIOLOMU. ### ⚡ OD 300-03-04 ZNIKA POWOD, DLA KTOREGO ROZKAZ NIE MIAL ADRESATA: LAWA SADZA KOWALA (Brusk od Miecha). Rozkaz do kuzni ma wreszcie komu byc wydany. · _kto:_ **BRAN + kowal + Orbelo** · _zamyka:_ cztery kafary z wlascicielem i terminem, albo pisemne 'nie da sie i dlaczego'
- **300-03-10** — GROBLA STOI PRZEZ ODWILZ - cztery kafary i zalogi STOJA BEZCZYNNIE. Dzien, w ktorym KAFAR ZNOWU WCHODZI W GRUNT, zalezy od odwilzy i NIKT GO NIE ZNA; jedyny czlowiek, ktory ten dzien rozpozna, to BRAN. Sztandarowa budowa lenna nie ma daty wznowienia. · _kto:_ **BRAN** · _zamyka:_ meldunek: kafar wszedl w grunt / nadal stoi I DLACZEGO
- **300-03-07** — CZTERY ROBOTY BIJA SIE O TE SAME RECE I NIKT TEGO NIE POLICZYL: GROBLA (stoi, ludzie bezczynni) - TORFIARNIE (to one trzymaja ludzi przy robocie w zimie, czyli program zatrudnienia) - TRZCINA Z PRZYWILEJU (zglosilo sie kilkunastu, prawie wszyscy do jednego rzemiosla) - EKIPA POMIAROWA. Piata dolozona 300-03-01: torf do ludzi. · _kto:_ **WARRYN + MELLA (rejestr dniowek)** · _zamyka:_ jedna karta rak: ile glow na kazda robote, i ktora ustepuje
- **300-03-06** — ROZPOZNANIE PRZEWLOKI - profil, grunt, dlugosc PO NASZEJ STRONIE. Rzeczy wlasne i niesporne, robione od 300-03-01. ODDZIELONE OD POMIARU POD DWIE PIECZECIE, ktory zaczyna sie dopiero, gdy przy sznurze stanie czlowiek Wymana (300-03-06). Joint-walk zachowany, precedens lady Dustin nietkniety. · _kto:_ **WEYLIN + ORBELO** · _zamyka:_ liczba po naszej stronie, gotowa PRZED wspolnym przejsciem
- **300-03-09** — TRAKT DO DORZECZA - PIERWSZA RZECZ DO ZROBIENIA NIE JEST KOPANIEM: PRZEJSC ODCINEK I ZMIERZYC. Standard z punktu 10: 'ZADEN ODCINEK BEZ NAZWISKA I BEZ DATY'; liczby na calosc nie da sie podac uczciwie, dopoki nie przeszlo sie odcinka. Rece z rejestru dniowek, ten sam mechanizm co przy przewloce. ⚠ KOLIZJA: prowadzi BRAN, a Bran ma groble - albo dostaje zastepce przy grobli, albo trakt staje w dniu, w ktorym rusza grobla. · _kto:_ **BRAN + KORM PALIK (zastepca od 300-03-03)** · _zamyka:_ zmierzony pierwszy odcinek z nazwiskiem i data
- **300-03-03** — ZLECENIE DLA WILLI - ZWEZENIE (300-01-27): PRZESTAC SZUKAC POSREDNIKA, ZAWEZIC DO PETYRA BAELISHA I DO KROLEWSKIEJ PRZYSTANI. Podstawa - jej wlasny trop docisniety: obce srebro, spekulacja zbozowa, 'najlepszy umysl od monety i cienia', cierpliwy pieniadz. · _kto:_ **WILLA** · _zamyka:_ nazwisko albo uczciwe 'slad sie urwal i gdzie'
- **300-03-08** — ZLECENIE DLA HARLA W BARROWTON - ziarno siewne. ⚠ TRACI NA WARTOSCI od 300-03-02: Dustin sprzedal zboze, zeby zaplacic danine W MONECIE. 'Niech pyta, ale nie liczmy na to.' Goniec za kolumna wyslany 300-03-02. · _kto:_ **HARL** · _zamyka:_ korce albo pisemne nie
- **300-03-20** — ETAP I SPICHLERZA POLNOCY - JEDNA KSIEGA na: spichrze Krola, Zimowe Miasto, komory, Kamienny Brod. Krol policzyl JEDNA DZIESIATA spichlerzy krolestwa - a bez tej liczby otwarcie bramy dzikim jest 'wyrokiem wydanym przez nikogo'. · _kto:_ **GAWEN + OSWYN** · _zamyka:_ jedna ksiega, cztery sklady, jedna miara
- **300-03-09** — ETAPY MIASTA CAILIN: I - co pod ziemia · II - co zarabia (waga, targ, sklady, brama) · III - co widac (bruk, mury, latarnie) · IV - co oddycha (dzielnica zimowa). ETAP II MA SAM NA SIEBIE ZARABIAC: myto z grobli i clo z komory. ⚠ MYTO WLASNIE ZMIENIONO NA 1/40 OD WARTOSCI - rachunek Etapu II trzeba przeliczyc. · _kto:_ **WARRYN + GERRIK RACHUBA** · _zamyka:_ rachunek Etapu II po nowym mycie
- **300-03-10** — TORFIARNIE - maja ciac WIECEJ, a mierniczego torfu wakat po Harrolu zamkniety dopiero 300-03-03 (Jorren Lut). To jest zarazem PROGRAM ZATRUDNIENIA ZIMOWEGO: 'to one trzymaja ludzi przy robocie w zimie'. ⚠ I od 300-03-03 torf placi 7,5 proc. zamiast 15 - powod, zeby ciac wiecej, wlasnie sie podwoil. · _kto:_ **JORREN LUT + WARRYN** · _zamyka:_ liczba: ile ciety tygodniowo i iloma rekami
- **300-04-02** — MELDUNEK VIII OSRICA - CO TRZYDZIESCI DNI, TAKZE GDY STOI NA NIM 'NIC'. ⚠ ZMIANA ADRESU, ta sama, ktora wprowadzono Torrenowi 300-02-17: MELDUNEK IDZIE TAM, GDZIE JEST NAMIESTNIK, NIE DO WINTERFELL. Meldunek VII szedl okrezna droga i lezal, bo adres byl staly, a Namiestnik nie. Od dzis adres jest ruchomy: do 300-03-07 Fosa, potem Bialy Port, od ~300-20 Winterfell. · _kto:_ **OSRIC -> kancelaria Garricka** · _zamyka:_ karta na stole, takze pusta
- **PRZED RADA 300-03-30** — CZTERY TYSIACE OSIEMSET Z KLANOW - LICZBA, KTOREJ KROLESTWO NIGDY NIE MIALO. Krol powiedzial 300-02-06: 'UMBEROWIE, FLINTOWIE, KLANY Z GOR TO SA PIERWSI LUDZIE - ta sama krew, te same stare bogi'. Teraz ta sama krew ma liczbe, a Rada otwiera sie punktem 0 - MUR. To jest jedyna liczba z tej sprawy, ktora jest SWIEZA, WLASNA i DOBRA. · _kto:_ **SYMON** · _zamyka:_ liczba wypowiedziana przy punkcie 0
- **300-03-07** — OSIEM RUBRYK DLA TRZECH BUDOW - nie urzedy, bo te sa obsadzone od pol roku, tylko FORMA MELDUNKU. BORS (Przystan Wilka), DONNEL OBROK (Dustinport) i THEOMORE (Glebokorzen) nie maja ani rubryk, ani dnia. TORREN DOSTAL OSIEM RUBRYK 300-02-17 I OD RAZU ZACZAL PISAC - po 190 dniach milczenia. Ta sama forma, te same osiem rubryk, ten sam dzien miesiaca. · _kto:_ **SYMON** · _zamyka:_ trzy karty osmiorubrykowe wyslane, z dniem miesiaca

_Zamkniete ostatnio:_ cena minimalna z iloscia + cena dzisiejsza + oferta kupna na (zrobione 300-03-03) · MELDUNEK VII OSRICA - TRZY LICZBY I JEDNA ICH BRAK. (1) STRA (zrobione)

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
- **bez daty - CISZA** — MELDUNEK VII OSRICA (Mur) - zalegly. ⚠ TO NIE JEST ZALEGLOSC URZEDOWA: TEDY MA WROCIC ODPOWIEDZ OD MANCE'A RAYDERA. Poslaniec za Mur wyszedl 300-02-07; Osric jest jedynym kanalem, ktorym to moze przyjsc. Jego cisza i cisza zza Muru to JEDNA CISZA, nie dwie.
- **bez daty - CISZA** — PRZYSTAN WILKA - status budowy; pyta CERWYN jako wspolwlasciciel cwiartki; podanie nazwiska budowniczego jest czescia odpowiedzi
- **bez daty - CISZA** — DONNEL OBROK (Dustinport, budowa) - pytanie pod pieczecia, jezdziec eskadry
- **bez daty** — GARTH: liczba miesieczna dziury w komorach wodnych - zmierzona 299-10-01 i NIE ZMIERZONA PONOWNIE
- **bez daty** — BERON: wszystko, co przyszlo od BRYNDENA TULLY'EGO od 299-07, z datami; potem list do Blackfisha (poludniowa sciana, nie traktat)
- **bez daty** — THEOMORE - PYTANIA POPRAWIONE 300-03-03. STARE BYLY ZLE ZADANE: kolebka JEST USTALONA (Nowy Zamek w Bialym Porcie, dar Wymana 299-08-11), a pierwsza dziesiatka uczniow JEST WZIETA od 299-09-21. WLASCIWE PYTANIA: ILU Z DZIESIECIU ZOSTALO I CO SPISALI · ile kosztowal PIERWSZY ROK NAPRAWDE · kiedy gmach w Przystani Wilka bedzie gotowy przejac serce · i CZY DZIESIECIU WYSTARCZY, skoro Fosa ma teraz wlasna szkole i ochmistrza nauki.
- **300-03-04** — URBARZ ZALOZONY - cztery kolumny KTO / Z CZEGO / ILE / KIEDY; pierwszy wpis to szesc tygodni niepobranego czynszu (od 300-02-07)
- **300-03-04** — LAWA MIASTA SADZA KOWALA (Brusk od Miecha, wskazala Mella) - kuznia idzie pierwsza albo nie idzie nic
- **300-03-05** — CERWYN WYJEZDZA - ma zostawic TOMMARDA KOSE jako lustratora Fosy na rok
- **ten tydzien** — SOLTYSI: ktore wsie wybraly, kiedy i kogo - pytanie zadane dawno, odpowiedzi nie bylo
- **300-03-30** — AKADEMIA WOJSKOWA: data po Radzie, platnik Kasa 3, baszta w Przystani Wilka; pierwszy mistrz BRYNDEN TULLY, zapasowo zbrojmistrz Fosy
- **wyslane 300-02-27 - CISZA** — PRZYPOMNIENIE O REJESTRATORZE KORONY. Jedno zdanie, bez nazwiska, spisane przez Garricka pod dyktando: 'KRZESLO REJESTRATORA KORONY STOI PUSTE CZWARTY MIESIAC. NAZWISKA NIE PODAJE, BO ZASTRZEGLISCIE JE SOBIE. PODAJE DATE.' Ten sam goniec co prosba o zwyczaj, OSOBNA KARTA - zeby nie zamienic tamtej w upomnienie. UWAGA: UCHO KORONY I REJESTRATOR KORONY TO JEDNO KRZESLO (odkryte 300-02-27) - puste jest wieksze, niz wyglada.
- **PRZED Rada 300-03-30 - WARUNKOWE** — SPRAWA CAILIN (prawo skladu + garnizon). KROL OBIECAL 300-02-07: rozstrzygnie PRZED Rada, ale DOPIERO GDY PRZYJDZIE PISMO MIASTA, NIE NAMIESTNIKA. Prosba miasta o piec dni targowych stoi na slupie od 300-03-03 - ALE NA SLUPIE, NIE W WINTERFELL. Dopoki lawa nie wysle wlasnego pisma, zegar Krola nie ruszyl. ROZSTRZYGNIECIE GRACZA 300-03-03: lawa wysyla wlasne pismo 300-03-04, krukiem.
- **300-03-04 SWIT** — PISMO MIASTA CAILIN DO KORONY - wlasna pieczec miasta, podpisy lawy, krukiem z Fosy (2 dni). TRESC: TYLKO sprawa Cailin (przymus skladu piec dni targowych + garnizon). NIE laczyc z ustrojem miast - tamto Krol przyjmie tylko OD WSZYSTKICH NARAZ i pismo Cailin utknie za czternastoma innymi. WARUNEK FORMY: Symon nie dyktuje ani slowa; podaje Herwinowi TYLKO to, ze warunek Krola istnieje.
- **~300-03-06** — PISMO MIASTA W WINTERFELL - od tej chwili biegnie obietnica Krola z 300-02-07: rozstrzygnie PRZED Rada
- **wyslany 300-02-27 - odpowiedz IV/300 najwczesniej** — LIST DO LADY OLENNY TYRELL. Tresc: Polnoc przezywa zime; Dom chce wejsc do Highgarden PO CICHU, zeby moc rozmawiac blizej. PIERWSZY WLASNY RUCH DOMU NA REACH - nie pismo Namiestnika, tylko Domu Handlowego (Kasa 1). PODSTAWA RELACJI: od 300-02-25 to nie jest 'tajny kanal', tylko RELACJA HANDLOWA Z DRUGIM SPICHLERZEM WESTEROS - obie strony maja powod, zeby jej nie zerwac, i zadna nie musi tlumaczyc, po co pisze. ZBIEGA SIE Z: placowka HIGHGARDEN na liscie do Hala (Bialy Port ~300-03-13) - TEN SAM CEL, DWIE DROGI. Nie wysylac trzeciej. ⚠ KOREKTA KANALU 300-03-03: poszedl KRUKIEM, nie droga morska Domu - wiec wraca TYGODNIE, nie miesiace. Koszt tej szybkosci: lancuch maesterski na poludnie idzie przez STARMIASTO, a pismo mialo byc 'po cichu'.
- **wyslany 300-02-07 - CISZA MIESIAC** — LIST DO HALA: WYKUPIC WEKSEL DANY BOLTONOM. Podstawa: 299-10-20 Dreadfort, zamiec - postoj oplacony WEKSLEM NA DOM TALLY, Roose przyjal papier bez pytania. Lezy piaty miesiac. NA DREADFORCIE LEZY PODPIS SYMONA - papier z jego nazwiskiem i CUDZA WOLA, platny na zadanie, ktory kladzie sie na stol wtedy, kiedy sie chce. PILNE PRZEZ TRZY ZBIEGI: cichy kupiec na Dreadfort 300-03-10, Ramsay wezwany przed 300-04-01, Rada 300-04-01 z Boltonami na sali.
- **wyslany 300-02-27** — LIST DO ROOSE'A BOLTONA - nie czeka na spotkanie. Ta sama sprawa co weksel.
- **300-02-25 (ponowiony; pierwszy 299-09-08)** — LIST DO HOWLANDA REEDA. KANALU KRUCZEGO NIE MA - Greywater Watch PLYWA. Protokol: poslaniec jedzie na Przesmyk, staje w umowionym miejscu PRZY GROBLI i czeka, az krannogowie sami wyjda. MOZE DZIEN, MOZE DWA TYGODNIE - cisza tutaj NIE JEST cisza.
- **wyslany 300-03-01, osobnym jezdzcem** — LIST DO SKARBNIKA GAWENA - PAKIET MONETARNY, PIEC POZYCJI. Podstawa liczbowa: dochod monetarny Korony w normalnym roku 8000-20000 smokow, DZIS 3000-6000. Mennica Wilk bije od 299.
- **wyslany 300-02-07** — LIST DO GAWENA: czlowiek do PRZYSTANI WILKA - 'czego szukac, nie kogo'. Zbiega sie z cisza o statusie budowy Przystani (pyta tez Cerwyn jako wspolwlasciciel cwiartki).
- **wyslany 300-03-01** — LIST DO KROLA - PROSBA O ROZMOWE O PORZADKU, NIE WYKLAD O NIM. Forma narzucona zasada, ktora Krol sam nalozyl na Symona przy Karcie Wychowankow: 'idzcie do niego DZIS. NIE Z KARTA - Z PYTANIEM'. List niesie prosbe i powod, nie argumentacje. OSOBNY od pisma z 02-19 i od przypomnienia o Rejestratorze.
- **zlecone 300-03-02** — KANON JADLA POLNOCY - zadanie dla WYSTANA, trzy czesci: (1) dieta i dania z waloru miejscowego; (2) kanon potraw - co siac, co do szklarni, co hodowac, co lowic; (3) ruszyc ze szklarniami i szkolkami rolniczymi. OD 300-03-03 MA WYKONAWCE: LOWCZY HAKON OD JASZCZURA - wczesniej kanon byl lista bez rak.
- **~300-03-15 (termin podany w samym liscie)** — ODPOWIEDZ MIRY - DZIESIEC DROBNYCH PYTAN O SZKOLE. Reka Symona, NIE rozkazem Korony (wskazowka Luwina: 'na rozkaz odpowie tez, ale na list odpowie PRAWDE O TYM, CO JEJ NIE WYCHODZI'). Zapisany bieg kruka: WRACA PRZED DRUGA POLOWA TRZECIEGO MIESIACA. ZDERZA SIE Z ROZWIAZANIEM - moze nie byc w stanie odpisac.
- **wyslany 300-02-28** — LIST DO MIRY: 'kto nauczy tych dziesiecioro UCZYC' - druga sprawa szkolna, z powrotna.
- **RIVERRUN - jest na miejscu** — LADY CATELYN W RIVERRUN. Wyjechala z Winterfell 299-10-05; cel od poczatku: RIVERRUN, negocjowac w imieniu Polnocy. OKNO PRZEJAZDU PRZEZ FOSE (02-25..03-07) SIE ZAMKNELO - nie przejezdza, siedzi u brata. JEJ ROLA, nietknieta od 299-09-19: ONA OTWIERA DRZWI jako TULLY, w domu swojego ojca, do swojego brata. Korona przez nie wchodzi - ona nie podpisuje, nie ustepuje, nie negocjuje za Polnoc. LIST SYMONA do rak wlasnych (napisany 300-02-16, wlasna reka, BEZ pieczeci Namiestnika) idzie PRZEZ LUCANA od 300-02-27 - a Lucan siedzi w Dorzeczu, wiec kanal jest wlasciwy. KARTKA U WARRYNA NA FOSIE ZOSTAJE - na wypadek, gdyby wracala tedy.
- **wyslany 300-02-17** — NESTA - CZWARTE ZLECENIE: fracht na zachodnim morzu (nie okret - LADOWNIA; domy braavoskie maja kantory w Lannisporcie i Starym Miescie) + LUPACZ KAMIENIA. Kolejka wypisana wprost: (1) ksiega Antaryonow (2) karta cen (3) wschod i dziewczyna (4) to. 'Czwarta jest czwarta i ma nia zostac.'
- **wyslany 300-02-07** — NESTA - KADRY Z BRAAVOS (pozycja 2 kolejki).
- **wyslany 300-03-01** — NESTA - ROZGLOSIC W BRAAVOS PRZYWILEJE FOSY; ludzie maja kierunek. ALE rozglaszanie ZACZYNA SIE PO PODPISIE, nie przed.
- **wyslany 300-03-03 o brzasku** — KRUK DO BIALEGO PORTU - pytanie o Mire. Poczta DOMU, pieczec DOMU, nie Korony. Dojdzie w dwa dni i tak czy inaczej PO FAKCIE - wysylany nie po to, zeby zdazyc, tylko zeby ktos tam wiedzial, ze pytano tego dnia.
- **WIOSNA 300 - WYMAGALNE TERAZ** — POMIAR OSWYNA - zlecenie z 299-09-13: przez cala zime MIERZYC TEN SAM SKLAD przy zsypaniu i przy wysypaniu i spisywac roznice. W zleceniu stoi wprost: 'DO WIOSNY Skarbnik bedzie mial czym UZASADNIC ogloszona liczbe, zamiast ja wymyslic'. WIOSNA JEST TERAZ, A LICZBY NIKT NIE ZAZADAL. Ksiega spichlerza Zimowego Miasta miala byc WZOREM dla ksiag skladowych krolestwa - i cala dzisiejsza maszyna zbozowa (cena minimalna, rubryka stanu ziarna, przymus skladu) stoi bez tego pomiaru.
- **PRZED ~300-03-13 (Bialy Port)** — ZLECENIE DLA GAWENA z 299-09-14: policzyc i OGLOSIC, ile placi JEDEN LADUNEK NA FOSIE RAZEM - myto lenna PLUS clo Korony, wedle rodzaju towaru. Warunek zapisany w zleceniu: 'ma byc gotowe i jawne ZANIM Wyman otworzy ksiegi Bialego Portu'. SYMON JEDZIE DO WYMANA ZA DZIESIEC DNI. Cel podwojny: dac Manderly'emu wzorzec i dowod dobrej wiary; sprawdzic, czy wlasna brama nie jest juz zaporowa - NIKT NIGDY NIE ZSUMOWAL OBU WARSTW.
- **wyslany 299-09-15 - CISZA POL ROKU** — LIST DO MAESTERA AEMONA (Czarny Zamek). Pismo PRYWATNE - od czlowieka, ktory przysylal ziarno, nie od Namiestnika Krola; Aemon pisal do SYMONA, nie do Winterfell, i podal powod: 'to WY przysylaliscie ziarno; ludzie tutaj wiedza, czyje ono bylo'. DRUGA CISZA Z TEGO SAMEGO MIEJSCA - obok zaleglego meldunku VII Osrica.
- **wyslany 299-09-15 - CISZA POL ROKU** — LIST DO STANNISA BARATHEONA, redakcja II, z ZAPROSZENIEM DO PENTOS. Os odmowy udzialu w wojnie wyrzucona - sprawa miedzy koronami zamknieta od sierpnia 299 (Stannis PIERWSZY uznal niepodleglosc Polnocy na pismie). Zostaje zaproszenie i to, co po nim.
- **wyslane 299-12-18 - odpowiedz III/IV 300, NIE ZALEGLE** — PISMO DO CECHU PISARZY W SPRAWIE ILARIA. Dyktowane przez glowe domu, ktory juz nie utrzyma piora przez strone: ze oskarzenie, na ktorym cech oparl skreslenie, WYSZLO Z JEGO DOMU I BYLO FALSZYWE, i ze oswiadcza to WIEDZAC, ZE OSWIADCZA PRZECIW SOBIE. Jego wlasne ostrzezenie co do wartosci tego papieru zostalo zapisane razem z pismem.
- **od 299-08-14 - STALE** — FOSA CAILIN JAKO KLIRINHAUS NOCNEJ STRAZY. List do WSZYSTKICH KROLESTW POLUDNIA: honorujcie Straz, slijcie chetnych; kazdy chetny z poludnia idzie do Fosy. Apel byl darmowy, ale NIGDY NIE POLICZONO, ILU PRZYSZLO. Miara istnieje od 300-02-12 (ksiega bramy) i od 300-02-28 (rejestr Melli) - wystarczy zapytac.
- **300-03-03 wieczor - WYSLANE** — ZADANIE POMIARU OSWYNA - kruk do Winterfell, do GAWENA i BERONA razem: przyslac liczbe roznicy zsyp/wysyp za cala zime, tak jak zlecono 299-09-13. Kruk 2 dni w kazda strone - LICZBA MOZE BYC NA FOSIE 300-03-07, w dniu wyjazdu, albo dogoni Symona w Bialym Porcie.
- **300-03-03 wieczor - WYSLANE** — KARTA DO BERONA: czy w kancelarii Korony lezy cokolwiek od STANNISA (od 299-09) oraz ODPOWIEDZ AEMONA NA PYTANIE O OBSYDIAN (kruk 299-09-22) - ta ostatnia BYLA ADRESOWANA DO WINTERFELL, NIE DO SYMONA, i on jej nigdy nie widzial.
- **PILNE - przed wyjazdem 300-03-07** — MYTO OD WARTOSCI - ROZSTRZYGNIECIE GRACZA 300-03-03. Plaskie 12 jeleni od wozu ZNIESIONE; myto lenna idzie 1/40 (2,5 proc.) wartosci, ta sama forma co clo Korony (1/20). PO ZMIANIE KAZDY LADUNEK PLACI 7,5 PROC. LACZNIE: torf spada z 15 na 7,5, owies stoi na 7,7 -> 7,5, futra i bursztyn rosna z 5,3 na 7,5. WYCENY NIE TRZEBA BUDOWAC - GARTH JUZ WYCENIA KAZDY WOZ, bo clo Korony od zawsze jest od wartosci. Myto jedzie na tej samej liczbie, zero nowego aparatu. MYTO TO REGALE LENNA (Kasa 2) - Krol niepotrzebny, oglasza sie na slupie. ⚠ KOREKTA 300-03-03: 2,7 proc. to NIE byla srednia, tylko woz ZBOZA. Plaskie myto 12 jeleni to bylo 10 proc. na torfie, 2,73 na owsie i 0,3 na futrach. STAWKI NEUTRALNEJ DLA SKARBU NIE DA SIE POLICZYC, DOPOKI NIKT NIE POLICZYL, CO PRZEZ TE BRAME JEDZIE. Ksiega bramy Gartha (od 300-02-12) jest tym, z czego to wyjdzie. 1/40 zostaje jako stawka wyjsciowa - ale jako DECYZJA, nie jako wyliczenie.
- **PILNE** — JEDENASTU NA MUR - klirinhaus nigdy nie zadzialal. Ksiega bramy (od 300-02-12) notuje JEDENASTU, ktorzy przy wejsciu podali 'na Mur'. SIEDMIU Z NICH STOI DZIS W REJESTRZE MELLI jako dniowkowi na Fosie. Nikt ich dalej nie poslal, bo urzedu, ktory mial ich kierowac, nie bylo - byla tylko zapowiedz z 299-08-14. Fosa wchlonela rekrutow Muru.
- **300-03-04** — SLUP W CAILIN: MYTO 1/40 OD WARTOSCI zamiast 12 jeleni od wozu. Jedno zdanie, data na wierzchu. Idzie tym samym posiedzeniem lawy, co kowal i pismo miasta.
- **PILNE - do karty zywnosciowej 300-03-07** — UBYTEK SKLADOWY 7 PROC. - liczba Oswyna za zime (na 100 korcy zsypanych wysypalo sie 93). DNO CENY MUSI POKRYWAC UBYTEK, inaczej sklad traci na samym trzymaniu. Dno ustalone 300-03-03 (owies 3 jelenie 20, jeczmien 3 jelenie 60) LICZONO BEZ TEGO. Przeliczyc; sprawdzic tez cztery przegrody Fosy - NIGDY nie mierzone zsyp/wysyp.
- **300-03-04** — SLUP - TRZY LICZBY ZBOZOWE, PRZELICZONE POPRAWNIE 300-03-03: (1) NORMA UBYTKU 7 NA STO, ogloszona; w normie placi SKLADAJACY, ponad norme SKLAD. (2) NARZUT SKLADU 7,53 PROC. (nie 7 - zeby odzyskac 7 straconych, trzeba dolozyc 7,53): owies kupuje 11 / sprzedaje 11 jeleni 83; jeczmien 12 / 12 jeleni 90. (3) DNO SPRZEDAZY: owies 3 jelenie 44, jeczmien 3 jelenie 87. Dno KUPNA zostaje 3-20 i 3-60.
- **PILNE - do Rady 300-03-30** — LICZBA MURU - MA JUZ SZESC MIESIECY. List Aemona przyszedl i zostal przeczytany 299-09-18: MORMONT ZABITY PRZEZ WLASNYCH, OBJAZD WYBITY, MANCE PROWADZI CALY LUD, NIESPELNA SZESCIUSET LUDZI NA TRZYSTA MIL. Symon nazwal to wtedy: 'to nie jest wiadomosc, to jest zapalka' i NIE PODAL TRESCI UMBEROWI. PUNKT 0 WIELKIEJ RADY (MUR - meldunek i aklamacja) STOI DZIS NA TEJ SZESCIOMIESIECZNEJ LICZBIE, bo meldunek VII Osrica jest zalegly. NIC NOWEGO Z MURU NIE PRZYSZLO OD WRZESNIA.
- **PILNE - przed wyjazdem 300-03-07** — STRUKTURA RUCHU PRZEZ BRAME - z ksiegi Gartha od 300-02-12: ile wozow, jakiego towaru, o jakiej wartosci. BEZ TEJ LICZBY stawka myta 1/40 jest decyzja, a nie wyliczeniem, i nikt nie wie, czy Kasa 2 na zmianie zyskuje czy traci.
- **wyslany 299-09-22 - ODPOWIEDZ NIGDY NIE DOSZLA DO SYMONA** — PYTANIE O OBSYDIAN DO MAESTERA AEMONA. Pytanie wymyslil BRAN STARK 299-09-08: 'Pierwsi Ludzie mieli juz braz; po co lud, ktory zyl obok ludzi z metalem, trzymal sie nozy z kamienia - albo byli glupi, albo kamien robil cos, czego braz nie robil'. Kruk poszedl do najstarszego maestera w Westeros. ### W ZAPISIE STOI WPROST: 'ODPOWIEDZ PRZYJDZIE DO WINTERFELL, NIE DO SYMONA'. To ten sam ksztalt, co pismo Rejestratora - odpowiedz zaadresowana obok Namiestnika. ### SPRAWA NIE JEST DZIS CIEKAWOSTKA: Reed potwierdzil obsydian 299-10-04 (stare ostrza WYCHODZA Z TORFU, a torfiarnie Fosy tna ten sam torf), a 300-01-26 SYMON POWIEDZIAL WYMANOWI 'CZARNE SZKLO' i Wyman pierwszy raz tego wieczoru byl zaskoczony. ODPOWIEDZ AEMONA JEST JEDYNYM ZRODLEM ARCHIWALNYM, KTOREGO W TEJ SPRAWIE NIE ODCZYTANO.
- **NIE WYSLANY - sprawdzone 300-03-03** — DAENERYS A AEMON: LISTU NIE BYLO. Przeszukane wszystkie wystapienia obu imion - w zadnym pismie do Czarnego Zamku nie ma Daenerys ani slowa 'Targaryen'. Pytanie o Daenerys poszlo JEDEN RAZ i nie tam: do NESTY, 300-03-02, i zapis mowi wprost, ze wczesniejsze listy do Nesty (299-09-19, 300-02-18) TEGO PYTANIA NIE NIOSLY. Odpowiedz realnie V/300. ### CO ISTNIEJE I JEST BLISKO: list do Aemona z 299-09-15, sekcja IV - o CZLOWIEKU, KTOREGO IMIENIA NIE PADA ANI RAZU, i o slowie, ktorego Aemon nie napisze, dopoki nie uslyszy go od tego, kogo dotyczy. TO JEST JON SNOW, NIE DAENERYS (watki jon_snow_krew_neda_na_murze_299_06, jon_snow_po_drugiej_stronie_299_09). ### I RZECZ, KTORA Z TEGO WYNIKA: przy Daenerys stoi 'ANI JEDNEJ DROGI', a najstarszy maester w Westeros koresponduje z Symonem PRYWATNIE od pol roku i ma archiwum Nocnej Strazy. TO JEST DROGA, KTOREJ NIKT NIE PROBOWAL - i jedyna, ktora nie wymaga czekania do maja.
- **WYSZEDL 300-02-07 - 25 DNI CISZY** — POSLANIEC ZA MUR DO MANCE'A RAYDERA - o DELEGACJE PRZED GLOWNA BRAME. Rozkaz wydany rano 300-02-07, zameldowany Krolowi tego samego dnia slowami: 'NIE MOWIE WAM, ZE SIE UDA. MOWIE, ZE WYSZLO'. RAZEM Z NIM: TLUMACZ ZATRZYMANY, PLATNY Z KASY 3 (zold pod Murem, biezaco, potwierdzony 300-02-15) - o co OSRIC PROSIL NA PISMIE I CZEKAL. PODSTAWA: stanowisko Symona przed Krolem 300-02-06 - 'poslac kogos za Mur do Mance'a Raydera PO ICH RELACJE i poprosic o DOWOD W POSTACI DOSTARCZENIA NIEUMARLYCH'. KANAL: nie ma kruka za Mur. Czlowiek wychodzi i wraca albo nie wraca. Odpowiedz wroci PRZEZ OSRICA - i dlatego jego zalegly meldunek VII jest dzis najwazniejsza cisza w grze.
- **NIEODPOWIEDZIANE OD 300-02-06 - przed Rada 300-03-30** — TRZY WARUNKI KROLA PRZED OTWARCIEM BRAMY DZIKIM - postawione 300-02-06 i DO DZIS BEZ ODPOWIEDZI: (1) KTO IDZIE ZA MUR - 'nie wyslecie posla, POSEL TO JEST AKT; wyslecie kogos, kto umie tam wejsc i wyjsc'. (2) CO SIE ROBI Z DOWODEM - kto go niesie i przez ile mil, gdzie go trzymamy, kto przy nim stoi w nocy, CZYM GO ZABIJAMY, gdyby sie ruszyl: 'stal nie robi nic, ogien robi', a JEDYNE CZARNE SZKLO NA POLNOCY TO DWA OSTRZA W PLOTNIE. 'Jesli cos pojdzie nie tak, nie stracimy dowodu - STRACIMY WSZYSTKO, CO TEN DOWOD MIAL UDOWODNIC.' (3) CZYM ICH NAKARMIC - 20-40 TYSIECY, wiecej niz Bialy Port, w krolestwie, ktorego Krol policzyl JEDNA DZIESIATA spichlerzy. 'Nie mowie nie. Mowie, ze bez tej liczby otwarcie bramy jest WYROKIEM WYDANYM PRZEZ NIKOGO.'
- **WIOSNA 300 - JEST TERAZ** — TLUMACZ SPOD MURU ODCHODZI NA WIOSNE. Zatrzymany za pieniadze od 300-02-07 (Kasa 3) - ale zatrzymanie bylo NA TE ZIME. Trzej dzicy zyja, JEDEN MOWI WIECEJ. To sa JEDYNE TRZY USTA, jakie Polnoc ma z tamtej strony, i jedyny czlowiek, ktory je rozumie. Krol powiedzial to wprost: 'chcecie rozmawiac z Mance'em Rayderem, a jeszcze nie odpisaliscie czlowiekowi, ktory pilnuje jedynych trzech ust, jakie mamy'.
- **300-03-03 - WIADOMOSC JEST** — POSLANIEC ZA MUR NIE WROCIL (rzut 20). Wyszedl 300-02-07 z przewodnikiem z klanow gorskich - jedyna droga. PRZEWODNIK WROCIL SAM PO DZIEWIECIU DNIACH: rozstali sie w umowionym miejscu, poslaniec poszedl dalej Z LUDZMI, KTORYCH PRZEWODNIK NIE ZNAL. Nikt nie wie, czy dotarl do Mance'a. NIE MA CIALA, NIE MA ODMOWY, NIE MA DELEGACJI.
- **300-03-03 - WIADOMOSC JEST** — TLUMACZ ZOSTAL (rzut 29) - pieniadze z Kasy 3 doszly i przyjal. ALE OSWIADCZYL OSRICOWI, ZE ZA MUR DRUGI RAZ NIE POJDZIE. Kanal do trzech ust istnieje; PRZEWODNIKA DO MANCE'A NIE MA. Drugiego poslanca nie ma kto poprowadzic.
- **wyslany 300-03-02 o brzasku** — WYMIANA LIST JENCOW - DO ZELAZNEGO TRONU. Kruk maestera, PODPIS CERWYNA JAKO JUSTYCJARIUSZA (nie Namiestnika - to akt sadowy, nie polityczny). DOKUMENT: 271 NAZWISK - 31 rangi + 240 prostych, dolozonych decyzja gracza, ZEBY DOKUMENT BYL NUDNY. HARRION KARSTARK stoi jako SIEDEMNASTY WIERSZ Z TRZYDZIESTU JEDNU, NA CZWARTEJ STRONIE, miedzy dwoma rycerzami z Zachodu, o ktorych nie wiemy nic. METODA: nie pytamy o Harriona, pytamy o CALA LISTE - 'czlowiek, o ktorego nikt nie pytal przez siedem miesiecy, jest tani; czlowiek, o ktorego pyta Namiestnik, ma cene'. ### TO JEST DRUGIE PISMO W TEJ SAMEJ SPRAWIE: pierwsze poszlo DO KROLA (status jencow, trzej dzicy, pieczec Namiestnika, od 300-02-19). Dwa pisma, dwaj adresaci, jedna sprawa.
- **300-03-05** — KAFARY NIE MAJA WLASCICIELA - jedyna rzecz realnie hamujaca groble, i NIKT NIE MA ROZKAZU JEJ USUNAC. Cerwyn 300-02-20 i Bran 300-02-25 powiedzieli to samo: 'nie brakuje nam pieniedzy, stoimy, bo mamy cztery kafary; kafary robi sie z DREWNA I Z ZELAZA, NIE Z MONETY, i trzeba je komus KAZAC zrobic'. Plac budowy BEZ MISTRZA, KUZNI I KAMIENIOLOMU. ### ⚡ OD 300-03-04 ZNIKA POWOD, DLA KTOREGO ROZKAZ NIE MIAL ADRESATA: LAWA SADZA KOWALA (Brusk od Miecha). Rozkaz do kuzni ma wreszcie komu byc wydany.
- **300-03-10** — GROBLA STOI PRZEZ ODWILZ - cztery kafary i zalogi STOJA BEZCZYNNIE. Dzien, w ktorym KAFAR ZNOWU WCHODZI W GRUNT, zalezy od odwilzy i NIKT GO NIE ZNA; jedyny czlowiek, ktory ten dzien rozpozna, to BRAN. Sztandarowa budowa lenna nie ma daty wznowienia.
- **300-03-07** — CZTERY ROBOTY BIJA SIE O TE SAME RECE I NIKT TEGO NIE POLICZYL: GROBLA (stoi, ludzie bezczynni) - TORFIARNIE (to one trzymaja ludzi przy robocie w zimie, czyli program zatrudnienia) - TRZCINA Z PRZYWILEJU (zglosilo sie kilkunastu, prawie wszyscy do jednego rzemiosla) - EKIPA POMIAROWA. Piata dolozona 300-03-01: torf do ludzi.
- **300-03-06** — ROZPOZNANIE PRZEWLOKI - profil, grunt, dlugosc PO NASZEJ STRONIE. Rzeczy wlasne i niesporne, robione od 300-03-01. ODDZIELONE OD POMIARU POD DWIE PIECZECIE, ktory zaczyna sie dopiero, gdy przy sznurze stanie czlowiek Wymana (300-03-06). Joint-walk zachowany, precedens lady Dustin nietkniety.
- **300-03-09** — TRAKT DO DORZECZA - PIERWSZA RZECZ DO ZROBIENIA NIE JEST KOPANIEM: PRZEJSC ODCINEK I ZMIERZYC. Standard z punktu 10: 'ZADEN ODCINEK BEZ NAZWISKA I BEZ DATY'; liczby na calosc nie da sie podac uczciwie, dopoki nie przeszlo sie odcinka. Rece z rejestru dniowek, ten sam mechanizm co przy przewloce. ⚠ KOLIZJA: prowadzi BRAN, a Bran ma groble - albo dostaje zastepce przy grobli, albo trakt staje w dniu, w ktorym rusza grobla.
- **300-03-03** — ZLECENIE DLA WILLI - ZWEZENIE (300-01-27): PRZESTAC SZUKAC POSREDNIKA, ZAWEZIC DO PETYRA BAELISHA I DO KROLEWSKIEJ PRZYSTANI. Podstawa - jej wlasny trop docisniety: obce srebro, spekulacja zbozowa, 'najlepszy umysl od monety i cienia', cierpliwy pieniadz.
- **300-03-08** — ZLECENIE DLA HARLA W BARROWTON - ziarno siewne. ⚠ TRACI NA WARTOSCI od 300-03-02: Dustin sprzedal zboze, zeby zaplacic danine W MONECIE. 'Niech pyta, ale nie liczmy na to.' Goniec za kolumna wyslany 300-03-02.
- **300-03-20** — ETAP I SPICHLERZA POLNOCY - JEDNA KSIEGA na: spichrze Krola, Zimowe Miasto, komory, Kamienny Brod. Krol policzyl JEDNA DZIESIATA spichlerzy krolestwa - a bez tej liczby otwarcie bramy dzikim jest 'wyrokiem wydanym przez nikogo'.
- **300-03-09** — ETAPY MIASTA CAILIN: I - co pod ziemia · II - co zarabia (waga, targ, sklady, brama) · III - co widac (bruk, mury, latarnie) · IV - co oddycha (dzielnica zimowa). ETAP II MA SAM NA SIEBIE ZARABIAC: myto z grobli i clo z komory. ⚠ MYTO WLASNIE ZMIENIONO NA 1/40 OD WARTOSCI - rachunek Etapu II trzeba przeliczyc.
- **300-03-10** — TORFIARNIE - maja ciac WIECEJ, a mierniczego torfu wakat po Harrolu zamkniety dopiero 300-03-03 (Jorren Lut). To jest zarazem PROGRAM ZATRUDNIENIA ZIMOWEGO: 'to one trzymaja ludzi przy robocie w zimie'. ⚠ I od 300-03-03 torf placi 7,5 proc. zamiast 15 - powod, zeby ciac wiecej, wlasnie sie podwoil.
- **300-03-03 - PRZYSZLO** — MELDUNEK VII OSRICA - TRZY LICZBY I JEDNA ICH BRAK. (1) STRAZ, liczona NAZWISKO PO NAZWISKU przeciw rolce: PIECIUSET TRZYDZIESTU ludzi, ZDATNYCH DO WALKI TRZYSTU CZTERDZIESTU, na trzech obsadzonych zamkach. Rolka mowi dziewiecset. Aemon mowil we wrzesniu niespelna szesciuset - UBYLO SIEDEMDZIESIECIU W POL ROKU, BEZ ANI JEDNEJ BITWY. I rzecz, ktora zbiega sie z odczytem bramy Fosy: Z TYCH TRZYSTU CZTERDZIESTU DZIEWIECDZIESIECIU CZTERECH PRZYSZLO Z POLUDNIA W CIAGU ROKU. (2) KLANY GOR - DZIURA W MUSTRZE ZAMKNIETA PIERWSZY RAZ W DZIEJACH: CZTERY TYSIACE OSIEMSET MEZCZYZN ZDOLNYCH NOSIC BRON. 'Nie dali sie policzyc nikomu, bo nikt nigdy nie przyjechal do nich PIERWSZY. Ja mialem co powiedziec: ZE MOWILI PIERWSI.' (3) ZA MUREM - liczone JEGO METODA, nie po wloczniach: po wsiach, ktore opustoszaly, i po zwierzynie, ktora przestala chodzic. NIE WIECEJ NIZ DWADZIESCIA DWA TYSIACE LUDZI, KTORZY IDA O WLASNYCH SILACH - z tego NA BRON zdolna najwyzej jedna trzecia. 'Reszta to geby. I to jest wasz problem, nie ich wlocznie.' Margines podany wprost: plus minus trzy tysiace, i powiedzial, w ktorym miejscu zgaduje. (4) CZEGO NIE MA: ANI SLOWA O POSLANCU ZA MUR. 'Dlatego meldunek jest spozniony. Czekalem, zeby miec co napisac, i nie doczekalem sie. Nie przywioze wam zgadywanki - ale nie wolno mi tez kazac wam czekac dalej.'
- **300-04-02** — MELDUNEK VIII OSRICA - CO TRZYDZIESCI DNI, TAKZE GDY STOI NA NIM 'NIC'. ⚠ ZMIANA ADRESU, ta sama, ktora wprowadzono Torrenowi 300-02-17: MELDUNEK IDZIE TAM, GDZIE JEST NAMIESTNIK, NIE DO WINTERFELL. Meldunek VII szedl okrezna droga i lezal, bo adres byl staly, a Namiestnik nie. Od dzis adres jest ruchomy: do 300-03-07 Fosa, potem Bialy Port, od ~300-20 Winterfell.
- **PRZED RADA 300-03-30** — CZTERY TYSIACE OSIEMSET Z KLANOW - LICZBA, KTOREJ KROLESTWO NIGDY NIE MIALO. Krol powiedzial 300-02-06: 'UMBEROWIE, FLINTOWIE, KLANY Z GOR TO SA PIERWSI LUDZIE - ta sama krew, te same stare bogi'. Teraz ta sama krew ma liczbe, a Rada otwiera sie punktem 0 - MUR. To jest jedyna liczba z tej sprawy, ktora jest SWIEZA, WLASNA i DOBRA.
- **300-03-07** — OSIEM RUBRYK DLA TRZECH BUDOW - nie urzedy, bo te sa obsadzone od pol roku, tylko FORMA MELDUNKU. BORS (Przystan Wilka), DONNEL OBROK (Dustinport) i THEOMORE (Glebokorzen) nie maja ani rubryk, ani dnia. TORREN DOSTAL OSIEM RUBRYK 300-02-17 I OD RAZU ZACZAL PISAC - po 190 dniach milczenia. Ta sama forma, te same osiem rubryk, ten sam dzien miesiaca.

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
- [300-03-03] `projekt_cailin`: ### BUDOWY DOSTAJA URZEDY, NIE NAZWISKA - rozstrzygniecie gracza 300-03-03: 'te brakujace budowy niech osoby beda wyznaczone jako instytucje do realizacji'. ### ZASTOSOWANA WLASNA REGULA DOM…
- [300-03-03] `rozwidlenie_dwie_nogi`: ### BUDOWY DOSTAJA URZEDY, NIE NAZWISKA - rozstrzygniecie gracza 300-03-03: 'te brakujace budowy niech osoby beda wyznaczone jako instytucje do realizacji'. ### ZASTOSOWANA WLASNA REGULA DOM…
- [300-03-03] `agronomia_chlodu_glebokorzen_299_08`: ### BUDOWY DOSTAJA URZEDY, NIE NAZWISKA - rozstrzygniecie gracza 300-03-03: 'te brakujace budowy niech osoby beda wyznaczone jako instytucje do realizacji'. ### ZASTOSOWANA WLASNA REGULA DOM…
- [300-03-03] `lenno/BRAN`: ### BUDOWY DOSTAJA URZEDY, NIE NAZWISKA - rozstrzygniecie gracza 300-03-03: 'te brakujace budowy niech osoby beda wyznaczone jako instytucje do realizacji'. ### ZASTOSOWANA WLASNA REGULA DOM…
- [300-03-03] `lenno/WEYLIN`: ### BUDOWY DOSTAJA URZEDY, NIE NAZWISKA - rozstrzygniecie gracza 300-03-03: 'te brakujace budowy niech osoby beda wyznaczone jako instytucje do realizacji'. ### ZASTOSOWANA WLASNA REGULA DOM…
- [300-03-03] `lenno/ORBELO`: ### BUDOWY DOSTAJA URZEDY, NIE NAZWISKA - rozstrzygniecie gracza 300-03-03: 'te brakujace budowy niech osoby beda wyznaczone jako instytucje do realizacji'. ### ZASTOSOWANA WLASNA REGULA DOM…
- [300-03-03] `agronomia_chlodu_glebokorzen_299_08`: ### VOID (GM), PODWOJNY - TWIERDZILEM O BRAKU TAM, GDZIE OD POL ROKU STOI NAZWISKO Z RZUTEM. Wskazania gracza 300-03-03. || ### (1) PRZYSTAN WILKA MA MISTRZA ROBOT I MA GO OD 299-08-27 (rzut…
- [300-03-03] `ustroj_urzedow`: ### VOID (GM), PODWOJNY - TWIERDZILEM O BRAKU TAM, GDZIE OD POL ROKU STOI NAZWISKO Z RZUTEM. Wskazania gracza 300-03-03. || ### (1) PRZYSTAN WILKA MA MISTRZA ROBOT I MA GO OD 299-08-27 (rzut…
- [300-03-03] `przystanie_ladunkowe_wschodu_300_02`: ### VOID (GM), PODWOJNY - TWIERDZILEM O BRAKU TAM, GDZIE OD POL ROKU STOI NAZWISKO Z RZUTEM. Wskazania gracza 300-03-03. || ### (1) PRZYSTAN WILKA MA MISTRZA ROBOT I MA GO OD 299-08-27 (rzut…
- [300-03-03] `korona/THEOMORE`: ### VOID (GM), PODWOJNY - TWIERDZILEM O BRAKU TAM, GDZIE OD POL ROKU STOI NAZWISKO Z RZUTEM. Wskazania gracza 300-03-03. || ### (1) PRZYSTAN WILKA MA MISTRZA ROBOT I MA GO OD 299-08-27 (rzut…
- [300-03-03] `korona/GAWEN`: ### VOID (GM), PODWOJNY - TWIERDZILEM O BRAKU TAM, GDZIE OD POL ROKU STOI NAZWISKO Z RZUTEM. Wskazania gracza 300-03-03. || ### (1) PRZYSTAN WILKA MA MISTRZA ROBOT I MA GO OD 299-08-27 (rzut…
- [300-03-03] `korona/DONNEL`: ### VOID (GM), PODWOJNY - TWIERDZILEM O BRAKU TAM, GDZIE OD POL ROKU STOI NAZWISKO Z RZUTEM. Wskazania gracza 300-03-03. || ### (1) PRZYSTAN WILKA MA MISTRZA ROBOT I MA GO OD 299-08-27 (rzut…
