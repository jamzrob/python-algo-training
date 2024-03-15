from katas import day1

def test_bubble_sort():
    arr = [9, 3, 7, 4, 69, 420, 42]
    day1.bubble_sort(arr)
    assert arr == [3, 4, 7, 9, 42, 69, 420]
