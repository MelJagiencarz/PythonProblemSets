from bank import value

def test_hello():
    assert value('Hello') == 0
def test_with_H():
    assert value('Hey') == 20
def test_without_H():
    assert value('What’s up') == 100


