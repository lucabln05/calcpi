#This program calculates the square root of a number with a given number of decimal places

from decimal import *
import numpy as np


#estimate_pi
import math
import random 

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

def pi(decimal_places: int) -> Decimal:
    #Bailey-Borwein-Plouffe (BBP) formula
    getcontext().prec = decimal_places
    pi = Decimal(0)
    for k in range(decimal_places):
        print(k)
        pi += (Decimal(1) / 16**k) * (
            Decimal(4) / (8*k+1) - Decimal(2) / (8*k+4) -
            Decimal(1) / (8*k+5) - Decimal(1) / (8*k+6))
    return pi

def pi_own_method(decimal_places: int) -> Decimal:
    # some late night math fun
    getcontext().prec = decimal_places
    result = Decimal(0)
    n = 1/decimal_places
    for k in range(decimal_places):
        result += Decimal(((1-(k*n)**2)**0.5)*n)
    return result*4

def estimate_pi(num_trials: int) -> float:
    """
    https://www.youtube.com/watch?v=wlYWZMtXJR4
    Some late night math fun.
    Rolls two dice and checks if the resulting points lie within the unit circle.
    Returns an estimate of pi based on the proportion of times the points lie within the unit circle.
    
    :param num_trials: The number of times to run the simulation.
    :type num_trials: int
    :return: An estimate of pi.
    :rtype: float
    """
    num_points_inside_circle = 0
    
    for i in range(num_trials):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = math.sqrt(x**2 + y**2)
        if z <= 1:
            num_points_inside_circle += 1
    
    # Estimate pi using the proportion of points inside the circle
    pi_estimate = 4 * num_points_inside_circle / num_trials
    
    return pi_estimate

def average_estimate_pi(num_trails: int) ->float:
    sum = 0
    for i in range(num_trails):
        print(i)
        sum += estimate_pi(num_trails)
        
    return sum/num_trails

