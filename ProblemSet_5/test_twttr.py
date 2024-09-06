from twttr import shorten

def test_lowercase():
    assert shorten('banana') == 'bnn'
    assert shorten('kiwi') == 'kw'

def test_uppercase():
    assert shorten('BANANA') == 'BNN'
    assert shorten('KIWI') == 'KW'

def test_with_numbers():
    assert shorten('banana3') == 'bnn3'
    assert shorten('BANANA4') == 'BNN4'

def test_without_vocals():
    assert shorten('CS50') == 'CS50'

def test_with_punctuation():
    assert shorten('CS.50') == 'CS.50'
