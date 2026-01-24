import pytest
from travelpy.convert_currency import convert_currency

def test_invalid_rate():
    """Test that a rate below 0 raises a value error."""
    with pytest.raises(ValueError, match = "Rate must be greater than 0."):
        convert_currency(amount = 50, rate = -0.5)

def test_invalid_amount():
    """Test that an amount below 0 outputs a value error."""
    with pytest.raises(ValueError, match = "Amount must be greater than 0 dollars."):
        convert_currency(amount = -50, rate = 1.2)

def test_amount_0_to_100():
    """Test that a valid amount less than 100 results in a service fee being applied."""
    currency = convert_currency(amount = 50, rate = 1.2)
    assert currency < (50 * 1.2)

def test_amount_above_100():
    """Test that a valid amount greater than 100 results in no service fee being applied."""
    currency = convert_currency(amount = 180, rate = 1.2)
    assert currency == (180 * 1.2)
