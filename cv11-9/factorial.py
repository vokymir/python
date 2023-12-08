def fact(i: int)-> int:
    if i == 0:
        return 1
    return i * fact(i-1)

if(__name__ == "__main__"):
    print(fact(5))
        