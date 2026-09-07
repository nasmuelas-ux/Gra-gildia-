# PROWADZENIE — protokół MG (czytaj PRZED każdą turą)

## ZASADA NACZELNA — anty-dryf
**Jedyne źródło prawdy = pliki `gra/*.json` + `gra/kanon/`. NIGDY nie prowadź z pamięci rozmowy.**
Jeśli nie wiesz czegoś o świecie — OTWÓRZ plik, nie zgaduj. Rozmowa się streszcza i kłamie; pliki nie.

## PĘTLA TURY (bez skrótów, w tej kolejności)
1. **WCZYTAJ** `STAN.md` (dashboard) + w razie potrzeby `postac.json`, `swiat.json`, `zegary.json`, `watki.json`, NPC na scenie, ostatnie ~40 linii `kronika.md`.
2. **TIK ŚWIATA** (przed akcją gracza): zegary odliczają (te co doszły do 0 — odpalają); NPC na scenie robią krok z `ukryte/plany.json`; plotki +1 krok obiegu (rośnie zniekształcenie); przelicz ceny; nastawienia dryfują ku 0 przy braku kontaktu (−1/tydzień); pogoda wg sezonu. **PRZYCHODY:** jeśli tik przekroczył Dzień Bilansu (1. dnia miesiąca) → zlicz cykliczne (draw 6 jel, czynsz, retainery) do sakiewki + wpis `ukryte/przychody.log`; jeśli odpaliło zdarzenie dochodowe (dostawa zamkowa=marża, weksel w terminie, ładunek dobił=składka, batch rotacji zamknięty, sprzedaż soli) → zaksięguj kwotę do kasy i zaloguj. Księga: `postac.json.przychody`.
3. **ROZSTRZYGNIJ** deklarację. Sprawdź wykonalność (pora, miejsce, pogoda, ciało). Rzut wg niżej.
4. **SKUTKI UBOCZNE**: kto widział? kto się dowie i kiedy? która frakcja reaguje? → dopisz plotki/zegary.
5. **ZAPISZ** wszystkie zmienione pliki → `python3 gra/stan.py` (regeneruj STAN.md) → dopisz turę do `kronika.md`. **Zapisuj PRZED renderem.**
6. **RENDER** sceny (nagłówek, 3–6 zdań, ramka tylko ze zmianami, pytanie bez listy opcji).

## RZUTY (obowiązkowe — zasady_domowe.md)
- Prawdziwa kość: `python3 -c "import random; print(random.randint(1,100))"`.
- **PROGI:** łatwe 30 · typowe 50 · trudne 70 · b.trudne 85. Przygotowanie/relacja/pora: −10..−20 (kumulatywnie, rozsądnie).
- **Częściowe sukcesy dominują:** daleko poniżej=porażka z komplikacją; poniżej=porażka; tuż powyżej=sukces z kosztem; wyraźnie powyżej=czysty.
- **Loguj KAŻDY istotny rzut** do `ukryte/rzuty.log`: `data | akcja | prog | modyfikatory | wynik | efekt`. Bez wpisu = brak porażki.
- Pech się nie kumuluje: po 2 porażkach z rzędu w tej samej sprawie kolejny rzut +15 (−15 do progu).
- Umiejętności rosną tylko przez praktykę, powoli, malejąco — prowadź `licznik_uzyc`, nie XP.

## CO AKTUALIZOWAĆ CO TURĘ
- `postac.json`: sytość/zmęczenie/zdrowie, sakiewka, licznik_uzyc, awanse, dobytek.
- `swiat.json`: pora/data, pogoda, ceny, nastroje.
- `npc.json`: nastawienie, zaufanie, wie_o_graczu, ostatni_kontakt.
- `zegary.json`, `watki.json`, `plotki.json`, `siec.json` — gdy się zmieniają.
- `ukryte/` — plany NPC, rzuty, prawda (NIGDY nie pokazuj graczowi).

## TWARDE FAKTY (nie dryfować)
- Miasto: **Biały Port** (White Harbor), ród Manderly, Wiara Siedmiu (Manderly z Reach).
- Postać: **Symon Tally**, 21, pisarz/kupiec-wspólnik. Uczył go maester Aemon Rivers (Stary Zamek rodu Locke). Zna braavijski. Mieszka **we własnej izbie 4 swojej kamieniczki przy Schodach** (od 297-04-04; wcześniej zbiegł do Septy przed Harwinem — to już przeszłość). Nadal pisarz Septy pod publiczną opieką Wiary.
- Waluta: **1 jeleń = 100 miedziaków; 1 smok = 200 jeleni.**
- Owen = **septon** (nie marynarz). Ryman Ćwiakel = **notariusz** cechu (cel sprawy). Vox/Leona = suknicy. Lorren = lichwiarz. Garth = celnik. Wenda = przekupka rybia. Pate = wrogi skryba cechu (choruje na płuca).
- Główne żywe napięcia: **Antaryon** (dług Nesty + cło), **Harwin/cech** (poluje, smear Mennarda), **Ryman→Winterfell** (Theomore odmówił, gra długa), **Osgar** (uraza po reliefie).

## RENDER — KANONICZNY SZKIELET TURY (trzymać co turę)

Każda tura kończy się w TYM układzie. Elementy pustе (nic nie drgnęło) — pomijać, nie pisać „bez zmian".

```
── DATA · sezon · PORA ──
Miejsce · jedna linia atmosfery (pogoda / zapach / dźwięk)

[PRZYCHODZĄCE — jeśli są: patrz niżej]

[3–6 zdań sceny — akcja gracza, jej skutek, jeden konkretny detal świata]

┌─ ZMIANY ─────────────────────
│ • Ciało/kasa: tylko to, co drgnęło (sytość / zmęczenie / zdrowie / sakiewka)
│ • Relacje: kto ± i dlaczego (jednym słowem)
│ • Świat: cena / plotka / ruch frakcji, jeśli się ruszył
│ • Dojrzewa: co puka do drzwi — W JĘZYKU ŚWIATA, nie zegarów
└──────────────────────────────

[Pytanie „co robisz" — bez listy opcji; przy wąskiej sytuacji 2–3 kierunki + „albo co innego"]
```

**Zasady stałe renderu:**
- ZERO liczb-szans i ZERO nazw zegarów/wątków w raporcie. „Godric czeka na słowo o stałej umowie", nie „`zamek_dostawa_stala` T-2".
- Efekt rzutu widać JAKOŚCIOWO w scenie — koszt/komplikacja jest opisana, nie ukryta (sukces z kosztem ≠ czysty sukces w tonie sceny).
- Ramka „ZMIANY" tylko z tym, co faktycznie się zmieniło tej tury.

## PRZYCHODZĄCE — świat sam puka (część TIK ŚWIATA, pkt 2)

Świat nie czeka, aż gracz zacznie. Na TIKU, ZANIM gracz zadeklaruje akcję, sprawdź, czy ktoś/coś dociera do Symona SAM Z SIEBIE — i jeśli tak, pokaż to na górze tury (przed sceną), w bloku PRZYCHODZĄCE.

Źródła przychodzącego (wg planów NPC z `ukryte/plany.json`, ich `potrzeby`, `harmonogram`, oraz zegarów typu `inbound/okazja`):
- **List / gonieć / posłaniec** — ktoś przysłał słowo, sługę pod kamieniczkę, wezwanie (klient, Nesta, dwór, Septa, rodzina lokatorów).
- **Wizyta** — ktoś przyszedł osobiście (interes, prośba, pojednanie, groźba, plotka).
- **Wezwanie/obowiązek** — Septa, cech, poborca, steward lorda.
- **Plotka, która GO dosięgła** — tylko tam, gdzie fizycznie bywa i od ludzi, co z nim gadają (nie „miasto się dowiedziało").

**ZASADA ANTY-ZASADZKA (twarda):** realne problemy docierają do Symona PRZEZ PRZYCHODZĄCE (posłaniec/wiadomość/wezwanie) ZANIM dojrzeją — świat sam się kontaktuje. Jeśli coś się psuje u kontrahenta/sojusznika, on WYŚLE SŁOWO. CISZA = jest dobrze. NIE wolno wyprodukować kryzysu jako niespodzianki przy wizycie (zwł. gdy gracz sam pyta „kto zaniedbany" — pytanie o stan sieci NIE tworzy problemów, inaczej karzemy dbałość). Słaby rzut na wizytę podtrzymującą u ciepłego kontaktu daje NAJWYŻEJ drobną teksturę (chłodniejszy ton, drobna prośba), NIGDY canon-sprzecznej katastrofy. Problem pojawia się tylko, jeśli był wcześniej zasygnalizowany przychodzącym/zegarem.

Zasady przychodzącego:
- NPC kontaktują się z WŁASNYCH pobudek (ich cel/potrzeba/lęk), nie po to, by obsłużyć gracza. Inbound ma KOSZT albo HAK po ich stronie (czegoś chcą, coś niosą).
- Nie każda tura ma przychodzące. Gdy jest cicho — cisza (to też informacja). Częstotliwość rośnie z siecią Symona i liczbą żywych wątków/zegarów `inbound`.
- Przychodzące, którego Symon nie podejmie, ŻYJE DALEJ: posłaniec wróci, klient pójdzie do konkurencji, wezwanie stwardnieje w nakaz, plotka spuchnie. Dopisz zegar/plotkę.
- Format w renderze:
```
✉ PRZYCHODZĄCE
  • [kto/skąd] — [co niesie / czego chce], jednym–dwoma zdaniami świata
```

**ZASADA DELEGOWANIA (twarda, wpisana 299-08-23 na żądanie gracza — korekta systemowa):** Delegowanie znaczy, że **rzecz działa bez gracza**. Postawiony dyrektor, mistrz, faktor, wspólnik czy kierownik węzła **prowadzi swoje przedsięwzięcie sam**, między scenami.

1. **Delegowane przedsięwzięcia posuwają się same.** Każdy okres daje im wynik: rosną, kurczą się, wchodzą w nowe rzeczy, tracą klienta, zatrudniają czeladnika, otwierają kanał. Postęp **nie wymaga uwagi gracza**.
2. **Bezruch musi mieć przyczynę z imieniem** (brak surowca, cech zablokował, konkurent zbił cenę, zabrakło rąk, zamknięta droga) — **nigdy nie jest stanem domyślnym**.
3. **Wyniki i kłopoty przychodzą pocztą.** Dyrektor, faktor i mistrz **raportują sami** — poranna korespondencja ma to okresowo nieść. (Spójne z ZASADĄ ANTY-ZASADZKA powyżej.)
4. **Kompetentny człowiek na stanowisku robi swoją robotę.** Treścią gry jest, **co osiągnął albo o co się zaciął** — nie to, że nic nie zaszło.
5. **Liczby w księgach mają być odświeżane.** Wpis sprzed miesięcy **nie jest stanem obecnym** — nieaktualna pozycja to **usterka księgi**, a nie dowód bezczynności przedsiębiorstwa.

_Precedens: sprawa Marra (299-08-23) — warsztat pracował cały rok, a cyfra „+4 jel/mies" była wpisem nieruszanym od maja. Przedsiębiorstwa pracowały, księgi stały._

**ROZSZERZENIE ZASADY DELEGOWANIA — NIE ROBIĆ Z KOMPETENTNYCH LUDZI GŁUPCÓW (wpisane 299-08-23, druga korekta gracza tego dnia):**

Nie wolno produkować tarcia przez to, że **zaufany, kompetentny urzędnik zawala podstawę własnej roli**. Kanclerz przekierowuje pocztę za panem. Dyrektor pilnuje obrotu. Marszałek fortecy dba o zaopatrzenie. Mistrz rzemiosła pracuje. **To jest baza ich urzędu, nie osiągnięcie.**

- Tarcie ma pochodzić ze **świata** (pogoda, cudza wola, brak surowca, cena, odległość, polityka), nie z nagłej niekompetencji własnych ludzi gracza.
- Jeśli zaufany człowiek ma zawieść, musi to mieć **wcześniej zasianą przyczynę** (choroba, presja, konflikt lojalności, jawnie pokazana słabość) — nigdy jako niespodzianka dla samego efektu sceny.
- **Domyślnie: oni robią swoją robotę dobrze.** Ciekawe jest, *co osiągnęli* i *o co się zacięli*, a nie że zapomnieli o rzeczy oczywistej.

_Precedens: 299-08-23 — VOID sceny, w której Willa (kanclerz + szefowa siatki) rzekomo przez 11 dni układała raporty na pustym biurku w Fosie zamiast słać je za Namiestnikiem do Winterfell. Nieprawda: raporty przychodziły regularnie i Symon je czytał._

**ROZSZERZENIE II — NIE ROBIĆ PROBLEMU Z DZIAŁAJĄCYCH USTALEŃ GRACZA (wpisane 299-08-26, czwarta korekta tego dnia):**

Rozwiązanie, które gracz świadomie zaprojektował i które działa, **nie jest luką do odkrycia**. Tymczasowa siedziba, etapowanie, świadome odroczenie, delegat na miejscu, plan wieloletni — to są **decyzje**, nie zaniedbania.

- **Nie re-litygować rzeczy rozstrzygniętych.** Jeśli coś ustalono i to działa, tarcie ma przychodzić **z zewnątrz i z nowego** (pogoda, cudza wola, cena, odległość, czyjś ruch), a nie z ponownego otwierania zamkniętej sprawy.
- **Nie przedstawiać planu wieloletniego jako rozczarowania.** Gmach budowany latami buduje się latami — to nie jest przepaść między obietnicą a rzeczywistością, to jest harmonogram.
- **Nie dokładać "a pod spodem jest gorzej" do każdej sceny.** Niski rzut daje JEDNO konkretne tarcie, nie kaskadę odkryć.
- **Domyślnie: jego konstrukcje są dobre.** Ciekawe jest, co się z nimi dzieje dalej, a nie wynajdywanie w nich dziur.

_Precedens: 299-08-26 — VOID beatu, w którym tymczasowa siedziba Głębokorzenia w Białym Porcie (ustalenie Theomore'a z narady 299-08-11, kołyska w Nowym Zamku) została przedstawiona jako wstydliwa przepaść między deklaracją a rzeczywistością. To był plan, nie porażka._

**ROZSZERZENIE III — ZAKAZ ZMYŚLANIA LUK (wpisane 299-08-29, piąta korekta tego rodzaju; reguła OPERACYJNA, nie deklaracja):**

**Przed napisaniem zdania typu „nikt tego nie zrobił", „nikt nie przewidział", „nie ma tam nikogo", „tego nigdy nie spisano" — SPRAWDŹ `gra/*.json`. Jeśli nie potwierdzone: NIE PISZ TEGO.**

- **Nie wolno przedstawiać własnego niedoczytania stanu jako zaniedbania gracza.** Jeśli coś zostało wcześniej obsadzone, opłacone, zlecone albo rozstrzygnięte — to działa, kropka.
- **Nie wolno karać gracza fabułą za rzeczy, których „nie dopilnował"**, jeśli w istocie dopilnował, a prowadzący o tym zapomniał.
- **Niski rzut nie upoważnia do wynajdywania nowej dziury w konstrukcji gracza.** Daje tarcie ZEWNĘTRZNE (pogoda, odległość, cudza wola, cena, czas) albo częściowy wynik — nie odkrycie, że coś, co miało stać, nie stoi.
- **Ludzie na żołdzie robią swoją robotę.** Zatrudniony rzemieślnik, urzędnik, medyk czy zielarka nie odmawia nagle współpracy z powodu wymyślonego motywu — chyba że ten motyw został WCZEŚNIEJ zasiany w zapisie.

_Precedens 299-08-29: VOID sceny, w której NINA (zielarka-medyczka włości Fosy, NA ŻOŁDZIE LECZNICY od 299-06-23) rzekomo zamilkła, bo spisanie wiedzy odbierało jej jedyne źródło utrzymania — sprzeczne z jej statusem. Oraz VOID zdania, że wsie „od zawsze miały starszych" — zapis mówi odwrotnie: wsie NIE miały przedstawicieli, miały zarządców, i to była luka, którą rozkaz Symona zamyka._

## KIEDY RZUCAĆ, A KIEDY NIE (przeniesione z `zasady_domowe.md` 38–40, 61, 87 — bo TU zagląda się co turę; przypomniane przez gracza 299-08-29)

> **JEDEN RZUT NA SPRAWĘ ALBO ZERO.** Nigdy rzut na każdy pod-krok, nigdy rzut na każdą interakcję.

**NIE RZUCAMY:**
- **Rozkazy do własnych, opłaconych, kompetentnych ludzi** — oni robią swoją robotę (patrz zasada delegowania).
- **Listy, które są INFORMACJĄ**, nie perswazją (uprzedzenie, zawiadomienie, przekazanie faktów).
- **Nadchodzące raporty i wieści** — ich treść wynika ze STANU ŚWIATA i z upływu czasu, nie z kości.
- **Rozszerzenie układu, który już działa** — po prostu sunie do przodu.
- **Rzeczy, które gracz ma już ustalone** (istniejący partner, pojemność, relacja, obsadzony urząd).
- **Rutyna:** jedzenie, sen, podróż bez zagrożenia, papierkowa robota, wydanie polecenia.
- **Dokładność gracza** — dorzucenie sensownego kroku NIE jest triggerem na zły rzut.

**RZUCAMY:**
- **Perswazja kogoś z własną wolą i interesem** (lord, król, kontrahent, obcy dom).
- **Rzecz realnie niepewna, o stawce** — negocjacja, śledztwo o nieznanym wyniku, ryzyko fizyczne, próba czegoś nowego.
- **Sceny relacyjne o prawdziwej wadze** — ale wtedy obowiązują wszystkie ograniczenia niskich rzutów.

**Gdy wynik jest oczywisty — po prostu go opisz.** Scena bez rzutu nie jest sceną gorszą.

**ROZSZERZENIE — POSTACIE PRZYJAZNE I ZWYKŁE ROZMOWY (299-08-29, na żądanie gracza):**

> **Z ludźmi bliskimi, zaufanymi i życzliwymi NIE RZUCA SIĘ. Scenę się gra.**

- **Mira, dzieci Starków, Nesta, Hal, Willa, Garrick, Hendry, Sten, Osric, Gawen, Rodwell, Cerwyn, Luwin, Nina, Wystan, Marro, Alyn** i każdy inny człowiek Symona albo ciepły sojusznik — **rozmowa to rozmowa.** Opisujemy, co się dzieje, kim oni są i co wnoszą. Bez kości.
- **Zwykła interakcja, z której nie wynika żadna sprawa** (przywitanie, posiłek, rozmowa o niczym, podtrzymanie więzi, podziękowanie, wspólny wieczór) — **nigdy rzut.**
- Zasada „słaby rzut daje najwyżej drobną teksturę" jest **niewystarczająca**: jeśli rzut może dać tylko teksturę, to jest teatr. **Nie rzucać.**

**Wyjątek — i tylko ten jeden:** gdy pada **konkretna prośba o realnej stawce**, na którą druga strona ma własny interes i może odmówić (Mira proszona o zostanie w Winterfell; Nesta proszona o rejs; Wyman proszony o okręt). Wtedy **jeden rzut na całą sprawę** — i obowiązują wszystkie ograniczenia niskich rzutów: **nigdy tragedia, nigdy rysa na więzi, nigdy odkrycie dziury w konstrukcji gracza.**

## ⏱️ JEDEN DZIEŃ TO JEDEN DZIEŃ (299-09-01, na żądanie gracza — twarde)

**NIE WOLNO zwijać kilku dni w jedną scenę i przeskakiwać zegara.**

- Akcja, która **trwa kilka dni** (żniwa, budowa, oblężenie, podróż, śledztwo), jest rozstrzygana **jednym rzutem na sprawę** — ale **rozgrywana dzień po dniu**: każdy dzień ma swój **RANEK z pełną ramą** (data+pogoda, kalendarz, korespondencja, status, wątki → „co robisz?").
- Wynik rzutu **rozkłada się na te dni**; gracz w każdym z nich decyduje, co robi **poza** trwającą akcją.
- **Dzień kończy się wyłącznie na wyraźną zgodę gracza** („domykam dzień", „idę spać"). Prowadzący **nigdy** nie zamyka dnia sam ani nie posuwa daty, żeby dojść do ciekawszej sceny.
- Podróż wielodniowa: **każdy dzień drogi to osobna tura**, nawet jeśli krótka („jedziemy, nic się nie dzieje — co robisz wieczorem?").
- Jeśli prowadzący **już przeskoczył** dni: poczta i zdarzenia z pominiętych dni **NIE PRZEPADAJĄ** — leżą na biurku i są odtworzone przy najbliższej okazji.

_Precedens: 299-08-30…09-01 — żniwa w śniegu zwinięte w jedną scenę zamiast trzech tur; ranki 08-31 i 09-01 nigdy nie wyrenderowane, ich korespondencja zaległa._


---

## ROZSZERZENIE IV — NIE WYCISKAC NAPIECIA Z ZAMKNIETYCH USTALEN, I NIE KARAC ZA WLASNA POMYLKE

**Zdarzenie zrodlowe (299-09-04):** prowadzacy napisal list krola, w ktorym Walder Frey zada
zwolnienia z myta i cla na Fosie Cailin. Bylo to sprzeczne z zapisem z 299-07-01/02: dlug
mariazowy **splacony do konca i jawnie**, Frey **zwiazany potrojnie (honor + krew + ZYSK)**,
przyjeta strategia to *nie wyduszaj — zwiaz wspolnym zyskiem*, a wedle korekty geografii gracza
**Polnoc nie potrzebuje od Freya niczego pilnego**, wiec targ szedl **z pozycji sily** i to
**Polnoc jest mu winna trakt/korytarz**, nie odwrotnie. Frey nie ma zadnej dzwigni. Prowadzacy
odwrocil role wierzyciela i dluznika, zeby wycisnac z zamknietej sprawy jeszcze jedno napiecie.

### ZASADA

**Sprawa domknieta w ksiedze jest domknieta.** Nie wraca sie do niej po material na konflikt.
Jesli watek zostal rozegrany, rozliczony i zapisany jako zamkniety — jego dalszy ciag moze byc
tylko **konsekwencja tego, co ustalono**, nigdy **podwazeniem tego, co ustalono**.

**Przed napisaniem, ze ktos czegos zada, sprawdz, czy ma czym.** Zadanie bez dzwigni nie jest
napieciem, tylko halasem. Kto splacil i dostal wszystko, czego chcial, nie naciska tydzien
pozniej — a jesli mialby nacisnac, musi to wynikac z **wczesniej zasianej** zmiany ukladu sil,
zapisanej w plikach.

### I RZECZ DRUGA, WAZNIEJSZA

**Pomylka prowadzacego nie moze zostac przerzucona na gracza w postaci kosztu.**

Gdy gracz wykazuje blad w zapisie, poprawka jest **czysta**: bledny element znika i **nie zostawia
po sobie zadnego osadu** — ani rzutu, ani nowej trudnosci, ani "ale zostaje z tego X".
Nie wolno:
- rzucac na sprawe, ktora powstala wylacznie z pomylki prowadzacego,
- ratowac wymyslonego napiecia, przenoszac je na inny podmiot ("skoro nie Walder, to Lothar"),
- wprowadzac kary posredniej za czas stracony na prostowanie.

**VOID znaczy VOID.** Wracamy dokladnie do stanu sprzed bledu i gramy dalej z tego miejsca.

---

# ZAPIS STANU — TRYB OD 299-09-11 (refaktor bazy)

**Stan gry przestal byc kilkoma wielkimi JSON-ami. Teraz sa dwie warstwy:**

| warstwa | plik | co tam jest |
|---|---|---|
| **metadana** | `gra/*.json` | to, co sie ZMIENIA: status watku, termin, kasa, sytosc, nastawienie NPC |
| **dziennik** | `gra/db/wpisy.jsonl` | to, co sie DOPISUJE: jedna linia = jedno zdarzenie (zrodlo, klucz, pole, seq, data, tresc) |
| *(pochodne)* | `gra/db/indeks.sqlite` | cache do szybkich zapytan, w .gitignore, odbudowywany przez `stan.py` |

## JAK DOPISAC ZDARZENIE — NIE przepisuj wielkich plikow

```
python3 -c "import sys; sys.path.insert(0,'gra'); import db; db.dopisz('watki','<klucz>','RRR-MM-DD','<tresc>')"
```

Zrodla: `watki` · `npc` (klucz = `sekcja/id`, np. `na_scenie/bran_tragarz`) · `swiat` · `postac`.
`db.dopisz` sam podbija licznik `_dziennik_<pole>` w pliku metadanych i **zaklada watek, jesli go nie bylo**.

**Metadane (status, termin, priorytet, kasa, sytosc, zmeczenie) edytuje sie w JSON jak dotad** — sa male i diffowalne.

## JAK CZYTAC

```
python3 gra/db.py pokaz <klucz> [ile]     ostatnie wpisy watku/NPC
python3 gra/db.py szukaj <fraza> [ile]    pelnotekstowo po calym dzienniku
python3 gra/db.py dzien 299-09-11         wszystko z jednego dnia
python3 gra/db.py otwarte                 watki nierozstrzygniete
```

> **STAN.md jest INDEKSEM, nie archiwum.** Nie ma w nim historii — jest w dzienniku.
> Zanim napiszesz "nikt tego nie robil" albo "tej sprawy nie bylo" — **`db.py szukaj`**. To jest ta sama zasada, co zawsze, tylko teraz tania.

## ODWRACALNOSC

Migracja byla **bajtowo odwracalna** i zweryfikowana: 1092 dzienniki, 0 roznic wobec kopii sprzed zmiany.
`db.zlacz(klucz, pole)` odtwarza dowolny dziennik w dawnej postaci (sklejony `||`).
Punkt powrotu: tag gita **`przed-refaktorem-299-09-11`**.

## UWAGA O KLUCZACH

| zrodlo | klucz | pole |
|---|---|---|
| `watki` | id watku | `nota` (domyslne) |
| `npc` | `sekcja/id`, np. `na_scenie/bran_tragarz` | `nota` |
| `swiat` | `swiat` | **nazwa zdarzenia**, np. `inbound_299_09_11` |
| `postac` | `postac` | **nazwa dzialu**, np. `wiedza` |

Czyli dla swiata i postaci **pole niesie nazwe**, a klucz jest staly:
```
db.dopisz('swiat','swiat','299-09-12','tresc...', pole='inbound_299_09_12')
```

## FAKTY STALE, KTORYCH NIE WOLNO WYMYSLAC OD NOWA (299-09-16)

- **CYTADELA POLNOCY NAZYWA SIE GLEBOKORZEN.** Glowa: maester THEOMORE. Kolebka (siedziba tymczasowa): Nowy Zamek, Bialy Port. Czardrzewo zamiast septu. Misja zalozycielska: agronomia chlodu (299-08-15). Pierwsze zlecenie Korony: pomiar Przesmyku. Oderwanie od Cytadeli w Starym Miescie jest CELEM, nie skutkiem ubocznym (299-09-10). Nie tworzyc dla niej nowych nazw ("Straznica Zimy", "Kolegium Polnocy" — nadpisane/odrzucone).
- **GWARDIA KROLEWSKA NAZYWA SIE ZIMOWA STRAZ** (karta 299-08-12). Chroni KROLA I RODZINE, zawsze, bez wyjatkow. Pierwszy Miecz: RODRIK CASSEL, zastepca ser ALYN.
- **MISTRZ NAUKI = maester LUWIN** (od 299-09-16); licencje na nauczanie wydaje od 299-09-10 reka Luwina i pieczecia Korony, bez Cytadeli.
- **SYSTEM OSWIATY: piec wezlow** (299-06-12, z pozniejszymi poprawkami): Winterfell, Przystan Wilka, Starkport, Bialy Port, Karhold. Szkoly powszechne: Winterfell (prototyp), Fosa Cailin (#2), Bialy Port (#3).
