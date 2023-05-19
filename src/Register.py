import hashlib
from tkinter import Tk, Canvas, Button, Entry, messagebox, Checkbutton, END
import tkinter as Tk
import psycopg2
from datetime import datetime
import re

class RegisterPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Register()
    
    def Register(self):
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
            140.0,
            30.0,
            anchor="nw",
            text="Register",
            fill="#000000",
            font=("MontserratRoman SemiBold", 30 * -1)
        )

        self.canvas.create_text(
            50.0,
            100.0,
            anchor="nw",
            text="Nomor Rekening",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )

        self.entry_1 = Entry(
            bd=0,
            bg="#BCD9EA",
            fg="#000000",
            highlightthickness=0,
            insertbackground = "#000000",
            font=("MontserratRoman SemiBold", 12 * -1)
        )
        self.entry_1.place(
            x=50.0,
            y=120.0,
            width=300.0,
            height=30.0
        )

        self.canvas.create_text(
            50.0,
            170.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )

        self.entry_2 = Entry(
            bd=0,
            bg="#BCD9EA",
            fg="#000000",
            highlightthickness=0,
            insertbackground = "#000000",
            font=("MontserratRoman SemiBold", 12 * -1)
        )
        self.entry_2.place(
            x=50.0,
            y=190.0,
            width=300.0,
            height=30.0
        )

        self.canvas.create_text(
            50.0,
            240.0,
            anchor="nw",
            text="Username",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )

        self.entry_3 = Entry(
            bd=0,
            bg="#BCD9EA",
            fg="#000000",
            highlightthickness=0,
            insertbackground = "#000000",
            font=("MontserratRoman SemiBold", 12 * -1)
        )
        self.entry_3.place(
            x=50.0,
            y=260.0,
            width=300.0,
            height=30.0
        )

        self.canvas.create_text(
            50.0,
            310.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1),
        )

        self.entry_4 = Entry(
            bd=0,
            bg="#BCD9EA",
            fg="#000000",
            highlightthickness=0,
            insertbackground = "#000000",
            font=("MontserratRoman SemiBold", 12 * -1),
            show='*'
        )
        self.entry_4.place(
            x=50.0,
            y=330.0,
            width=300.0,
            height=30.0
        )

        self.canvas.create_text(
            50.0,
            380.0,
            anchor="nw",
            text="PIN (6 angka)",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1),
        )

        self.entry_5 = Entry(
            bd=0,
            bg="#BCD9EA",
            fg="#000000",
            highlightthickness=0,
            insertbackground = "#000000",
            font=("MontserratRoman SemiBold", 12 * -1),
            show='*'
        )
        self.entry_5.place(
            x=50.0,
            y=400.0,
            width=300.0,
            height=30.0
        )

        self.b1 = Button(text="Register", bg='#026AA7', command=self.registration_done)
        self.b1.place(
            x=140.0,
            y=480.0,
            width=120.0,
            height=40.0
        )
        
        self.cb1 = Checkbutton(text="Show Password", bg='#FFFFFF', command=self.show_password_1)
        self.cb1.place(
            x=240.0,
            y=305.0,
        )

        self.cb2 = Checkbutton(text="Show Password", bg='#FFFFFF', command=self.show_password_2)
        self.cb2.place(
            x=240.0,
            y=375.0,
        )
        
    def show_password_1(self):
        if self.entry_4.cget('show') == "*":
            self.entry_4.config(show='')
        else:
            self.entry_4.config(show="*")

    def show_password_2(self):
        if self.entry_5.cget('show') == "*":
            self.entry_5.config(show='')
        else:
            self.entry_5.config(show="*")
    
    def get_register_time(self):
        return datetime.now()

    def registration_done(self):
        try:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="datapengguna",
                user="postgres",
                password="postgres",
                port=5432
            )
            cursor = connection.cursor()
            email_pattern = r"[^@]+@[^@]+\.[^@]+"
            username_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"
            password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$"
            if self.entry_1.get() == "" or self.entry_2.get() == "" or self.entry_3.get() == "" or self.entry_4.get() == "" or self.entry_5.get() == "":
                messagebox.showerror("Error", "Tolong isi semua input")
            elif not self.entry_1.get().isdigit():
                messagebox.showerror("Error", "Nomor rekening harus berupa angka")
            elif not re.match(email_pattern, self.entry_2.get()):
                messagebox.showerror("Error", "Email tidak valid")
            elif not re.match(username_pattern, self.entry_3.get()):  # Memeriksa username
                messagebox.showerror("Error", "Username harus memiliki setidaknya satu huruf kecil, satu huruf besar, dan satu angka")
            elif not re.match(password_pattern, self.entry_4.get()):  # Memeriksa password
                messagebox.showerror("Error", "Password harus memiliki setidaknya satu huruf kecil, satu huruf besar, dan satu angka")
            elif len(self.entry_5.get()) != 6:
                messagebox.showerror("Error", "PIN harus terdiri dari 6 digit")
            elif not self.entry_5.get().isdigit():
                messagebox.showerror("Error", "PIN harus berupa angka")
            else:
                check_nomor_rekening_query = "SELECT * FROM datapengguna WHERE nomor_rekening = %s"
                values_check_nomor_rekening = (
                    self.entry_1.get(),
                )
                cursor.execute(check_nomor_rekening_query, values_check_nomor_rekening)
                result_check_nomor_rekening = cursor.fetchone()
                check_email_query = "SELECT * FROM datapengguna WHERE email = %s"
                values_check_email = (
                    self.entry_2.get(),
                )
                cursor.execute(check_email_query, values_check_email)
                result_check_email = cursor.fetchone()
                check_username_query = "SELECT * FROM datapengguna WHERE username = %s"
                values_check_username = (
                    self.entry_3.get(),
                )
                cursor.execute(check_username_query, values_check_username)
                result_check_username = cursor.fetchone()
                if result_check_nomor_rekening is not None:
                    messagebox.showerror("Error", "Nomor rekening sudah pernah digunakan")
                elif result_check_email is not None:
                    messagebox.showerror("Error", "Email sudah pernah digunakan")
                elif result_check_username is not None:
                    messagebox.showerror("Error", "Username sudah pernah digunakan")
                else :
                    query = "INSERT INTO datapengguna (nomor_rekening, email, username, password, pin, otp, register_time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (
                        self.entry_1.get(),
                        self.entry_2.get(),
                        self.entry_3.get(),
                        self.entry_4.get(),
                        self.entry_5.get(),
                        self.generate_otp(),
                        self.get_register_time()
                    )
                    cursor.execute(query, values)
                    connection.commit()
                    
                    self.clear()
                    messagebox.showinfo("Success", "Your OTP is " + str(values[5]) + ". Please input OTP in 5 minutes")
                    self.origin.VerifyRegisterOtp()
                    cursor.close()
                    connection.close()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            messagebox.showerror("Error", "An error occurred while saving data to the database")

    def clear (self):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)
        self.entry_4.delete(0, END)
        self.entry_5.delete(0, END)

    def generate_otp(self):
        input_string = self.entry_1.get() + self.entry_2.get() + self.entry_3.get() + self.entry_4.get() + self.entry_5.get() + str(self.get_register_time())
        hashed_string = hashlib.sha256(input_string.encode()).hexdigest()
        otp = hashed_string[:6]
        numeric_otp = int(otp, 16) % 1000000
        return numeric_otp
    
    def startPage(self):
        self.mainloop()
