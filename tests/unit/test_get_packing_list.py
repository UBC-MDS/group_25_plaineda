import pytest
from travelpy.get_packing_list import get_packing_list

def test_get_packing_list_duration_validation():
    """Test that duration less than 1 raises ValueError."""
    with pytest.raises(ValueError, match="Trip duration must be at least 1 day."):
        get_packing_list("warm", 0)

def test_get_packing_list_base_items_only():
    """Test that base items are returned for neutral weather and short trips."""
    out = get_packing_list("mild", 3)
    assert out == ["Passport", "Toothbrush"]

def test_get_packing_list_cold_weather():
    """Test that cold weather adds heavy jacket and gloves."""
    out = get_packing_list("cold", 5)
    assert out == ["Passport", "Toothbrush", "Heavy Jacket", "Gloves"]

def test_get_packing_list_rainy_weather():
    """Test that rainy weather adds an umbrella."""
    out = get_packing_list("rainy", 2)
    assert out == ["Passport", "Toothbrush", "Umbrella"]

def test_get_packing_list_warm_long_trip():
    """Test that warm weather and long duration add sunscreen and laundry kit."""
    out = get_packing_list("warm", 10)
    assert out == ["Passport", "Toothbrush", "Sunscreen", "Laundry kit"]

def test_long_trip_boundary_exact_seven():
    """Test that a trip of exactly 7 days does NOT add a laundry kit."""
    assert "Laundry kit" not in get_packing_list("mild", 7)

def test_long_trip_boundary_above_seven():
    """Test that a trip of 8 days adds a laundry kit."""
    assert "Laundry kit" in get_packing_list("mild", 8)

def test_combined_weather_scenarios():
    """Test that combined weather descriptions trigger multiple additions."""
    result = get_packing_list("cold rainy", 3)
    assert "Heavy Jacket" in result
    assert "Umbrella" in result

def test_weather_input_normalization():
    """Test that input is case-insensitive and handles extra whitespace."""
    result = get_packing_list("  CoLd  ", 3)
    assert "Heavy Jacket" in result

def test_invalid_duration_type():
    """Test that a non-numeric duration raises a TypeError."""
    with pytest.raises(TypeError):
        get_packing_list("mild", "five")