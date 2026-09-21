# Skryba — silnik symulacji

Realistyczne tekstowe RPG (po polsku) osadzone w świecie *Pieśni Lodu i Ognia*.
Grasz jako **21-letni piśmienny człowiek nieszlacheckiego pochodzenia** w jednym
z miast Westeros lub w Braavos. Umiesz czytać, pisać i rachować — w świecie,
gdzie potrafi to może jeden na dwudziestu mieszczan. To twoja jedyna przewaga:
bez majątku, bez koligacji, bez rodziny w mieście.

Świat **nie kręci się wokół gracza**. Istnieje niezależnie, ma własne procesy,
a ty jesteś jednym z tysięcy ludzi, których te procesy mielą. Tura to pół dnia.

## Jak grać

Gra jest zaimplementowana jako komenda Claude Code: [`/skryba`](.claude/commands/skryba.md).
Uruchom Claude Code w tym katalogu i wpisz:

```
/skryba nowa
```

Mistrz Gry zada maksymalnie 5 pytań (miasto, skąd znasz litery, obecne
utrzymanie, jedna zaleta, jedno obciążenie), wygeneruje kanon świata i rozpocznie
grę od zwykłego, przyziemnego poranka.

### Komendy

| Komenda | Działanie |
|---|---|
| `/skryba` lub `/skryba dalej` | rozegraj kolejną turę |
| `/skryba nowa` | nowa gra (ostrzega, jeśli `gra/` już istnieje) |
| `/skryba podsumowanie` | stan postaci, relacji, majątku, otwartych spraw |
| `/skryba mapa` | znane miejsca i trasy |
| `/skryba ludzie` | znani NPC z nastawieniem i ostatnim kontaktem |
| `/skryba zapisz` | wymuś zapis + kopia do `gra/backup/` |
| `/skryba meta <pytanie>` | wyjdź z roli, rozmawiaj o zasadach |

## Sześć warstw symulacji

1. **Lokalna** — miasto jako fizyczne miejsce z geografią, którą da się przejść, i rytmem dnia wyznaczanym dzwonami septy.
2. **Personalna** — NPC z potrzebami, harmonogramem i pamięcią; działają także pod nieobecność gracza.
3. **Społeczna** — stan, honor, patronat, pokrewieństwo; pozycja wynika z urodzenia.
4. **Ekonomiczna** — ceny, które się poruszają wraz z sezonem, pogodą, wojną i plotką; dług jako mechanika.
5. **Polityczna** — władza lokalna (rada, straż, cechy, Wiara); wielka polityka tylko w tle.
6. **Informacyjna** — plotka jako mechanika: rozchodzi się przez konkretnych ludzi, zniekształca się, reagują na nią frakcje.

## Stan gry

Cały stan zapisywany jest w katalogu `gra/` (tworzonym przy `nowa`):

- `kanon/` — geografia, kalendarz i ceny bazowe; **niezmienne** po utworzeniu.
- `postac.json`, `swiat.json`, `npc.json`, `frakcje.json`, `siec.json`,
  `plotki.json`, `zegary.json`, `watki.json` — bieżący stan symulacji.
- `kronika.md` — dziennik tur (append-only).
- `ukryte/` — kulisy widoczne tylko dla Mistrza Gry, nigdy dla gracza.

Katalog `gra/` (zapisy) jest ignorowany przez git — każda rozgrywka jest
prywatna i lokalna. Zobacz [`.gitignore`](.gitignore).

## Ton

Surowy realizm: bez heroicznej fantazji, bez magii dla gracza, bez taryfy
ulgowej. Awans mierzy się w latach gry, nie tygodniach. Śmierć i kalectwo są
realne. Pełna specyfikacja silnika znajduje się w
[`.claude/commands/skryba.md`](.claude/commands/skryba.md).
