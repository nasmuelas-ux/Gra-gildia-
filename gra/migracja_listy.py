#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MIGRACJA II: dlugie LISTY STRINGOW (wie_o_graczu, wiedza, dobytek...) tez sa
dziennikami — kazdy element to osobny wpis. Wychodza do gra/db/wpisy.jsonl.

Odwracalne: lista odtwarza sie z wpisow po seq, element w element.
Uruchom:  python3 gra/migracja_listy.py [--zapisz]
"""
import json, os, re, sys, io

D = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(D, "db")
PROG = 8000                      # lista stringow wieksza niz to (znakow) = dziennik
DATA_RE = re.compile(r"^\s*(\d{3})-(\d{2})-(\d{2})")


def wczytaj(n):
    with io.open(os.path.join(D, n), encoding="utf-8") as f:
        return json.load(f)


def jest_dziennikiem(v):
    return (isinstance(v, list) and v
            and all(isinstance(x, str) for x in v)
            and sum(len(x) for x in v) > PROG)


def data_z(s, ost):
    m = DATA_RE.match(s)
    return "%s-%s-%s" % m.groups() if m else ost


def przetworz(obj, zrodlo, klucz, wpisy):
    """Zamienia listy-dzienniki w obiekcie na licznik. Zwraca liczbe zamian."""
    n = 0
    for pole in list(obj.keys()):
        v = obj[pole]
        if jest_dziennikiem(v):
            d = None
            for i, el in enumerate(v):
                d = data_z(el, d)
                wpisy.append({"zrodlo": zrodlo, "klucz": klucz, "pole": pole,
                              "seq": i, "data": d, "tresc": el, "lista": True})
            obj[pole] = {"_lista_w_dzienniku": len(v)}
            n += 1
    return n


def main():
    zapis = "--zapisz" in sys.argv
    wpisy, zamian = [], 0
    oryginaly = {}

    npc = wczytaj("npc.json")
    for sekcja, zaw in npc.items():
        if isinstance(zaw, list):
            for rek in zaw:
                if isinstance(rek, dict):
                    k = sekcja + "/" + (rek.get("id") or rek.get("imie") or "?")
                    for pole, v in rek.items():
                        if jest_dziennikiem(v):
                            oryginaly[("npc", k, pole)] = list(v)
                    zamian += przetworz(rek, "npc", k, wpisy)

    p = wczytaj("postac.json")
    for pole, v in p.items():
        if jest_dziennikiem(v):
            oryginaly[("postac", "postac", pole)] = list(v)
    zamian += przetworz(p, "postac", "postac", wpisy)

    # weryfikacja element-w-element
    buf = {}
    for w in wpisy:
        buf.setdefault((w["zrodlo"], w["klucz"], w["pole"]), []).append((w["seq"], w["tresc"]))
    bledy = [k for k, orig in oryginaly.items()
             if [t for _, t in sorted(buf.get(k, []))] != orig]

    print("list zamienionych: %d | wpisow: %d | bledow: %d" % (zamian, len(wpisy), len(bledy)))
    if bledy:
        for b in bledy[:5]:
            print("   BLAD:", b)
        return 1
    if not zapis:
        print("[test na sucho] OK. Uruchom z --zapisz.")
        return 0

    with io.open(os.path.join(DB, "wpisy.jsonl"), "a", encoding="utf-8") as f:
        for r in wpisy:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    for nazwa, dane in (("npc.json", npc), ("postac.json", p)):
        with io.open(os.path.join(D, nazwa), "w", encoding="utf-8") as f:
            json.dump(dane, f, ensure_ascii=False, indent=1)
    print("ZAPISANO.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
