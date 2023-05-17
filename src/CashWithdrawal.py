from datetime import datetime
from pathlib import Path
from tkinter import Checkbutton, StringVar, Tk, Canvas, Button, Entry, messagebox, Radiobutton
import tkinter as Tk
from tkinter.ttk import Combobox
import psycopg2
import hashlib

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CashWithdrawalPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.CashWithdrawal()
    
    def CashWithdrawal(self):
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 550,
            width = 400,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.canvas.create_text(
            120.0,
            40.0,
            anchor="nw",
            text="Tarik Tunai",
            fill="#000000",
            font=("MontserratRoman SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            50.0,
            100.0,
            anchor="nw",
            text="Sumber Dana",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )

        self.canvas.create_text(
            50.0,
            140.0,
            anchor="nw",
            text="Jalur Tarik Tunai",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )

        self.cb1 = Combobox(self.master, state='readonly')
        self.cb1.place(
            x=50.0, 
            y=170.0, 
            width=140.0, 
            height=30.0
        )
        self.cb1['values'] = ('ATM', 'Indomaret', 'Agen Bank Yahuu')
        self.cb1.set('Pilih Jalur Tarik Tunai')
        
        self.canvas.create_text(
            50.0,
            220.0,
            anchor="nw",
            text="Pilih Nominal",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )
        
        self.radio1 = StringVar()
        self.radio1.set(None) 
        self.rb1 = Radiobutton(self.master, text="Rp 100.000", variable=self.radio1, value="Rp 100.000", bg="#FFFFFF")
        self.rb1.place(
            x=50.0, 
            y=240.0, 
        )

        self.rb2 = Radiobutton(self.master, text="Rp 300.000", variable=self.radio1, value="Rp 300.000", bg="#FFFFFF")
        self.rb2.place(
            x=50.0, 
            y=260.0, 
        )

        self.rb3 = Radiobutton(self.master, text="Rp 500.000", variable=self.radio1, value="Rp 500.000", bg="#FFFFFF")
        self.rb3.place(
            x=50.0, 
            y=280.0, 
        )

        self.rb4 = Radiobutton(self.master, text="Rp 700.000", variable=self.radio1, value="Rp 700.000", bg="#FFFFFF")
        self.rb4.place(
            x=50.0, 
            y=300.0, 
        )

        self.rb5 = Radiobutton(self.master, text="Rp 900.000", variable=self.radio1, value="Rp 900.000", bg="#FFFFFF")
        self.rb5.place(
            x=50.0, 
            y=320.0, 
        )

        self.rb6 = Radiobutton(self.master, text="Rp 200.000", variable=self.radio1, value="Rp 200.000", bg="#FFFFFF")
        self.rb6.place(
            x=200.0, 
            y=240.0, 
        )

        self.rb7 = Radiobutton(self.master, text="Rp 400.000", variable=self.radio1, value="Rp 400.000", bg="#FFFFFF")
        self.rb7.place(
            x=200.0, 
            y=260.0, 
        )

        self.rb8 = Radiobutton(self.master, text="Rp 600.000", variable=self.radio1, value="Rp 600.000", bg="#FFFFFF")
        self.rb8.place(
            x=200.0, 
            y=280.0, 
        )

        self.rb9 = Radiobutton(self.master, text="Rp 800.000", variable=self.radio1, value="Rp 800.000", bg="#FFFFFF")
        self.rb9.place(
            x=200.0, 
            y=300.0, 
        )

        self.rb10 = Radiobutton(self.master, text="Rp 1.000.000", variable=self.radio1, value="Rp 1.000.000", bg="#FFFFFF")
        self.rb10.place(
            x=200.0, 
            y=320.0, 
        )

        self.canvas.create_text(
            50.0,
            370.0,
            anchor="nw",
            text="PIN",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )

        self.entry_1 = Entry(
            bd=0,
            bg="#FA8072",
            fg="#FFFFFF",
            highlightthickness=0,
            insertbackground = "#000000",
            font=("MontserratRoman SemiBold", 12 * -1),
            show='*'
        )
        self.entry_1.place(
            x=50.0,
            y=390.0,
            width=300.0,
            height=30.0
        )

        self.b1 = Button(text="Konfirmasi", bg='#FA8072', command=self.generate_otp)
        self.b1.place(
            x=130.0,
            y=450.0,
            width=120.0,
            height=40.0
        )

        self.cb1 = Checkbutton(text="Show Password", bg='#FFFFFF', command=self.show_password)
        self.cb1.place(
            x=240.0,
            y=365.0,
        )

        self. get_nomor_rekening()

    def show_password(self):
        if self.entry_1.cget('show') == "*":
            self.entry_1.config(show='')
        else:
            self.entry_1.config(show="*")

    def get_logged_in_account(self):
        try:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="datapengguna",
                user="postgres",
                password="postgres",
                port=5432
            )

            cursor = connection.cursor()

            logged_in_account_query = "SELECT username FROM datalogin ORDER BY username DESC LIMIT 1"
            cursor.execute(logged_in_account_query)
            logged_in_account = cursor.fetchone()[0]

            return logged_in_account

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            messagebox.showerror("Error", "An error occurred while retrieving logged-in account")

    def get_nomor_rekening(self):
        try:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="datapengguna",
                user="postgres",
                password="postgres",
                port=5432
            )
            
            cursor = connection.cursor()

            logged_in_account_query = "SELECT username FROM datalogin ORDER BY username DESC LIMIT 1"
            cursor.execute(logged_in_account_query)
            logged_in_account = cursor.fetchone()[0]
            
            # Retrieve the 'nomor_rekening' based on the logged-in account
            query = f"SELECT dp.nomor_rekening FROM datapengguna dp JOIN datalogin dl ON dp.username = dl.username WHERE dl.username = '{logged_in_account}'"
            cursor.execute(query)
            result = cursor.fetchone()[0]
            
            # Update the field in the GUI with the retrieved 'nomor_rekening'
            if result:
                nomor_rekening = result
                self.canvas.create_text(
                    180.0,
                    100.0,
                    anchor="nw",
                    text=nomor_rekening,
                    fill="#000000",
                    font=("MontserratRoman SemiBold", 14 * -1)
                )
                return nomor_rekening
            else:
                messagebox.showerror("Error", "Account not found.")
        
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            messagebox.showerror("Error", "An error occurred while saving data to the database")

    def generate_otp(self):
        input_string = self.entry_1.get() + self.get_logged_in_account() + self.get_nomor_rekening() + self.radio1.get() +  str(datetime.now())
        hashed_string = hashlib.sha256(input_string.encode()).hexdigest()
        otp = hashed_string[:6]
        numeric_otp = int(otp, 16) % 1000000
        return numeric_otp
    
    def startPage(self):
        self.mainloop()