#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator STAN.md — ZWIEZLY INDEKS stanu gry, nie archiwum.

Zasada: STAN.md ma miescic sie w kilku tysiacach tokenow i odpowiadac na pytania
"co teraz, co otwarte, co dojrzewa, ile mam pieniedzy". SZCZEGOLY dociaga sie
na zadanie z dziennika:

    python3 gra/db.py pokaz <klucz>     ostatnie wpisy watku
    python3 gra/db.py szukaj <fraza>    pelnotekstowo
    python3 gra/db.py dzien 299-09-11   wszystko z dnia

Zrodlo prawdy = gra/*.json + gra/db/wpisy.jsonl. NIGDY pamiec rozmowy.
Uruchom: python3 gra/stan.py
"""
import json, os, io

D = os.path.dirname(os.path.abspath(__file__))
ZAMKNIETE = ("zrealizowany", "rozstrzygniete", "zamkniete", "uniewazniony", "void")
LIMIT_WATKOW = 45
LIMIT_WPISOW_DZIENNYCH = 12


def L(f):
    try:
        with io.open(os.path.join(D, f), encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def skrot(t, n=150):
    t = " ".join(str(t).split())
    return t if len(t) <= n else t[:n] + "…"


p, s, z = L("postac.json"), L("swiat.json"), L("zegary.json")
npc, wa = L("npc.json"), L("watki.json")

d = s.get("data", {})
data_txt = "%s-%02d-%02d %s" % (d.get("rok", "?"), d.get("miesiac", 0),
                                d.get("dzien", 0), s.get("pora", "?"))


# ---------- STARZENIE (wiek liczony z kalendarza; wszyscy starzeja sie sami) ----------
def _wiek(rok, mies, dzien, rok_ur, data_ur):
    if rok_ur is None or not isinstance(rok, int):
        return None
    w = rok - rok_ur
    if data_ur:
        bm, bd = data_ur.get("miesiac"), data_ur.get("dzien")
        if bm is not None and bd is not None and isinstance(mies, int) and isinstance(dzien, int):
            if (mies, dzien) < (bm, bd):
                w -= 1
    return w


_r, _m, _dz = d.get("rok"), d.get("miesiac"), d.get("dzien")
_nw = _wiek(_r, _m, _dz, p.get("rok_urodzenia"), p.get("data_urodzin"))
if _nw is not None and _nw != p.get("wiek"):
    p["wiek"] = _nw
    with io.open(os.path.join(D, "postac.json"), "w", encoding="utf-8") as f:
        json.dump(p, f, ensure_ascii=False, indent=1)
_ch = False
for _sekcja in ("na_scenie", "w_orbicie", "orbita"):
    for _x in (npc.get(_sekcja) or []):
        if isinstance(_x, dict) and _x.get("rok_urodzenia") is not None:
            _w = _wiek(_r, _m, _dz, _x.get("rok_urodzenia"), _x.get("data_urodzin"))
            if _w is not None and _w != _x.get("wiek"):
                _x["wiek"], _ch = _w, True
if _ch:
    with io.open(os.path.join(D, "npc.json"), "w", encoding="utf-8") as f:
        json.dump(npc, f, ensure_ascii=False, indent=1)

def _wczytaj(nazwa):
    sc = os.path.join(D, nazwa)
    if not os.path.exists(sc):
        return None
    with io.open(sc, encoding="utf-8") as f:
        return json.load(f)

TERMINY = _wczytaj("terminy.json")
OBSADA = _wczytaj("obsada.json")

o = []
A = o.append

A("# STAN GRY — indeks (regenerowany z JSON+JSONL, NIE edytuj recznie)")
A("_Zrodlo prawdy: gra/*.json + gra/db/wpisy.jsonl. Szczegoly: `python3 gra/db.py pokaz <klucz>` / `szukaj <fraza>` / `dzien <data>`._\n")

A("## ⚠️ 38 ZASAD SILNIKA — `gra/PROWADZENIE.md`, sekcja od \"TRZYDZIESCI PIEC ZASAD\"\n"
  "**PRZECZYTAJ JE PO KAZDYM KOMPAKTOWANIU.** Przy sprzecznosci z czymkolwiek innym — tamte wygrywaja.\n"
  "Skrot najczesciej lamanych: **1** nie twierdze, nie sprawdziwszy · **3** blad GM nie przechodzi na gracza (VOID znaczy VOID) ·\n"
  "**7** moja cisza nie jest zastojem (rzecz zlecona i obsadzona idzie sama) · **8** postep rodzi problemy, nie wstazki ·\n"
  "**12** kryterium to OBSADZENIE, nie nazwisko · **22** prerogatywa nie idzie pod glosy · **27** jeden rzut na sprawe albo zero ·\n"
  "**31** nie pisze mysli gracza, nie zamieniam rozmowy w akt, nie posuwam czasu w rozmowie · **34** bez kanalu nie ma wiadomosci.\n"
  "### **36 - DWA POZIOMY:** SPRAWA zyje latami i NIE ma sie zamykac (filar) · OPERACJA ma dzien, cel i spust, i MUSI sie zamknac.\n"
  "Test: czy to moze sie skonczyc konkretnego dnia? Meldunek idzie z poziomu OPERACJI - filary stoja, melduje sie to, co sie pod nimi rusza.\n"
  "**ALARM: sprawa zywa, pod ktora nie ma ANI JEDNEJ otwartej operacji** - to nie brak postepu, to ja nie otworzylem nastepnego kroku.\n"
  "### **37 - SZUKA SIE W DWOCH KSIEGACH, NIGDY W JEDNEJ** (stala, 300-03-03).\n"
  "Przed obsadzeniem KAZDEGO krzesla i przed powiedzeniem, ze kogos NIE MA, czyta sie OBA spisy Fosy:\n"
  "**(1) SPIS MIESZKANCOW 299-06 - 640 dusz IMIENNIE**, zawod = co umie rekami, trzy osobne rubryki CZYTA/PISZE/LICZY,\n"
  "dzieci z imienia, wiekiem i rodzicem (takze dziewczeta) - obejmuje ludnosc SPRZED przybycia czterystu;\n"
  "**(2) REJESTR DNIOWEK MELLI od 300-02-28** - czterystu przybyszow, kolumna CO UMIE, wpis imieniem ALBO znakiem,\n"
  "plus ksiega bramy od 02-12. **Zaden nie pokrywa calosci - dlatego zawsze oba.**\n"
  "### **38 - OBSADY I TERMINOW NIE PODAJE SIE Z PAMIECI** (stala, 300-03-03).\n"
  "Sa DANYMI: `gra/obsada.json` i `gra/terminy.json`, oba renderowane nizej w tym pliku.\n"
  "**Kazde nadanie, kazdy wakat i kazdy termin dopisuje sie TAM w tej samej turze, w ktorej padl.**\n"
  "**Termin bez zapisanego ZAMKNIECIA nie jest terminem - tylko data, ktora minie.**\n")

if TERMINY:
    A("## 📅 TERMINY — `gra/terminy.json` (JEDYNE ZRODLO; kalendarz ranka generuj STAD, nie z pamieci)")
    A("_Kazda pozycja: co · kto · czym sie ZAMYKA. Termin bez zamkniecia tylko mija._\n")
    _ot = [t for t in TERMINY.get("terminy", []) if not str(t.get("status", "")).startswith("zrobione")]
    _zr = [t for t in TERMINY.get("terminy", []) if str(t.get("status", "")).startswith("zrobione")]
    for t in _ot:
        _st = t.get("status", "")
        _m = " **⚠ " + _st.upper() + "**" if _st and _st != "otwarte" else ""
        A("- **%s** — %s · _kto:_ **%s** · _zamyka:_ %s%s" % (
            t.get("data", "?"), t.get("co", "?"), t.get("kto", "?"), t.get("zamyka", "?"), _m))
    if _zr:
        A("\n_Zamkniete ostatnio:_ " + " · ".join("%s (%s)" % (t.get("co", "?")[:60], t.get("status")) for t in _zr))
    A("")

if OBSADA:
    A("## 👤 OBSADA — `gra/obsada.json` (NIE PODAWAC OBSADY Z PAMIECI — CZYTAC STAD)")
    for _drab, _tresc in (OBSADA.get("drabiny") or {}).items():
        _kasa = _tresc.get("_kasa", "")
        _nota = _tresc.get("_nota", "")
        A("### %s%s" % (_drab, (" — _%s_" % _kasa) if _kasa else ""))
        if _nota:
            A("_%s_" % _nota)
        for _urz, _d in _tresc.items():
            if _urz.startswith("_"):
                continue
            _kto = _d.get("kto") or "### PUSTE"
            A("- **%s:** %s%s" % (_urz, _kto, (" _(%s)_" % _d["nota"]) if _d.get("nota") else ""))
        A("")
    _sd = OBSADA.get("struktura_dworu") or {}
    if _sd:
        A("### 🏛️ PIEC DEPARTAMENTOW (schemat dworu — urzad → kto go faktycznie robi)")
        for _dep, _poz in _sd.items():
            if _dep.startswith("_"):
                continue
            A("**%s**" % _dep)
            for _u, _op in _poz.items():
                A("- **%s** — %s" % (_u, _op))
        A("")
    _wak = OBSADA.get("wakaty") or []
    if _wak:
        A("### 🔴 WAKATY (%d)" % len(_wak))
        for _w in _wak:
            _p = " **%s**" % _w["pilnosc"] if _w.get("pilnosc") else ""
            A("- **%s** _(%s)_%s — %s" % (_w.get("urzad", "?"), _w.get("drabina", "?"), _p, _w.get("nota", "")))
        A("")

A("## ⚠️ OBOWIAZKOWA RAMA RANKA (nie pomijac po kompaktowaniu!)\n"
  "Kazdy RANEK renderuj W TEJ KOLEJNOSCI, ZAWSZE:\n"
  "1. **DATA + POGODA** — pogoda ma niesc skutek, nie ozdobe.\n"
  "2. **KALENDARZ** — najblizsze terminy (patrz blok TERMINY nizej).\n"
  "3. **📬 KORESPONDENCJA — TRZY RZECZY**, renderuj SAM, nie na zadanie:\n"
  "   - CO PRZYSZLO Z ZEWNATRZ — rzut na inbound, losowany **Z LISTY \"CO SLEDZIMY\"** (gra/KSIEGA_ZOBOWIAZAN.md, sekcja III), NIE z powietrza. Podaj KANAL (zasada 34).\n"
  "   - CO SAMO DOJRZALO — meldunki ludzi i urzedow, ktorym cos zlecono. **BEZ RZUTU** (zasada 7). Forma z zasady 8: co zrobione / na czym utknal / ile kosztowalo / czego chce ode mnie.\n"
  "   - CISZA JEST PRAWDZIWA W DRODZE (zasada 11). Jak nic nie przyszlo → napisz \"cisza\".\n"
  "4. **STATUS** — sytosc/zmeczenie/zdrowie + kasa (wolne + skrot).\n"
  "5. **🧵 WATKI — MAKSIMUM TRZY LINIE, TYLKO WYJATKI:** ZAPADA DZIS · SPOZNIONE (ile dni) · BEZ TERMINU albo PUSTE KRZESLO.\n"
  "   Potem \"co robisz?\" — bez listy opcji.\n\n"
  "**DZIEN BILANSU (1. dnia miesiaca)** ma stala zawartosc: kasa · daniny · **MELDUNKI BUDOW wedle zasady 33**\n"
  "(ile stoi · ilu ludzi · co ich zatrzymuje · czego potrzebuja z zewnatrz), po jednym akapicie z kazdego miejsca.\n")

A("## ⚠️ ZAPIS STANU — NOWY TRYB (od 299-09-11)\n"
  "NIE przepisuj wielkich JSON-ow. Dopisuj JEDNA LINIE do dziennika:\n"
  "```\n"
  "python3 -c \"import sys; sys.path.insert(0,'gra'); import db; db.dopisz('watki','<klucz>','RRR-MM-DD','<tresc>')\"\n"
  "```\n"
  "Zrodla: `watki` · `npc` (klucz = `sekcja/id`) · `swiat` · `postac`. Metadane (status, termin, kasa, sytosc) edytuje sie w JSON jak dotad.\n")

A("## TERAZ")
A("- **Data:** %s · %s" % (data_txt, s.get("sezon", "")))
A("- **Miejsce:** %s" % skrot(s.get("lokacja", "?"), 120))
A("- **Postac:** %s %s, l.%s — %s" % (p.get("imie", "?"), p.get("przydomek", ""),
                                      p.get("wiek", "?"), skrot(p.get("nazwisko", ""), 110)))
A("- **Zdrowie %s · Sytosc %s · Zmeczenie %s**" % (p.get("zdrowie", "?"),
                                                   p.get("sytosc", "?"), p.get("zmeczenie", "?")))

sk = p.get("sakiewka", {})
A("\n## KASA (1 jelen=100 mied · 1 smok=200 jel)")
A("- **Wolne:** %s smokow + %s jeleni + %s mied" % (sk.get("smoki", 0),
                                                    sk.get("jelenie", 0), sk.get("miedziaki", 0)))
prz = p.get("przychody", {})
if prz:
    A("- **Dzien Bilansu:** %s · nastepny %s" % (prz.get("dzien_bilansu", "?"),
                                                 prz.get("nastepny_bilans", "?")))

um = p.get("umiejetnosci", {})
if um:
    A("\n## UMIEJETNOSCI\n" + " · ".join("%s %s" % (k, v) for k, v in um.items()))
rep = p.get("reputacja", {})
if rep:
    A("**Reputacja:** " + " · ".join("%s %s" % (k, v) for k, v in rep.items()))

# --- KTO CZYJ JEST + TERMINY (dodane 300-02-25, po pomyleniu watkow przez GM) ---
lud = L("ludzie.json") or {}
if lud:
    A("\n## ⚠️ PUDELKA — pelna tabela w gra/ludzie.json; tu tylko WYJATKI")
    niepewni = []
    for box in ("DOM_TALLY", "LENNO_FOSY", "KORONA"):
        for osoba in ((lud.get(box) or {}).get("ludzie") or []):
            if osoba.get("pewne") is False:
                niepewni.append("%s (%s)" % (osoba.get("imie","?"), box))
    if niepewni:
        A("- ### `?` NIEPEWNE — NIE WKLADAC W USTA, PYTAC: " + " · ".join(niepewni))
    for sz in (lud.get("SZWY") or []):
        A("- ### SZEW: **%s** — %s" % (sz.get("kto","?"), skrot(sz.get("opis",""), 150)))

spr = L("sprawy.json") or {}
if spr:
    A("\n## 🧩 SPRAWY SIE PRZEPLATAJA — CZYSTE MA BYC ROZSTRZYGNIECIE, NIE SPRAWA")
    A("_" + spr.get("_zasada_glowna","") + "_")
    A("### " + spr.get("_szew_glowny",""))
    A("**Zamiast odsylac NPC, GM pyta:** " + " · ".join(spr.get("pytania_ktore_gm_ma_zadac_zamiast_odsylac", [])))
    A("_(pelna lista spraw: gra/sprawy.json)_")


try:
    kz = io.open(os.path.join(D, "KSIEGA_ZOBOWIAZAN.md"), encoding="utf-8").read()
    MARK = ("SPOZNIONE", "SPÓŹNIONE", "BEZ TERMINU", "BEZ DATY", "PUSTY",
            "CISZA OD", "BEZ KANALU", "BEZ KANAŁU", "BEZ RUCHU", "PO TERMINIE",
            "ANI JEDNEJ DROGI", "NIE MA GO WCALE")
    wyj = [l.strip() for l in kz.splitlines()
           if l.strip().startswith("|") and any(m in l.upper() for m in MARK)]
    if wyj:
        A("\n## 🧵 KSIEGA ZOBOWIAZAN — SAME WYJATKI (pelna: gra/KSIEGA_ZOBOWIAZAN.md)")
        for l in wyj[:14]:
            A(l)
except Exception:
    pass



ter = L("terminy.json") or {}
if ter.get("terminy"):
    A("\n## ⏳ TERMINY Z DATA")
    for t in ter["terminy"]:
        A("- **%s** — %s%s" % (t.get("data","?"), t.get("co","?"),
            ("  _(" + t["gdzie"] + ")_") if t.get("gdzie") else ""))
A("\n## LUDZIE NA SCENIE")
for x in (npc.get("na_scenie") or []):
    if isinstance(x, dict):
        A("- **%s** (`%s`) — %s · nast %s" % (x.get("imie", "?"), x.get("id", ""),
                                              skrot(x.get("zawod", ""), 55),
                                              x.get("nastawienie_do_gracza", "?")))

zeg = z.get("zegary") or []
if zeg:
    A("\n## ZEGARY")
    for c in zeg:
        mk = "⚠" if c.get("typ") == "zagrozenie" else "◆"
        A("- %s `%s` %s: %s" % (mk, c.get("odlicza_do", "?"), c.get("id", ""),
                                skrot(c.get("opis", ""), 95)))

otw = [x for x in (wa.get("watki") or [])
       if isinstance(x, dict)
       and not any(k in str(x.get("status", "")).lower() for k in ZAMKNIETE)]
A("\n## WATKI OTWARTE (%d; ostatnie %d — pelna lista: `python3 gra/db.py otwarte`)"
  % (len(otw), min(LIMIT_WATKOW, len(otw))))
for x in otw[-LIMIT_WATKOW:]:
    term = " · termin %s" % x["termin"] if x.get("termin") else ""
    A("- `%s` [%s]%s %s" % (x.get("id", "?"), x.get("status", "?"), term,
                            skrot(x.get("tytul") or "", 110)))

# ostatnie wpisy dziennika — pamiec krotka, zeby po kompaktowaniu bylo od czego zaczac
try:
    import sys
    sys.path.insert(0, D)
    import db as _db
    ost = _db.czytaj_wpisy()[-LIMIT_WPISOW_DZIENNYCH:]
    if ost:
        A("\n## OSTATNIE WPISY DZIENNIKA")
        for w in ost:
            A("- [%s] `%s`: %s" % (w.get("data"), w["klucz"], skrot(w["tresc"], 190)))
    _db.zbuduj_indeks()
except Exception as e:
    A("\n_(dziennik niedostepny: %s)_" % e)

with io.open(os.path.join(D, "STAN.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(o) + "\n")
print("STAN.md zregenerowany:", data_txt)
