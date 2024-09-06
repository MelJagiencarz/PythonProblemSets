from numb3rs import validate
import pytest

def test_3repititions():
    assert validate('222.111.133.1000') == False
    assert validate('123.2.133.82') == True

def test_greater_than_255():
    assert validate('275.0.1.0') == False
    assert validate('200.0.0.276') == False
    assert validate('255.255.255.255') == True

def test_not_an_ip():
    assert validate('bunny') == False

def test_valid():
    assert validate('192.168.1.1') == True
    assert validate('0.0.0.0') == True
