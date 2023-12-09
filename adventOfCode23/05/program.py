from datetime import datetime

class Route:
    def __init__(self, source:int = -1, destination:int = -1, length:int = -1) -> None:
        self.source:int = source
        self.destination:int = destination
        self.length:int = length

class Map:
    def __init__(self,source:str="",dest:str="") -> None:
        self.source:str
        self.dest:str
        self.routes:list[Route] = []

def extractHeading(map:Map, string:str):
    info:list[str] = string.replace(" ","-").split("-")
    map.source = info[0]
    map.dest = info[2]

def extractLine(map:Map, string:str):
    info:list[str] = string.split(" ")
    dest:int = int(info[0])
    source:int = int(info[1])
    length:int = int(info[2])
    map.routes.append(Route(source,dest,length))

def extractSeeds(string:str) -> list[int]:
    orig:list[str] = string.split(" ")
    res:list[int] = []
    
    """
    #it works well for first half of the assignment
    for i in range(len(orig)):
        if i == 0:
            continue
        res.append(int(orig[i]))
    """

    print(f"Going to: {int((len(orig)-1)/2)}")
    print()
    for i in range(len(orig)):
        if i == 0:
            continue
        if i%2 == 0:
            continue
        for j in range(int(orig[i+1])):
            res.append(int(orig[i])+j)
            print(f"\033[F{i} | {(j+1)/int(orig[i])*100:.2f}% | {j+1}/{orig[i]} | {str(datetime.now())}")
        print()
    return res

def goThroughMap(input:int, map:Map) -> int:
    res:int = input

    for i in range(len(map.routes)):
        x:Route = map.routes[i]
        if x.source <= input and input <= x.source + x.length - 1:
            res = x.destination + (input - x.source)
    
    return res

def findRightMap(inp:list[Map],currMap:Map) -> int:
    res:int = -1
    lookFor:str = currMap.dest

    for i in range(len(inp)):
        if inp[i].source == lookFor:
            res = i
            break
    
    return res


if __name__ == "__main__":
    last:str = "lol"
    lowestNum:int = -1

    startTime = str(datetime.now())
    print(startTime)

    seeds:list[int] = extractSeeds(input())
    maps:list[Map] = []

    input()

    while True:
        x:str = input()
        if x == "" and last == "":
            break
        map:Map = Map()
        extractHeading(map,x)
        maps.append(map)
        while True:
            y:str = input()
            if y == "":
                last = y
                break
            extractLine(map,y)
        
    midTime = str(datetime.now())
    print(midTime)

    print(f"Going to: {int((len(seeds)-1))}")
    print()
    
    for i in range(len(seeds)):
        
        print(f"\033[F{i+1} | {((i+1)/(len(seeds)-1))*100:.2f}% | {str(datetime.now())}")
        
        
        mapIndex:int = 0
        #print(f"{i+1}. seed: {seeds[i]}")
        number:int = goThroughMap(seeds[i],maps[mapIndex])

        while True:
            #print(f"{maps[mapIndex].source} -> {maps[mapIndex].dest}\n{number}")

            if mapIndex == len(maps) - 1:
                break

            mapIndex = findRightMap(maps,maps[mapIndex])
            number = goThroughMap(number,maps[mapIndex])

            

        
        if lowestNum == -1 or number < lowestNum:
            lowestNum = number
    
    endTime = str(datetime.now())
    print(f"Start: {startTime}\nEnd: {endTime}")
    print(f"Lowest Location:\n{lowestNum}")



