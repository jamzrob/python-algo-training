from katas import day1

def test_merge_sort():
    assert day1.merge_sort([5, 3, 8, 4, 2, 7, 1, 10]) == [1, 2, 3, 4, 5, 7, 8, 10]
    assert day1.merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
