import pytest
from src.hello import say_hello

def test_say_hello_returns_correct_string():
    expected = "Hello, World!"
    result = say_hello()
    assert expected == result, f"Expected: {expected}, but got: {result}"
