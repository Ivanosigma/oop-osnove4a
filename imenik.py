import sqlite3


# --------------------------------------------------
# INICIJALIZACIJA BAZE I TABLICE
# --------------------------------------------------
def inicijalizacija():
    conn = sqlite3.connect("Imenik.db")
    cur = conn.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS Kontakti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ime_prezime TEXT NOT NULL,
        broj_mobitela TEXT NOT NULL
    );
    """
    cur.execute(sql)
    conn.commit()
    conn.close()


# --------------------------------------------------
# CREATE – UNOS NOVOG KONTAKTA
# --------------------------------------------------
def unesi_kontakt():
    ime = input("Unesi ime i prezime: ")
    broj = input("Unesi broj mobitela: ")

    conn = sqlite3.connect("Imenik.db")
    cur = conn.cursor()

    sql = "INSERT INTO Kontakti (ime_prezime, broj_mobitela) VALUES (?, ?)"
    cur.execute(sql, (ime, broj))

    conn.commit()
    conn.close()

    print("Kontakt uspješno dodan!")


# --------------------------------------------------
# READ – ISPIS SVIH KONTAKATA
# --------------------------------------------------
def ispisi_kontakte():
    conn = sqlite3.connect("Imenik.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Kontakti")
    kontakti = cur.fetchall()

    print("\n--- TELEFONSKI IMENIK ---")
    print(f"{'ID':<5} | {'IME I PREZIME':<25} | {'BROJ'}")
    print("-" * 50)

    for k in kontakti:
        print(f"{k[0]:<5} | {k[1]:<25} | {k[2]}")

    conn.close()


# --------------------------------------------------
# DELETE – BRISANJE KONTAKTA
# --------------------------------------------------
def obrisi_kontakt():
    ispisi_kontakte()
    id_kontakta = input("\nUnesi ID kontakta za brisanje: ")

    conn = sqlite3.connect("Imenik.db")
    cur = conn.cursor()

    sql = "DELETE FROM Kontakti WHERE id = ?"
    cur.execute(sql, (id_kontakta,))

    if cur.rowcount > 0:
        print("Kontakt je obrisan.")
    else:
        print("Kontakt s tim ID-em ne postoji.")

    conn.commit()
    conn.close()


# --------------------------------------------------
# GLAVNI IZBORNIK
# -------------
