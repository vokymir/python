from __future__ import annotations
import random
from track import Track

class Playlist:
    """
    Contains list of tracks, has totalLength property.
    sortByRating() from the best
    shuffle()
    selectTotalLength() returns new playlist with only as much songs as the length argument says
    addTrack()
    and has __str__

    Jakub Vokoun
    23-12-07
    """
    def __init__(self, tracks:list[Track]) -> None:
        self.__tracks = tracks.copy()

    @property
    def totalLength(self) -> int:
        res:int = 0
        for item in self.__tracks:
            res += item.length
        return res
    
    def sortByRating(self):
        """
        Metoda seřadí stopy v playlistu sestupně podle hodnocení některou z následujících metod: 
        Bubble sort, Insertion sort, Selection sort.
        """
        for i in range(len(self.__tracks)-1):
            for j in range(len(self.__tracks)-1-i):
                if self.__tracks[j].rating < self.__tracks[j+1].rating:
                    self.__tracks[j], self.__tracks[j+1] = self.__tracks[j+1], self.__tracks[j]

    def shuffle(self):
        """
        Metoda náhodně proháže pořadí stop
        (nepoužívejte vestavěnou funkci shuffle). 
        Zamíchání musí být vždy náhodné. 
        Pokud nad stejnými daty zavolám shuffle, dostanu pokaždé jiný výsledek.

        Tip: náhodného pořadí lze docílit například tak, 
        že pro každý index vygenerujete druhý náhodný index, 
        a položky vzájemně prohodíte.
        """
        rand = random.Random()
        for i in range(len(self.__tracks)):
            x:int = rand.randint(0,len(self.__tracks)-1)
            self.__tracks[i], self.__tracks[x] = self.__tracks[x], self.__tracks[i]

    def addTrack(self,track:Track):
        """
        Prida jeden track k aktualnimu playlistu.
        """
        self.__tracks.append(track)

    def selectTotalLength(self,minLength:int) -> Playlist:
        """
        Metoda vygeneruje z originálního playlistu nový, 
        který obsahuje přesně tolik stop (od začátku playlistu), 
        aby jejich celková délka byla větší nebo rovna zadanému parametru 
        a neobsahovala žádnou stopu navíc. 
        V případě že stop není dostatek, vrátí metoda všechny stopy.
        """
        total:int = 0
        res:Playlist = Playlist([])
        
        for i in range(len(self.__tracks)):
            if total > minLength:
                break
            res.addTrack(self.__tracks[i])
            total+= self.__tracks[i].length

        return res

    def __str__(self):
        """
        Vrátí textovou reprezentaci playlistu, 
        kde na samostatných řádkách budou uvedeny 
        jednotlivé stopy (Track.__str__()) 
        a poslední řádka bude obsahovat celkový čas playlistu 
        ve formátu [Minuty:Sekundy] 
        (i pro playlisty překračující jednu hodinu 
        uvádějte pouze minuty a sekundy např. [87:25])        
        """
        res:str = ""
        for i in range(len(self.__tracks)):
            res += f"{self.__tracks[i]}\n"
        res += f"[{self.totalLength // 60:02d}:{self.totalLength % 60:02d}]"
        return res