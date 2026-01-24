# MIT License
#
# Copyright (c) 2026 Kwok Hoi Hin, Esteki Hooman, Jaskiel Derrick, Rebecca Rosette Nanfuka
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
TravelPy - A lightweight Python package for travel planning.

This package provides tools for students and travelers to plan their trips
by considering budgeting, currency conversion, and packing preparation.
"""

from dsci_524_group_25.estimate_trip_cost import estimate_trip_cost
from dsci_524_group_25.convert_currency import convert_currency
from dsci_524_group_25.get_packing_list import get_packing_list
from dsci_524_group_25.format_destination import format_destination

__all__ = [
    "estimate_trip_cost",
    "convert_currency",
    "get_packing_list",
    "format_destination",
]
