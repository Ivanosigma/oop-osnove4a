import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET
import os

# ------------------ PODACI O RESTORANU ------------------
IME_RESTORANA = "Skibidi Has"
RADNO_VRIJEME = "08:00 - 02:00"
XML_FILE = "rezervacije.xml"
TXT_FILE = "rezervacije.txt"

# ------------------ MODEL REZERVACIJE ------------------
class Rezervacija:
    def __init__(self, ime_prezime, broj_osoba, datum, broj_stola):
        self.ime_prezime = ime_prezime
        self.broj_osoba = broj_osoba
        self.datum = datum
        self.broj_stola = broj_stola

# ------------------ APLIKACIJA ------------------
class RezervacijaApp:
    def __init__(self, root):
        self.root = root
        self.root.title(IME_RESTORANA)
        self.root.geometry("700x500")
        self.root.configure(bg="#F3E7D1")

        self.rezervacije = []

        # -------- MENI --------
        self.menu = tk.Menu(self.root, bg="#936F47", fg="white")
        self.root.config(menu=self.menu)

        meni = tk.Menu(self.menu, tearoff=0, bg="#EFCD55")
        self.menu.add_cascade(label="Meni", menu=meni)
        meni.add_command(label="O aplikaciji", command=self.show_about)
        meni.add_command(label="Raspored stolova", command=self.show_stolovi)
        meni.add_command(label="Rezervacija", command=self.open_rezervacija_window)

        # -------- NASLOV --------
        self.info = tk.Label(
            root,
            text=f"{IME_RESTORANA}\nRadno vrijeme: {RADNO_VRIJEME}",
            font=("Arial", 18, "bold"),
            bg="#F3E7D1",
            fg="#BB6065"
        )
        self.info.pack(pady=20)

        # -------- LISTA REZERVACIJA --------
        self.lista = tk.Listbox(
            root,
            width=80,
            height=10,
            bg="#E5A8A8",
            fg="white",
            font=("Courier", 10)
        )
        self.lista.pack(padx=20, pady=10)

        tk.Button(
            root,
            text="Nova rezervacija",
            command=self.open_rezervacija_window,
            bg="#EFCD55",
            fg="#6B3E26",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        # Učitaj podatke pri pokretanju
        self.ucitaj_xml()
        self.osvjezi_listu()

    # ------------------ O APLIKACIJI ------------------
    def show_about(self):
        messagebox.showinfo(
            "O aplikaciji",
            f"Restoran: {IME_RESTORANA}\nRadno vrijeme: {RADNO_VRIJEME}\n\nAutor: Ivano Kljajić"
        )

    # ------------------ RASPORED STOLOVA ------------------
    def show_stolovi(self):
        win = tk.Toplevel(self.root)
        win.title("Raspored stolova")
        win.configure(bg="#F3E7D1")

        try:
            # Napomena: raspored.png mora biti u istom folderu kao i skripta
            img = tk.PhotoImage(file="raspored.png")
            lbl = tk.Label(win, image=img, bg="#F3E7D1")
            lbl.image = img
            lbl.pack(padx=10, pady=10)
        except:
            messagebox.showerror("Greška", "Slika 'raspored.png' nije pronađena u direktoriju.")
            win.destroy()

    # ------------------ PROZOR ZA REZERVACIJU ------------------
    def open_rezervacija_window(self):
        self.win_rez = tk.Toplevel(self.root)
        self.win_rez.title("Nova Rezervacija")
        self.win_rez.configure(bg="#F3E7D1")

        labels = ["Ime i prezime", "Broj osoba", "Datum", "Broj stola"]
        self.entries = []

        for i, text in enumerate(labels):
            tk.Label(self.win_rez, text=text, bg="#F3E7D1").grid(row=i, column=0, pady=5, padx=5, sticky="e")
            e = tk.Entry(self.win_rez)
            e.grid(row=i, column=1, pady=5, padx=5)
            self.entries.append(e)

        tk.Button(
            self.win_rez,
            text="Spremi",
            command=self.spremi_rezervaciju,
            bg="#EFCD55",
            fg="#6B3E26",
            font=("Arial", 11, "bold")
        ).grid(row=4, column=0, columnspan=2, pady=15)

    # ------------------ SPREMANJE ------------------
    def spremi_rezervaciju(self):
        podaci = [e.get() for e in self.entries]

        if not all(podaci):
            messagebox.showwarning("Upozorenje", "Sva polja moraju biti popunjena!")
            return

        ime, osobe, datum, stol = podaci
        r = Rezervacija(ime, osobe, datum, stol)
        self.rezervacije.append(r)

        self.spremi_xml()
        self.spremi_txt(r)
        self.osvjezi_listu()
        
        messagebox.showinfo("Uspjeh", "Rezervacija je uspješno spremljena.")
        self.win_rez.destroy() # Zatvara prozor nakon spremanja

    # ------------------ XML LOGIKA ------------------
    def spremi_xml(self):
        root = ET.Element("Rezervacije")
        for r in self.rezervacije:
            rez = ET.SubElement(root, "Rezervacija")
            ET.SubElement(rez, "ImePrezime").text = r.ime_prezime
            ET.SubElement(rez, "BrojOsoba").text = r.broj_osoba
            ET.SubElement(rez, "Datum").text = r.datum
            ET.SubElement(rez, "BrojStola").text = r.broj_stola

        tree = ET.ElementTree(root)
        tree.write(XML_FILE, encoding="utf-8", xml_declaration=True)

    def ucitaj_xml(self):
        if not os.path.exists(XML_FILE):
            return

        try:
            tree = ET.parse(XML_FILE)
            root = tree.getroot()

            self.rezervacije = [] # Resetiramo listu prije učitavanja
            for rez in root.findall("Rezervacija"):
                self.rezervacije.append(
                    Rezervacija(
                        rez.find("ImePrezime").text,
                        rez.find("BrojOsoba").text,
                        rez.find("Datum").text,
                        rez.find("BrojStola").text
                    )
                )
        except Exception as e:
            print(f"Greška pri učitavanju XML-a: {e}")

    # ------------------ TXT LOGIKA ------------------
    def spremi_txt(self, r):
        with open(TXT_FILE, "a", encoding="utf-8") as f:
            f.write(f"{r.ime_prezime}, {r.broj_osoba}, {r.datum}, {r.broj_stola}\n")

    # ------------------ OSVJEŽAVANJE LISTE ------------------
    def osvjezi_listu(self):
        self.lista.delete(0, tk.END)
        for r in self.rezervacije:
            prikaz = f"{r.ime_prezime.ljust(20)} | Gosti: {r.broj_osoba} | Datum: {r.datum} | Stol: {r.broj_stola}"
            self.lista.insert(tk.END, prikaz)

# ------------------ START ------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = RezervacijaApp(root)
    root.mainloop()
