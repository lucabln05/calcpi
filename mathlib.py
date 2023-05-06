#This program calculates the square root of a number with a given number of decimal places

from decimal import *
import numpy as np

def sqrt(x: float, decimal_places: int) -> Decimal:
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    if decimal_places < 0:
        raise ValueError("Cannot calculate square root to a negative number of decimal places")
    #Returns the square root of x with decimal_places decimal places.
    getcontext().prec = decimal_places
    x = Decimal(x)
    a = Decimal(1)
    while True:
        last_a = a
        a = (a + x/a) / 2
        if a == last_a:
            break
    return a

#print(sqrt(3.141, 1000))

def pi(decimal_places: int) -> Decimal:
    getcontext().prec = decimal_places
    pi = Decimal(0)
    for k in range(decimal_places):
        pi += (Decimal(1) / 16**k) * (
            Decimal(4) / (8*k+1) - Decimal(2) / (8*k+4) -
            Decimal(1) / (8*k+5) - Decimal(1) / (8*k+6))
    return pi


def pislow(decimal_places: int) -> Decimal:
    # some late night math fun
    getcontext().prec = decimal_places
    result = Decimal(0)
    n = 1/decimal_places
    for k in range(decimal_places):
        result += Decimal(((1-(k*n)**2)**0.5)*n)
    return result*4

def pi_dice(decimal_places: int) -> Decimal:
    getcontext().prec = decimal_places
    result = Decimal(0)
    def pi_dice_term(x: int, y: int)
    for k in range(decimal_places):
        x = random.randint(1, 6)
        y = random.randint(1, 6)



