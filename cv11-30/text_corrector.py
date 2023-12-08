
def String_correct(string:str) -> str:
    arr:list[str] = string.split(" ")
    sentenceEnders:str = ".?!"
    shouldCap:bool = True
    for i in range(len(arr)):
        if shouldCap:
            arr[i] = arr[i].capitalize()
            shouldCap = False
        if arr[i][-1] in sentenceEnders:
            shouldCap = True
    return " ".join(arr)

if __name__ == "__main__":
    print(String_correct(input()))