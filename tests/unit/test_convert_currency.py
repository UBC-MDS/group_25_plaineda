import pytest
from travelpy.convert_currency import convert_currency

def test_invalid_rate_negative():
    """Test that a negative rate raises a ValueError."""
    with pytest.raises(ValueError, match="Rate must be greater than 0"):
        convert_currency(amount=50, rate=-0.5)

def test_invalid_rate_zero():
    """Test that a rate of 0 raises a ValueError."""
    with pytest.raises(ValueError, match="Rate must be greater than 0"):
        convert_currency(amount=50, rate=0)

def test_invalid_amount_negative():
    """Test that a negative amount raises a ValueError."""
    with pytest.raises(ValueError, match="Amount must be greater than 5"):
        convert_currency(amount=-50, rate=1.2)

def test_invalid_amount_less_five():
    """Test that an amount between 0 and 5 raises a ValueError."""
    with pytest.raises(ValueError, match="Amount must be greater than 5"):
        convert_currency(amount=-50, rate=1.2)

def test_invalid_amount_zero():
    """Test that an amount of 0 raises a ValueError (Edge Case)."""
    with pytest.raises(ValueError, match="Amount must be greater than 5"):
        convert_currency(amount=0, rate=1.2)

def test_amount_0_to_100():
    """Test that a valid amount less than 100 results in a service fee being applied."""
    currency = convert_currency(amount = 50, rate = 1.2)
    assert currency < (50 * 1.2)

def test_amount_above_100():
    """Test that a valid amount greater than 100 results in no service fee being applied."""
    currency = convert_currency(amount = 180, rate = 1.2)
    assert currency == (180 * 1.2)

def test_invalid_input_types():
    """Test that specific invalid types (string, None) raise a TypeError."""
    with pytest.raises(TypeError):
        convert_currency(amount="fifty", rate=1.2)
    with pytest.raises(TypeError):
        convert_currency(amount=50, rate="1.2")
    with pytest.raises(TypeError):
        convert_currency(amount=50, rate=None)