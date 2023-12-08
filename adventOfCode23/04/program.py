class Card:
    def __init__(self, number:int) -> None:
        self.number:int = number
        self.winning:list[int] = []
        self.have:list[int] = []

    def addWinning(self, num:int):
        self.winning.append(num)

    def addHave(self, num:int):
        self.have.append(num)
    
    def editNumber(self, num:int):
        self.number = num

    @property
    def points(self) -> int:
        res:int = 0

        for i in range(len(self.have)):
            if self.have[i] in self.winning:
                if res == 0:
                    res = 1
                else:
                    res *= 2

        return res

    @property
    def haveWinnings(self) -> int:
        res:int = 0

        for i in range(len(self.have)):
            if self.have[i] in self.winning:
                res += 1

        return res


def extractCardFromInput(string:str) -> Card:
    strings:list[str] = string.split(" ")
    card:Card = Card(-1)
    winningStart:int
    winningEnd:int
    haveStart:int

    for i in range(len(strings)):
        if strings[i] == "":
            continue

        if ":" in strings[i]:
            card.editNumber(int(strings[i][:-1]))
            winningStart = i + 1
        if "|" in strings[i]:
            winningEnd = i - 1
            haveStart = i + 1
    
    for i in range(winningStart, winningEnd + 1):
        if strings[i] == "":
            continue
        card.addWinning(int(strings[i]))

    for i in range(haveStart,len(strings)):
        if strings[i] == "":
            continue
        card.addHave(int(strings[i]))

    return card

def addCount(card:Card, array:list[int]):
    for i in range(card.haveWinnings):
        array[card.number + 1 + i] += 1

if __name__ == "__main__":
    """
    Pretty funny algorithm, as I managed to read like 5 chapters from Bible while waiting 
    for it to end. The result is 23806951 and I add print(currCard.num) for sanity reasons,
    so I won't go insane don't knowing how much is done already.
    """
    x:str = input()
    myCards:list[Card] = []
    myCardsCount:list[int] = [0]*200
    sum:int = 0
    sumOfCards:int = 0

    while x != "":
        currentCard:Card = extractCardFromInput(x)
        myCards.append(currentCard)
        myCardsCount[currentCard.number] += 1
        for i in range(myCardsCount[currentCard.number]):
            addCount(currentCard,myCardsCount)
        sum += currentCard.points
        sumOfCards += myCardsCount[currentCard.number]
        print(currentCard.number)
        x = input()

    print(sumOfCards)