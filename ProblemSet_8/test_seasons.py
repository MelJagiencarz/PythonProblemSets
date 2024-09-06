import pytest
from seasons import convert

def test_invalid_format():
    with pytest.raises(SystemExit):
        convert('29-08-2023')
        convert('08-22-2022')
        convert('08-2021-22')

def test_one_year_ago():
    assert convert('2023-08-29') == 'Five hundred twenty-seven thousand forty minutes'

def test_two_years_ago():
    assert convert('2022-08-29') == 'One million, fifty-two thousand, six hundred forty minutes'
