from spell_checker.trie import Trie

def test_insert_and_search():
    trie = Trie()
    trie.insert("sanakirja")
    trie.insert("kissa")
    trie.insert("koira")

    assert trie.search("sanakirja")
    assert trie.search("kissa")
    assert trie.search("koira")
    assert not trie.search("sana")
    assert not trie.search("kilpikonna")

def test_empty_trie():
    trie = Trie()
    assert not trie.search("kissa")

def test_iterator():
    trie = Trie()
    trie.insert("kissa")
    trie.insert("koira")
    trie.insert("kala")
    words = sorted(list(trie))
    assert words == ["kala", "kissa", "koira"]
