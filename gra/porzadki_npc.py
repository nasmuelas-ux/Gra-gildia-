#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PORZADKI W NPC — 299-09-11.

Trzy rzeczy naraz, bo wszystkie trzy zalezą od siebie:

1. KLUCZE DZIENNIKA NPC: 'sekcja/id' -> 'id'.
   Dopoki klucz zawieral sekcje, przeniesienie NPC miedzy sekcjami sierocilo
   jego dziennik. Po zmianie NPC mozna przenosic dowolnie.

2. DUBLE: ten sam czlowiek w dwoch sekcjach (howland_reed, ottar_faktor_zbozowy,
   nesta, garrick, medger_cerwyn, donnel...). Rekordy sie scala (bogatszy wygrywa,
   pola sie uzupelniaja), dzienniki lacza w kolejnosci sekcji.

3. SEKCJE: 'na_scenie' ma znaczyc "stoi obok Symona TERAZ", a nie "kiedys stal".
   Symon jest w Winterfell od tygodni, a na scenie siedziala obsada Bialego Portu
   sprzed dwoch lat — razem z Eddardem Starkiem, ktory nie zyje od 298-10.

Nic nie jest kasowane: ludzie sa PRZENOSZENI. Uruchom: python3 gra/porzadki_npc.py [--zapisz]
"""
import json, os, sys, io

D = os.path.dirname(os.path.abspath(__file__))
WPISY = os.path.join(D, "db", "wpisy.jsonl")
RANGA = {"na_scenie": 0, "w_orbicie": 1, "orbita": 2, "poza_scena": 3}

# KTO STOI OBOK SYMONA W WINTERFELL, 299-09-11
WINTERFELL = {
    "maester_luwin", "bran_stark", "sansa_stark", "rickon_stark", "arya_stark",
    "stara_niania", "szafarz_roggen", "rodrik_cassel",
    "lord_medger_cerwyn", "gawen_skarbnik", "ser_alyn_zastepca",
    "rodwell_dyrektor_domu_starkow", "notariusz_beron",
}
# nie zyja / poza swiatem gry
POZA = {"lord_eddard_stark"}

# skroty-duble: ten sam czlowiek zapisany drugi raz uboga kartka (id, imie, rola)
ALIASY = {
    "garrick": "garrick_straznik",
    "nesta": "nesta_braavijka",
    "medger_cerwyn": "lord_medger_cerwyn",
    "donnel": "mistrz_donnel",
    "wylis_manderly": "kasztelan_wylis",
}


def wczytaj(n):
    with io.open(os.path.join(D, n), encoding="utf-8") as f:
        return json.load(f)


def main():
    zapis = "--zapisz" in sys.argv
    npc = wczytaj("npc.json")

    # ---------- 1+2: scalenie rekordow po ID ----------
    scalone, skad = {}, {}
    smieci = 0
    for sekcja in sorted(npc, key=lambda s: RANGA.get(s, 9)):
        zaw = npc[sekcja]
        if not isinstance(zaw, list):
            continue
        for rek in zaw:
            if not isinstance(rek, dict):
                continue
            nid = rek.get("id") or rek.get("imie")
            if not nid or nid == "?":
                smieci += 1
                continue
            nid = ALIASY.get(nid, nid)
            rek = dict(rek, id=nid)
            if nid in scalone:
                for k, v in rek.items():                 # uzupelnij braki
                    if k not in scalone[nid] or scalone[nid][k] in (None, "", "?"):
                        scalone[nid][k] = v
            else:
                scalone[nid] = dict(rek)
                skad[nid] = sekcja

    # ---------- 3: nowy przydzial sekcji ----------
    nowe = {"na_scenie": [], "w_orbicie": [], "orbita": [], "poza_scena": []}
    for nid, rek in scalone.items():
        if nid in POZA:
            cel = "poza_scena"
        elif nid in WINTERFELL:
            cel = "na_scenie"
        elif skad[nid] in ("orbita", "poza_scena"):
            cel = skad[nid]
        else:
            cel = "w_orbicie"
        nowe[cel].append(rek)
    for sekcja, zaw in npc.items():                       # sekcje nie-listowe zostaja
        if not isinstance(zaw, list):
            nowe[sekcja] = zaw

    # ---------- dziennik: rekey + przenumerowanie ----------
    linie = [json.loads(l) for l in io.open(WPISY, encoding="utf-8") if l.strip()]
    grupy, reszta = {}, []
    for w in linie:
        if w["zrodlo"] == "npc" and "/" in w["klucz"]:
            sek, _, nid = w["klucz"].partition("/")
            nid = ALIASY.get(nid, nid)
            grupy.setdefault((nid, w["pole"]), []).append((RANGA.get(sek, 9), w["seq"], w))
        else:
            reszta.append(w)
    nowe_wpisy = []
    for (nid, pole), lst in grupy.items():
        for i, (_, _, w) in enumerate(sorted(lst, key=lambda x: (x[0], x[1]))):
            w = dict(w)
            w["klucz"], w["seq"] = nid, i
            nowe_wpisy.append(w)

    # kontrola: zadna tresc nie moze zniknac
    przed = sorted(x["tresc"] for x in linie)
    po = sorted(x["tresc"] for x in reszta + nowe_wpisy)
    zgodne = przed == po

    print("NPC przed: %d rekordow w listach" % sum(
        len(v) for v in npc.values() if isinstance(v, list)))
    print("NPC po scaleniu: %d unikalnych (%d dubli/smieci usunietych)" % (
        len(scalone), sum(len(v) for v in npc.values() if isinstance(v, list)) - len(scalone)))
    print("  na_scenie %d · w_orbicie %d · orbita %d · poza_scena %d" % (
        len(nowe["na_scenie"]), len(nowe["w_orbicie"]),
        len(nowe["orbita"]), len(nowe["poza_scena"])))
    print("wpisow dziennika: %d (npc przekluczonych: %d)" % (len(linie), len(nowe_wpisy)))
    print("tresci nietkniete:", "TAK" if zgodne else "NIE — PRZERYWAM")
    if not zgodne:
        return 1
    if not zapis:
        print("\n[test na sucho] Uruchom z --zapisz.")
        return 0

    with io.open(WPISY, "w", encoding="utf-8") as f:
        for w in reszta + nowe_wpisy:
            f.write(json.dumps(w, ensure_ascii=False) + "\n")
    with io.open(os.path.join(D, "npc.json"), "w", encoding="utf-8") as f:
        json.dump(nowe, f, ensure_ascii=False, indent=1)
    print("ZAPISANO.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
