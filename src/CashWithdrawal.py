from datetime import datetime, timedelta
from pathlib import Path
from tkinter import END, Checkbutton, StringVar, Tk, Canvas, Button, Entry, messagebox, Radiobutton
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

        self.cbb1 = Combobox(self.master, state='readonly')
        self.cbb1.place(
            x=50.0, 
            y=170.0, 
            width=140.0, 
            height=30.0
        )
        self.cbb1['values'] = ('ATM', 'Indomaret', 'Agen Bank Yahuu')
        self.cbb1.set('Pilih Jalur Tarik Tunai')
        
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
        self.rb1 = Radiobutton(self.master, text="Rp 100.000", variable=self.radio1, value="Rp100.000", bg="#FFFFFF")
        self.rb1.place(
            x=50.0, 
            y=240.0, 
        )

        self.rb2 = Radiobutton(self.master, text="Rp 300.000", variable=self.radio1, value="Rp300.000", bg="#FFFFFF")
        self.rb2.place(
            x=50.0, 
            y=260.0, 
        )

        self.rb3 = Radiobutton(self.master, text="Rp 500.000", variable=self.radio1, value="Rp500.000", bg="#FFFFFF")
        self.rb3.place(
            x=50.0, 
            y=280.0, 
        )

        self.rb4 = Radiobutton(self.master, text="Rp 700.000", variable=self.radio1, value="Rp700.000", bg="#FFFFFF")
        self.rb4.place(
            x=50.0, 
            y=300.0, 
        )

        self.rb5 = Radiobutton(self.master, text="Rp 900.000", variable=self.radio1, value="Rp900.000", bg="#FFFFFF")
        self.rb5.place(
            x=50.0, 
            y=320.0, 
        )

        self.rb6 = Radiobutton(self.master, text="Rp 200.000", variable=self.radio1, value="Rp200.000", bg="#FFFFFF")
        self.rb6.place(
            x=200.0, 
            y=240.0, 
        )

        self.rb7 = Radiobutton(self.master, text="Rp 400.000", variable=self.radio1, value="Rp400.000", bg="#FFFFFF")
        self.rb7.place(
            x=200.0, 
            y=260.0, 
        )

        self.rb8 = Radiobutton(self.master, text="Rp 600.000", variable=self.radio1, value="Rp600.000", bg="#FFFFFF")
        self.rb8.place(
            x=200.0, 
            y=280.0, 
        )

        self.rb9 = Radiobutton(self.master, text="Rp 800.000", variable=self.radio1, value="Rp800.000", bg="#FFFFFF")
        self.rb9.place(
            x=200.0, 
            y=300.0, 
        )

        self.rb10 = Radiobutton(self.master, text="Rp 1.000.000", variable=self.radio1, value="Rp1.000.000", bg="#FFFFFF")
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
            bg="#BCD9EA",
            fg="#000000",
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

        self.b1 = Button(text="Konfirmasi", bg='#026AA7', command=self.confirmation_done)
        self.b1.place(
            x=140.0,
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

    def get_cashwithdrawal_time(self):
        return datetime.now()
    
    def confirmation_done(self):
        try:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="datapengguna",
                user="postgres",
                password="postgres",
                port=5432
            )        
            cursor = connection.cursor()
            if self.cbb1.get() == "Pilih Jalur Tarik Tunai" or self.radio1.get() == "" or self.entry_1.get() == "" :
                messagebox.showerror("Error", "Tolong isi semua input")
            elif len(self.entry_1.get()) != 6:
                messagebox.showerror("Error", "PIN harus terdiri dari 6 digit")
            elif not self.entry_1.get().isdigit():
                messagebox.showerror("Error", "PIN harus berupa angka")
            elif self.entry_1.get() != self.get_pin():
                messagebox.showerror("Error", "PIN salah!")
            else:
                query = "INSERT INTO datatransaksi (username, nomor_rekening, jalur_tarik_tunai, nominal, pin, otp, cashwithdrawal_time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (
                    self.get_logged_in_account(),
                    self.get_nomor_rekening(),
                    self.cbb1.get(),
                    self.radio1.get(),
                    self.entry_1.get(),
                    self.generate_otp(),
                    self.get_cashwithdrawal_time()
                )
                cursor.execute(query, values)
                connection.commit()
                self.clear()
                messagebox.showinfo("Success", "Your OTP is " + str(values[5]) + ". Please input OTP in 5 minutes")        
                otp_time = values[6]
                current_time = datetime.now()
                if current_time < otp_time + timedelta(minutes=5) :
                    delete_query = f"DELETE FROM datatransaksi where username = '{self.get_logged_in_account()}'"
                    cursor.execute(delete_query)
                    connection.commit()
                    self.origin.Home()
                elif current_time > otp_time + timedelta(minutes=5) :
                    messagebox.showwarning("Times Up", "Registration failed")
                    delete_query = f"DELETE FROM datatransaksi where username = '{self.get_logged_in_account()}'"
                    cursor.execute(delete_query)
                    connection.commit()
                    self.origin.Home()
                cursor.close()
                connection.close()      
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            messagebox.showerror("Error", "An error occurred while saving data to the database")

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
            logged_in_account_query = "SELECT username FROM datalogin ORDER BY login_time DESC LIMIT 1"
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
            logged_in_account_query = "SELECT username FROM datalogin ORDER BY login_time DESC LIMIT 1"
            cursor.execute(logged_in_account_query)
            logged_in_account = cursor.fetchone()[0]
            query = f"SELECT dp.nomor_rekening FROM datapengguna dp JOIN datalogin dl ON dp.username = dl.username WHERE dl.username = '{logged_in_account}'"
            cursor.execute(query)
            result = cursor.fetchone()[0]
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

    def get_pin(self):
        try:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="datapengguna",
                user="postgres",
                password="postgres",
                port=5432
            )
            cursor = connection.cursor()
            logged_in_account_query = "SELECT username FROM datalogin ORDER BY login_time DESC LIMIT 1"
            cursor.execute(logged_in_account_query)
            logged_in_account = cursor.fetchone()[0]
            pin_query = f"SELECT dp.pin FROM datapengguna dp JOIN datalogin dl ON dp.username = dl.username WHERE dl.username = '{logged_in_account}'"
            cursor.execute(pin_query)
            pin = cursor.fetchone()[0]
            return pin
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            messagebox.showerror("Error", "An error occurred while saving data to the database")

    def generate_otp(self):
        input_string = self.entry_1.get() + self.get_logged_in_account() + self.get_nomor_rekening() + self.radio1.get() + self.cbb1.get() + str(self.get_cashwithdrawal_time())
        hashed_string = hashlib.sha256(input_string.encode()).hexdigest()
        otp = hashed_string[:6]
        numeric_otp = int(otp, 16) % 1000000
        return numeric_otp
    
    def clear(self):
        self.cbb1.set('Pilih Jalur Tarik Tunai')
        self.radio1.set(None)
        self.entry_1.delete(0, END)

    def startPage(self):
        self.mainloop()
