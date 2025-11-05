import tkinter as tk
import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom



radterase="radi"
class restoran:
    def __init__(self,radno_vrijeme,ime):
        self.radno_vrijeme=radno_vrijeme
        self.ime=ime

    def prikazi_info(self):
        print(f"radno vrijeme: {self.radno_vrijeme},ime: {self.ime}")
class stolovi:
    def __init__(self,radno_vrijeme,ime,broj_stolova,lokacija,):
        super().__init__(radno_vrijeme,ime)
        self.broj_stolova=broj_stolova
        self.lokacija=lokacija

    def prikazi_info(self):
        super().prikazi_info()
        print(f"broj stolova: {self.broj_stolova}\nlokacija: {self.lokacija})")
class rezervacija:
    rezervacija=[]
    def __init__(self,radno_vrijeme,ime,broj_stolova,lokacija,broj_stola,ime_prezime,broj_osoba,datum):
        super().__init__(radno_vrijeme,ime,broj_stolova,lokacija)
        self.ime_prezime=ime_prezime
        self.broj_stola=broj_stola
        self.broj_osoba=broj_osoba
        self.datum=datum
    def prikazi_info(self):
        super().prikazi_info()
        print(f"ime i prezime: {self.ime_prezime}\nbroj osoba: {self.broj_osoba}\ndatum: {self.datum}\nbroj stola: {self.broj_stola}")




    

        

    
    


        

class RezervacijaApp:
    def open_rezervacija_window(self):
        rezervacija_window = tk.Toplevel(self.root)
        self.root=root
        self.root.title("Rezervacija stolova")
        self.root.rowconfigure(0,weight=0)
        self.root.rowconfigure(1,weight=1)
        self.root.rowconfigure(2,weight=0)
        self.root.columnconfigure(0,weight=1)
        self.unos_frame=tk.Frame(self.root,padx=10,pady=10)
        self.unos_frame.grid(row=0,column=0,sticky="ew")
        self.unos_frame.columnconfigure(1,weight=1)
        tk.Label(self.unos_frame,text="Ime i prezime:").grid(row=0,column=0,sticky="w",pady=2)
        self.entry_ime=tk.Entry(self.unos_frame)
        self.entry_ime.grid(row=0,column=1,sticky="ew",pady=2)
        tk.Label(self.unos_frame,text="Broj osoba:").grid(row=1,column=0,sticky="w",pady=2)
        self.entry_broj_osoba=tk.Entry(self.unos_frame)
        self.entry_broj_osoba.grid(row=1,column=1,sticky="ew",pady=2)
        tk.Label(self.unos_frame,text="Datum:").grid(row=2,column=0,sticky="w",pady=2)
        self.entry_datum=tk.Entry(self.unos_frame)
        self.entry_datum.grid(row=2,column=1,sticky="ew",pady=2)
        tk.Label(self.unos_frame,text="Broj stola:").grid(row=3,column=0,sticky="w",pady=2)
        self.broj_stola=tk.Entry(self.unos_frame)
        self.broj_stola.grid(row=3,column=1,sticky="ew",pady=2)
        self.gumbi_frame=tk.Frame(self.root,padx=10,pady=10)
        self.gumbi_frame.grid(row=4,column=0,sticky="ew")
        self.gumbi_frame.columnconfigure((0,1),weight=1)

        self.rezerviraj_button = tk.Button(self.gumbi_frame, text="Rezerviraj stol", command=self.rezerviraj_stol)
        self.rezerviraj_button.grid(row=0, column=0, columnspan=2, pady=10)

        self.lista_rezervacija_frame = tk.Frame(self.root, padx=10, pady=10)
        self.lista_rezervacija_frame.grid(row=1, column=0, sticky="nsew")
        self.lista_rezervacija_listbox = tk.Listbox(self.lista_rezervacija_frame, height=10, width=50)
        self.lista_rezervacija_listbox.pack(side=tk.LEFT, fill="both", expand=True)

    def osvjezi_listu_rezervacija(self):
        self.lista_rezervacija_listbox.delete(0, tk.END)
        for r in rezervacija.rezervacija:
            self.lista_rezervacija_listbox.insert(tk.END, f"Ime: {r.ime_prezime}, Osobe: {r.broj_osoba}, Datum: {r.datum}, Stol: {r.broj_stola}")


    def __init__(self, root):
        self.root = root
        self.root.title("Kljajic rerstaurant")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.gumbi_frame=tk.Frame(self.root,padx=10,pady=10)
        self.gumbi_frame.grid(row=4,column=0,sticky="ew")
        self.gumbi_frame.columnconfigure((0,1),weight=1)

        self.rezerviraj_button = tk.Button(self.gumbi_frame, text="Rezerviraj stol", command=self.open_rezervacija_window)
        self.rezerviraj_button.grid(row=0, column=0, columnspan=2, pady=10)




    def rezerviraj_stol(self):
        ime_prezime = self.entry_ime.get()
        broj_osoba = self.entry_broj_osoba.get()
        datum = self.entry_datum.get()
        broj_stola=self.broj_stola.get()
        rezervacijon=rezervacija(ime_prezime,broj_stola,datum,broj_osoba)
        # The following line is problematic as 'rezervacija' class constructor expects more arguments.
        if ime_prezime and broj_osoba and datum and broj_stola:
            rezervacija.rezervacija.append(rezervacijon)
            self.osvjezi_listu_rezervacija()
    


    def osvjezi_listu_rezervacija(self):
        self.lista_rezervacija_listbox.delete(0, tk.END)
        for r in rezervacija.rezervacija:
            self.lista_rezervacija_listbox.insert(tk.END, f"Ime: {r.ime_prezime}, Osobe: {r.broj_osoba}, Datum: {r.datum}, Stol: {r.broj_stola}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RezervacijaApp(root)
root.mainloop()