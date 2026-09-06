#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BAZA STANU GRY — czytanie i dopisywanie.

ZRODLO PRAWDY = tekst:
  gra/*.json           metadana (watki, npc, postac, swiat) — male, diffowalne
  gra/db/wpisy.jsonl   dziennik zdarzen, jedna linia = jeden wpis, TYLKO DOPISYWANY
  gra/db/indeks.sqlite POCHODNY indeks do szybkich zapytan — kasowalny, odbudowywalny

UZYCIE Z LINII POLECEN
  python3 gra/db.py pokaz <klucz> [ile]      ostatnie wpisy watku/npc (domyslnie 5)
  python3 gra/db.py szukaj <fraza> [ile]     pelnotekstowo po calym dzienniku
  python3 gra/db.py otwarte [ile]            watki nierozstrzygniete
  python3 gra/db.py dzien <RRR-MM-DD>        wszystko z danego dnia
  python3 gra/db.py indeks                   przebuduj indeks SQLite
  python3 gra/db.py dopisz <zrodlo> <klucz> <data> <tresc>

UZYCIE Z PYTHONA
  import db; db.dopisz("watki", "ucho_korony_druga_siatka_299_09", "299-09-12", "...")
"""
import json, os, sys, io, sqlite3

D = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(D, "db")
WPISY = os.path.join(DB, "wpisy.jsonl")
INDEKS = os.path.join(DB, "indeks.sqlite")
ZAMKNIETE = ("zrealizowany", "rozstrzygniete", "zamkniete", "uniewazniony", "void")


# ---------------------------------------------------------------- odczyt

def czytaj_wpisy():
    if not os.path.exists(WPISY):
        return []
    out = []
    with io.open(WPISY, encoding="utf-8") as f:
        for linia in f:
            linia = linia.strip()
            if linia:
                out.append(json.loads(linia))
    return out


def wpisy(klucz=None, zrodlo=None, pole=None, data=None, szukaj=None, ile=None):
    """Filtruje dziennik. Zwraca liste wpisow w kolejnosci zapisu."""
    out = []
    for w in czytaj_wpisy():
        if klucz and klucz not in w["klucz"]:
            continue
        if zrodlo and w["zrodlo"] != zrodlo:
            continue
        if pole and w["pole"] != pole:
            continue
        if data and w.get("data") != data:
            continue
        if szukaj and szukaj.lower() not in w["tresc"].lower():
            continue
        out.append(w)
    return out[-ile:] if ile else out


def zlacz(klucz, pole="nota"):
    """Odtwarza pelny dziennik jako jeden string (jak przed migracja)."""
    cz = [w for w in czytaj_wpisy() if w["klucz"] == klucz and w["pole"] == pole]
    return "||".join(w["tresc"] for w in sorted(cz, key=lambda x: x["seq"]))


def watki(otwarte_tylko=False):
    with io.open(os.path.join(D, "watki.json"), encoding="utf-8") as f:
        w = json.load(f).get("watki", [])
    if otwarte_tylko:
        w = [x for x in w if not any(z in str(x.get("status", "")).lower() for z in ZAMKNIETE)]
    return w


# ---------------------------------------------------------------- zapis

def dopisz(zrodlo, klucz, data, tresc, pole="nota"):
    """Dopisuje JEDNA LINIE do dziennika. Nie przepisuje zadnego duzego pliku."""
    ile = len([w for w in czytaj_wpisy() if w["klucz"] == klucz and w["pole"] == pole])
    rek = {"zrodlo": zrodlo, "klucz": klucz, "pole": pole,
           "seq": ile, "data": data, "tresc": tresc}
    os.makedirs(DB, exist_ok=True)
    with io.open(WPISY, "a", encoding="utf-8") as f:
        f.write(json.dumps(rek, ensure_ascii=False) + "\n")
    _podbij_licznik(zrodlo, klucz, pole)
    return rek


def _podbij_licznik(zrodlo, klucz, pole):
    """Utrzymuje '_dziennik_<pole>' w pliku metadanych, zeby liczby sie zgadzaly."""
    plik = {"watki": "watki.json", "npc": "npc.json",
            "swiat": "swiat.json", "postac": "postac.json"}.get(zrodlo)
    if not plik:
        return
    sciezka = os.path.join(D, plik)
    with io.open(sciezka, encoding="utf-8") as f:
        dane = json.load(f)
    znacznik = "_dziennik_" + pole
    trafiony = False
    if zrodlo == "watki":
        for rek in dane.get("watki", []):
            if rek.get("id") == klucz:
                rek[znacznik] = rek.get(znacznik, 0) + 1
                trafiony = True
        if not trafiony:
            dane.setdefault("watki", []).append(
                {"id": klucz, "status": "otwarty", znacznik: 1})
            trafiony = True
    elif zrodlo in ("swiat", "postac"):
        dane[znacznik] = dane.get(znacznik, 0) + 1
        trafiony = True
    else:  # npc — klucz ma postac "sekcja/id"
        sekcja, _, nid = klucz.partition("/")
        for rek in (dane.get(sekcja) or []):
            if isinstance(rek, dict) and (rek.get("id") == nid or rek.get("imie") == nid):
                rek[znacznik] = rek.get(znacznik, 0) + 1
                trafiony = True
    if trafiony:
        with io.open(sciezka, "w", encoding="utf-8") as f:
            json.dump(dane, f, ensure_ascii=False, indent=1)


# ---------------------------------------------------------------- indeks

def zbuduj_indeks():
    """Buduje POCHODNY indeks SQLite z JSONL. Zawsze od zera — to tylko cache."""
    os.makedirs(DB, exist_ok=True)
    if os.path.exists(INDEKS):
        os.remove(INDEKS)
    con = sqlite3.connect(INDEKS)
    con.executescript("""
        CREATE TABLE wpis (zrodlo TEXT, klucz TEXT, pole TEXT, seq INT,
                           data TEXT, tresc TEXT);
        CREATE INDEX i_klucz ON wpis(klucz);
        CREATE INDEX i_data  ON wpis(data);
        CREATE VIRTUAL TABLE szukaj USING fts5(klucz, data, tresc);
        CREATE TABLE watek (id TEXT PRIMARY KEY, tytul TEXT, status TEXT,
                            priorytet TEXT, termin TEXT, wpisow INT);
    """)
    ws = czytaj_wpisy()
    con.executemany("INSERT INTO wpis VALUES (?,?,?,?,?,?)",
                    [(w["zrodlo"], w["klucz"], w["pole"], w["seq"],
                      w.get("data"), w["tresc"]) for w in ws])
    con.executemany("INSERT INTO szukaj VALUES (?,?,?)",
                    [(w["klucz"], w.get("data") or "", w["tresc"]) for w in ws])
    con.executemany("INSERT OR REPLACE INTO watek VALUES (?,?,?,?,?,?)",
                    [(x.get("id"), x.get("tytul"), x.get("status"),
                      str(x.get("priorytet") or ""), x.get("termin"),
                      sum(v for k, v in x.items()
                          if k.startswith("_dziennik_") and isinstance(v, int)))
                     for x in watki()])
    con.commit()
    con.close()
    return len(ws)


# ---------------------------------------------------------------- CLI

def _skrot(t, n=220):
    t = " ".join(t.split())
    return t if len(t) <= n else t[:n] + "…"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 0
    cmd = argv[1]
    if cmd == "pokaz":
        ile = int(argv[3]) if len(argv) > 3 else 5
        for w in wpisy(klucz=argv[2], ile=ile):
            print("[%s] %s/%s #%d\n   %s\n" % (w.get("data"), w["klucz"], w["pole"],
                                               w["seq"], _skrot(w["tresc"], 600)))
    elif cmd == "szukaj":
        ile = int(argv[3]) if len(argv) > 3 else 10
        for w in wpisy(szukaj=argv[2], ile=ile):
            print("[%s] %s: %s" % (w.get("data"), w["klucz"], _skrot(w["tresc"])))
    elif cmd == "dzien":
        for w in wpisy(data=argv[2]):
            print("[%s] %s: %s" % (w["data"], w["klucz"], _skrot(w["tresc"])))
    elif cmd == "otwarte":
        ile = int(argv[2]) if len(argv) > 2 else 40
        for x in watki(otwarte_tylko=True)[-ile:]:
            print("- %s [%s] %s" % (x.get("id"), x.get("status", "?"),
                                    _skrot(x.get("tytul") or "", 90)))
    elif cmd == "indeks":
        print("indeks zbudowany, wpisow: %d" % zbuduj_indeks())
    elif cmd == "dopisz":
        r = dopisz(argv[2], argv[3], argv[4], argv[5])
        print("dopisano #%d do %s" % (r["seq"], r["klucz"]))
    else:
        print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
