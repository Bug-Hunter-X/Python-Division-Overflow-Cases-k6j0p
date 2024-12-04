import sys
def function_with_uncommon_error(a, b):
    try:
        if abs(a) == float('inf') or abs(b) == 0:
          return "Division by zero or infinity"
        result = a / b
        if result > sys.float_info.max or result < -sys.float_info.max:
          return "OverflowError"
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"
    except OverflowError:
        return "OverflowError"

result = function_with_uncommon_error(float('inf'), 1)
print(result)
result = function_with_uncommon_error(1,0)
print(result)
result = function_with_uncommon_error(1e308 * 2,1)
print(result) 