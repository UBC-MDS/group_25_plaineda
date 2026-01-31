# TravelPy

| | |
|----------|------|
| CI/CD | [![CI Build](https://github.com/UBC-MDS/DSCI_524_group_25/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/DSCI_524_group_25/actions/workflows/build.yml) [![codecov](https://codecov.io/gh/UBC-MDS/DSCI_524_group_25/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/DSCI_524_group_25) |
| Docs | [![Documentation](https://github.com/UBC-MDS/DSCI_524_group_25/actions/workflows/docs.yml/badge.svg)](https://ubc-mds.github.io/DSCI_524_group_25/) |
| Package | [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/) [![TestPyPI](https://img.shields.io/badge/TestPyPI-v0.2.7-blue)](https://test.pypi.org/project/travelpy/) |
| Meta | [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE) [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md) |

## Overview

TravelPy is a lightweight Python package that provides a simplified way for students and travelers to plan their trips by considering budgeting, conversion, and preparing their packing list in one toolkit.

---

## Documentation

Full documentation: **https://ubc-mds.github.io/DSCI_524_group_25/**

---

## Installation

Install from TestPyPI:
```bash
pip install -i https://test.pypi.org/simple/ travelpy
```

---

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
from travelpy.estimate_trip_cost import estimate_trip_cost

estimate_trip_cost(150, 1.7, 12)   # Returns: 21.25
estimate_trip_cost(900, 1.7, 12)   # Returns: 146.62 (includes 15% contingency)
estimate_trip_cost(-100, 1.7, 12)  # ValueError: Distance must be greater than 0 km
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
from travelpy.convert_currency import convert_currency

convert_currency(150, 1.2)  # Returns: 180.0
convert_currency(50, 1.2)   # Returns: 55.0 (fee applied)
convert_currency(-50, 1.2)  # ValueError: Amount must be greater than 5 dollars
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
from travelpy.get_packing_list import get_packing_list

get_packing_list("cold", 3)   # Returns: ["Passport", "Toothbrush", "Heavy Jacket", "Gloves"]
get_packing_list("warm", 10)  # Returns: ["Passport", "Toothbrush", "Sunscreen", "Laundry kit"]
get_packing_list("rainy", 5)  # Returns: ["Passport", "Toothbrush", "Umbrella"]
get_packing_list("cold", 0)   # ValueError: Trip duration must be at least 1 day
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
from travelpy.format_destination import format_destination

format_destination("vancouver", "ca")    # Returns: "Vancouver, CA"
format_destination("  paris ", " fr ")   # Returns: "Paris, FR"
format_destination("TOKYO", "jp")        # Returns: "Tokyo, JP"
format_destination("", "ca")             # ValueError: city and country_code must not be empty
```

---

## Why TravelPy?

TravelPy fits into the broader Python ecosystem as a small utility package that prioritizes integration, clarity, and offline usability over breadth or real-time data. Rather than competing with established libraries like `currencyconverter` or `pycountry`, TravelPy complements them by focusing on common travel-planning workflows. TravelPy is particularly valuable in situations where developers want practical functionality without external APIs, heavy dependencies, or complex configuration.

Planning a trip often involves juggling multiple tools and websites: one for estimating fuel costs, another for currency conversion, and yet another for creating packing lists. **TravelPy solves this problem by bundling these common travel-planning tasks into a single, easy-to-use Python package.**

### The Problem

When planning a road trip or international travel, you typically need to:

- Calculate fuel costs using distance, gas prices, and vehicle efficiency
- Convert your budget to foreign currencies with realistic fee expectations
- Create weather-appropriate packing lists based on trip duration
- Format destination names consistently for itineraries or documents

Each of these tasks individually is simple arithmetic or string manipulation, but **the value of TravelPy is integration and convenience**. Instead of writing custom code or using multiple websites, TravelPy provides tested, documented functions that handle edge cases (like long-trip contingencies, small-transaction fees, and input validation).

### Who Should Use TravelPy?

- **Students** learning Python who want practical, real-world examples
- **Travelers** who prefer programmatic trip planning over web tools
- **Developers** building travel-related applications who need utility functions
- **Data scientists** analyzing travel costs or patterns

### How TravelPy Complements the Python Ecosystem

| Existing Package | Purpose | TravelPy Difference |
|------------------|---------|---------------------|
| [forex-python](https://pypi.org/project/forex-python/) | Real-time currency rates via API | TravelPy uses user-provided rates (works offline, includes fee logic) |
| [currencyconverter](https://pypi.org/project/currencyconverter/) | Historical exchange rates | TravelPy focuses on trip budgeting with service fees |
| [pycountry](https://pypi.org/project/pycountry/) | Country/language codes | TravelPy formats destinations for display, not lookup |

**TravelPy is intentionally simple and dependency-free**, making it ideal for learning, lightweight scripts, or embedding in larger applications without bloating dependencies.

---

## Quick Start

```python
from travelpy.estimate_trip_cost import estimate_trip_cost
from travelpy.convert_currency import convert_currency
from travelpy.get_packing_list import get_packing_list
from travelpy.format_destination import format_destination

# Plan a trip to Paris
destination = format_destination("paris", "fr")  # "Paris, FR"
fuel_cost = estimate_trip_cost(500, 1.8, 10)     # $103.5 CAD
budget_eur = convert_currency(500, 0.68)          # €340.0
packing = get_packing_list("cold", 7)             # ['Passport', 'Toothbrush', 'Heavy Jacket', 'Gloves']
```

---

## Developer Guide

### Clone the Repository

```bash
git clone https://github.com/UBC-MDS/DSCI_524_group_25.git
cd DSCI_524_group_25
```

### Set up the Development Environment

```bash
conda env create -f environment.yml
conda activate travelpy
```

### Install the Package in Development Mode

```bash
pip install -e .
```

### Run Tests

```bash
hatch run test:run
```

### Build Documentation

```bash
quartodoc build
quarto render
```

Or using hatch:
```bash
hatch run docs:build
```

### Preview Documentation

```bash
quarto preview
```

Or using hatch:
```bash
hatch run docs:serve
```

### Deploy Documentation

Documentation is automatically deployed to GitHub Pages on push to `main` via GitHub Actions.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. This project follows a [Code of Conduct](CODE_OF_CONDUCT.md).

## Contributors

- Hoi Hin Kwok 
- Hooman Esteki 
- Derrick Jaskiel 
- Rebecca Rosette Nanfuka

## Citation

If you use TravelPy in your work, please cite:

```
Kwok, H.H., Esteki, H., Jaskiel, D., & Nanfuka, R.R. (2026). TravelPy: A Python package for travel planning. 
https://github.com/UBC-MDS/DSCI_524_group_25
```

## License

MIT License © 2026 Hoi Hin Kwok, Hooman Esteki, Derrick Jaskiel and Rebecca Rosette Nanfuka.
