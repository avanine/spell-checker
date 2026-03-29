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

def test_empty_trie():
    empty_trie = Trie()
    results = suggest(empty_trie, "kissa")
    assert not results
