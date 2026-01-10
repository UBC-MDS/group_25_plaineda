def convert_currency(amount, rate):
    """
    Convert a monetary amount between currencies with a specified exchange rate,
    deducting a $5 service fee if the inital amount is not at least $100.

    Parameters
    ----------
    amount : float
        The original monetary amount to be converted. Must be a positive number.
    rate : float
        The currency exchange rate used to convert the amount. Must be a positive
        number.

    Returns
    -------
    float
        The final converted amount after the exchange rate and potential service
        fee are applied.

    Raises
    ------
    ValueError
        If amount is not a positive number.
    ValueError
        If rate is not a positive number.

    Examples
    --------
    >>> convert_currency(50.0, 1.2)
    55.0
    >>> convert_currency(150.0, 1.2)
    180.0
    """
    pass