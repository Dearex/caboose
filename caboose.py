import sympy
import datetime

STEP_SIZE = 2**1
TARGET_RATIO = 0.5

def check_caboose(numbers) -> None:
    primes = 0
    checked = 0
    for n in numbers:
        checked += 1
        if sympy.isprime(n*n-n+caboose_check):
            primes += 1
        if primes/checked < TARGET_RATIO:
            return 
    print(f"{caboose_check} has {primes/checked*100} % Primes")

print("START", datetime.datetime.now())
for caboose_check in range(3, 1_000_000_000, 2):
    if (caboose_check-1) % 100000 == 0:
        print(f"Currently at {caboose_check}")
    check_caboose(range(1, caboose_check, STEP_SIZE))

print("END", datetime.datetime.now())

