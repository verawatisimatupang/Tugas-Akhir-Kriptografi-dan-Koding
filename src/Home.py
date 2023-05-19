from pathlib import Path
from tkinter import Tk, Canvas, Button, Entry
import tkinter as Tk
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HomePage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Home()
    
    def Home(self):
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
            text="Bank Yahuu",
            fill="#000000",
            font=("MontserratRoman SemiBold", 30 * -1)
        )

        image_path = relative_to_assets("saving.png")
        image = Image.open(image_path)
        resized_image = image.resize((250, 200))  # Adjust the desired width and height
        self.image_login = ImageTk.PhotoImage(resized_image)
        self.login = self.canvas.create_image(
            200.0,
            200.0,
            image=self.image_login
        )

        self.b1 = Button(text="Tarik Tunai", bg='#026AA7', command=lambda: self.click_cashwithdrawal())
        self.b1.place(
            x=140.0,
            y=355.0,
            width=120.0,
            height=40.0
        )

        self.b2 = Button(text="Keluar", bg='#FFFFFF', command=lambda: self.click_splash())
        self.b2.place(
            x=140.0,
            y=400.0,
            width=120.0,
            height=40.0
        )

    def startPage(self):
        self.mainloop()
    
    def click_splash(self):
        self.origin.Splash()
    
    def click_cashwithdrawal(self):
        self.origin.CashWithdrawal()
