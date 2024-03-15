from katas import day1


def test_binary_search_list():
    assert day1.bs_list([1, 2, 3, 4, 5], 3) == 2
    assert day1.bs_list([1, 2, 3, 4, 5], 6) == -1
