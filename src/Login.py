from pathlib import Path
from tkinter import END, Checkbutton, Tk, Canvas, Button, Entry, messagebox
import tkinter as Tk
from PIL import Image, ImageTk
import psycopg2
from datetime import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class LoginPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Login()
    
    def Login(self):
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
            160.0,
            40.0,
            anchor="nw",
            text="Login",
            fill="#000000",
            font=("MontserratRoman SemiBold", 30 * -1)
        )
        
        image_path = relative_to_assets("login.png")
        image = Image.open(image_path)
        resized_image = image.resize((300, 200))  # Adjust the desired width and height
        self.image_login = ImageTk.PhotoImage(resized_image)
        self.login = self.canvas.create_image(
            200.0,
            180.0,
            image=self.image_login
        )

        self.canvas.create_text(
            50.0,
            300.0,
            anchor="nw",
            text="Username",
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
            y=320.0,
            width=300.0,
            height=30.0
        )
        
        self.canvas.create_text(
            50.0,
            380.0,
            anchor="nw",
            text="Password",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )

        self.entry_2 = Entry(
            bd=0,
            bg="#BCD9EA",
            fg="#000000",
            highlightthickness=0,
            insertbackground = "#000000",
            font=("MontserratRoman SemiBold", 12 * -1),
            show='*'
        )
        self.entry_2.place(
            x=50.0,
            y=400.0,
            width=300.0,
            height=30.0
        )

        self.b1 = Button(text="Login", bg='#026AA7',command=self.login_done)
        self.b1.place(
            x=140.0,
            y=480.0,
            width=120.0,
            height=40.0
        )

        self.cb1 = Checkbutton(text="Show Password", bg='#FFFFFF', command=self.show_password)
        self.cb1.place(
            x=240.0,
            y=375.0,
        )

    def show_password(self):
        if self.entry_2.cget('show') == "*":
            self.entry_2.config(show='')
        else:
            self.entry_2.config(show="*")
    
    def login_done(self):
        try:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="datapengguna",
                user="postgres",
                password="postgres",
                port=5432
            )
            
            cursor = connection.cursor()
            if self.entry_1.get() == "" or self.entry_2.get() == "":
                messagebox.showerror("Error", "Tolong isi semua input")
                self.clear()
            else:
                cursor.execute("SELECT * FROM datapengguna WHERE username = %s AND password = %s", (self.entry_1.get(), self.entry_2.get()))
                user = cursor.fetchone()
                if user:
                    query = "INSERT INTO datalogin (username, password, login_time) VALUES (%s, %s, %s)"
                    values = (
                        self.entry_1.get(),
                        self.entry_2.get(),
                        datetime.now()
                    )
                    cursor.execute(query, values)
                    connection.commit() 
                    self.origin.Home()
                else:
                    messagebox.showerror("Error", "Invalid username or password")
                    self.clear()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            messagebox.showerror("Error", "An error occurred while saving data to the database")

    def clear (self):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)

    def startPage(self):
        self.mainloop()
