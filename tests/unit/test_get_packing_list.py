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
```
