import pytest
from working import convert

def test_without_mins():
    assert convert('7 AM to 6 PM') == '07:00 to 18:00'
    assert convert('8:00 PM to 5:00 PM') == '20:00 to 17:00'

def test_with_mins():
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'
    assert convert('10:30 PM to 8 AM') == '22:30 to 08:00'

def test_errors():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
        convert('9 AM - 5 PM')
        convert('09:00 AM - 17:00 PM')
        convert('9 AM5 PM')
        convert('25 AM to 26     PM')
