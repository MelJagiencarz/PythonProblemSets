from fuel import convert, gauge
import pytest

def test_convert_case():
    assert convert('1/4') == 25
    assert convert('1/2') == 50

def test_convert_exceptions():
    with pytest.raises(ValueError):
          convert("cat/dog")
    with pytest.raises(ValueError):
          convert("4/2")
    with pytest.raises(ZeroDivisionError):
          convert("2/0")

def test_gauge_case():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(75) == '75%'
