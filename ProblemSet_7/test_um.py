from um import count
import pytest

def test_words():
    assert count('Um yummy') == 1
    assert count('Umbrella') == 0

def test_uppercase():
    assert count('UM...') == 1
    assert count('Um thanks') == 1

def test_simbols():
    assert count('Um?') == 1
    assert count('Um... UM') == 2
