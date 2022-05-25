import math

# addition
def add(num1, num2):
    ret = num1 + num2
    return ret

# subtraction
def sub(num1, num2):
    ret = num1 - num2
    return ret

# multiplication
def mul(num1, num2):
    ret = num1 * num2
    return ret

# division
def div(num1, num2):
    ret = num1 / num2
    return ret

# squareroot
def sqrt(num1):
    ret = math.sqrt(num1)
    return int(precFormat(ret))

# squareroot floor
def sqfl(num1):
    ret = math.floor(math.sqrt(num1))
    return ret

# squareroot ceil
def sqce(num1):
    ret = math.ceil(math.sqrt(num1)) 
    return ret

# square
def sq(num1):
    ret = mul(num1, num1)
    return int(precFormat(ret))

# precision formatting
def precFormat(num1):
    prec = 0
    return f'{num1:.{prec}f}'

# modulus 10
def mod10(num1):
    ret = num1 % 10
    return ret