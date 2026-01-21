# Welcome to TravelPy

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/travelpy.svg)](https://pypi.org/project/travelpy/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/travelpy.svg)](https://pypi.org/project/travelpy/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*

## Overview

TravelPy is a lightweight Python package for travel planning that combines trip budgeting, currency conversion, packing list generation, and destination formatting into one simple toolkit for students and casual travelers.

## Functions

- `estimate_trip_cost(distance, fuel_price, efficiency)`: Calculates total fuel cost for a trip and adds a long-haul contingency fee for trips over 500 miles, returning a rounded total.
- `convert_currency(amount, rate)`: Converts a monetary amount using a provided exchange rate and applies a flat service fee for transactions under $100.
- `get_packing_list(weather, duration)`: Generates a customized packing checklist based on expected weather conditions and trip length, with clear validation for short trips.
- `format_destination(city, country_code)`: Normalizes destination names into a standard "City, COUNTRY_CODE" format, handling empty inputs and validating country codes.

## Python Ecosystem

TravelPy fits into the Python ecosystem alongside focused utilities such as `forex-python` (currency conversion, https://pypi.org/project/forex-python/), `currencyconverter` (offline conversion, https://pypi.org/project/currencyconverter/), and `pycountry` (country code lookup, https://pypi.org/project/pycountry/). Unlike these single-purpose libraries, TravelPy bundles several travel-planning helpers in one place for quick, everyday use.

## Contributors

- Kwok Hoi Hin
- Esteki Hooman
- Jaskiel Derrick
- Rebecca Rosette Nanfuka

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install travelpy
```

To use travelpy in your code:

```python
>>> import travelpy
>>> travelpy.hello_world()
```

## Copyright

- Copyright © 2026 Kwok Hoi Hin, Esteki Hooman, Jaskiel Derrick, Rebecca Rosette Nanfuka.
- Free software distributed under the [MIT License](./LICENSE).
