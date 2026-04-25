import pytest
from spell_checker.trie import Trie
from spell_checker.suggestions import suggest

@pytest.fixture
def trie():
    word_trie = Trie()
    for word in ["kissa", "koira", "kala"]:
        word_trie.insert(word)
    return word_trie

def test_exact_match(trie):
    results = suggest(trie, "kissa")
    assert "kissa" in results

def test_single_edit_found(trie):
    results = suggest(trie, "kisssa")
    assert "kissa" in results

def test_transposition_found(trie):
    results = suggest(trie, "ikssa")
    assert "kissa" in results

def test_too_far_not_suggested(trie):
    results = suggest(trie, "auto")
    assert "kissa" not in results
    assert "koira" not in results
    assert "kala" not in results

def test_frequency_ranking():
    word_trie = Trie()
    word_trie.insert("cat", frequency_rank=0)
    word_trie.insert("car", frequency_rank=1)
    word_trie.insert("cap", frequency_rank=2)
    results = suggest(word_trie, "cas")
    assert results[0] == "cat"
    assert results[1] == "car"
    assert results[2] == "cap"

def test_empty_trie():
    empty_trie = Trie()
    results = suggest(empty_trie, "kissa")
    assert not results
