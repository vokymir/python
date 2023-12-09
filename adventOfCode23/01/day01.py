def numFromStr(string:str) -> int:
    tens:int = 0
    ones:int = 0
    for i in range(len(string)):
        if string[i].isdigit():
            tens = int(string[i])
            break
    for i in range(len(string)):
        actualIndex:int = len(string) - 1 - i
        if string[actualIndex].isdigit():
            ones = int(string[actualIndex])
            break
    return tens*10+ones

"""
def arrMinIndex(arr:list[int]) -> int:
    smallest:int = arr[0]
    index:int = 0
    for i in range(len(arr) - 1):
        if smallest == -1:
            smallest = arr[i + 1]
            index = i + 1
        elif arr[i+1] < smallest and arr[i + 1] != -1:
            smallest = arr[i+1]
            index = i+1
    if smallest == -1:
        index = len(arr)-1
    return index
"""

"""
def arrMaxIndex(arr:list[int]) -> int:
    biggest = arr[0]
    index = 0
    for i in range(len(arr) - 1):
        if arr[i+1] > biggest and arr[i + 1] != -1:
            biggest = arr[i+1]
            index = i+1
    return index
"""

def minFromArr(arr:list[int]) -> tuple:
    smallest:int = arr[0]
    index:int = 0
    for i in range(len(arr)-1):
        if smallest == -1:
            smallest = arr[i + 1]
            index = i + 1
        elif arr[i+1] < smallest and arr[i + 1] != -1:
            smallest = arr[i+1]
            index = i+1
    return (index,smallest)

def minFromTwoArr(arr1:list[int],arr2:list[int])-> int:
    arr2min:tuple = minFromArr(arr2)
    
    arr1.append(arr2min[1])
    smallest:tuple = minFromArr(arr1)
    if smallest[0] == 9:
        return arr2min[0]
    return smallest[0]


def numEvenWrittenFromStr(string:str) -> int:
    tens:int = 0
    ones:int = 0
    numsStr:list[str] = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    numsInt:list[str] = ["1","2","3","4","5","6","7","8","9"]
    numsStrIndex:list[int] = []
    numsIntIndex:list[int] = []

    for j in range(9):
        numsStrIndex.append(string.find(numsStr[j]))
        numsIntIndex.append(string.find(numsInt[j]))
    
    tens = 1 + minFromTwoArr(numsStrIndex, numsIntIndex)
    
    string = string[::-1]
    numsStrIndex = []
    numsIntIndex = []

    for i in range(len(numsStr)):
        numsStr[i] = numsStr[i][::-1]

    for j in range(9):
        numsStrIndex.append(string.find(numsStr[j]))
        numsIntIndex.append(string.find(numsInt[j]))
    
    ones = 1 + minFromTwoArr(numsStrIndex, numsIntIndex)

    return (tens*10 + ones)


if __name__ == "__main__":
    x:str = input()
    sum:int = 0
    while x != "":
        sum += numEvenWrittenFromStr(x)
#        print(numEvenWrittenFromStr(x))
        x = input()
    print(sum)