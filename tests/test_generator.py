import pytest

from src.generator import random_str


def test_length_8():
    length = len(random_str(length=8))

    assert length == 8


def test_length_12():
    length = len(random_str(length=12))

    assert length == 12
