def z1():
    #Definirajte klasu Knjiga
    class knjiga:
        def __init__(self, naslov, autor, godina_izdanja):
            self.naslov = naslov
            self.autor = autor
            self.godina_izdanja = godina_izdanja

    #unos   
    knjiga1 = knjiga("Gospodar prstenova", "J.R.R. Tolkien", 1954)
    knjiga2=knjiga("Farenheit 451","Ray Bradbury",1953)
    #print
    print(f"Naslov: {knjiga1.naslov}, Autor: {knjiga1.autor}, Godina izdavanja: {knjiga1.godina_izdanja}")
    print(f"Naslov: {knjiga2.naslov}, Autor: {knjiga2.autor}, Godina izdavanja: {knjiga2.godina_izdanja}")
z1()
def z2():
    #klas BankovniRačun
    class BankovniRačun:
        def __init__(self, ime_prezime, broj_računa, stanje):
            self.ime_prezime = ime_prezime
            self.broj_računa = broj_računa
            self.stanje = stanje
        def uplati(self, iznos ):
            self.stanje += iznos
            if iznos<=0:
                print("iznos mora biti veci od nule")
                return
            else:
                print("uplata je uspješna")
        def isplata(self, iznos):
            self.stanje -= iznos
            if iznos>self.stanje:
                print("iznos je veci od stanja računa")
                return
            else:
                print("isplata je uspješna")
        def info(self):
            print(f"Ime i prezime: {self.ime_prezime}",f"Broj računa: {self.broj_računa}",f"Stanje: {self.stanje:.2f}")

    
    BankovniRačun1=BankovniRačun("Ivano","11111111",0.00)
    BankovniRačun1.uplati(1000.00)
    BankovniRačun1.isplata(500.00)
    BankovniRačun1.info()
z2()