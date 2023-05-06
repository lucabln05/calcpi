def arc_sin(x):
    result = 0
    sign = 1
    power = x
    for n in range(1, 100, 2):
        term = sign * power / n
        result += term
        sign *= -1
        power *= x**2
    return result

x = float(input("Geben Sie den Wert ein, für den der Arkussinus berechnet werden soll: "))
if abs(x) <= 1:
    print(f"Der Arkussinus von {x} ist {arc_sin(x)}")
else:
    print("Fehler: Der Wert muss zwischen -1 und 1 liegen.")