def array_min(array:list[int]) -> int:
    res:int = array[0]
    for i in range(len(array)):
        if res > array[i]:
            res = array[i]
    return res

def array_max(array:list[int]) -> int:
    res:int = array[0]
    for i in range(len(array)):
        if res < array[i]:
            res = array[i]
    return res

def array_sum(array:list[int]) -> int:
    sum:int = 0
    for x in array:
        sum += x
    return sum

def array_avg(array:list[int]) -> float:
    return array_sum(array) / len(array)

pole:list[int] =  [0,1,2,3,4,5]
print(array_min(pole))
print(array_max(pole))
print(array_sum(pole))
print(array_avg(pole))