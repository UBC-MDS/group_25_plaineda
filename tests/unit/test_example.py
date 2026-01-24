"""
A test module that tests the example module.
"""

from travelpy.example import add_numbers

def test_add_numbers():
    """
    Test that add_numbers works as expected.
    """
    out = add_numbers(1, 2)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"