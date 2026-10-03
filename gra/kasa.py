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


def miesiecy_od(txt, r, m):
    """Ile pelnych miesiecy uplynelo od daty 'txt' do miesiaca (r,m)."""
    v = parsuj(txt)
    if not v:
        return 0
    return max(0, (r * MIES_W_ROKU + m) - (v[0] * MIES_W_ROKU + v[1]))


def marza_hala(E, r, m):
    """Marza Domu rosnie z kazdym miesiacem, ktory Hal spedzil na krzesle."""
    h = E.get("_hal")
    if not h:
        return None
    n = miesiecy_od(h["od"], r, m)
    return min(h["marza_sufit"], h["marza_start"] + n * h["przyrost_marzy_na_miesiac"])


def sezon_dla(M, m):
    for nazwa, mies in M["sezony"].items():
        if m in mies:
            return nazwa
    return "wiosna"


def placowki_za(E, r, m):
    """Zwraca (obrot, zysk, rozbicie) dla miesiaca (r,m)."""
    M = E.get("_model_placowek")
    if not M:
        return None
    n = miesiecy_od("299-12-01", r, m)
    sez = sezon_dla(M, m)
    marza = marza_hala(E, r, m)
    obrot = zysk = 0.0
    roz = []
    for nazwa, p in M["placowki"].items():
        o = min(p["pulap"], p["baza_xii"] * ((1.0 + p["wzrost"]) ** n)) * p["sezon"][sez]
        z = o * marza
        obrot += o
        zysk += z
        roz.append((nazwa, o, z))
    return (obrot, zysk, roz, marza, sez)


def skala(E, kasa, poz, r, m):
    """KOREKTA SKALI (rozstrzygniecie gracza 300-04-26): przychody Kas 1-3
    od wskazanego miesiaca mnozone min x2, max x3. Koszty, obrot informacyjny
    i pozycje z 'bez_skali' - bez zmian. Zwraca (fmin, fmax)."""
    K = E.get("_korekta_skali")
    if not K or kasa not in K["kasy"]:
        return (1.0, 1.0)
    if poz is not None and (poz.get("typ") in ("koszt", "obrot") or poz.get("bez_skali")):
        return (1.0, 1.0)
    v = parsuj(K["od"])
    if (r * MIES_W_ROKU + m) < (v[0] * MIES_W_ROKU + v[1]):
        return (1.0, 1.0)
    f0, f1 = float(K["mnoznik_min"]), float(K["mnoznik_max"])
    # korekty dodatkowe (np. +10% od 300-06-01, rozstrzygniecie gracza 300-06-05)
    for D in E.get("_korekty_dodatkowe", []):
        if kasa not in D["kasy"]:
            continue
        w = parsuj(D["od"])
        if (r * MIES_W_ROKU + m) >= (w[0] * MIES_W_ROKU + w[1]):
            f0 *= float(D["mnoznik"])
            f1 *= float(D["mnoznik"])
    return (f0, f1)


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
            if st is not None and poz.get("wzrost_mies"):
                # wzrost skladany od daty 'od', z sufitem
                mies = sorted(set((a, b) for a, b, _ in dni_lista))
                lo = hi = 0.0
                for (a, b) in mies:
                    if not w_oknie(poz, a, b, 15):
                        continue
                    n = miesiecy_od(poz.get("od"), a, b)
                    mn = min(poz.get("sufit", 1e9), float(poz.get("min", 0)) * ((1 + poz["wzrost_mies"]) ** n))
                    mx = min(poz.get("sufit", 1e9), float(poz.get("max", 0)) * ((1 + poz["wzrost_mies"]) ** n))
                    zn = -1.0 if poz.get("typ") == "koszt" else 1.0
                    f0, f1 = skala(E, nazwa, poz, a, b)
                    lo += zn * mn * f0
                    hi += zn * mx * f1
                if abs(lo) > 1e-9 or abs(hi) > 1e-9:
                    wiersze.append((poz["nazwa"] + " [rosnie]", lo, hi, poz["zrodlo"]))
                continue
            if st is None:
                nieznane.append({"nazwa": poz.get("nazwa", "?"),
                                 "powod": "brak stawki i brak widelek"})
                continue
            lo = hi = 0.0
            for (a, b, c) in dni_lista:
                if w_oknie(poz, a, b, c):
                    f0, f1 = skala(E, nazwa, poz, a, b)
                    lo += st[0] * f0
                    hi += st[1] * f1
            if abs(lo) > 1e-9 or abs(hi) > 1e-9:
                (obrot if poz.get("typ") == "obrot" else wiersze).append(
                    (poz["nazwa"], lo, hi, poz["zrodlo"]))

        if nazwa.startswith("KASA 1") and E.get("_model_placowek"):
            mies = sorted(set((a, b) for a, b, _ in dni_lista))
            so_lo = so_hi = sz_lo = sz_hi = 0.0
            ost = None
            for (a, b) in mies:
                if (a * MIES_W_ROKU + b) < (299 * MIES_W_ROKU + 12):
                    continue
                o, z, roz, marza, sez = placowki_za(E, a, b)
                f0, f1 = skala(E, nazwa, None, a, b)
                so_lo += o * f0
                so_hi += o * f1
                sz_lo += z * f0
                sz_hi += z * f1
                ost = (roz, marza, sez, f0, f1)
            if sz_hi:
                wiersze.insert(0, ("zysk PIECIU placowek handlowych [model wzrostu]", sz_lo, sz_hi,
                                   E["_model_placowek"]["_wzor"]))
                obrot.append(("obrot pieciu placowek [model wzrostu]", so_lo, so_hi, "model"))
                kasa = dict(kasa)
                kasa["_rozbicie"] = ost

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
        K = L("ekonomia.json").get("_korekta_skali")
        if K:
            print("KOREKTA SKALI od %s: przychody %s x%g (min) .. x%g (max); koszty bez zmian."
                  % (K["od"], "/".join(k.split(" - ")[0] for k in K["kasy"]), K["mnoznik_min"], K["mnoznik_max"]))
        for D in L("ekonomia.json").get("_korekty_dodatkowe", []):
            print("KOREKTA DODATKOWA od %s: przychody %s x%g." % (D["od"], "/".join(k.split(" - ")[0] for k in D["kasy"]), D["mnoznik"]))
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
        olo, ohi = slo, shi
        print("  " + "-" * 76)
        print("  %-62s %s" % (">>> WYNIK OPERACYJNY (to, co dom zarabia co miesiac)", fmt(olo, ohi, 13)))
        if k["zdarzenia"]:
            print("  --- ZDARZENIA JEDNORAZOWE (nie powtarzaja sie) ---")
        for (dt, op, lo, hi, st, zr) in k["zdarzenia"]:
            print("  %-62s %s" % (("[%s] %s" % (dt, op))[:62], fmt(lo, hi, 13)))
            if st:
                print("      status: %s" % st)
            slo += lo
            shi += hi
        print("  " + "-" * 76)
        print("  %-62s %s" % ("RAZEM Z ZDARZENIAMI", fmt(slo, shi, 13)))
        if not nazwa.startswith("KASA 4"):
            glo += slo
            ghi += shi
        else:
            print("      (kasa miejska NIE wchodzi do sumy Symona - prowadzi ja lawa, nie lord)")
        roz = k["_kasa"].get("_rozbicie")
        if roz:
            lista, marza, sez, f0, f1 = roz
            print("  --- rozbicie placowek, OSTATNI miesiac zakresu (sezon: %s, marza Hala: %.1f%%) ---"
                  % (sez, marza * 100))
            if (f0, f1) != (1.0, 1.0):
                print("      (liczby przed KOREKTA SKALI x%g..x%g - w wyniku sa juz przemnozone)" % (f0, f1))
            for (n, o, z) in lista:
                print("      %-28s obrot %8.1f   zysk %7.1f" % (n, o, z))
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
    if zakres in ("miesiac", "rok"):
        rachunek_domu(L("ekonomia.json"), wynik, r, m, zakres)
    stopka(glo, ghi)


def _pasuje(nazwa, slownik):
    for k in slownik:
        if nazwa.startswith(k):
            return k
    return None


def rachunek_domu(E, wynik, r, m, zakres):
    """CZTERY LICZBY DOMU (rozstrzygniecie gracza 300-05-05):
    OBROT z dzwignia -> PRZYCHOD -> ZYSK -> WOLNA GOTOWKA,
    plus warsztaty i zaklady kazdy osobno (sprzedaz i zysk)."""
    R = E.get("_rachunek_domu")
    k1 = wynik.get("KASA 1 - DOM HANDLOWY TALLY")
    if not R or not k1:
        return
    k2 = wynik.get("KASA 2 - LENNO FOSY CAILIN", {"wiersze": []})
    zysk_lo = sum(x[1] for x in k1["wiersze"])
    zysk_hi = sum(x[2] for x in k1["wiersze"])

    # obrot towarowy placowek (model, juz po korekcie skali)
    tow_lo = tow_hi = 0.0
    for (n, lo, hi, zr) in k1["obrot"]:
        if n.startswith("obrot pieciu placowek"):
            tow_lo, tow_hi = lo, hi
    es_lo = es_hi = 0.0
    warsztaty = []
    prow_lo = prow_hi = 0.0
    fin = []
    for zrodlo_k, wiersze in (("Dom", k1["wiersze"]), ("Lenno", k2["wiersze"])):
        for (n, lo, hi, zr) in wiersze:
            if lo < 0 and hi < 0:
                continue
            w = _pasuje(n, R["warsztaty"])
            if w:
                mm = sum(R["warsztaty"][w]) / 2.0
                warsztaty.append((zrodlo_k, w.upper(), lo / mm, hi / mm, lo, hi))
                continue
            if zrodlo_k != "Dom":
                continue
            e = _pasuje(n, R["handel_essos"])
            if e:
                mm = sum(R["handel_essos"][e]) / 2.0
                es_lo += lo / mm
                es_hi += hi / mm
                continue
            f = _pasuje(n, R["finanse"])
            if f:
                ss = sum(R["finanse"][f]["stopa"]) / 2.0
                fin.append((R["finanse"][f]["co"], lo / ss, hi / ss))
                prow_lo += lo
                prow_hi += hi
                continue
            if n.startswith("zysk PIECIU placowek"):
                continue
            prow_lo += lo     # udzialy, ekstra zysk itp. - wchodza do przychodu po nominale
            prow_hi += hi
    ws_lo = sum(x[2] for x in warsztaty if x[0] == "Dom")
    ws_hi = sum(x[3] for x in warsztaty if x[0] == "Dom")
    prz_lo = tow_lo + es_lo + ws_lo + prow_lo
    prz_hi = tow_hi + es_hi + ws_hi + prow_hi
    pap_lo = sum(x[1] for x in fin)
    pap_hi = sum(x[2] for x in fin)
    obr_lo, obr_hi = prz_lo + pap_lo, prz_hi + pap_hi

    mies = 12 if zakres == "rok" else 1
    r0, r1 = R["reinwestycja"]
    reinw_lo, reinw_hi = zysk_lo * r0, zysk_hi * r1
    B = R.get("bufor", {})
    buf = 0.0
    v = parsuj(B.get("napelniany_w"))
    if v and ((zakres == "miesiac" and (r, m) == (v[0], v[1])) or (zakres == "rok" and r == v[0])):
        buf = float(B.get("cel", 0))
    wol_lo = max(0.0, zysk_lo - zysk_lo * r1 - buf)
    wol_hi = max(0.0, zysk_hi - zysk_hi * r0 - buf)
    kw0, kw1 = R["kapital_wlasny"]

    print("\n  " + "=" * 76)
    print("  RACHUNEK DOMU - CZTERY LICZBY (rozstrzygniecie gracza 300-05-05)")
    print("  " + "=" * 76)
    print("  %-62s %s" % ("1. OBROT - towar i operacje przez Dom (z dzwignia)", fmt(obr_lo, obr_hi, 13)))
    print("       w tym przychod (nizej)                                 %s" % fmt(prz_lo, prz_hi))
    for (co, lo, hi) in fin:
        print("       w tym %-50s %s" % (co[:50], fmt(lo, hi)))
    print("       DZWIGNIA: obrot / kapital wlasny (%d-%d) = x%.1f .. x%.1f"
          % (kw0, kw1, obr_lo / mies / kw1, obr_hi / mies / kw0))
    print("  %-62s %s" % ("2. PRZYCHOD - sprzedaz, marze, prowizje, odsetki", fmt(prz_lo, prz_hi, 13)))
    print("       towar pieciu placowek (Westeros)                       %s" % fmt(tow_lo, tow_hi))
    print("       towar placowek Essos i Seagard                         %s" % fmt(es_lo, es_hi))
    print("       sprzedaz warsztatow Domu                               %s" % fmt(ws_lo, ws_hi))
    print("       prowizje, odsetki, udzialy                             %s" % fmt(prow_lo, prow_hi))
    print("  %-62s %s" % ("3. ZYSK - wynik operacyjny po kosztach", fmt(zysk_lo, zysk_hi, 13)))
    print("  %-62s %s" % ("4. WOLNA GOTOWKA - do dyspozycji pana", fmt(wol_lo, wol_hi, 13)))
    print("       = zysk minus reinwestycja %d-%d%% (%s)"
          % (r0 * 100, r1 * 100, fmt(-reinw_hi, -reinw_lo)))
    if buf:
        print("       minus BUFOR HALA %d (jednorazowo, %s) - od nastepnego miesiaca stoi pelny"
              % (buf, B.get("napelniany_w")))
    print("       towar wlosci placony moneta = kapital obrotowy, NIE odplyw (wraca w marzy)")
    print("  " + "-" * 76)
    print("  ### WARSZTATY I ZAKLADY - KAZDY OSOBNO (sprzedaz / zysk)")
    for (zk, n, s0, s1, z0, z1) in warsztaty:
        print("   %-5s %-26s sprzedaz %-20s zysk %s" % (zk, n[:26], fmt(s0, s1), fmt(z0, z1)))
    print("   (Lenno = Kasa 2, Fosa Cailin; Dom = Kasa 1. Sprzedaz = zysk / srednia marza warsztatu - szacunek GM, do korekty.)")


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
        print("  ### HISTORIA - SYNTEZA DOMU SPRZED KOREKTY SKALI (%s) - NIEAKTUALNA, patrz RACHUNEK DOMU" % s.get("zrodlo", "?"))
        print("      obrot na ~%d%% pulapu · zysk netto %d-%d/mies · wolna gotowka %d-%d/mies"
              % (s["obrot_na_procent_pulapu"], s["zysk_netto_mies_min"], s["zysk_netto_mies_max"],
                 s["wolna_gotowka_mies_min"], s["wolna_gotowka_mies_max"]))
        print("      MAJATEK NETTO DOMU: %d - %d smokow" % (s["majatek_netto_min"], s["majatek_netto_max"]))
        if s.get("uwaga"):
            print("      " + zawijaj(s["uwaga"]))
    p = kasa.get("przedsiebiorstwa")
    if p:
        print("  ### PRZEDSIEBIORSTWA - OPISY (liczby: blok WARSZTATY I ZAKLADY w RACHUNKU DOMU)")
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
    print("UWAGA: suma obejmuje WYLACZNIE pozycje ze zrodlem; blok NIEZNANE do niej nie wchodzi.")
    print("Warsztaty Domu i lenna maja WLASNE linie (sprzedaz i zysk) - patrz RACHUNEK DOMU.")


def wolne(r, m, d):
    """ILE JEST WOLNYCH SRODKOW - skrzynia: bufor Hala + wolna gotowka narastajaca
    co miesiac (zysk x (1 - reinwestycja)); rozstrzygniecie gracza 300-05-05."""
    E = L("ekonomia.json")
    S = E["_skrzynia"]
    R = E.get("_rachunek_domu", {})
    r0, r1 = R.get("reinwestycja", [0.25, 0.35])
    v = parsuj(S["na_dzien"])
    print("=" * 78)
    print("SKRZYNIA KASY 1 na %d-%02d-%02d" % (r, m, d))
    print("=" * 78)
    print("  %-56s %12.2f" % ("BUFOR HALA (stoi pelny, nie do wydawania)", S.get("bufor", 0)))
    lo, hi = float(S.get("wolna_min", 0)), float(S.get("wolna_max", 0))
    print("  %-56s %s" % ("wolna gotowka na %s" % S["na_dzien"], fmt(lo, hi)))
    # pelne miesiace po dniu bazowym + czesc biezacego
    rr, mm = v[0], v[1] + 1
    if mm > MIES_W_ROKU:
        rr, mm = rr + 1, 1
    while (rr * MIES_W_ROKU + mm) <= (r * MIES_W_ROKU + m):
        w = licz("miesiac", rr, mm)["KASA 1 - DOM HANDLOWY TALLY"]
        zl = sum(x[1] for x in w["wiersze"])
        zh = sum(x[2] for x in w["wiersze"])
        czesc = 1.0 if (rr, mm) != (r, m) else d / float(DNI_W_MIESIACU)
        dl, dh = zl * (1 - r1) * czesc, zh * (1 - r0) * czesc
        print("  %-56s %s" % ("+ wolna gotowka %d-%02d%s" % (rr, mm, "" if czesc == 1.0 else " (do %d. dnia)" % d), fmt(dl, dh)))
        lo += dl
        hi += dh
        mm += 1
        if mm > MIES_W_ROKU:
            rr, mm = rr + 1, 1
    print("  " + "-" * 74)
    print("  %-56s %s" % (">>> WOLNA GOTOWKA DZIS (do dyspozycji pana)", fmt(lo, hi)))
    zob = [z for z in S["zobowiazania"] if not z.get("poza_suma")]
    if zob:
        print("\n  ZOBOWIAZANIA OTWARTE:")
        for z in zob:
            print("   - [%s] %s - %s" % (z["data"], z["co"], z["status"]))
    print("=" * 78)


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
    if zakres == "wolne":
        wolne(r, m, d or S["dzien"])
        return
    drukuj(zakres, r, m, d, licz(zakres, r, m, d))


if __name__ == "__main__":
    main()
