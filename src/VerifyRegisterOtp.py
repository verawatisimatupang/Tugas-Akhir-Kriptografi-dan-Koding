from datetime import datetime, timedelta
from pathlib import Path
from tkinter import END, Tk, Canvas, Button, Entry, messagebox
import tkinter as Tk
import psycopg2
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class VerifyRegisterOtpPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.VerifyRegisterOtp()
    
    def VerifyRegisterOtp(self):
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
            60.0,
            30.0,
            anchor="nw",
            text="Masukkan Kode OTP",
            fill="#000000",
            font=("MontserratRoman SemiBold", 30 * -1)
        )

        image_path = relative_to_assets("otp.png")
        image = Image.open(image_path)
        resized_image = image.resize((200, 150))  # Adjust the desired width and height
        self.image_login = ImageTk.PhotoImage(resized_image)
        self.login = self.canvas.create_image(
            200.0,
            170.0,
            image=self.image_login
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
            y=300.0,
            width=300.0,
            height=30.0
        )

        self.b1 = Button(text="Submit", bg='#026AA7', command=self.verify_otp)
        self.b1.place(
            x=140.0,
            y=480.0,
            width=120.0,
            height=40.0
        )

    def verify_otp(self):
        try:
            connection = psycopg2.connect(
                host="127.0.0.1",
                database="datapengguna",
                user="postgres",
                password="postgres",
                port=5432
            )
            cursor = connection.cursor()
            logged_in_account_query = "SELECT username FROM datapengguna ORDER BY register_time DESC LIMIT 1"
            cursor.execute(logged_in_account_query)
            logged_in_account = cursor.fetchone()[0]
            query = f"SELECT otp, register_time FROM datapengguna where username = '{logged_in_account}'"
            cursor.execute(query)
            result = cursor.fetchone()
            otp_time = result[1]
            current_time = datetime.now()
            if result[0] == str(self.entry_1.get()) and current_time < otp_time + timedelta(minutes=5) :
                self.clear()
                messagebox.showinfo("Success", "Registration successfully")
                self.origin.Login()
            elif current_time > otp_time + timedelta(minutes=5) :
                self.clear()
                messagebox.showwarning("Times Up", "Registration failed")
                delete_query = f"DELETE FROM datapengguna where username = '{logged_in_account}'"
                cursor.execute(delete_query)
                connection.commit()
                self.origin.Register()
            elif result[0] != str(self.entry_1.get()) :
                self.clear()
                messagebox.showerror("Error", "Invalid otp")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
            messagebox.showerror("Error", "An error occurred while saving data to the database")

    def clear (self):
        self.entry_1.delete(0, END)

    def startPage(self):
        self.mainloop()
