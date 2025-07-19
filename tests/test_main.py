import pytest
from main import hello, bye

def test_hello():
    assert hello() == "hi"

def test_bye():
    assert bye() == "bye"
