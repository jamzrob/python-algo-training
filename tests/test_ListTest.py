from .context import day1

def test_list(list_instance: DoublyLinkedList):
    list_instance.append(5)
    list_instance.append(7)
    list_instance.append(9)

    assert list_instance.get(2) == 9
    assert list_instance.removeAt(1) == 7
    assert len(list_instance) == 2

    list_instance.append(11)
    assert list_instance.removeAt(1) == 9
    assert list_instance.remove(9) is None
    assert list_instance.removeAt(0) == 5
    assert list_instance.removeAt(0) == 11
    assert len(list_instance) == 0

    list_instance.prepend(5)
    list_instance.prepend(7)
    list_instance.prepend(9)

    assert list_instance.get(2) == 5
    assert list_instance.get(0) == 9
    assert list_instance.remove(9) == 9
    assert len(list_instance) == 2
    assert list_instance.get(0) == 7
