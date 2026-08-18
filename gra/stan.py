#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator dashboardu STAN.md z plikow JSON (jedyne zrodlo prawdy).
Uruchom: python3 gra/stan.py   (regeneruje gra/STAN.md)
NIGDY nie edytuj STAN.md recznie — edytuj JSON-y i przelicz."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
def L(f):
    try: return json.load(open(os.path.join(D, f), encoding="utf-8"))
    except Exception: return {}

p, s, z = L("postac.json"), L("swiat.json"), L("zegary.json")
npc, wa = L("npc.json"), L("watki.json")

d = s.get("data", {})
data = f"{d.get('rok','?')}-{d.get('miesiac','?'):0>2}-{d.get('dzien','?'):0>2} {s.get('pora','?')}"

# --- STARZENIE: wiek wyliczany z kalendarza (rok_urodzenia + data_urodzin) ---
# Dzieki temu wszyscy starzeja sie sami z uplywem lat gry, w nieskonczonosc.
def _wiek(rok, mies, dzien, rok_ur, data_ur):
    if rok_ur is None or not isinstance(rok, int):
        return None
    w = rok - rok_ur
    if data_ur:
        bm, bd = data_ur.get("miesiac"), data_ur.get("dzien")
        if bm is not None and bd is not None and isinstance(mies, int) and isinstance(dzien, int):
            if (mies, dzien) < (bm, bd):
                w -= 1  # urodziny w tym roku jeszcze nie minely
    return w

_rok, _mc, _dz = d.get("rok"), d.get("miesiac"), d.get("dzien")
# Symon
_nw = _wiek(_rok, _mc, _dz, p.get("rok_urodzenia"), p.get("data_urodzin"))
if _nw is not None and _nw != p.get("wiek"):
    p["wiek"] = _nw
    json.dump(p, open(os.path.join(D, "postac.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
# NPC (rok_urodzenia u kazdego; data_urodzin opcjonalna — bez niej wiek roczny/przyblizony)
_ch = False
for _sect in ("na_scenie", "w_orbicie", "orbita"):
    _v = npc.get(_sect)
    for _x in (_v if isinstance(_v, list) else []):
        if isinstance(_x, dict) and _x.get("rok_urodzenia") is not None:
            _w = _wiek(_rok, _mc, _dz, _x.get("rok_urodzenia"), _x.get("data_urodzin"))
            if _w is not None and _w != _x.get("wiek"):
                _x["wiek"] = _w
                _ch = True
if _ch:
    json.dump(npc, open(os.path.join(D, "npc.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
# --- koniec starzenia ---
out = []
out.append(f"# STAN GRY — regenerowany z JSON (NIE edytuj recznie)")
out.append(f"_Prowadzenie: czytaj TEN plik na starcie kazdej tury. Zrodlo prawdy = gra/*.json, NIGDY pamiec rozmowy._\n")
out.append(
    "## ⚠️ OBOWIAZKOWA RAMA RANKA (nie pomijac po kompaktowaniu!)\n"
    "Kazdy RANEK renderuj W TEJ KOLEJNOSCI, ZAWSZE:\n"
    "1. Naglowek daty + pogoda/zdarzenie\n"
    "2. Kalendarz (targ/swieto/clo)\n"
    "3. **📬 WIADOMOSCI / KORESPONDENCJA** — osobna ramka: kto sie odezwal/przyslal poslanca/jaka wiesc/co dojrzalo (rzut na inbound); jak nic → napisz \"cisza\". TO NIE JEST NA ZADANIE — renderuj SAM co ranek (zasada od 297-05-21; lapse'y 05-19 i 12-19/21 — nie powtorzyc).\n"
    "4. STATUS: jedzenie (sytosc/zmeczenie/zdrowie) + hajs (wolne + skrot)\n"
    "5. Watki w toku → pytanie \"co robisz\" (bez listy opcji)\n"
)
out.append(f"## TERAZ\n- **Data:** {data} · {s.get('sezon','')}\n- **Miasto:** Bialy Port (White Harbor) · rod Manderly")
out.append(f"- **Postac:** {p.get('imie','?')}, l.{p.get('wiek','?')} — {p.get('utrzymanie','')[:120]}")
out.append(f"- **Mieszka:** {p.get('mieszka','?')}")
out.append(f"- **Nastroje:** {s.get('nastroje_miasta','')[:200]}")

sk = p.get("sakiewka", {})
out.append(f"\n## KASA (kurs: 1 jelen=100 mied; 1 smok=200 jel)")
out.append(f"- **Wolne:** {sk.get('jelenie',0)} jeleni + {sk.get('miedziaki',0)} mied + {sk.get('smoki',0)} smokow")
for it in p.get("dobytek", []):
    if any(k in it for k in ("depozyt", "SPOLKA", "ZADATEK", "udzial")):
        out.append(f"- {it}")
poz = p.get("pozycje", {})
if poz:
    out.append("\n## POZYCJE (nie-gotowka: naleznosci, inwestycje, udzialy)")
    for k, v in poz.items():
        out.append(f"- {v}")
prz = p.get("przychody", {})
if prz:
    out.append("\n## KSIEGA PRZYCHODOW (gdzie/kiedy laduje wplyw)")
    out.append(f"- **Dzien Bilansu:** {prz.get('dzien_bilansu','?')} · nastepny {prz.get('nastepny_bilans','?')} (ostatni: {prz.get('ostatni_bilans','?')})")
    cyk = prz.get("strumienie_cykliczne_miesieczne", {})
    if cyk:
        out.append("- _Cykliczne (zmiatane w Dniu Bilansu):_")
        for k, v in cyk.items():
            out.append(f"    - {k}: {v}")
    pz = prz.get("strumienie_per_zdarzenie", {})
    if pz:
        out.append("- _Per-zdarzenie (ksiegowane przy zdarzeniu):_")
        for k, v in pz.items():
            out.append(f"    - {k}: {v}")
    if prz.get("koszty_cykliczne_uwaga"):
        out.append(f"- _Koszty (dla netto):_ {prz['koszty_cykliczne_uwaga']}")
out.append(f"- Zdrowie {p.get('zdrowie','?')} · Sytosc {p.get('sytosc','?')} · Zmeczenie {p.get('zmeczenie','?')}")

um = p.get("umiejetnosci", {})
out.append("\n## UMIEJETNOSCI (0-10)")
out.append(" · ".join(f"{k} {v}" for k, v in um.items()))
rep = p.get("reputacja", {})
out.append("**Reputacja:** " + " · ".join(f"{k} {v}" for k, v in rep.items()))
if p.get("wiedza"):
    out.append("**Wiedza/drzewko miekkie:** " + "; ".join(w.split(":")[0].split("(")[0].strip() for w in p["wiedza"]))

out.append("\n## LUDZIE NA SCENIE (nast. do gracza)")
for x in npc.get("na_scenie", []):
    out.append(f"- **{x.get('imie','?')}** ({x.get('id','')}) — {x.get('zawod','')[:60]} · nast {x.get('nastawienie_do_gracza','?')}")

out.append("\n## ZEGARY (odliczaja)")
for c in z.get("zegary", []):
    mk = "⚠" if c.get("typ") == "zagrozenie" else "◆"
    out.append(f"- {mk} `{c.get('odlicza_do','?')}` {c.get('id','')}: {c.get('opis','')[:110]}")

out.append("\n## WATKI OTWARTE (najwazniejsze u gory)")
prio = ["audyt_dlugu_antaryon", "wolnosc_od_harwina", "list_ze_starego_zamku",
        "spolka_egzotyczna", "kanal_polnoc_futra", "odbior_skor", "uraza_osgara",
        "sojusz_kolodzieje", "sprawa_elny_lorren", "wiekszy_patron"]
wl = {x.get("id"): x for x in wa.get("watki", [])}
seen = set()
for i in prio:
    x = wl.get(i)
    if x:
        seen.add(i)
        out.append(f"- **{i}** [{x.get('stan','')[:8] if isinstance(x.get('stan'),str) else ''}]: {(x.get('stan') or x.get('opis',''))[:150]}")
open(os.path.join(D, "STAN.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("STAN.md zregenerowany:", data)
