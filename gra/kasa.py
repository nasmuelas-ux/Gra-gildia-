#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SILNIK KAS - dzienne naliczanie i dokladne zamkniecie miesiaca.

    python3 gra/kasa.py                 -> dzien z gra/swiat.json
    python3 gra/kasa.py dzien 300-03-15 -> naliczenie za jeden dzien
    python3 gra/kasa.py miesiac 300-03  -> ZAMKNIECIE MIESIACA
    python3 gra/kasa.py rok 300         -> zamkniecie roku

ZASADA NACZELNA (zasady 1a, 43, 44):
  Kazda pozycja ma 'zrodlo'. Pozycja bez zrodla NIE WCHODZI DO SUMY.
  Czego nie ma w zapisie, trafia do bloku NIEZNANE - i tam zostaje.
  Widelki (min/max) sumuje sie OSOBNO. Nigdy sie ich nie usrednia.

Kalendarz swiata: 12 miesiecy po 30 dni (tak liczy gra/dzien.py).
"""
import json, os, io, sys, re

D = os.path.dirname(os.path.abspath(__file__))
DNI_W_MIESIACU = 30
MIES_W_ROKU = 12


def L(f):
    with io.open(os.path.join(D, f), encoding="utf-8") as fh:
        return json.load(fh)


def dni(r, m, d):
    return (r * MIES_W_ROKU + m) * DNI_W_MIESIACU + d


def parsuj(txt):
    """'300-03-15' -> (300,3,15); '300-03' -> (300,3,None); inaczej None."""
    m = re.match(r"^(\d{3,4})-(\d{2})(?:-(\d{2}))?$", str(txt or "").strip())
    if not m:
        return None
    return (int(m.group(1)), int(m.group(2)),
            int(m.group(3)) if m.group(3) else None)


def w_oknie(poz, r, m, d):
    """Czy pozycja obowiazuje danego dnia (pola 'od' / 'do')."""
    teraz = dni(r, m, d)
    for pole, znak in (("od", 1), ("do", -1)):
        v = parsuj(poz.get(pole))
        if v:
            g = dni(v[0], v[1], v[2] or (1 if pole == "od" else DNI_W_MIESIACU))
            if znak > 0 and teraz < g:
                return False
            if znak < 0 and teraz > g:
                return False
    return True


def na_dzien(poz):
    """Stawka pozycji przeliczona na JEDEN DZIEN. Zwraca (min, max)."""
    okres = poz.get("okres", "miesiac")
    dzielnik = {"dzien": 1, "miesiac": DNI_W_MIESIACU,
                "kwartal": DNI_W_MIESIACU * 3,
                "rok": DNI_W_MIESIACU * MIES_W_ROKU}.get(okres, DNI_W_MIESIACU)
    if "stawka" in poz:
        lo = hi = float(poz["stawka"])
    elif "min" in poz or "max" in poz:
        lo = float(poz.get("min", poz.get("max", 0)))
        hi = float(poz.get("max", poz.get("min", 0)))
    else:
        return None
    znak = -1.0 if poz.get("typ") == "koszt" else 1.0
    return (znak * lo / dzielnik, znak * hi / dzielnik)


def seria_za(poz, r, m):
    """Wartosc z 'serie' dla danego miesiaca albo None."""
    s = poz.get("serie")
    if not s:
        return None
    v = s.get("%d-%02d" % (r, m))
    return None if v is None else float(v)


def fmt(lo, hi, szer=0):
    t = ("%+.2f" % lo) if abs(lo - hi) < 1e-9 else ("%+.2f..%+.2f" % (lo, hi))
    return t.rjust(szer) if szer else t


# --------------------------------------------------------------------------

def licz(zakres, r, m, d=None):
    """zakres: 'dzien' | 'miesiac' | 'rok'. Zwraca strukture do wydruku."""
    E = L("ekonomia.json")
    if zakres == "dzien":
        dni_lista = [(r, m, d)]
    elif zakres == "miesiac":
        dni_lista = [(r, m, i) for i in range(1, DNI_W_MIESIACU + 1)]
    else:
        dni_lista = [(r, mm, i) for mm in range(1, MIES_W_ROKU + 1)
                     for i in range(1, DNI_W_MIESIACU + 1)]

    wynik = {}
    for nazwa, kasa in E["kasy"].items():
        wiersze, obrot, nieznane = [], [], list(kasa.get("nieznane", []))
        for poz in kasa["pozycje"]:
            if not poz.get("zrodlo"):
                nieznane.append({"nazwa": poz.get("nazwa", "?"),
                                 "powod": "POZYCJA BEZ ZRODLA - poza suma (zasada 43)"})
                continue
            if poz.get("serie"):
                # serie sa miesieczne: licz tylko pelne miesiace z zakresu
                mies = sorted(set((a, b) for a, b, _ in dni_lista))
                suma = 0.0
                trafien = 0
                for (a, b) in mies:
                    v = seria_za(poz, a, b)
                    if v is not None:
                        suma += v
                        trafien += 1
                brak = len(mies) - trafien
                cel = obrot if poz.get("typ") == "obrot" else wiersze
                if trafien:
                    znak = -1.0 if poz.get("typ") == "koszt" else 1.0
                    cel.append((poz["nazwa"], znak * suma, znak * suma, poz["zrodlo"]))
                if brak:
                    nieznane.append({
                        "nazwa": poz["nazwa"],
                        "powod": "brak zapisu dla %d z %d miesiecy zakresu" % (brak, len(mies))})
                continue
            st = na_dzien(poz)
            if st is None:
                nieznane.append({"nazwa": poz.get("nazwa", "?"),
                                 "powod": "brak stawki i brak widelek"})
                continue
            lo = hi = 0.0
            for (a, b, c) in dni_lista:
                if w_oknie(poz, a, b, c):
                    lo += st[0]
                    hi += st[1]
            if abs(lo) > 1e-9 or abs(hi) > 1e-9:
                (obrot if poz.get("typ") == "obrot" else wiersze).append(
                    (poz["nazwa"], lo, hi, poz["zrodlo"]))

        zdarz = []
        for z in E.get("zdarzenia", []):
            if z.get("kasa") != nazwa:
                continue
            v = parsuj(z.get("data"))
            if not v:
                continue
            if not any((v[0], v[1], v[2]) == t for t in dni_lista):
                continue
            if "kwota" in z:
                lo = hi = float(z["kwota"])
            else:
                lo, hi = float(z.get("min", 0)), float(z.get("max", 0))
            zdarz.append((z["data"], z["opis"], lo, hi,
                          z.get("status", ""), z.get("zrodlo", "")))

        wynik[nazwa] = {"wiersze": wiersze, "obrot": obrot, "_kasa": kasa,
                        "zdarzenia": zdarz, "nieznane": nieznane,
                        "skrzynia": kasa.get("skrzynia"),
                        "skrzynia_na": kasa.get("skrzynia_na")}
    return wynik


def drukuj(zakres, r, m, d, wynik):
    tytul = {"dzien": "NALICZENIE ZA DZIEN %d-%02d-%02d" % (r, m, d or 0),
             "miesiac": "ZAMKNIECIE MIESIACA %d-%02d" % (r, m),
             "rok": "ZAMKNIECIE ROKU %d" % r}[zakres]
    print("=" * 78)
    print(tytul + "   (wszystko w SMOKACH; 1 smok = 200 jeleni = 20 000 miedziakow)")
    print("=" * 78)
    sym = L("ekonomia.json").get("_symulacje")
    if sym:
        print("POZYCJE USTALONE %s - MAJA MOC ZAPISU (zasada 43)." % sym["_data"])
        print("Nie kwestionuje sie ich ponownie i nie wracaja jako 'nieznane'.")
        print("-" * 78)
    glo = ghi = 0.0
    for nazwa, k in wynik.items():
        print("\n### " + nazwa)
        if k["skrzynia"] is not None:
            print("    skrzynia %s: %.2f" % (k["skrzynia_na"], k["skrzynia"]))
        slo = shi = 0.0
        for (n, lo, hi, zr) in k["wiersze"]:
            print("  %-62s %s" % (n[:62], fmt(lo, hi, 13)))
            slo += lo
            shi += hi
        for (dt, op, lo, hi, st, zr) in k["zdarzenia"]:
            print("  %-62s %s" % (("[%s] %s" % (dt, op))[:62], fmt(lo, hi, 13)))
            if st:
                print("      status: %s" % st)
            slo += lo
            shi += hi
        print("  " + "-" * 76)
        print("  %-62s %s" % ("RAZEM", fmt(slo, shi, 13)))
        glo += slo
        ghi += shi
        if k["obrot"]:
            print("  --- obrot (informacyjnie, NIE wchodzi do wyniku) ---")
            for (n, lo, hi, zr) in k["obrot"]:
                print("  %-62s %s" % (n[:62], fmt(lo, hi, 13)))
        if k["nieznane"]:
            print("  ### NIEZNANE - POZA SUMA (zasada 43: liczb sie nie zgaduje)")
            for u in k["nieznane"]:
                print("   - %s" % u["nazwa"])
                print("     %s" % u["powod"])
        drukuj_przedsiebiorstwa(k["_kasa"])
    stopka(glo, ghi)


def zawijaj(txt, wciecie=7, szer=70):
    slowa, linia, out = str(txt).split(), "", []
    for w in slowa:
        if len(linia) + len(w) + 1 > szer:
            out.append(linia)
            linia = w
        else:
            linia = (linia + " " + w).strip()
    if linia:
        out.append(linia)
    return ("\n" + " " * wciecie).join(out)


def drukuj_przedsiebiorstwa(kasa):
    """PRZEDSIEBIORSTWA - warstwa, ktorej nie widac w naliczeniu dziennym,
    bo wiekszosc siedzi w obrocie placowek albo w aparacie jako koszt."""
    s = kasa.get("synteza")
    if s:
        print("  ### SYNTEZA DOMU (%s)" % s.get("zrodlo", "?"))
        print("      obrot na ~%d%% pulapu · zysk netto %d-%d/mies · wolna gotowka %d-%d/mies"
              % (s["obrot_na_procent_pulapu"], s["zysk_netto_mies_min"], s["zysk_netto_mies_max"],
                 s["wolna_gotowka_mies_min"], s["wolna_gotowka_mies_max"]))
        print("      MAJATEK NETTO DOMU: %d - %d smokow" % (s["majatek_netto_min"], s["majatek_netto_max"]))
        if s.get("uwaga"):
            print("      " + zawijaj(s["uwaga"]))
    p = kasa.get("przedsiebiorstwa")
    if p:
        print("  ### PRZEDSIEBIORSTWA - wiekszosc NIE MA osobnej liczby i siedzi w obrocie placowek")
        for z in p:
            print("   * %s" % z["nazwa"])
            for pole in ("stan", "w_ksiegach"):
                if z.get(pole):
                    print("     %s" % zawijaj(z[pole]))
            if z.get("potencjal_mies_min") is not None:
                print("     TERAZ %.2f/mies  ->  POTENCJAL %d-%d/mies"
                      % (z.get("teraz_mies", 0), z["potencjal_mies_min"], z["potencjal_mies_max"]))
    if kasa.get("korekta_dochodu"):
        print("  ### " + zawijaj(kasa["korekta_dochodu"], 6))
    if kasa.get("w_naturze"):
        print("  ### " + zawijaj(kasa["w_naturze"], 6))
    n = kasa.get("nie_moje")
    if n:
        print("  ### CO NIE JEST MOJE - I MA TAK ZOSTAC")
        for z in n:
            print("   * %s" % z["nazwa"])
            print("     %s" % zawijaj(z["powod"]))
    c = kasa.get("co_prowadzi_a_nie_posiada")
    if c:
        print("  ### CO PROWADZE, A CZEGO NIE POSIADAM")
        for z in c:
            print("   * %s" % z["nazwa"])
            print("     %s" % zawijaj(z["stan"]))


def stopka(glo, ghi):
    print("\n" + "=" * 78)
    print("%-64s %s" % ("WSZYSTKIE KASY RAZEM", fmt(glo, ghi, 13)))
    print("=" * 78)
    print("UWAGA: suma obejmuje WYLACZNIE pozycje ze zrodlem. Blok NIEZNANE i cala")
    print("warstwa PRZEDSIEBIORSTW do niej NIE WCHODZA - wiekszosc zakladow nie ma")
    print("osobnej liczby i siedzi w obrocie placowek albo w aparacie jako koszt.")
    print("To jest cala wartosc tej tabeli: pokazuje, czego NIE policzono.")


def main():
    a = sys.argv[1:]
    S = L("swiat.json")["data"]
    if not a:
        zakres, r, m, d = "dzien", S["rok"], S["miesiac"], S["dzien"]
    else:
        zakres = a[0]
        v = parsuj(a[1]) if len(a) > 1 else None
        if v:
            r, m, d = v[0], v[1], v[2]
        else:
            r, m, d = S["rok"], S["miesiac"], S["dzien"]
        if zakres == "dzien" and d is None:
            d = S["dzien"]
    drukuj(zakres, r, m, d, licz(zakres, r, m, d))


if __name__ == "__main__":
    main()
