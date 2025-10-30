from algo import edit_distance


def test_edit_distance_example():
    word1 = "kitten"
    word2 = "sitting"
    assert edit_distance(word1, word2) == 3
