from levenshtein_distance import levenshtein_distance


def test_levenshtein_distance():
    str1 = 'kitten'
    str2 = 'sitting'
    d = levenshtein_distance(str1, str2)
    assert d == 3

    str1 = 'cute cat'
    str2 = 'cute cat'
    d = levenshtein_distance(str1, str2)
    assert d == 0

