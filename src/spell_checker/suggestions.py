"""Kirjoitusvirheiden korjausehdotusten hakeminen."""

from spell_checker.damerau_levenshtein import DamerauLevenshtein

def suggest(trie, word, max_distance=2):
    """Vertaa annettua sanaa jokaiseen sanakirjan sanaan yksi kerrallaan.
    Palauttaa listan sanoista, joiden etäisyys on enintään max_distance."""
    dl = DamerauLevenshtein()
    suggestions = []
    for trie_word in trie:
        if dl.distance(word, trie_word) <= max_distance:
            suggestions.append(trie_word)
    return suggestions
