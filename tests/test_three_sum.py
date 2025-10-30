from algo import three_sum


def test_three_sum_example():
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert all(sorted(triplet) in [sorted(e) for e in expected] for triplet in result)
    assert len(result) == len(expected)
