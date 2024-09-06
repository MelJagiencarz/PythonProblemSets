from plates import is_valid

def test_validone():
    assert is_valid('CS50') == True
    assert is_valid('CSTR') == True

def test_tooshort():
    assert is_valid('H') == False

def test_toolong():
    assert is_valid('OUTATIME') == False

def test_first_num_0():
    assert is_valid('CS07') == False

def test_punctuation():
    assert is_valid('CS 07') == False
    assert is_valid('CS50!') == False

def test_nums():
    assert is_valid('CS50P') == False
    assert is_valid('50CS') == False


