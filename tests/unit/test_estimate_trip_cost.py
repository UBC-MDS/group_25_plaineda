"""
A test module that tests the estimate_trip_cost module.
"""
import pytest
from travelpy.estimate_trip_cost import estimate_trip_cost

def test_general_cost_short_trip():
    """Test a standard trip cost calculation without surcharge."""
    assert estimate_trip_cost(100, 2, 4) == pytest.approx(50.0)

def test_boundary_exact_500_no_surcharge():
    """Test that a distance of exactly 500km has no surcharge applied."""
    assert estimate_trip_cost(500, 1, 10) == pytest.approx(50.0)
    
def test_long_haul_cost_surcharge():
    """Test that long trips include the surcharge."""
    assert estimate_trip_cost(1000, 2, 4) == pytest.approx(575.0)

def test_invalid_distance_negative():
    """Test that a negative distance raises a ValueError."""
    with pytest.raises(ValueError, match="Distance must be greater than 0"):
        estimate_trip_cost(-100, 2, 4)

def test_invalid_distance_zero():
    """Test that a distance of 0 raises a ValueError."""
    with pytest.raises(ValueError, match="Distance must be greater than 0"):
        estimate_trip_cost(0, 2, 4)

def test_invalid_fuel_price_negative():
    """Test that a negative fuel price raises a ValueError."""
    with pytest.raises(ValueError, match="Fuel price must be greater than 0"):
        estimate_trip_cost(100, -2, 4)

def test_invalid_fuel_price_zero():
    """Test that a fuel price of 0 raises a ValueError."""
    with pytest.raises(ValueError, match="Fuel price must be greater than 0"):
        estimate_trip_cost(100, 0, 4)

def test_invalid_efficiency_negative():
    """Test that negative efficiency raises a ValueError."""
    with pytest.raises(ValueError, match="Efficiency must be greater than 0"):
        estimate_trip_cost(100, 2, -4)

def test_invalid_efficiency_zero():
    """Test that 0 efficiency raises a ValueError."""
    with pytest.raises(ValueError, match="Efficiency must be greater than 0"):
        estimate_trip_cost(100, 2, 0)
        
def test_invalid_input_types():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError):
        estimate_trip_cost("100", 2, 4)
    with pytest.raises(TypeError):
        estimate_trip_cost(100, "2", 4)
    with pytest.raises(TypeError):
        estimate_trip_cost(100, 2, "4")
        