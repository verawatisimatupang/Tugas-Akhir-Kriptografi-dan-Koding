from tkinter import Tk
import Splash, Login, Register, Home, CashWithdrawal

class PageManager():
    def __init__(self):
        self.user = None
        self.window = Tk()
        self.window.geometry("400x550")
        self.window.configure(bg = "#FFFFFF")
        self.window.title('Kriptografi dan Koding')
        self.window.resizable(False, False)

        self.page = Splash.SplashPage(master = self.window, pageManager = self)

    def run(self):
        self.page.startPage()
    
    def Splash(self):
        self.page = Splash.SplashPage(master = self.window, pageManager = self)
        self.page.startPage()

    def Login(self):
        self.page = Login.LoginPage(master = self.window, pageManager = self)
        self.page.startPage()
    
    def Register(self):
        self.page = Register.RegisterPage(master = self.window, pageManager = self)
        self.page.startPage()
    
    def Home(self):
        self.page = Home.HomePage(master = self.window, pageManager = self)
        self.page.startPage()
    
    def CashWithdrawal(self):
        self.page = CashWithdrawal.CashWithdrawalPage(master = self.window, pageManager = self)
        self.page.startPage()