class GrabbedCubes:
    def __init__(self, red:int = 0, green:int = 0, blue:int = 0) -> None:
        self.__red = red
        self.__green = green
        self.__blue = blue
    
    @property
    def r(self) -> int:
        return self.__red
    
    @r.setter
    def r(self, i:int):
        self.__red = i
    
    @property
    def g(self) -> int:
        return self.__green
    
    @g.setter
    def g(self, i:int):
        self.__green = i
    @property
    def b(self) -> int:
        return self.__blue
    
    @b.setter
    def b(self, i:int):
        self.__blue = i
    

class Game:
    def __init__(self, number:int, grabbed:list[GrabbedCubes] = []) -> None:
        self.__number = number
        self.__grabbed = []
        for i in range(len(grabbed)):
            self.__grabbed.append(GrabbedCubes(grabbed[i].r, grabbed[i].g, grabbed[i].b))

    @property
    def grabbed(self) -> list[GrabbedCubes]:
        return self.__grabbed

    @grabbed.setter
    def grabbed(self, i:int, x:GrabbedCubes):
        self.__grabbed[i] = x

    def addGrabbed(self, r:int, g:int, b:int):
        self.__grabbed.append(GrabbedCubes(r,g,b))

    def addGrabbedAsIs(self, x:GrabbedCubes):
        self.__grabbed.append(x)

    @property
    def n(self)->int:
        return self.__number

    def powerOfGame(self) -> int:
        redMin:int = 1
        greenMin:int = 1
        blueMin:int = 1
        for i in range(len(self.__grabbed)):
            item = self.__grabbed[i]
            if redMin < item.r:
                redMin = item.r
            if greenMin < item.g:
                greenMin = item.g
            if blueMin < item.b:
                blueMin = item.b
        return redMin * greenMin * blueMin

    def isPossible(self, rTotal:int, gTotal:int, bTotal:int) -> int:
        premise:bool = True
        for i in range(len(self.__grabbed)):
            item:GrabbedCubes = self.__grabbed[i]
            if item.r > rTotal or item.g > gTotal or item.b > bTotal:
                premise = False
                return 0
        return self.__number

def analyzeText(string:str) -> GrabbedCubes:
    text:list[str] = string.split(" ")
    r:int = 0
    g:int = 0
    b:int = 0
    for i in range(len(text)):
        if text[i] == "red" or text[i] == "red,":
            r = int(text[i-1])
        elif text[i] == "green" or text[i] == "green,":
            g = int(text[i-1])
        elif text[i] == "blue" or text[i] == "blue,":
            b = int(text[i-1])

    return GrabbedCubes(r,g,b)

def oneGameDecrypted(string:str) -> Game:
    parts:list[tuple] = []
    parts.append(string.partition(":"))
    lol:list[str] = parts[0][0].split(" ")
    num:int = int(lol[-1])
    res:Game = Game(num)

    while parts[-1][2] != "":
        parts.append(parts[-1][2].partition(";"))
        res.addGrabbedAsIs(analyzeText(parts[-1][0]))
    
    return res

if __name__ == "__main__":
    allGames:list[Game] = []
    redTotal:int = 12
    greenTotal:int = 13
    blueTotal:int = 14
    summa:int = 0
    summaOfPower:int = 0
    while True:
        x:str = input()
        if x == "":
            break
        allGames.append(oneGameDecrypted(x))
        y:Game = allGames[-1]
        summa += y.isPossible(redTotal,greenTotal,blueTotal)
        summaOfPower += y.powerOfGame()
    print(summaOfPower)