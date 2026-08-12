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
out = []
out.append(f"# STAN GRY — regenerowany z JSON (NIE edytuj recznie)")
out.append(f"_Prowadzenie: czytaj TEN plik na starcie kazdej tury. Zrodlo prawdy = gra/*.json, NIGDY pamiec rozmowy._\n")
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
