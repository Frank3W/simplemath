from simplemath.numbers import get_fibonacci

def test_fibonacci():
    assert get_fibonacci(1) == [1]
    assert get_fibonacci(2) == [1, 1]
    assert get_fibonacci(3) == [1, 1, 2]