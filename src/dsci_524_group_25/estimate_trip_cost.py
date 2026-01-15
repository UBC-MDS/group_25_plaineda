def estimate_trip_cost(distance, fuel_price, efficiency):
    """
    Calculate the total fuel cost of a trip in Canada (Metric units), 
    including a contingency fee for long trips.

    Parameters
    ----------
    distance : float
        The distance of the trip in kilometers (km).
    fuel_price : float
        The price of fuel per liter (CAD/L).
    efficiency : float
        The fuel efficiency of the vehicle in kilometers per liter (km/L).

    Returns
    -------
    float
        The estimated cost of the trip rounded to 2 decimal places.

    Raises
    ------
    ValueError
        If distance, fuel_price, or efficiency are less than or equal to zero.
    
    Examples
    --------
    >>> estimate_trip_cost(150, 1.70, 12)
    21.25
    >>> estimate_trip_cost(900, 1.70, 12)
    146.62
    """
    
    # Comment out for milestone 1
    # # Input Validation
    # if distance <= 0:
    #     raise ValueError("Distance must be greater than 0 km.")
    # if fuel_price <= 0:
    #     raise ValueError("Fuel price must be greater than 0.")
    # if efficiency <= 0:
    #     raise ValueError("Efficiency (km/L) must be greater than 0.")

    # # Calculate base fuel cost
    # liters_needed = distance / efficiency
    # total_cost = liters_needed * fuel_price

    # # Logic: Long-haul contingency
    # if distance > 500:
    #     total_cost *= 1.15  # Add 15% contingency

    # # Formatting
    # return round(total_cost, 2)

    pass