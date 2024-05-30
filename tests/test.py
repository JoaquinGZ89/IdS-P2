from code import sum

def test_add():
    assert sum(1, 2) == 3
    assert sum(-1, 1) == 0
    assert sum(-1, -1) == -2