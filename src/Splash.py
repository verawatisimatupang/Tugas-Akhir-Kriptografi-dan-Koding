from pathlib import Path
from tkinter import Tk, Canvas, Button
import tkinter as Tk
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class SplashPage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Splash()
    
    def Splash(self):
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
            20.0,
            60.0,
            anchor="nw",
            text="Selamat Datang di Mobile Banking Yahuu",
            fill="#000000",
            font=("MontserratRoman SemiBold", 20 * -1)
        )

        self.canvas.create_text(
            60.0,
            90.0,
            anchor="nw",
            text="Verawati Esteria S. Simatupang - 18220002",
            fill="#000000",
            font=("MontserratRoman SemiBold", 14 * -1)
        )

        image_path = relative_to_assets("splash.png")
        image = Image.open(image_path)
        resized_image = image.resize((300, 200))  # Adjust the desired width and height
        self.image_splash = ImageTk.PhotoImage(resized_image)
        self.splash = self.canvas.create_image(
            200.0,
            230.0,
            image=self.image_splash
        )

        self.b1 = Button(text="Punya Akun", bg='#026AA7', command=lambda: self.click_login())
        self.b1.place(
            x=140.0,
            y=355.0,
            width=120.0,
            height=40.0
        )

        self.b2 = Button(text="Belum Punya Akun", bg='#FFFFFF', command=lambda: self.click_register())
        self.b2.place(
            x=140.0,
            y=400.0,
            width=120.0,
            height=40.0
        )

    def startPage(self):
        self.mainloop()
    
    def click_login(self):
        self.origin.Login()
    
    def click_register(self):
        self.origin.Register()
