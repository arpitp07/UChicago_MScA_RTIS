# Q2
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pocket_calculator' function below.
#
class OperatorNotRecognizedError(Exception):
    pass

class NegativeInputError(Exception):
    pass

class NegativeOutputError(Exception):
    pass

class NonIntegerInputError(Exception):
    pass

class OutputTooLargeError(Exception):
    pass


def pocket_calculator(x, operator, y):
    # Write your code here
    
    ops = { '+' : (lambda x, y: (x + y)),
            '-' : (lambda x, y: (x - y)),
            'x' : (lambda x, y: (x * y)),
            '/' : (lambda x, y: math.floor(x / y))}
    
    op = ops.get(operator)
    

    try:
        if operator not in ['+', '-', 'x', '/']:
            raise OperatorNotRecognizedError
        
        if (x.find('-') != -1) | (y.find('-') != -1):
            raise NegativeInputError
        
        if (x.find('.') != -1) | (y.find('.') != -1):
            raise NonIntegerInputError
        
        if (int(y) == 0) & (operator == '/'):
            return '0'

        if op(int(x), int(y)) < 0:
            raise NegativeOutputError
        
        if op(int(x), int(y)) > 9999999:
            raise OutputTooLargeError
        
        result = op(int(x), int(y))
        
            
    except OperatorNotRecognizedError:
        return 'OperatorNotRecognized'
    
    except ValueError:
        return 'InputNotANumber'

    except NegativeInputError:
        return 'NegativeInput'
        
    except NegativeOutputError:
        return 'NegativeOutput'
        
    except NonIntegerInputError:
        return 'NonIntegerInput'
        
    except OutputTooLargeError:
        return 'OutputTooLarge'

    return str(result)

pocket_calculator('0', '/', '0')