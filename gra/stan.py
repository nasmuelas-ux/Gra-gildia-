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

o = []
A = o.append

A("# STAN GRY — indeks (regenerowany z JSON+JSONL, NIE edytuj recznie)")
A("_Zrodlo prawdy: gra/*.json + gra/db/wpisy.jsonl. Szczegoly: `python3 gra/db.py pokaz <klucz>` / `szukaj <fraza>` / `dzien <data>`._\n")

A("## ⚠️ OBOWIAZKOWA RAMA RANKA (nie pomijac po kompaktowaniu!)\n"
  "Kazdy RANEK renderuj W TEJ KOLEJNOSCI, ZAWSZE:\n"
  "1. Naglowek daty + pogoda/zdarzenie\n"
  "2. Kalendarz (targ/swieto/clo)\n"
  "3. **📬 WIADOMOSCI / KORESPONDENCJA** — osobna ramka: kto sie odezwal/przyslal poslanca/jaka wiesc/co dojrzalo (rzut na inbound); jak nic → napisz \"cisza\". TO NIE JEST NA ZADANIE — renderuj SAM co ranek.\n"
  "4. STATUS: jedzenie (sytosc/zmeczenie/zdrowie) + hajs (wolne + skrot)\n"
  "5. Watki w toku → pytanie \"co robisz\" (bez listy opcji)\n")

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
