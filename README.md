# TravelPy

[![CI Build](https://github.com/UBC-MDS/DSCI_524_group_25/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_group_25/actions/workflows/build.yml)
[![Deploy to TestPyPI](https://github.com/UBC-MDS/DSCI_524_group_25/actions/workflows/deploy.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_group_25/actions/workflows/deploy.yml)
[![Documentation](https://github.com/UBC-MDS/DSCI_524_group_25/actions/workflows/docs.yml/badge.svg)](https://ubc-mds.github.io/DSCI_524_group_25/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

## Overview

TravelPy is a lightweight Python package that provides a simplified way for students and travelers to plan their trips by considering budgeting, conversion, and preparing their packing list in one toolkit.

## Installation

Install from TestPyPI:

```bash
pip install -i https://test.pypi.org/simple/ dsci_524_group_25
```

## Functions

### `estimate_trip_cost(distance, fuel_price, efficiency)`

Calculates total fuel cost for a trip in Canada (metric units), including a 15% contingency fee for trips over 500 km.

| Parameter | Type | Description |
|-----------|------|-------------|
| `distance` | float | Distance of the trip in kilometers |
| `fuel_price` | float | Price of fuel per liter (CAD/L) |
| `efficiency` | float | Fuel efficiency in km/L |

**Returns:** `float`, Estimated cost rounded to 2 decimal places.

```python
from dsci_524_group_25.estimate_trip_cost import estimate_trip_cost

estimate_trip_cost(150, 1.7, 12)   # Returns: 21.25
estimate_trip_cost(900, 1.7, 12)   # Returns: 146.62 (includes 15% contingency)
```

---

### `convert_currency(amount, rate)`

Converts a monetary amount using a provided exchange rate. Applies a $5 service fee for transactions under $100.

| Parameter | Type | Description |
|-----------|------|-------------|
| `amount` | float | Original amount to convert (must be positive) |
| `rate` | float | Exchange rate (must be positive) |

**Returns:** `float`, Converted amount after fees.

```python
from dsci_524_group_25.convert_currency import convert_currency

convert_currency(150, 1.2)  # Returns: 180.0
convert_currency(50, 1.2)   # Returns: 55.0 (fee applied)
```

---

### `get_packing_list(weather, duration)`

Generates a packing checklist based on weather conditions and trip duration.

| Parameter | Type | Description |
|-----------|------|-------------|
| `weather` | str | Expected conditions: "cold", "warm", or "rainy" |
| `duration` | int | Number of days for the trip |

**Returns:** `list`, Packing items based on conditions.

```python
from dsci_524_group_25.get_packing_list import get_packing_list

get_packing_list("cold", 3)   # Returns: ["Passport", "Toothbrush", "Heavy Jacket", "Gloves"]
get_packing_list("warm", 10)  # Returns: ["Passport", "Toothbrush", "Sunscreen", "Laundry kit"]
get_packing_list("rainy", 5)  # Returns: ["Passport", "Toothbrush", "Umbrella"]
```

---

### `format_destination(city, country_code)`

Normalizes destination names into "City, COUNTRY_CODE" format.

| Parameter | Type | Description |
|-----------|------|-------------|
| `city` | str | City name |
| `country_code` | str | Two-letter country code |

**Returns:** `str`, Formatted destination string.

```python
from dsci_524_group_25.format_destination import format_destination

format_destination("vancouver", "ca")    # Returns: "Vancouver, CA"
format_destination("  paris ", " fr ")   # Returns: "Paris, FR"
format_destination("TOKYO", "jp")        # Returns: "Tokyo, JP"
```

---

## Documentation

Full documentation: **https://ubc-mds.github.io/DSCI_524_group_25/**

---

## Developer Guide

### Set up the development environment

```bash
conda env create -f environment.yml
conda activate dsci_524_group_25
```

### Install the package

```bash
pip install -e .
```

### Run tests

```bash
hatch run test:run
```

### Build documentation

```bash
quartodoc build
quarto render
```

Or using hatch:

```bash
hatch run docs:build
```

### Deploy documentation

Documentation is automatically deployed to GitHub Pages on push to `main` via GitHub Actions.

---

## Python Ecosystem

TravelPy complements existing Python utilities:

- [forex-python](https://pypi.org/project/forex-python/) : Currency conversion
- [currencyconverter](https://pypi.org/project/currencyconverter/) : Offline conversion
- [pycountry](https://pypi.org/project/pycountry/) : Country code lookup

Unlike single-purpose libraries, TravelPy bundles multiple travel-planning tools in one package.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. This project follows a [Code of Conduct](CODE_OF_CONDUCT.md).

## Contributors

- Kwok Hoi Hin
- Esteki Hooman
- Jaskiel Derrick
- Rebecca Rosette Nanfuka

## License

MIT License © 2026 Kwok Hoi Hin, Esteki Hooman, Jaskiel Derrick and Rebecca Rosette Nanfuka.
