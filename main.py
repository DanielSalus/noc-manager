import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tela_conf()
        self.menu_lateral()
    def tela_conf(self):
        self.title("NOC MANAGER")
        self.geometry("1100x650")
        self.resizable(False, False)

    def menu_lateral(self):
        self.menu_lat = ctk.CTkFrame(self, width =200, fg_color="#061F3E")
        self.menu_lat.pack(side="left", fill="y")
        self.titulo_noc = ctk.CTkLabel(self.menu_lat,
                                       text="NOC MANAGER", font=("verdana", 20, "bold"), text_color="white")
        self.titulo_noc.place(relx=0.46, rely=0.05, anchor="center")

        self.subtitulo_noc = ctk.CTkLabel(self.menu_lat,
                                       text="Central de incidentes", font=("verdana", 13, "bold"), text_color="gray" )
        self.subtitulo_noc.place(relx=0.46, rely=0.09, anchor="center")

        self.button_dashBoard = ctk.CTkButton(
            self.menu_lat, text="Dashboard", text_color="white", width=185, height=40, font=("verdana", 12, "bold"),
            fg_color="#1818D3"

        )
        self.button_dashBoard.place(relx=0.49, rely=0.18, anchor="center")

        self.button_incidentes = ctk.CTkButton(
            self.menu_lat,text="Incidentes", text_color="white", width=185, height=40, font=("verdana", 12, "bold"),
            fg_color="#1818D3"

        )
        self.button_incidentes.place(relx=0.49, rely=0.26, anchor="center")

        self.button_novo_inci = ctk.CTkButton(self.menu_lat, text="Novo Incidentes",
        font=("verdana", 12, "bold"), text_color="white", width=185, height=40, fg_color="#1818D3" )

        self.button_novo_inci.place(relx=0.49, rely=0.34, anchor="center")

        self.button_sair = ctk.CTkButton(self.menu_lat, text="Sair",
                                              font=("verdana", 12, "bold"), text_color="white", width=185, height=45,
                                              fg_color="#041C53")

        self.button_sair.place(relx=0.49, rely=0.93, anchor="center",)




if __name__ == "__main__":
    app = App()
    app.mainloop()