import random

def input_array(n:int) -> list[int]:
    # načte z klávesnice pole zadané délky a vrátí jej
    arr:list[int] = []
    for i in range(n):
        while True:
            try:
                x = int(input(f"Enter value at position {i}: "))
            except:
                print("Please enter valid value (int)!")
            else:
                break
        arr.append(x)
    return arr

def generate_range(n:int, first:int, step:int) -> list[int]:
    # vygeneruje pole zadané délky, naplněné hodnotami od first s krokem step
    arr:list[int]= [0]*n
    for i in range(n):
        arr[i] = first + i*step
    return arr

def generate_random_array(n:int, min:int, max:int) -> list[int]:
    #vygeneruje pole zadané délky naplněné náhodnými čísly z intervalu <min, max>
    arr:list[int] = [0] * n
    for i in range(len(arr)):
        arr[i] = random.randint(min,max)
    return arr

def print_array(array:list[int]):
    # vytiskne pole ve formátu: [1, 2, 3, 4, 5]
    print("[", end="")

    for i in range(len(array)-1):
        print(array[i], end=", ")
    print(array[-1], end="")
    
    print("]")

