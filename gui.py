import tkinter as tk

imena_lista = []

def klik_na_gumb():
    ime = unos_imena.get()
    if ime:
        pozdrav_label = tk.Label(prozor, text=f"Pozdrav {ime}")
        pozdrav_label.pack()
        imena_lista.append(ime) 
        print(f"Sva unesena imena: {imena_lista}") 


prozor = tk.Tk()
prozor.title("moj prvi GUI program")

uputa = tk.Label(prozor, text="unesite svoje ime")
uputa.pack()

prozor.geometry("400x300")
gumb = tk.Button(prozor, text="pozdravi me", command=klik_na_gumb)
gumb.pack()
unos_imena = tk.Entry(prozor)
unos_imena.pack()
prozor.mainloop()
