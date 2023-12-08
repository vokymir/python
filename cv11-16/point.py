def array_find_most_occur(arr:list[int]) -> int:
    res:int
    resCount:int = 0
    for x in arr:
        count:int = arr.count(x)
        if count > resCount:
            resCount = count
            res = x
    return res

pole:list[int] = [0,1,5,2,3,4,5]
pole1:list[int] = [1,5,8,3,1,3,7,6,3,3]
print(array_find_most_occur(pole))
print(array_find_most_occur(pole1))