def get_packing_list(weather, duration):
    """This function generates a customized list of travel essentials based on
    expected weather conditions and trip duration. It adjusts recommended
    items using conditional rules to better prepare travelers for different
    environments and trip lengths.

    Parameters
    ----------
    weather : str
        Expected conditions (e.g., "cold", "warm", "rainy").
    duration : int
        Total number of days for the trip.

    Returns
    -------
    list
        Items in this order: base essentials first, then additions based on
        weather and trip length.

    Raises
    ------
    ValueError
        If duration is less than 1; error message must be
        "Trip duration must be at least 1 day.".

    Specification
    -------------
    - Base items: every list starts with ["Passport", "Toothbrush"].
    - If cold: add "Heavy Jacket" and "Gloves".
    - If rainy: add "Umbrella".
    - If warm: add "Sunscreen".
    - If duration > 7: add "Laundry kit".
    """
    pass
