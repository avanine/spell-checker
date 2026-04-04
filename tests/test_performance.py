import time
from pathlib import Path
from spell_checker.trie import Trie
from spell_checker.suggestions import suggest

def load_trie():
    data_path = Path(__file__).resolve().parents[1] / "data" / "finnish_words_kotus.txt"
    trie = Trie()
    with open(data_path, encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            if word:
                trie.insert(word)
    return trie

def test_suggest_speed():
    trie = load_trie()
    word = "kisssa"

    start = time.time()
    results = suggest(trie, word)
    elapsed = time.time() - start

    print(f"\nSuggest '{word}': {len(results)} ehdotusta, {elapsed:.2f} s")
