#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MIGRACJA: dzienniki dopisywane ("nota", "stan", pola ad-hoc) wychodza z JSON-ow
do gra/db/wpisy.jsonl jako osobne rekordy. W plikach zrodlowych zostaje METADANA.

Gwarancja: migracja jest BAJTOWO ODWRACALNA. Sklejenie wpisow separatorem '||'
odtwarza oryginalny string co do znaku. Weryfikator ponizej to sprawdza i
przerywa migracje, jesli cokolwiek sie nie zgadza.

Uruchom:  python3 gra/migracja_jsonl.py            (test na sucho, nic nie zapisuje)
          python3 gra/migracja_jsonl.py --zapisz   (wykonuje migracje)
"""
import json, os, re, sys, io

D = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(D, "db")
SEP = "||"
PROG_DZIENNIKA = 400          # string dluzszy niz to = dziennik, nie metadana
DATA_RE = re.compile(r"^\s*(\d{3})-(\d{2})-(\d{2})")

# pola, ktore ZAWSZE zostaja w pliku zrodlowym (metadana, nie dziennik)
METADANA = {"id", "tytul", "status", "priorytet", "typ", "termin", "wobec",
            "waga", "widoczny_graczowi", "imie", "zawod", "rola",
            "nastawienie_do_gracza", "zaufanie", "rok_urodzenia", "wiek",
            "data_urodzin", "lokacja", "frakcja"}


def wczytaj(nazwa):
    with io.open(os.path.join(D, nazwa), encoding="utf-8") as f:
        return json.load(f)


def jest_dziennikiem(pole, wartosc):
    if pole in METADANA or not isinstance(wartosc, str):
        return False
    return SEP in wartosc or len(wartosc) > PROG_DZIENNIKA


def tnij(s):
    """Dzieli dziennik na surowe kawalki. Sklejenie przez SEP odtwarza oryginal."""
    return s.split(SEP)


def data_wpisu(kawalek, ostatnia):
    m = DATA_RE.match(kawalek)
    if m:
        return "%s-%s-%s" % m.groups()
    return ostatnia


def zbierz(zrodlo, klucz, obiekt, wpisy, ostatnia_data):
    """Wyjmuje z obiektu pola-dzienniki. Zwraca (metadana, liczba_wpisow)."""
    meta, n = {}, 0
    for pole, wartosc in obiekt.items():
        if jest_dziennikiem(pole, wartosc):
            kawalki = tnij(wartosc)
            d = ostatnia_data
            for i, kaw in enumerate(kawalki):
                d = data_wpisu(kaw, d)
                wpisy.append({
                    "zrodlo": zrodlo, "klucz": klucz, "pole": pole,
                    "seq": i, "data": d, "tresc": kaw,
                })
            n += len(kawalki)
            meta["_dziennik_" + pole] = len(kawalki)
        else:
            meta[pole] = wartosc
    return meta, n


def odtworz(wpisy):
    """Weryfikacja: sklada wpisy z powrotem w oryginalne stringi."""
    buf = {}
    for w in wpisy:
        buf.setdefault((w["zrodlo"], w["klucz"], w["pole"]), []).append((w["seq"], w["tresc"]))
    return {k: SEP.join(t for _, t in sorted(v)) for k, v in buf.items()}


def main():
    zapis = "--zapisz" in sys.argv
    wpisy = []
    nowe = {}

    # ---------- WATKI ----------
    w = wczytaj("watki.json")
    watki_meta = []
    for rek in w.get("watki", []):
        wid = rek.get("id") or "bez_id_%d" % len(watki_meta)
        meta, _ = zbierz("watki", wid, rek, wpisy, None)
        watki_meta.append(meta)
    # bledne klucze najwyzszego poziomu (dodane omylkowo jako stringi) -> normalne watki
    for k, v in w.items():
        if k == "watki":
            continue
        if isinstance(v, str):
            meta, _ = zbierz("watki", k, {"id": k, "status": "otwarty", "nota": v}, wpisy, None)
            watki_meta.append(meta)
        else:
            nowe.setdefault("watki_inne", {})[k] = v
    nowe["watki.json"] = {"watki": watki_meta}

    # ---------- NPC ----------
    n = wczytaj("npc.json")
    npc_nowe = {}
    for sekcja, zawartosc in n.items():
        if isinstance(zawartosc, list):
            lista = []
            for rek in zawartosc:
                if isinstance(rek, dict):
                    nid = sekcja + "/" + (rek.get("id") or rek.get("imie") or "npc_%d" % len(lista))
                    meta, _ = zbierz("npc", nid, rek, wpisy, None)
                    lista.append(meta)
                else:
                    lista.append(rek)
            npc_nowe[sekcja] = lista
        elif isinstance(zawartosc, dict):
            d = {}
            for nid, rek in zawartosc.items():
                if isinstance(rek, dict):
                    meta, _ = zbierz("npc", sekcja + "/" + nid, rek, wpisy, None)
                    d[nid] = meta
                elif isinstance(rek, str) and jest_dziennikiem("nota", rek):
                    meta, _ = zbierz("npc", sekcja + "/" + nid, {"nota": rek}, wpisy, None)
                    d[nid] = meta
                else:
                    d[nid] = rek
            npc_nowe[sekcja] = d
        else:
            npc_nowe[sekcja] = zawartosc
    nowe["npc.json"] = npc_nowe

    # ---------- SWIAT / POSTAC (plaskie slowniki blobow) ----------
    for plik, zrodlo in (("swiat.json", "swiat"), ("postac.json", "postac")):
        src = wczytaj(plik)
        meta, _ = zbierz(zrodlo, zrodlo, src, wpisy, None)
        nowe[plik] = meta

    # ---------- WERYFIKACJA BAJTOWA ----------
    odtworzone = odtworz(wpisy)
    bledy, sprawdzone = [], 0
    zrodla = {"watki.json": None, "npc.json": None, "swiat.json": None, "postac.json": None}
    for plik in zrodla:
        zrodla[plik] = wczytaj(plik)

    def porownaj(zrodlo, klucz, obiekt):
        nonlocal sprawdzone
        for pole, wartosc in obiekt.items():
            if jest_dziennikiem(pole, wartosc):
                sprawdzone += 1
                got = odtworzone.get((zrodlo, klucz, pole))
                if got != wartosc:
                    bledy.append("%s/%s/%s" % (zrodlo, klucz, pole))

    for rek in zrodla["watki.json"].get("watki", []):
        porownaj("watki", rek.get("id"), rek)
    for k, v in zrodla["watki.json"].items():
        if k != "watki" and isinstance(v, str):
            porownaj("watki", k, {"nota": v})
    for sekcja, zawartosc in zrodla["npc.json"].items():
        if isinstance(zawartosc, list):
            for rek in zawartosc:
                if isinstance(rek, dict):
                    porownaj("npc", sekcja + "/" + (rek.get("id") or rek.get("imie") or ""), rek)
        elif isinstance(zawartosc, dict):
            for nid, rek in zawartosc.items():
                if isinstance(rek, dict):
                    porownaj("npc", sekcja + "/" + nid, rek)
                elif isinstance(rek, str) and jest_dziennikiem("nota", rek):
                    porownaj("npc", sekcja + "/" + nid, {"nota": rek})
    porownaj("swiat", "swiat", zrodla["swiat.json"])
    porownaj("postac", "postac", zrodla["postac.json"])

    print("wpisow wyodrebnionych: %d" % len(wpisy))
    print("dziennikow sprawdzonych: %d" % sprawdzone)
    print("bledow odtworzenia: %d" % len(bledy))
    if bledy:
        for b in bledy[:10]:
            print("   BLAD:", b)
        print("MIGRACJA PRZERWANA — nie zapisuje niczego.")
        return 1

    if not zapis:
        print("\n[test na sucho] Wszystko sie zgadza. Uruchom z --zapisz, zeby wykonac.")
        return 0

    os.makedirs(DB, exist_ok=True)
    with io.open(os.path.join(DB, "wpisy.jsonl"), "w", encoding="utf-8") as f:
        for rek in wpisy:
            f.write(json.dumps(rek, ensure_ascii=False) + "\n")
    for plik, dane in nowe.items():
        if not plik.endswith(".json"):
            continue
        with io.open(os.path.join(D, plik), "w", encoding="utf-8") as f:
            json.dump(dane, f, ensure_ascii=False, indent=1)
    print("ZAPISANO: gra/db/wpisy.jsonl + odchudzone %s" % ", ".join(
        k for k in nowe if k.endswith(".json")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
