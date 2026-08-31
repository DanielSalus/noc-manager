import customtkinter as ctk
from tkinter import*
from tkinter import ttk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tela_conf()
        self.menu_lateral()
        self.menu_principal()
        self.frame_total()
        self.frame_abertos()
        self.frame_criticos()
        self.frame_resolvidos()
        self.frame_meio()
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

    def menu_principal(self):
        #criar um frame principal
        self.frame_principal = ctk.CTkFrame(self, width =880, height=638, fg_color="#e8e8e8",)
        self.frame_principal.place(relx=0.19, rely=0.01,)
        #criar um frame de qtd com duas labels dentro
        self.label_titulo_dash = ctk.CTkLabel(
            self.frame_principal, text="Dashboard", font=("verdana", 30, "bold"), text_color="Black",

        )
        self.label_titulo_dash.place(relx=0.02, rely=0.04,)
    def frame_total(self):
        pass
        #criar label total
        self.total_frame = ctk.CTkFrame(self.frame_principal, width =200, height=110, fg_color="white",)
        self.total_frame.place(relx=0.02, rely=0.14,)

        self.labe_total = ctk.CTkLabel(self.total_frame, text="Total", font=("verdana", 15, "bold"), text_color="Black")
        self.labe_total.place(relx=0.35, rely=0.17, )

        self.label_tot = ctk.CTkLabel(self.total_frame, text="0", font=("verdana", 30, "bold"), text_color="Blue")
        self.label_tot.place(relx=0.40, rely=0.45, )

    def frame_abertos(self):
        pass
        # criar label total
        self.abertos_frame = ctk.CTkFrame(self.frame_principal, width=200, height=110, fg_color="white", )
        self.abertos_frame.place(relx=0.26, rely=0.14, )

        self.labe_abertos = ctk.CTkLabel(self.abertos_frame, text="Abertos", font=("verdana", 15, "bold"), text_color="Black")
        self.labe_abertos.place(relx=0.35, rely=0.17, )

        self.label_tot_abertos = ctk.CTkLabel(self.abertos_frame, text="0", font=("verdana", 30, "bold"), text_color="Blue")
        self.label_tot_abertos.place(relx=0.46, rely=0.45, )

    def frame_criticos(self):
        pass
        # criar label total
        self.criticos_frame = ctk.CTkFrame(self.frame_principal, width=200, height=110, fg_color="white", )
        self.criticos_frame.place(relx=0.50, rely=0.14, )

        self.labe_criticos = ctk.CTkLabel(self.criticos_frame, text="Critícos", font=("verdana", 15, "bold"), text_color="Black")
        self.labe_criticos.place(relx=0.35, rely=0.17,)

        self.label_tot_criticos = ctk.CTkLabel(self.criticos_frame, text="0", font=("verdana", 30, "bold"),
                                              text_color="Red")
        self.label_tot_criticos.place(relx=0.46, rely=0.45, )

    def frame_resolvidos(self):
        pass
        # criar label total
        self.resolvidos_frame = ctk.CTkFrame(self.frame_principal, width=200, height=110, fg_color="white", )
        self.resolvidos_frame.place(relx=0.74, rely=0.14, )

        self.labe_resolvidos = ctk.CTkLabel(self.resolvidos_frame, text="Resolvidos", font=("verdana", 15, "bold"), text_color="Black")
        self.labe_resolvidos.place(relx=0.30, rely=0.17,)

        self.label_tot_resolvidos = ctk.CTkLabel(self.resolvidos_frame, text="0", font=("verdana", 30, "bold"),
                                              text_color="green")
        self.label_tot_resolvidos.place(relx=0.46, rely=0.45, )

    def frame_meio(self):
        self.frame_lista = ctk.CTkFrame(self.frame_principal, width=830, height=380, fg_color="white", )
        self.frame_lista.place(relx=0.02, rely=0.37, )

        self.label_incidentes = ctk.CTkLabel(self.frame_lista, text="Incidentes recentes", font=("verdana", 20, "bold"), text_color="Black")
        self.label_incidentes.place(relx=0.02, rely=0.06, )

        self.lista_incidentes = ttk.Treeview(self.frame_lista, columns=('colum1', 'colum2', 'colum3', 'colum4' ),)

        self.lista_incidentes.heading("#0", text="Protocolo",)
        self.lista_incidentes.heading("#1", text="Título",)
        self.lista_incidentes.heading("#2", text="Sistema",)
        self.lista_incidentes.heading("#3", text="Prioridade",)
        self.lista_incidentes.heading("#4", text="Status",)

        self.lista_incidentes.column("#0", width=1)
        self.lista_incidentes.column("#1", width=100)
        self.lista_incidentes.column("#2", width=100)
        self.lista_incidentes.column("#3", width=125)
        self.lista_incidentes.column("#4", width=125)

        self.lista_incidentes.place(relx=0.02, rely=0.17, relheight=0.78, relwidth=0.96 )
        self.style = ttk.Style()
        self.style.theme_use("clam")




if __name__ == "__main__":
    app = App()
    app.mainloop()