from calculator import Calculator

def test_add():
    calculator = calculator()
    assert calculator.add(10, 20) == 30
