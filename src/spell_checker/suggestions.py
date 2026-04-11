"""Kirjoitusvirheiden korjausehdotusten hakeminen."""

from spell_checker.damerau_levenshtein import DamerauLevenshtein

def suggest(trie, word, max_distance=2):
    """Hakee korjausehdotuksia käymällä trieä läpi ja karsimalla haaroja.
    Palauttaa enintään 5 lähintä sanaa, joiden etäisyys on enintään max_distance."""
    dl = DamerauLevenshtein()
    word = word.lower()
    results = []
    initial_row = list(range(len(word) + 1))

    for char, child_node in trie.root.children.items():
        _search_trie(
            dl, child_node, char, word, "", None,
            initial_row, None, results, max_distance
        )

    results.sort(key=lambda x: x[0])
    return [s for _, s in results[:5]]

def _search_trie(dl, node, char, word, prefix, prev_char,
                 previous_row, two_rows_back, results, max_distance):
    """Käy läpi trieä rekursiivisesti ja laskee DL-etäisyyden rivi kerrallaan."""
    current_prefix = prefix + char
    current_row = dl.compute_row(word, char, prev_char, previous_row, two_rows_back)

    if node.is_end_of_word and current_row[-1] <= max_distance:
        results.append((current_row[-1], current_prefix))

    if min(current_row) <= max_distance:
        for next_char, next_node in node.children.items():
            _search_trie(
                dl, next_node, next_char, word, current_prefix, char,
                current_row, previous_row, results, max_distance
            )
