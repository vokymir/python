class epicNumber:
    def __init__(self, number:int, posX:int, posY:int) -> None:
        self.number = number
        self.posXL = posX
        self.posXR = posX + numberOfDigits(number) -1
        self.posY = posY

class symbol:
    def __init__(self, posX:int, posY:int) -> None:
        self.posX = posX
        self.posY = posY
        self.first:int = 0
        self.second:int = 0

def numberOfDigits(number:int) -> int:
    res:int = 0
    while number > 0:
        number = number//10
        res += 1
    return res

def fromLineToNumbers(string:str, output:list[epicNumber], currentLine:int):
    numbers:str = "0123456789"
    i:int = 0
    while i < len(string):
        num:str = ""
        if string[i] in numbers:
            num = num + string[i]
            j:int = 1
            if i+j < len(string):
                while string[i+j] in numbers:
                    num = num + string[i+j]
                    j += 1
                    if i+j == len(string):
                        break
            numm:int = int(num)
            output.append(epicNumber(numm,i, currentLine))
            i += j - 1 #cause j is 1 on default
        i += 1

def isNextToStar(number:epicNumber, map:list[str]) -> bool:
    chars:str = "!@#$%^&*()/+-="
    leftPivot:int = max(0, number.posXL - 1)
    #line above number
    if number.posY > 0:
        for i in range(leftPivot,min(number.posXR+2,len(map[number.posY-1]))):
            if map[number.posY-1][i] in chars:
                return True
    #left from num
    if map[number.posY][leftPivot] in chars:
        return True
    #right
    if number.posXR != len(map[number.posY])-1:
        if map[number.posY][number.posXR+1] in chars:
            return True
    #line below number
    if number.posY < len(map)-1:
        for i in range(leftPivot,min(number.posXR+2,len(map[number.posY+1]))):
            if map[number.posY+1][i] in chars:
                return True
    #if nothing
    return False

def fromLineToSymbols(string:str, output:list[symbol], currentLine:int):
    symbols:str = "!@#$%^&*()/+-="
    for i in range(len(string)):
        if string[i] in symbols:
            output.append(symbol(i,currentLine))

def isNextToTwoNumbers(symbol:symbol, map:list[str], numbers:list[epicNumber]) -> bool:
    updatedNumbers:list[epicNumber] = []
    for i in range(len(numbers)):
        if abs(numbers[i].posY - symbol.posY) <= 1:
            updatedNumbers.append(numbers[i])
    
    finalNumbers:list[epicNumber] = []
    for i in range(len(updatedNumbers)):
        #checks for above and below but not for only diagonals
        if updatedNumbers[i].posXL <= symbol.posX and updatedNumbers[i].posXR >= symbol.posX:
            finalNumbers.append(updatedNumbers[i])
        #checks for diagonals and left & right
        elif updatedNumbers[i].posXR == symbol.posX - 1 or updatedNumbers[i].posXL == symbol.posX + 1 :
            finalNumbers.append(updatedNumbers[i])
    
    if len(finalNumbers) == 2:
        symbol.first = finalNumbers[0].number
        symbol.second = finalNumbers[1].number
        return True

    return False


if __name__ == "__main__":
    inputList:list[str] = []
    x:str = input()
    numbers:list[epicNumber] = []
    symbols:list[symbol] = []
    i:int = 0

    while x != "":
        inputList.append(x)
        fromLineToNumbers(x,numbers,i)
        fromLineToSymbols(x,symbols,i)
        x = input()
        i += 1
    
    sum:int = 0

    for i in range(len(numbers)):
        if isNextToStar(numbers[i],inputList):
            sum += numbers[i].number

    print(sum)

    sumEpic:int = 0

    for i in range(len(symbols)):
        if isNextToTwoNumbers(symbols[i],inputList,numbers):
            sumEpic += symbols[i].first * symbols[i].second

    print(sumEpic)


