"""Kirjoitusvirheiden korjausehdotusten hakeminen."""

from spell_checker.damerau_levenshtein import DamerauLevenshtein

def suggest(trie, word, max_distance=2):
    """Vertaa annettua sanaa jokaiseen sanakirjan sanaan yksi kerrallaan.
    Palauttaa enintään 5 lähintä sanaa, joiden etäisyys on enintään max_distance."""
    dl = DamerauLevenshtein()
    suggestions = []
    for trie_word in trie:
        dist = dl.distance(word, trie_word)
        if dist <= max_distance:
            suggestions.append((dist, trie_word))
    suggestions.sort(key=lambda x: x[0])
    return [s for _, s in suggestions[:5]]
