from algo import subset_sum


def test_subset_sum_example():
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    assert subset_sum(nums, target) is True
