import tkinter as tk
class Ucenik:
    ucenici = []
    def __init__(self, ime, prezime, razred):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
    def __str__(self):
        return f"{self.prezime} {self.ime} ({self.razred})"
class EvidencijaApp:
    def dodaj_ucenika(self):
        ime = self.ime_entry.get()
        prezime = self.prezime_entry.get()
        razred = self.razred_entry.get()
        dodani_ucenik = Ucenik(ime, prezime, razred)
        if ime and prezime and razred:
            Ucenik.ucenici.append(dodani_ucenik)
            self.osvjezi_listu_ucenika()
            self.ime_entry.delete(0, tk.END)
            self.prezime_entry.delete(0, tk.END)
            self.razred_entry.delete(0, tk.END)
    def __init__(self, root):
        self.root = root
        self.root.title("Evidencija Učenika")
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1) 
        self.unos_frame = tk.Frame(self.root, padx=10, pady=10)
        self.unos_frame.grid(row=0, column=0, sticky="ew")
        self.unos_frame.columnconfigure(1, weight=1)
        tk.Label(self.unos_frame, text="Ime:").grid(row=0, column=0, sticky="w", pady=2)
        self.ime_entry = tk.Entry(self.unos_frame)
        self.ime_entry.grid(row=0, column=1, sticky="ew", pady=2)
        tk.Label(self.unos_frame, text="Prezime:").grid(row=1, column=0, sticky="w", pady=2)
        self.prezime_entry = tk.Entry(self.unos_frame)
        self.prezime_entry.grid(row=1, column=1, sticky="ew", pady=2)
        tk.Label(self.unos_frame, text="Razred:").grid(row=2, column=0, sticky="w", pady=2)
        self.razred_entry = tk.Entry(self.unos_frame)
        self.razred_entry.grid(row=2, column=1, sticky="ew", pady=2)
        self.dodaj_button = tk.Button(self.unos_frame, text="Dodaj učenika", command=self.dodaj_ucenika)
        self.dodaj_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.spremi_izmjene_button = tk.Button(self.unos_frame, text="Spremi izmjene", command=self.spremi_izmjene)
        self.spremi_izmjene_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.lista_frame = tk.Frame(self.root, padx=10, pady=10)
        self.lista_frame.grid(row=1, column=0, sticky="nsew")
        self.lista_label = tk.Label(self.lista_frame, text="Popis učenika:")
        self.lista_label.pack(anchor="nw", pady=(0, 5))

        self.scrollbar = tk.Scrollbar(self.lista_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_ucenika_listbox = tk.Listbox(self.lista_frame, height=10, width=50, yscrollcommand=self.scrollbar.set)
        self.lista_ucenika_listbox.pack(side=tk.LEFT, fill="both", expand=True)

        self.scrollbar.config(command=self.lista_ucenika_listbox.yview)
    def odaberite_ucenika(self):
        selected_index = self.lista_ucenika_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_ucenik = Ucenik.ucenici[index]
            self.ime_entry.delete(0, tk.END)
            self.ime_entry.insert(0, selected_ucenik.ime)
            self.prezime_entry.delete(0, tk.END)
            self.prezime_entry.insert(0, selected_ucenik.prezime)
            self.razred_entry.delete(0, tk.END)
            self.razred_entry.insert(0, selected_ucenik.razred)
            

    def spremi_izmjene(self):
        selected_index = self.lista_ucenika_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            ucenik_za_izmjenu = Ucenik.ucenici[index]
            ucenik_za_izmjenu.ime = self.ime_entry.get()
            ucenik_za_izmjenu.prezime = self.prezime_entry.get()
            ucenik_za_izmjenu.razred = self.razred_entry.get()
            self.osvjezi_listu_ucenika()

    def osvjezi_listu_ucenika(self):
        self.lista_ucenika_listbox.delete(0, tk.END)
        for ucenik in Ucenik.ucenici:
            self.lista_ucenika_listbox.insert(tk.END, str(ucenik) + "\n")
        self.lista_ucenika_listbox.bind("<<ListboxSelect>>", lambda event: self.odaberite_ucenika())






if __name__ == "__main__":
    root = tk.Tk()
    app = EvidencijaApp(root)
root.mainloop()