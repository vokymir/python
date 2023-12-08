def input_number() -> int:
    """
    Funkce nacte cele cislo. Pokud uzivatel zada neco jineho,
    funkce ho upozorni a bude zadat nove zadani
    """
    while True:
        try:
            number = int(input("Zadej cele cislo: "))
            return number
        except:
            print("toto neni cislo!")

def input_operator() -> str:
    while True:
        operator = input("Zadej operator +,-,=: ")
        if operator in ["+","-","="]:
             return operator
        print("toto neni operator!")

number = input_number()
while True:
    operator = input_operator()
    if operator=="=":
        break

    if operator=="+":
        number += input_number()
    else:
        number -= input_number() 
print(number)