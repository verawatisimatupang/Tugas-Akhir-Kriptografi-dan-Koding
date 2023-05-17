import hashlib
from tkinter import Tk, Canvas, Button, Entry, messagebox, Checkbutton, END
import tkinter as Tk
import psycopg2
from datetime import datetime

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
            bg="#FA8072",
            fg="#FFFFFF",
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
            bg="#FA8072",
            fg="#FFFFFF",
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
            bg="#FA8072",
            fg="#FFFFFF",
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
            bg="#FA8072",
            fg="#FFFFFF",
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
            bg="#FA8072",
            fg="#FFFFFF",
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

        self.b1 = Button(text="Register", bg='#FA8072', command=self.registration_done)
        self.b1.place(
            x=150.0,
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
            
            query = "INSERT INTO datapengguna (nomor_rekening, email, username, password, pin) VALUES (%s, %s, %s, %s, %s)"
            values = (
                self.entry_1.get(),
                self.entry_2.get(),
                self.entry_3.get(),
                self.entry_4.get(),
                self.entry_5.get()
            )
            
            cursor.execute(query, values)
            connection.commit()
            
            # print(self.generate_otp())
            messagebox.showinfo("Success", "Registration succefully")
            self.clear()
            
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
        input_string = self.entry_1.get() + self.entry_2.get() + self.entry_3.get() + self.entry_4.get() + self.entry_5.get() + str(datetime.now())
        hashed_string = hashlib.sha256(input_string.encode()).hexdigest()
        otp = hashed_string[:6]
        numeric_otp = int(otp, 16) % 1000000
        return numeric_otp
    
    def startPage(self):
        self.mainloop()
