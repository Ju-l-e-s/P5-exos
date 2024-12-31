def square(value):
    """
    Return the square of a number.

    :param value: The number to square.
    :type value: int or float
    :raises TypeError: If the value is not a number (int or float).
    :return: The square of the value, or None if the value is invalid.
    :rtype: int or float
    """
    if not isinstance(value, (int, float)):
        print("The parameter must be a number!")
        return None
    return value ** 2
