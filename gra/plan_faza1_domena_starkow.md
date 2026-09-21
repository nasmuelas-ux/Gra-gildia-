# PLAN FAZA I — ROZWÓJ DOMENY STARKÓW
### Koncepcja Symona Tally, Namiestnika — 299-06-23, Fosa Cailin

> **DOKTRYNA NACZELNA: DOMENA NAJPIERW.**
> Najpierw musi urosnąć sam środek — domena Starków (Winterfell, Wintertown, ziemie własne Korony). Dopiero potem odważniej zmieniamy całość.
> **Dlaczego to rozwiązuje trzy ściany, o które rozbiła się stała armia:**
> - **Pieniądz:** rośnie dochód Korony we własnej domenie, zanim wydamy na wojsko/reformy całości.
> - **Lordowie:** nie narzucamy nic autonomicznym panom — pilotujemy u siebie. Dowodzimy **przykładem, nie dekretem**. Pan, który widzi syty, bogaty Winterfell, prosi o wzór; pan, któremu się go narzuca, sięga po żal (linia Boltona).
> - **Kultura:** pilot, nie rozkaz. Północ przyjmuje to, co widziała, że działa.
> **Cel Fazy I:** domena Starków widocznie silniejsza, syta przez zimę, lepiej rządzona = **DOWÓD**, który czyni Fazę II (całe królestwo) mile widzianą, nie budzącą strachu.

---

## 1. SZKLARNIE I PRODUKCJA ŻYWNOŚCI  `[buduj — atut unikalny]`
- **Co:** rozwinąć i powielić szklane ogrody Winterfell (grzane gorącymi źródłami — atut, jakiego nie ma nikt inny), maksymalizować produkcję żywności rosnącej mimo mrozu.
- **Już zasiane:** wątek `szklane_ogrody_model_zimy_299_06`.
- **Zależność:** **szkło** (drogie, sprowadzane) — potrzebny własny hutnik szkła (Myr przez kanały Braavos/Nesty/Willi) albo domenowa huta. Bez taniego szkła model się nie skaluje.
- **Sens:** udowodnić, że domena wyżywi się sama przez zimę → wzór dla całej Północy.

## 1b. PRZECHOWYWANIE ŻYWNOŚCI  `[natychmiast — tanie, bez tarcia]`
- **Co:** spichlerze, piwnice, solenie/wędzenie/suszenie, **lodownie** (Północ ma chłód za darmo — magazynować lód/mróz), walka ze zgnilizną i szkodnikiem.
- **Sens:** zimę przeżywa się z tego, co **zmagazynowane**, nie tylko z tego, co urośnie. Instynkt rachmistrza. Tanie, ogromny skutek, zero oporu politycznego.
- **Kolejność:** **fundament — robić od zaraz**, równolegle ze szklarniami.

## 2. KADRY I EDUKACJA  `[natychmiast — kręgosłup wszystkiego]`
- **Co:** poszerzyć potok piśmiennych/liczących urzędników, własnych maesterów (przejście z Cytadeli + hodować własnych), węzły oświaty.
- **Już zasiane:** `budowa_panstwa_maesterowie_wlasna_zdolnosc`, `system_oswiaty_polnocy_struktura` (5 węzłów), szkoła-prototyp w Winterfell (Luwin/Bran/doktryna lowbornów Miry).
- **Sens:** **bez kadry nic nie ruszy** — spichlerza, mennicy, rolek musteru, przywilejów miejskich nie poprowadzą analfabeci. To backbone, który uruchamia wszystkie pozostałe punkty.
- **Kolejność:** tor równoległy **od pierwszego dnia**.

## 3. TEST MIAST WOLNYCH + PRAWO AZYLU (w domenie Starków)  `[buduj — pilot]`
- **Co:** pilotaż modelu wolnego miasta na wzór Essos w JEDNYM mieście domeny (**Wintertown** — pod okiem Winterfell): karta/przywileje, samorząd, **prawo azylu** dla uczonych/rzemieślników, wolne enklawy.
- **Już zasiane:** `przywileje_miejskie_silnik_monety`, `prawo_azylu_uczonego_wolne_enklawy`, `polnocny_porzadek_uczonosci`.
- **Sens:** pilot w domenie = niskie ryzyko, dowodzi modelu i **ściąga talent** (azyl wabi uczonych/rzemieślników z Cytadeli i Essos), zanim zaoferujemy karty miastom lordów. Miasto = silnik monety, handlu, podatku.
- **Kolejność:** gdy baza (żywność+kadra) rośnie; azyl można ogłosić wcześnie (tani magnes).

## 4. PIERWSZA DRUŻYNA 1000 + SYSTEM MOBILIZACJI  `[gdy baza urośnie — po dochodzie]`
- **Co:** **1 tys.** zawodowej drużyny Korony (kręgosłup, wierny tylko Koronie, zawsze gotów) + **rolki musteru** i wyszkolona rezerwa (broń w składach, ujednolicone szkolenie) = szybkość i jakość bez ruinującego stałego kosztu.
- **Już zasiane:** `stala_armia_koronna_koncepcja` (1k zamiast 2-3k = wypłacalny kręgosłup), `rana_manpower_polnocy`.
- **Sens:** ostrze i przeciwwaga; oprawić jako tarczę wspólnego (brzeg vs żelaźni, zima/Mur, straż prawa), nie zaciskanie pięści. Dowództwo wg doktryny Marszałka (przysięga Koronie, rotacja, żaden pojedynczy lord).
- **Kolejność:** **dopiero po dochodzie**, który go utrzyma (nieopłacona drużyna = bunt). Ostatni punkt Fazy I.

## 5. REFORMY GOSPODARCZE — MONETA I MIARA  `[miara od zaraz; moneta gdy kruszec]`
- **Miara** `[natychmiast, tanie, bez tarcia]`: ujednolicone wagi i miary. Standard = zaufanie w handlu = kwitnący handel = rosnąca baza podatkowa. Reforma rachmistrza; **wszystkim pomaga**, więc politycznie łatwa. Pilotować w domenie, rozejdzie się przez naśladownictwo.
- **Moneta** `[buduj — gdy kruszec/mennica]`: własna moneta, przebicie. Zależy od `strategia_kruszcu_mennica` (zarobić srebro handlem + zwiad rud, BEZ długu u banku). Robb: „gdy będziesz miał pierwszych własnych piszących służących Północy — wybijemy razem pierwszą monetę".
- **Sens:** miara i moneta to układ krwionośny gospodarki, z której wszystko inne (armia, szkoły, relief) czerpie.

---

## SEKWENCJA WEWNĄTRZ FAZY I
1. **OD ZARAZ (tanie, bez tarcia, wszystko uruchamiają):** przechowywanie żywności (1b) · standardowa miara (5) · potok kadr/azyl (2 + magnes azylu z 3).
2. **BUDUJ (wymaga nakładu/umiejętności):** szklarnie+huta szkła (1) · moneta/mennica (5) · pilot wolnego miasta w Wintertown (3).
3. **GDY BAZA URasta (wymaga dochodu):** drużyna 1k + system musteru (4).

**→ Rezultat:** domena Starków syta, bogatsza, piśmienna, z pierwszym własnym miastem i pierwszą własną drużyną = żywy dowód. **Wtedy** Faza II: te wzory na całe królestwo — proszone, nie narzucone.

*Koncepcja do przedłożenia Robbowi (domena = jego własna) i radzie; zgodna z jego kompasem: wolność trwała, lud przez zimę, sprawiedliwość, wataha cała.*
