class Versenyzo:
    def __init__(self, sor:str) -> None:
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.szul:int = int(v[1])
        self.rajtszam:str = v[2]
        self.nem:bool = v[3] == 'f'
        self.kategoria:str = v[4]
        self.eredmenyek:dict[str, str] = {
            'úszás':        v[5],
            'I. depó':      v[6],
            'kerékpározás': v[7],
            'II. depó':     v[8],
            'futás':        v[9]
        }
        self.osszido:int = 0
        for ido in self.eredmenyek.values():
            opm:list[str] = ido.split(':')
            o:int = int(opm[0])
            p:int = int(opm[1])
            m:int = int(opm[2])
            self.osszido += o * 3600 + p * 60 + m