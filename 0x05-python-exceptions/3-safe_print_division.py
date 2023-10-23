#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide 2 integers and print result"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    except TypeError:
        result = None
    except ValueError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
