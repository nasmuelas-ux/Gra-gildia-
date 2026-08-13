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
