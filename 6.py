def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    :param numbers: List of numbers to calculate the average.
    :type numbers: list of int or float
    :return: The average of the numbers in the list.
    :rtype: float
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Example usage
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("The average is:", average)
