# Purpose: Calculate pi to the nth decimal place
# Program will run until the nth decimal place is reached, every 1000 iterations the program will print the percentage of completion to the console
#

from decimal import Decimal, getcontext


def pi(decimal_places: int) -> Decimal:
    #Bailey-Borwein-Plouffe (BBP) formula
    getcontext().prec = decimal_places
    ouput_interval = decimal_places/10000
    pi = Decimal(0)
    for k in range(decimal_places):
        pi += (Decimal(1) / 16**k) * (
            Decimal(4) / (8*k+1) - Decimal(2) / (8*k+4) -
            Decimal(1) / (8*k+5) - Decimal(1) / (8*k+6))
        if k % ouput_interval == 0:
            print(100*k/decimal_places, "%")
    return pi


# save output to file
with open("pi.txt", "w") as f:
     f.write(str(pi(1000)))


