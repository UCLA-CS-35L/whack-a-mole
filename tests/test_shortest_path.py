from algo import shortest_path


def test_shortest_path_example():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert shortest_path(grid) == 4
