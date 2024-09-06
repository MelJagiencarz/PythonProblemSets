from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._cookies == 0
    jar2 = Jar(26)
    assert jar2._capacity == 26

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(11)
    jar.deposit(6)
    assert jar._cookies == 6
    with pytest.raises(ValueError):
        jar.deposit(12)

def test_withdraw():
    jar = Jar(11)
    jar.deposit(6)
    jar.withdraw(1)
    assert jar._cookies == 5
    with pytest.raises(ValueError):
        jar.withdraw(7)
