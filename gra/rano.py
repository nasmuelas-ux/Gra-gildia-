#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ramka poranna Skryby - liczona z prawdy plikow gra/*.json.
Wypisuje: 📬 WIADOMOSCI (inbox) + 🍲 JEDZENIE + 💰 HAJS.
Uzycie: python3 gra/rano.py   (uruchamiac z katalogu repo)
"""
import json, re, os, sys

BASE = os.path.join(os.path.dirname(__file__))

def L(f):
    return json.load(open(os.path.join(BASE, f), encoding='utf-8'))

def daty_dzien(d):
    # zwraca (miesiac, dzien) jako liczby dla porownan w tym samym roku
    return d['miesiac'], d['dzien']

def kiedy_do_liczb(kiedy):
    # parsuje '~06-05' / '06-05' -> (mm, dd); zwraca None dla mglistych ('~tygodnie')
    m = re.search(r'(\d{1,2})-(\d{1,2})', str(kiedy))
    if m:
        return int(m.group(1)), int(m.group(2))
    return None

def main():
    p  = L('postac.json')
    sw = L('swiat.json')
    try:
        pl = L('ukryte/plany.json')
        kolejka = pl.get('inbound_kolejka', [])
    except Exception:
        kolejka = []

    data = sw['data']
    dzis = daty_dzien(data)  # (mm, dd)

    out = []
    # --- naglowek ---
    out.append(f"── {data['dzien']} dzien {data['miesiac']} miesiaca, {data['rok']} {data['era']} · {sw.get('sezon','')} · {sw['pora']} ──")

    # --- WIADOMOSCI ---
    pukaja = []
    for it in kolejka:
        term = kiedy_do_liczb(it.get('kiedy'))
        if term is not None:
            # puka, jesli termin <= dzis (ten sam rok)
            if term <= dzis:
                pukaja.append(it)
    out.append("")
    out.append("📬 WIADOMOSCI")
    if pukaja:
        for it in pukaja:
            out.append(f"   • {it.get('kto')}: {it.get('co')}")
    else:
        # pokaz co wisi na horyzoncie (mgliste/przyszle), ale to nie 'puka'
        czeka = []
        for it in kolejka:
            czeka.append(f"{it.get('kto')} ({it.get('kiedy')})")
        ogon = " · ".join(czeka) if czeka else "brak w kolejce"
        out.append(f"   cisza — nikt u progu. [na horyzoncie: {ogon}]")

    # --- JEDZENIE ---
    out.append("")
    out.append(f"🍲 JEDZENIE   sytosc {p.get('sytosc','?')} · zmeczenie {p.get('zmeczenie','?')} · zdrowie {p.get('zdrowie','?')}")

    # --- HAJS ---
    sak = p.get('sakiewka', {})
    jel = sak.get('jelenie', 0); mied = sak.get('miedziaki', 0); smoki = sak.get('smoki', 0)
    dep_mied = p.get('depozyt_u_nesty_mied', 0)
    inwest = p.get('inwestycja_faktoria_jel', 0)
    weksle = p.get('weksle_wystawione_jel', 0)
    zabezp = p.get('pozyczka_zabezpieczona_jel', 0)
    dep_jel = dep_mied / 100.0
    razem_jel = jel + mied/100.0 + dep_jel + inwest + weksle + zabezp
    wolne = f"{jel} jel + {mied} mied" + (f" + {smoki} smok" if smoki else "")
    out.append("")
    out.append(f"💰 HAJS   wolne: {wolne}")
    skrot = []
    if dep_mied: skrot.append(f"depozyt {dep_jel:.2f} jel")
    if inwest:   skrot.append(f"rotacja {inwest} jel (~zwrot)")
    if weksle:   skrot.append(f"weksle {weksle} jel")
    if zabezp:   skrot.append(f"pozyczka zabezp. {zabezp} jel")
    if skrot:
        out.append("          " + " · ".join(skrot))
    out.append(f"          razem ≈ {razem_jel:.2f} jel ≈ {razem_jel/200:.2f} smoka")

    print("\n".join([l for l in out if l is not None]))

if __name__ == '__main__':
    main()
