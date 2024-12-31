def log_decorator(func):
    """
    A decorator that logs the execution of a function by printing messages before and after the function call.

    :param func: The function to be decorated.
    :type func: function
    :return: The wrapped function with logging functionality.
    :rtype: function
    """
    def wrapper():
        print("Start of the function execution.")
        func()
        print("End of the function execution.")
    return wrapper


@log_decorator
def function_test():
    """
    A test function that does not take any arguments and prints a simple message.
    """
    print("Cette fonction ne prend pas d'arguments.")


function_test()
