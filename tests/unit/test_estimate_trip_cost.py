"""
A test module that tests the estimate_trip_cost module.
"""
import pytest
from travelpy.estimate_trip_cost import estimate_trip_cost

def test_general_cost():
    assert estimate_trip_cost(100, 2, 4) == 50

def test_long_haul_cost():
    assert estimate_trip_cost(1000, 2, 4) == 575

def test_invalid_distance():
    with pytest.raises(ValueError, match="Distance must be greater than 0 km."):
        estimate_trip_cost(-100, 2, 4)

def test_invalid_fuel_price():
    with pytest.raises(ValueError, match="Fuel price must be greater than 0."):
        estimate_trip_cost(100, -2, 4)

def test_invalid_efficiency():
    with pytest.raises(ValueError, match="Efficiency must be greater than 0."):
        estimate_trip_cost(100, 2, -4)
