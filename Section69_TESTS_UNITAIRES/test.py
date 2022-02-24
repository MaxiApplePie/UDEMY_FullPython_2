import pytest

from main import add


def test_add_two_numbers():
    assert add(5, 12) == 17


def test_add_two_booleans():
    assert add(True, False) == 1
    assert add(True, True) == 2
    assert add(False, True) == 1


def test_add_two_nones():
    with pytest.raises(TypeError):
        add(None, None)
