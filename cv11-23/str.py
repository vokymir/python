
def CapitalizeStr(string:str) -> str:
    arr:list[str] = string.split(". ")
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    return ". ".join(arr)


def CapitalizeStrBetter(string:str, sentenceEnders:str = ".?!", useDefaultSentenceEnders:bool = True) -> str:
    arr:list[str] = string.split()
    if useDefaultSentenceEnders:
        defaultSentenceEnders:str = ".?!"
        for x in defaultSentenceEnders:
            if not x in sentenceEnders:
                sentenceEnders += x
    ShouldCapitalize:bool = True
    for i in range(len(arr)):
        if ShouldCapitalize:
            arr[i] = arr[i].capitalize()
            ShouldCapitalize = False
        if arr[i][-1] in sentenceEnders:
            ShouldCapitalize = True
    return " ".join(arr)

if __name__ == "__main__":
    print(CapitalizeStrBetter("ahoj lidi. toto je babis! a jak je doma? no, nevadi. cau lidi."))