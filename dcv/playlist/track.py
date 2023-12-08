class Track:
    """
    Track contains title, length, rating of track(song), and has __str__() function.

    Jakub Vokoun
    23_12_07
    """
    def __init__(self, title:str, length:int, rating:float):
        """
        Kontruktor vytvoří instanci stopy.
        """
        self.__title = title
        self.__length = length
        self.__rating = rating

    @property
    def title(self) -> str:
        return self.__title

    @property
    def length(self) -> int:
        return self.__length
    
    @property
    def rating(self) -> float:
        return self.__rating
    
    def __str__(self)->str:
        """
        Metoda vrátí informace o stopě ve formátu název [čas] (hodnocení - počet hvězdiček/teček).

        Čas je délka stopy vypsaná ve formátu Minuty:Sekundy, a to i pro stopy s délkou nad hodinu (např. 62:25).

        Počet hvězdiček je dán celou částí hodnocení. Pro desetinnou část hodnocení se vygeneruje znak '.', pokud je větší nebo rovna 0,25 a znak '*', pokud je větší nebo rovna 0,75.
        """
        xdd:float = self.rating - self.rating.__floor__()
        lol:str = ""
        if xdd >= 0.75:
            lol = "*"
        elif xdd >= 0.25:
            lol = "."

        return f"{self.title} [{self.length // 60}:{self.length % 60:02d}] ({"*"*self.rating.__floor__()}{lol})"