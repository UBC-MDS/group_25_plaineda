"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""
import pytest
from dsci_524_group_25.estimate_trip_cost import estimate_trip_cost

def test_general_cost():
    """Test a valid, non-negative input."""
    assert estimate_trip_cost(100, 2, 4) == 50, f"Expected {50} but got {estimate_trip_cost(100, 2, 4)}"

def test_long_haul_cost():
    """Test a long haul case."""
    assert estimate_trip_cost(1000, 2, 4) == 575, f"Expected {575} but got {estimate_trip_cost(1000, 2, 4)}"

def test_invalid_distance():
    """Test a invalid distance case."""
    with pytest.raises(ValueError, match="Distance must be greater than 0 km."):
        estimate_trip_cost(-100, 2, 4)

def test_invalid_fuel_price():
    """Test a invalid fuel price case."""
    with pytest.raises(ValueError, match="Fuel price must be greater than 0."):
        estimate_trip_cost(100, -2, 4)

def test_invalid_efficiency():
    """Test a invalid efficiency case."""
    with pytest.raises(ValueError, match="Efficiency must be greater than 0."):
        estimate_trip_cost(100, 2, -4)
        