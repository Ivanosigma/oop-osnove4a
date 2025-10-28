class zaposlenik:
    def __init__(self,ime,prezime,placa):
        self.ime=ime
        self.prezime=prezime
        self.placa=placa
    def prikazi_info(self):
        print(f"Ime i prezime: {self.ime} {self.prezime}, Plaća: {self.placa} EUR")
class programer(zaposlenik):
    def __init__(self,ime,prezime,placa,programski_jezik):
        super().__init__(ime,prezime,placa)
        self.programski_jezik=programski_jezik
    def prikazi_info(self):
        super().prikazi_info()
        print(f"Programski jezik: {self.programski_jezik}")
class menadzer(zaposlenik):
    def __init__(self, ime, prezime, placa,tim):
        super().__init__(ime, prezime, placa)
        self.tim = tim
    def prikazi_info(self):
        super().prikazi_info()
        print(f"Tim: {self.tim}")  
    def dodaj_clana_tima(self, ime_prezime):
        self.tim.append(ime_prezime)
     
    


zaposlenik1=zaposlenik("Ivano","Kljajic",1000)
zaposlenik1.prikazi_info()

programer1=programer("Marko","Marić",1200,["Python","Java"])
programer1.prikazi_info()

menadzer1=menadzer("Ana","Anić",1500,["Marko Marić","Ivano Kljajic"])
menadzer2=menadzer("Ivan","Ivanic",1500,["Marko Marić","Ivano Kljajic"])
menadzer1.dodaj_clana_tima("Ivan Ivanic")
menadzer1.prikazi_info()
menadzer2.prikazi_info()



 
