from track import Track
from playlist import Playlist
import sys


def inputTrack() -> Track|None:
    """
    Funkce načte ze standardního vstupu na 
    jednotlivých řádkách název stopy, 
    délku v sekundách a hodnocení 
    a vrátí instanci třídy Track. 
    Pokud bude název prázdná řádka, 
    zadávání se okamžitě ukončí a vrátí se hodnota None. 
    Stejně tak se vrátí hodnota None v případě chybně zadaného číselného údaje.
    """
    name:str = input()
    if name == "":
        return None
    
    try:
        length:int = int(input())
    except:
        return None
    if length <= 0:
        return None
    
    try:
        rating:float = float(input())
    except:
        return None
    if rating < 0 or rating > 5.0:
        return None
    
    return Track(name,length,rating)

def inputPlaylist()->Playlist:
    """
    Funkce bude s využitím funkce inputTrack načítat stopy tak dlouho, 
    dokud se nevrátí prázdná stopa. Z takto načtených stop se vytvoří a vrátí Playlist.
    """
    res:Playlist = Playlist([])
    while True:
        x = inputTrack()
        if x == None:
            break
        res.addTrack(toTrack(x))

    return res

def toTrack(x:None|Track) -> Track:
    if type(x) == Track:
        return x
    return Track("",0,0)


def preparePlaylist(playlist:Playlist, minLength:int)->Playlist:
    """
    S pomocí funkcí playlistu vytvoří zamíchaný seznam nejlépe hodnocených skladeb, 
    jejichž celková délka bude alespoň minLength a playlist vrátí.

    Může se stát, že po zamíchání by šlo některé skladby z konce seznamu vyhodit, 
    tento problém neřešte.
    """
    res1:Playlist = playlist
    res1.sortByRating()
    res:Playlist = res1.selectTotalLength(minLength)
    res.shuffle()

    return res

if __name__ == "__main__":
    """
    Hlavní program spustí funkci inputPlaylist a načte jednotlivé stopy. 
    Dále zavolá funkci preparePlaylist, přičemž minimální délka bude zadána 
    jako první parametr příkazové řádky. Nakonec vypíše vygenerovaný playlist. 
    Pokud bude playlist krátký, vypíše ho a oznámí tuto skutečnost uživateli.
    """
    minLen:int = int(sys.argv[1])
    x:Playlist = preparePlaylist(inputPlaylist(),minLen)
    print(x)
    if x.totalLength < minLen:
        print("Tento plalist je kratsi nez minimalni delka.")