import pytest
from dsci_524_group_25.format_destination import format_destination

def test_basic():
    assert format_destination("vancouver", "ca") == "Vancouver, CA"

def test_stripping():
    assert format_destination("  paris ", " fr ") == "Paris, FR"

def test_empty_city():
    with pytest.raises(ValueError):
        format_destination("", "US")

def test_invalid_code():
    with pytest.raises(ValueError):
        format_destination("Rome", "ITA")

def test_non_string():
    with pytest.raises(TypeError):
        format_destination(123, "US")


# Milestone 3: Added 4 more unit tests (rubric requirement).

def test_uppercase_city_input():
    """Milestone 3: Test that uppercase city input is properly title-cased."""
    assert format_destination("TOKYO", "jp") == "Tokyo, JP"

def test_mixed_case_country_code():
    """Milestone 3: Test that mixed case country code is uppercased."""
    assert format_destination("berlin", "De") == "Berlin, DE"

def test_empty_country_code():
    """Milestone 3: Test that empty country code raises ValueError."""
    with pytest.raises(ValueError):
        format_destination("London", "")

def test_country_code_non_string():
    """Milestone 3: Test that non-string country code raises TypeError."""
    with pytest.raises(TypeError):
        format_destination("Madrid", 99)
