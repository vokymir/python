



origList:list[str] = [
    "Anna Smith", 
    "Bob Jones", 
    "Charlie Brown",
    "David Lee", 
    "Eve Green",
    "Frank Miller", 
    "Grace Chen", 
    "Harry Potter", 
    "Ivy Wilson", 
    "Jack White", 
    "Anna Smith", 
    "David Lee"
    ]

lol:list[str] = []

for item in origList:
    if not item in lol:
        lol.append(item)

for i in range(len(lol)-1):
    for j in range(len(lol)-1-i):
        if lol[i] > lol[i+1]:
            lol[i],lol[i+1] = lol[i+1],lol[i]


print(lol)

epic:list[str] = sorted(list(set(origList)))
print(epic)