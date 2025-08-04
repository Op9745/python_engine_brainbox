from exercises import is_prime, calculator

def test_is_prime():
    assert is_prime(7)
    assert not is_prime(8)

def test_calculator():
    assert calculator(10, 5, "add") == 15
    assert calculator(10, 0, "div") == "Error: Division by zero"
