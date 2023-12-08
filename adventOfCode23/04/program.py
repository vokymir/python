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

def extractCardFromInput(string:str) -> Card:
    strings:list[str] = string.split(" ")
    card:Card = Card(-1)
    winningStart:int
    winningEnd:int
    haveStart:int

    for i in range(len(strings)):
        if ":" in strings[i]:
            card.editNumber(int(strings[i][:-1]))
            winningStart = i + 1
        if "|" in strings[i]:
            pass


    return Card(1)