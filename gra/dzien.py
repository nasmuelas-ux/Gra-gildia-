#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Blok KALENDARZ + KOLEJKA INBOUND do ramy ranka (zasady 40 i 41).

Uruchamiac PRZED napisaniem ranka:   python3 gra/dzien.py
Zrodlo: gra/terminy.json + data z gra/swiat.json. NIGDY pamiec rozmowy.
"""
import json, os, io, re, sys

D = os.path.dirname(os.path.abspath(__file__))


def L(f):
    with io.open(os.path.join(D, f), encoding="utf-8") as fh:
        return json.load(fh)


def dni(r, m, d):
    return (r * 12 + m) * 30 + d


def parsuj(txt):
    m = re.search(r"(\d{3,4})-(\d{2})-(\d{2})", str(txt or ""))
    return (dni(int(m.group(1)), int(m.group(2)), int(m.group(3))), m.group(0)) if m else (None, None)


def skrot(t, n=115):
    t = " ".join(str(t).split())
    return t if len(t) <= n else t[:n] + "…"


def data_z(n):
    r, reszta = divmod(n, 360)
    m, dd = divmod(reszta, 30)
    if dd == 0:
        m, dd = m - 1, 30
    if m == 0:
        r, m = r - 1, 12
    return "%d-%02d-%02d" % (r, m, dd)


def wystapienia(c, do_dnia):
    """Daty PISANIA kolejnych meldunkow cyklicznych po 'ostatnio_odebrane', ktorych powrot <= do_dnia."""
    rytm, opozn = c.get("rytm", {}), int(c.get("opoznienie", 0))
    ost, _ = parsuj(c.get("ostatnio_odebrane"))
    wyn = []
    if "co_dni" in rytm:
        krok = int(rytm["co_dni"])
        n, _ = parsuj(rytm.get("start"))
        while n is not None and n + opozn <= do_dnia:
            if ost is None or n > ost:
                wyn.append(n)
            n += krok
    elif "dzien_miesiaca" in rytm:
        dm = int(rytm["dzien_miesiaca"])
        start = (ost if ost is not None else do_dnia - 60)
        r, reszta = divmod(start, 360)
        m = reszta // 30
        for k in range(0, 24):
            mm = m + k
            n = (r + (mm - 1) // 12) * 360 + (((mm - 1) % 12) + 1) * 30 + dm
            if n + opozn > do_dnia:
                break
            if (ost is None or n > ost):
                wyn.append(n)
    return wyn


# --- tryb: python3 gra/dzien.py odebrane <id> <data_pisania> ---
if len(sys.argv) >= 4 and sys.argv[1] == "odebrane":
    sciezka = os.path.join(D, "terminy.json")
    with io.open(sciezka, encoding="utf-8") as fh:
        TT = json.load(fh)
    for c in TT.get("cykliczne", []):
        if c.get("id") == sys.argv[2]:
            c["ostatnio_odebrane"] = sys.argv[3]
            break
    else:
        sys.exit("brak cyklicznego o id %s" % sys.argv[2])
    with io.open(sciezka, "w", encoding="utf-8") as fh:
        json.dump(TT, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("%s: ostatnio_odebrane = %s" % (sys.argv[2], sys.argv[3]))
    sys.exit(0)

s, T = L("swiat.json"), L("terminy.json")
d = s.get("data", {})
DZIS = dni(d.get("rok") or 0, d.get("miesiac") or 0, d.get("dzien") or 0)
HORYZONT = int(sys.argv[1]) if len(sys.argv) > 1 else 3

zal, dzis, blisko, bez = [], [], [], []
for t in T.get("terminy", []):
    if "otwarte" not in (t.get("status") or "").lower():
        continue
    n, _ = parsuj(t.get("wraca"))
    if n is None:
        bez.append(t)
    elif n < DZIS:
        zal.append((DZIS - n, t))
    elif n == DZIS:
        dzis.append(t)
    elif n - DZIS <= HORYZONT:
        blisko.append((n - DZIS, t))
for c in T.get("cykliczne", []):
    opozn = int(c.get("opoznienie", 0))
    for n in wystapienia(c, DZIS + HORYZONT):
        wraca = n + opozn
        t = {"co": "[CYKL %s, pisane %s] %s" % (c.get("id"), data_z(n), c.get("co", "?")),
             "kto": c.get("kto", "?"), "kanal": c.get("kanal", "BRAK"),
             "zamyka": "odebrane -> python3 gra/dzien.py odebrane %s %s" % (c.get("id"), data_z(n))}
        if wraca < DZIS:
            zal.append((DZIS - wraca, t))
        elif wraca == DZIS:
            dzis.append(t)
        else:
            blisko.append((wraca - DZIS, t))

zal.sort(key=lambda x: -x[0])
blisko.sort(key=lambda x: x[0])


def wypisz(t, pre=""):
    print("  %s%s" % (pre, skrot(t.get("co", "?"))))
    print("      kto: %s · kanal: %s · zamyka: %s" % (
        t.get("kto", "?"), t.get("kanal", "BRAK"), skrot(t.get("zamyka", "?"), 70)))


print("=" * 72)
print("KALENDARZ NA %s-%02d-%02d  (zasady 40 i 41 — ten blok wchodzi do ranka)" % (
    d.get("rok"), d.get("miesiac"), d.get("dzien")))
print("=" * 72)

print("\n### PRZETERMINOWANE (%d) — KAZDA MUSI DOSTAC ROZSTRZYGNIECIE DZIS" % len(zal))
print("### przyszlo / nie przyszlo I WIADOMO DLACZEGO / przyszlo co innego")
for sp, t in zal:
    wypisz(t, "+%d dni — " % sp)
if not zal:
    print("  (brak)")

print("\n### WRACA DZIS (%d)" % len(dzis))
for t in dzis:
    wypisz(t)
if not dzis:
    print("  (brak)")

print("\n### NAJBLIZSZE %d DNI (%d)" % (HORYZONT, len(blisko)))
for sp, t in blisko:
    wypisz(t, "za %d — " % sp)
if not blisko:
    print("  (brak)")

if bez:
    print("\n### BEZ DATY POWROTU (%d) — zasada 41: to nie sa terminy, tylko zyczenia" % len(bez))
    for t in bez:
        print("  %s" % skrot(t.get("co", "?"), 90))

print("\n" + "-" * 72)
print("INBOUND: rzut ciagnie sie Z TEJ LISTY (zasada 40), nie z pamieci.")
print("Rzut sprawie ZEWNETRZNEJ; wlasnym oplaconym ludziom — bez rzutu (zasada 7).")
print("OTWARTYCH LACZNIE: %d" % (len(zal) + len(dzis) + len(blisko) + len(bez)))
