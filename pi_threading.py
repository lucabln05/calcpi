from decimal import Decimal, getcontext
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

def calculate(k):
    return (Decimal(1) / 16**k) * (
        Decimal(4) / (8*k+1) - Decimal(2) / (8*k+4) -
        Decimal(1) / (8*k+5) - Decimal(1) / (8*k+6))

def pi(decimal_places: int) -> Decimal:
    getcontext().prec = decimal_places
    pi = Decimal(0)

    with Pool(cpu_count()) as p:
        results = list(tqdm(p.imap_unordered(calculate, range(decimal_places)), total=decimal_places))

    pi = sum(results)

    return pi

if __name__ == '__main__':
    pi_value = pi(1000)
    with open("pi.txt", "w") as f:
        f.write(str(pi_value))
    print(f"Finished calculating pi to {len(str(pi_value)) - 2} decimal places.")