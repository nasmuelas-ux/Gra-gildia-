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
