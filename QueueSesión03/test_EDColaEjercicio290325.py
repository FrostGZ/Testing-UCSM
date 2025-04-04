import pytest 
from EDColaEjercicio290325 import Queue
@pytest.mark.parametrize("size_max, expected_size, expected_empty", [
    (5, 0, True),
    (10, 0, True),
    (3, 0, True),
])
def test_inicializacion(size_max, expected_size, expected_empty):
    q = Queue(size_max)
    assert q.max == size_max
    assert q.size == expected_size
    assert q.empty() == expected_empty

@pytest.mark.parametrize("size_max, values_to_enqueue, expected_data", [
    (5, [10, 20, 30], [10, 20, 30, 0, 0]),
    (2, [10, 20], [10, 20]),
])
def test_enqueue(size_max, values_to_enqueue, expected_data):
    q = Queue(size_max)
    for val in values_to_enqueue:
        q.enqueue(val)
    
    for i in range(len(values_to_enqueue)):
        assert q.data[i] == expected_data[i]

@pytest.mark.parametrize("size_max, values_to_enqueue, expected_full", [
    (2, [10, 20], True),
    (3, [10, 20, 30], True),
    (3, [10, 20], False),
])
def test_full(size_max, values_to_enqueue, expected_full):
    q = Queue(size_max)
    for val in values_to_enqueue:
        q.enqueue(val)
    assert q.full() == expected_full

@pytest.mark.parametrize("size_max, values_to_enqueue, expected_dequeued", [
    (5, [10, 20, 30], 10),
    (3, [5, 10], 5),
])
def test_dequeue(size_max, values_to_enqueue, expected_dequeued):
    q = Queue(size_max)
    for val in values_to_enqueue:
        q.enqueue(val)
    
    assert q.dequeue() == expected_dequeued

@pytest.mark.parametrize("size_max, values_to_enqueue, expected_empty", [
    (3, [], True),
    (3, [10], False),
])
def test_empty(size_max, values_to_enqueue, expected_empty):
    q = Queue(size_max)
    for val in values_to_enqueue:
        q.enqueue(val)
    assert q.empty() == expected_empty

@pytest.mark.parametrize("size_max, values_to_enqueue, expected_dequeued", [
    (3, [], None),
])
def test_dequeue_empty(size_max, values_to_enqueue, expected_dequeued):
    q = Queue(size_max)
    for val in values_to_enqueue:
        q.enqueue(val)
    assert q.dequeue() == expected_dequeued
@pytest.mark.parametrize("size_max, values_to_enqueue, expected_full", [
    (2, [10, 20], True),
    (3, [10, 20, 30], True),
])
def test_enqueue_when_full(size_max, values_to_enqueue, expected_full):
    q = Queue(size_max)
    for val in values_to_enqueue:
        q.enqueue(val)
    assert q.full() == expected_full

@pytest.mark.parametrize("size_max, values_to_enqueue, expected_dequeued", [
    (3, [10, 20, 30], 10),
    (3, [15, 25], 15),
])
def test_circular_behavior(size_max, values_to_enqueue, expected_dequeued):
    q = Queue(size_max)
    for val in values_to_enqueue:
        q.enqueue(val)
    
    assert q.dequeue() == expected_dequeued

@pytest.mark.parametrize("size_max, expected_empty, enqueue_values, expected_dequeued", [
    (2, True, [10, 11], [10, 11]),
])
def test1(size_max, expected_empty, enqueue_values, expected_dequeued):
    q = Queue(size_max)
    assert q.empty() == expected_empty
    for val in enqueue_values:
        assert q.enqueue(val) == True
    for expected in expected_dequeued:
        assert q.dequeue() == expected
    assert q.empty() == True

@pytest.mark.parametrize("size_max, expected_dequeued, expected_empty", [
    (3, None, True),
])
def test2(size_max, expected_dequeued, expected_empty):
    q = Queue(size_max)
    assert q.dequeue() == expected_dequeued
    assert q.empty() == expected_empty

@pytest.mark.parametrize("size_max, enqueue_values, expected_dequeued, expected_full, expected_empty", [
    (3, [10, 20, 30], [10, 20, 30], False, True),
])
def test3(size_max, enqueue_values, expected_dequeued, expected_full, expected_empty):
    q = Queue(size_max)
    for val in enqueue_values:
        assert q.enqueue(val) == True
    
    for expected in expected_dequeued:
        assert q.dequeue() == expected

    assert q.empty() == expected_empty
    assert q.full() == expected_full
    assert q.enqueue(40) == True
    assert q.enqueue(50) == True
    assert q.dequeue() == 40
    assert q.dequeue() == 50