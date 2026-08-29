# Zasady domowe (obowiazuja od dnia 5, na zyczenie gracza)

1. KAZDY istotny skutek wymaga ZALOGOWANEGO rzutu. Bez wpisu w ukryte/rzuty.log
   scena nie moze zakonczyc sie porazka. Brak rzutu = brak porazki.

2. PROGI: latwe 30, typowe 50, trudne 70, bardzo trudne 85.
   Przygotowanie, dobra relacja i wlasciwa pora obnizaja prog o 10-20 (kumulatywnie,
   rozsadnie). Zapisuj w logu, jakie modyfikatory zeszly z progu.

3. PECH SIE NIE KUMULUJE W NIESKONCZONOSC: po DWoCH porazkach z rzedu w TEJ SAMEJ
   sprawie kolejny rzut w tej sprawie dostaje premie +15 (obniza prog o 15). Swiat
   nie dobija lezacego.

4. ZEGARY OKAZJI rowniez w zegary.json. Na kazde 2 zegary ZAGROZENIA przypada co
   najmniej 1 zegar OKAZJI (wracajaca galera, wakat u pisarza, swieto z jalmuzna,
   kupiec szukajacy tlumacza itp.). Okazje odliczaja tak samo jak zagrozenia.

5. NASTAWIENIE NPC ROSNIE od drobnych przyslug, nie tylko spada. Bractwa, parafia,
   sasiedzi i cechy pomocnicze udzielaja pomocy wzajemnej — to realizm epoki, nie
   ulga dla gracza. Pomoc ma swoja cene (zobowiazanie, wdziecznosc, przynaleznosc),
   ale ISTNIEJE.

## STARZENIE (mechanika wieku) — dodane 297-09-06
- **Nie trzymamy sztywnego wieku.** Każda postać (Symon + NPC) ma `rok_urodzenia`; wiek WYLICZA się z kalendarza świata.
- `stan.py` przy każdym odświeżeniu przelicza `wiek = rok_biezacy - rok_urodzenia` (minus 1, jeśli `data_urodzin` w tym roku jeszcze nie minęła) i zapisuje do JSON. Dzięki temu wszyscy starzeją się sami z upływem lat — działa w nieskończoność (grasz 50 lat → wszyscy +50).
- **Symon:** ur. 275 AC, 8. miesiąc, dzień 3 (start gry 296-08-03 = jego 21. urodziny). Ma pełną `data_urodzin` (precyzja co do dnia).
- **NPC:** mają `rok_urodzenia` (dodane hurtem 297-09-06 = 297 − ówczesny wiek). Bez `data_urodzin` → wiek roczny/przybliżony (wystarcza). Można dopisać `data_urodzin` komukolwiek, gdy fabuła tego zażąda.
- **Nowy NPC:** nadawaj `rok_urodzenia` (= rok bieżący − wiek), nie sztywny `wiek`.
- **Przyszłe:** przy bardzo długiej grze dojdzie ŚMIERTELNOŚĆ (starość/choroba) — do rozpisania osobno, gdy nadejdzie czas.

## KANON-GUARD: NIE fabrykowac wesela Bess (powtarzajacy sie blad 3x)
- **Bess (corka Wendy) jest ZAMEZNA** z Dake'em (mlody rybak) od poczatku 297. Symon przespal jej wesele przez febre (02, o krok od smierci).
- Wymyslilem jej "przyszle wesele" TRZY razy (05-19, 08-27, 09-08) jako inbound. To BLAD CIAGLOSCI. Nigdy wiecej.
- Jedyna niezamezna corka Wendy to MELLA - ale ZADNE jej wesele nie jest ustalone w kanonie; nie zmyslac drugiego, by zalatac.
- OGOLNA ZASADA: przed wprowadzeniem "wydarzenia z zycia NPC" (slub/narodziny/smierc) SPRAWDZ kartoteke i kronike, czy to juz sie nie odbylo.

## PROWADZENIE: nie rzucac adwersaryjnie na rutyne/rozszerzenia ustalonego (dodane 09-19)
- Rzuty sa od rzeczy NIEPEWNYCH/spornych/o realnej stawce - NIE od dopinania czegos, co gracz juz ma ustalone (istniejacy partner/pojemnosc/relacja).
- Rozszerzenie dzialajacego ukladu (np. wpiecie prowiantowania w skladki Aurane'a, ktory JUZ jest kregoslupem logistyki) => po prostu SUNIE do przodu, bez adwersaryjnego rzutu.
- NIE karac gracza za dokladnosc/dodatkowe rozsadne kroki losowym negatywem. Dorzucenie sensownego kroku != trigger na zly rzut.
- Sprawdzac CONTINUITY (co juz ustalone w plikach) zanim wygeneruje sie komplikacje sprzeczne ze stanem.

## RYGOR ZIMOWYCH SZLAKOW (od 297-09-26, po kryt-mrozie zalamania konwoju Torwyna)
- ZERO SKROTOW w mroz: 'twarda' droga klamie (przymarznięte oczka, podmokle laki, podmyty lod). Woz jedzie TYLKO trasa z zatwierdzonej listy, choćby dluzszej.
- LISTA ZATWIERDZONYCH TRAS do kazdego zrodla (Merrek, Torwyn) i do kasztelu; Bran (zna doki/drogi) nanosi pewne/zakazane, Hal papieruje, kazdy furman dostaje.
- TA SAMA KARTA dla SIECI RELIEFU (sanie Brana do zaulkow) - jeden rygor chroni zysk i biednych.
- NIKT SAM w najgorszy mroz: para wozow albo czlowiek z tylu na linie (dzis to uratowalo furmana - od teraz regula, nie szczescie).
- Zasada nadrzedna: katastrofie zapobiega sie miesiacami wczesniej (przezornosc), nie w dniu uderzenia. Roznica miedzy dobrym sercem a dobrym rzadem.

## REGULA RELIEFU — karmic z owocu, nie z korzenia (od 297-09-27)
1. Relief WYLACZNIE z ODPISU NADWYZKI: na kazdym Bilansie stala czesc NETTO miesiaca (odpis) -> rezerwa reliefu. Reszta nigdy.
2. NIGDY z kapitalu obrotowego: rotacja (400), weksle, principal underwritingu = NIETYKALNE (krew firmy).
3. Miesiac bez nadwyzki = relief kurczy sie do tego co na reku; nie zadluzac gwiazdy.
4. Wspolfinansowanie Wiary (Owen) odciaza rezerwe.
Zasada nadrzedna: dawac z owocu nie z korzenia; drzewo co zjada wlasny korzen nie karmi nikogo. Trwalosc to tez milosierdzie. (Decyzja gracza 09-27 po uczciwym rachunku: relief nie oplaca sie kupcowi, oplaca sie czlowiekowi rady - ale tylko karmiony zyskiem, nie zamiast niego.)

## GALKA DRAMATYZMU — operacyjne w tle, stawka pelnymi turami (od 297-10-05, decyzja gracza)
- SPRAWY OPERACYJNE (najmy staffu, rutynowe ksiegi, dostawy, drobne zakupy, rozszerzenia zespolu) => ROZSTRZYGAC LEKKO: jeden akapit/montaz, minimum kosci, koszt+efekt i dalej. NIE robic z tego wielosceniowego luku fabularnego.
- SPRAWY O STAWCE (polityka/lord, zagrozenia zycia/reputacji, relacje-progi, slub, karta Antaryona/firewall, wielkie interesy) => pelne prowadzenie turowe z rzutami.
- NIE naciagac motywow gry (firewall, 'niewygodny swiadek', widocznosc, zawisc) na KAZDY drobiazg. Zwykly klerk to zwykly klerk. Czasem najem to tylko najem.
- Nie mnozyc rzutow per pod-krok rutyny; jeden rzut na sprawe albo zero. Skrajne kosci przy rzeczach blahych = rozstrzygac proporcjonalnie, nie rozdmuchiwac do sagi.
- Kontekst: 10-05 profesjonalizacja firmy (analityk/handlowiec/ochrona) urosla do 'wydarzenia miesiaca' przez rozbicie na 6-8 scen z kostka kazda; korekta na przyszlosc.

## KANON DWORU NOWEGO ZAMKU — kasztelan-steward = JEDNA funkcja (locked 297-10-06, decyzja gracza)
- Nowy Zamek (Manderly) ma JEDNA polaczona funkcje: KASZTELAN-STEWARD - dowodzi zamkiem I zarzadza gospodarstwem/prowiantem/rachunkami (nie dwa osobne urzedy; w tym domu skumulowane w jeden). Terminy 'kasztelan' i 'steward' = TA SAMA osoba/urzad.
- Trzymal ja HELYARD -> ZLOZONY Z URZEDU 30-09 (tuszowal zdrade pierscienia przed lordem). Urzad WAKUJE.
- PO UPADKU PIERSCIENIA — 2 WAKATY na szczeblu nadzoru dworu (zrodlo 'luk w nadzorze', o ktorych mowil Wyman):
  1. KASZTELAN-STEWARD (Helyard, zlozony) - najwyzszy urzad domowy zamku, PUSTY.
  2. OFICER (Aldric, w celi - byl oficerem od nadzoru prowiantu/procurement, kupiony przez pierscien) - drugi urzad nadzorczy, PUSTY.
  (Dodatkowo poza urzedami zamku: Roldan/Rennifer zwinieci - to byli gracze pierscienia, nie formalne urzedy zamkowe.)
- GODRIC = zarzadca PRYWATNEGO domu blisko dworu + DOSTAWCA zamku (kanal Symona). Torhen = drugi zarzadca-dostawca. To NIE urzedy zamkowe, lecz zewnetrzni kontrahenci.
- LIVE THREAD: lord Wyman predzej czy pozniej OBSADZI wakaty (kasztelan-steward + oficer). Kto obejmie kasztelanie-stewardie WAZY dla dworu i sciezki rady Symona (nowy kasztelan moze byc sojusznikiem albo nowym zrodlem tarcia; zawisc ocalalych oficerow zyje). Swiat ma to rozegrac - nie zmyslac obsady z gory, niech przyjdzie jako wydarzenie.

## ZASADA: ROZMOWA NIE JEST PUŁAPKĄ (od 297-10-15, słuszna korekta gracza)
Gracz wskazał realną wadę: jeśli odwiedziny/rozmowy generują komplikacje, to gra
KARZE angażowanie się i opłaca się z nikim nie gadać. To odwrotność symulatora
społecznego. NAPRAWA:

1. **Ciepłe wizyty/rozmowy z sojusznikami i znajomymi = BEZ downside.** Dolny
   wynik takiej wizyty to „miło, choć bez wielkich wydarzeń" — NIGDY „pojawia się
   nowa komplikacja". Zwykle DOMYŚLNIE nie rzucaj na sam akt odwiedzin.
2. **Komplikacje/problemy przychodzą z WŁASNEGO PĘDU ŚWIATA** (inbound, zegary
   dojrzewające, NPC z własną agencją) — NIE są spawnowane jako kara za to, że
   gracz z kimś porozmawiał. Gdyby NPC miał realny problem, świat i tak by go
   wypchnął (inbound), niezależnie od tego, czy gracz wpadł powiedzieć „cześć".
   Problem NIE materializuje się dlatego, że gracz „zaczął temat".
3. **RZUTY (z możliwym kosztem) rezerwuj dla realnie NIEPEWNYCH, KONSEKWENTNYCH
   działań:** negocjacja o stawkę/warunki, audyt co może znaleźć albo nie,
   konfrontacja, przekonanie opornego do czegoś ważnego, ryzykowny ruch. NIE dla
   samego aktu odwiedzin/rozmowy/check-inu.
4. **Nawet gdy rzut jest zasadny: niski wynik = „nie osiągnąłeś celu / skromny
   plon", a nie „wymierzam ci nowy problem".** Framing: propozycje i rozwiązania,
   nie problemy (spójne z GAŁKĄ DRAMATYZMU).
5. **Efekt docelowy:** rozmawianie z ludźmi jest domyślnie NEUTRALNE-DO-POZYTYWNEGO
   (relacje, ciepło, czasem okazja). Angażowanie się NIGDY nie może być w
   oczekiwaniu gorsze niż siedzenie w domu.

## ZASADA: EWOLUCJA GRUNTOWANIA (od 297-10-17, słuszna uwaga gracza)
Gracz zauważył, że „nie zadzieraj nosa" stało się refrenem u wielu NPC. Prawda:
theme jest REALNY (pyszny pęd Symona + niebezpieczna pozycja szybko wschodzącego
nieszlachcica; „gbur sięga ponad stan" raz go realnie kosztowało — smear po głośnym
szukaniu handlowca). ALE ostatnio Symon ŻYJE lekcją (prep nie pchanie, służba
biednym, maszyna metodycznie, pyta o ludzi, sam się gruntuje). KOREKTA PROWADZENIA:
1. Grunt ma EWOLUOWAĆ z ostrzeżenia -> w UZNANIE ("widzimy, żeś to pojął") w miarę
   jak Symon dowodzi lekcji. Nie karać go ciągłym echem za flaw, którego już pilnuje.
2. NIE wszyscy NPC walą w ten sam bęben. Różnicować: jedni gruntują, inni już ufają/
   chwalą/idą dalej. Owen/Serla/Mira/Nesta mają RÓŻNE głosy, nie jeden refren.
3. Grunt wraca jako żywa korekta TYLKO gdy Symon faktycznie znów pcha/pyszni się —
   nie jako domyślny warm-NPC beat. Zasłużone uznanie > odruchowa przestroga.


## ZASADA: PRZEPLYW DNI / ZEGAR CZASU (dopisane ~298-09-30 po lapsusie w obozie)
Gra NIE liczy czasu automatycznie - GM przesuwa date/pore w swiat.json RECZNIE wg czasu, jaki akcja zjada.
- Kazda akcja ma REALNY koszt czasu. Pol-dniowy beat = pora do przodu; wielodniowy projekt (audyt, scalanie, wielowieczorowa obserwacja, budowa, podroz) = ADVANCE DATY o tyle dni, ile realnie trwa (powiedziec wprost 'to zajmuje ~N dni' i krok zegara).
- LAPSUS DO NIEPOWTORZENIA: w obozie hostu (09-26) ~10 akcji day-spanning przykleilo sie do jednej daty, bo porzucilem ramy kotwiczace (RANEK/domkniecie). Poprawiono na ~09-30.
- Przy nowym dniu RE-KOTWICZ czasem: render RANEK (data+pogoda+kalendarz+korespondencja+status) albo min. jawnie nazwij nowa date/pore. Nie pozwol wielu turom skleic sie w jedna date bez kroku zegara.
- Montaz/dlugie prace: rozliczaj z jawnym uplywem ('mija ~2 dni'), aktualizuj swiat.json.
