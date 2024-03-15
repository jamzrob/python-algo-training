from katas import day1

def test_stack_push():
    s = day1.Stack()
    s.push(1)
    assert s.peek() == 1
    s.push(2)
    assert s.peek() == 2

def test_stack_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1

def test_stack_peek():
    s = Stack()
    s.push(1)
    assert s.peek() == 1
    s.push(2)
    assert s.peek() == 2
