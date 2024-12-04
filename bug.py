def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

#Uncommon error: This function may raise an OverflowError if the result of the division is too large to be represented in Python's floating-point number format.
result = function_with_uncommon_error(float('inf'),1)
print(result)