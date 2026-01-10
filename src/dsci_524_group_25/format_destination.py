def format_destination(city, country_code):
    """
    Normalize destination names into the format: "City, COUNTRY_CODE".

    Rules:
      - city and country_code must be non-empty strings after stripping
      - country_code must be exactly 2 alphabetic letters
      - city is title-cased; country_code is upper-cased

    Parameters
    ----------
    city : str
        City name (e.g., "vancouver").
    country_code : str
        Two-letter country code (e.g., "ca", "FR").

    Returns
    -------
    str
        Formatted destination string: "City, COUNTRY_CODE".

    Raises
    ------
    ValueError
        If inputs are empty after stripping or country_code is invalid.
    TypeError
        If inputs are not strings.
    """
    # if not isinstance(city, str):
    #     raise TypeError("city must be a string.")
    # if not isinstance(country_code, str):
    #     raise TypeError("country_code must be a string.")

    # city_clean = city.strip()
    # code_clean = country_code.strip()

    # if city_clean == "" or code_clean == "":
    #     raise ValueError("city and country_code must not be empty.")

    # if len(code_clean) != 2 or not code_clean.isalpha():
    #     raise ValueError("country_code must be exactly two letters (A-Z).")

    # return f"{city_clean.title()}, {code_clean.upper()}"
    pass





