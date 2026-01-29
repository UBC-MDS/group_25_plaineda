import pytest
from travelpy.format_destination import format_destination

def test_basic():
    """Test standard formatting of lowercase city and country code."""
    assert format_destination("vancouver", "ca") == "Vancouver, CA"

def test_stripping():
    """Test that leading and trailing whitespace is removed from inputs."""
    assert format_destination("  paris ", " fr ") == "Paris, FR"

def test_empty_city():
    """Test that an empty city string raises a ValueError."""
    with pytest.raises(ValueError):
        format_destination("", "US")

def test_invalid_code():
    """Test that a country code not exactly two characters raises a ValueError."""
    with pytest.raises(ValueError):
        format_destination("Rome", "ITA")

def test_non_string():
    """Test that an integer city input raises a TypeError."""
    with pytest.raises(TypeError):
        format_destination(123, "US")

# Milestone 3: Added 4 more unit tests (rubric requirement).

def test_uppercase_city_input():
    """Test that fully capitalized city names are normalized to title case."""
    assert format_destination("TOKYO", "jp") == "Tokyo, JP"

def test_mixed_case_country_code():
    """Test that mixed-case country codes are normalized to uppercase."""
    assert format_destination("berlin", "De") == "Berlin, DE"

def test_empty_country_code():
    """Test that an empty country code string raises a ValueError."""
    with pytest.raises(ValueError):
        format_destination("London", "")

def test_country_code_non_string():
    """Test that a integer country code input raises a TypeError."""
    with pytest.raises(TypeError):
        format_destination("Madrid", 99)