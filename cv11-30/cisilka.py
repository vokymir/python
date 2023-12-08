jednotky:list[str] = ["","jedna", "dva", "tri", "ctyri", "pet", "sest", "sedm", "osm", "devet"]

nactky:list[str] = ["deset","jedenact", "dvanact", "trinact", "ctrnact", "patnact", "sestnact", "sedmnact", "osmnact", "devatenact"]

desitky:list[str] =["","","dvacet", "tricet", "ctyricet", "padesat", "sedesat", "sedmdesat", "osmdesat", "devadesat"]

if __name__ == "__main__":
    userIn = input()
    while userIn != "":
        try:
            number = int(userIn)
        except:
            number = -1
        if number >= 0 and number < 100:
            if number == 0:
                print("nula")
            elif number < 10:
                print(jednotky[number])
            elif number < 20:
                print(nactky[number-10])
            elif number < 100:
                print(f"{desitky[int(number/10)]}{jednotky[int(number%10)]}")
        else:
            if number == -1:
                print("kaaaamo, toto neni cislo. zkus to znovu: ")
            else:
                print("kaaaaaaaaaamo, toto cislo proste neumim. zkus do 99: ")
        userIn = input()