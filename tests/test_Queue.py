
from katas import day1

def test_queue():
    queue = day1.Queue()

    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)

    assert queue.dequeue() == 5
    assert queue.length == 2

    queue.enqueue(11)
    assert queue.dequeue() == 7
    assert queue.dequeue() == 9
    assert queue.peek() == 11
    assert queue.dequeue() == 11
    assert queue.dequeue() is None
    assert queue.length == 0

    queue.enqueue(69)
    assert queue.peek() == 69
    assert queue.length == 1
