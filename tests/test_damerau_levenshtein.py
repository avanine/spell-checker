from spell_checker.damerau_levenshtein import DamerauLevenshtein

dl = DamerauLevenshtein()

def test_identical_words():
    assert dl.distance("kissa", "kissa") == 0

def test_empty_strings():
    assert dl.distance("", "") == 0

def test_one_empty_string():
    assert dl.distance("", "sana") == 4
    assert dl.distance("sana", "") == 4

def test_single_insertion():
    assert dl.distance("kisa", "kissa") == 1

def test_single_deletion():
    assert dl.distance("kissa", "kisa") == 1

def test_single_substitution():
    assert dl.distance("kissa", "kassa") == 1

def test_single_transposition():
    assert dl.distance("ab", "ba") == 1
    assert dl.distance("abcd", "abdc") == 1
    assert dl.distance("abc", "bac") == 1

def test_multiple_edits():
    assert dl.distance("kissa", "koira") == 3
    assert dl.distance("sanakirja", "sana") == 5
    assert dl.distance("poro", "promo") == 2
