import copy
import random

def generate_random_array(n:int, min:int, max:int, seed: int|None = None) -> list[int]:
    res:list[int] = [0]*n
    rand = random.Random(seed)

    for i in range(n):
        res[i] = rand.randint(min,max)
    
    return res

def testIsSorted(data:list[int]):
    for i in range(len(data)-1):
        assert data[i] <= data[i+1], f"array is not sorted, the error is at data[{i}]: {data[i]}"

def testContainsSame(data1:list[int], data2:list[int]):
    data:list[int] = copy.deepcopy(data1)
    assert len(data1) == len(data2), f"arrays are of different length {len(data1)} vs {len(data2)}"

    for item in data2:
        found:bool = False
        for i in range(len(data2)-1):
            if item == data[i]:
                del data[i]
                found = True
                break
        assert found == True, f"arrays doesn't contain the same items"