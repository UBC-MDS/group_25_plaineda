def get_packing_list(weather, duration):
    """Create a packing list from weather and trip duration.

    Parameters
    ----------
    weather : str
        Expected conditions (e.g., "cold", "warm", "rainy").
    duration : int
        Total number of days for the trip.

    Returns
    -------
    list
        Base items first, then additions based on weather and trip length.

    Raises
    ------
    ValueError
        If duration is less than 1 with message
        "Trip duration must be at least 1 day.".

    Notes
    -----
    Base items are ["Passport", "Toothbrush"]. Add "Heavy Jacket" and "Gloves"
    for cold, "Umbrella" for rainy, "Sunscreen" for warm, and "Laundry kit" if
    duration > 7.

    Examples
    --------
    >>> get_packing_list("cold", 3)
    ['Passport', 'Toothbrush', 'Heavy Jacket', 'Gloves']
    >>> get_packing_list("rainy", 10)
    ['Passport', 'Toothbrush', 'Umbrella', 'Laundry kit']
    """
    if duration < 1:
        raise ValueError("Trip duration must be at least 1 day.")

    if not isinstance(weather, str):
        raise TypeError("Weather must be a string.")

    if not isinstance(duration, int):
        raise TypeError("Duration must be an integer.")
        
    items = ["Passport", "Toothbrush"]
    weather_normalized = str(weather).strip().lower()

    if "cold" in weather_normalized:
        items.extend(["Heavy Jacket", "Gloves"])
    if "rainy" in weather_normalized:
        items.append("Umbrella")
    if "warm" in weather_normalized:
        items.append("Sunscreen")
    if duration > 7:
        items.append("Laundry kit")

    return items
