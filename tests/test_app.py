import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import add, is_even

def test_add():
    assert add(2, 3) == 5

def test_is_even():
    assert is_even(4)
    assert not is_even(5)
