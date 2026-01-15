test_example.pyimport pytest
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
