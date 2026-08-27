import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tela_conf()
    def tela_conf(self):
        self.title("NOC MANAGER")
        self.geometry("1100x650")
        self.resizable(False, False)
if __name__ == "__main__":
    app = App()
    app.mainloop()