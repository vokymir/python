from invoice import *

def readItem() -> Item|None:
    name = input("Nazev polozky: ")
    if name == "":
        return None
    try:
        pricePerUnit = float(input("Cena/ks: "))
    except:
        return None
    try:
        units = int(input("Pocet kusu: "))
    except:
        return None
    return Item(name,pricePerUnit, units)

if __name__ == "__main__":
    invoice = Invoice()

    item = readItem()
    while not(item is None):
        invoice.addItem(item)
        item = readItem()
    print(invoice)

    