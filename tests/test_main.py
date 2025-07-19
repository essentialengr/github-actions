# test_main.py
from main import bye, hello


def test_hello():
    assert hello() == "hi"


def test_bye():
    assert bye() == "bye"
