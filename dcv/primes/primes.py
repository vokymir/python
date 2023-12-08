def is_prime(n:int) -> bool:
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def is_sum_of_primes(n:int) -> int:
    for i in range(n-1, 1,-1):
        if is_prime(i) and is_prime(n-i):
            return i
    return 0

def input_natural_number() -> int:
    while True:
        try:
            x:int = int(input("Enter natural number: "))
        except:
            pass
        else:
            if x > 0:
                break
    return x


if __name__ == "__main__":
    num:int = input_natural_number()
    x:int = is_sum_of_primes(num)
    if x != 0:
        print(f"Lze rozlozit: {x} + {num-x}")
    else:
        print("Nelze rozlozit.")

"""
if __name__ == "__main__":
    num:int = input_natural_number()
    x:int = is_sum_of_primes(num)
    if is_prime(x):
        print("Nelze rozlozit.")
    else:
        if x != 0:
            print(f"Lze rozlozit: {x} + {num-x}")
        else:
            print("Nelze rozlozit.")
"""