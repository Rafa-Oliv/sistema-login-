import customtkinter as ctk
from PIL import Image
from BD.data_base import DataBase


class App:

    def __init__(self, DB):
        self.DB = DB
        self.footer_label = None  # Definindo self.footer_label para acesso em outros métodos
    
    def modify_footer_text(self, text, color):
        self.footer_label.configure(text=text, text_color=color)  # Corrigido para self.footer_label

    def handle_user_action(self, action_function, failure_message):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        if self.username != '' and self.password != '':
            self.text, self.color = action_function(self.username, self.password)  # Removido self, o método não é da classe
            self.modify_footer_text(self.text, self.color)
        else:
            self.modify_footer_text(failure_message, 'red')

    def login(self):
        self.handle_user_action(self.DB.verify_user, "Digite usuário e senha")

    def sign_up(self):
        self.handle_user_action(self.DB.register_user, "Digite usuário e senha")

    def screen_login(self):
        # Inicializando a janela principal
        window = ctk.CTk()
        window.title("Login")
        width = 400
        height = 400
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
        window.resizable(False, False)

        # Definindo o tema e a cor
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Criando o frame principal
        main_frame = ctk.CTkFrame(window, width=width, height=height)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Rótulo de Login
        login_label = ctk.CTkLabel(main_frame, text="LOGIN", font=("Arial", 24))
        login_label.pack(pady=10)

        # Carregar e ajustar a imagem
        image = ctk.CTkImage(Image.open("./images/usr2.png"), size=(100, 100))
        # Criar um label para exibir a imagem (centralizada dentro do frame)
        image_label = ctk.CTkLabel(main_frame, image=image, text="")
        image_label.pack(pady=10)  # Posiciona a imagem logo abaixo do título

        # Entrada de usuário
        self.username_entry = ctk.CTkEntry(main_frame, placeholder_text="Username")
        self.username_entry.pack(pady=10, padx=10, fill="x")

        # Entrada de senha
        self.password_entry = ctk.CTkEntry(main_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10, padx=10, fill="x")

        # Criando frame para os botões de login e cadastro
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(pady=10)

        # Botão de Login
        login_button = ctk.CTkButton(button_frame, text="ENTRAR", width=150, command=self.login)
        login_button.grid(row=0, column=0, padx=10)

        # Botão de Cadastro
        sign_up_button = ctk.CTkButton(button_frame, text="CADASTRAR", width=150, command=self.sign_up)
        sign_up_button.grid(row=0, column=1, padx=10)

        # Texto de informação para o usuário
        self.footer_label = ctk.CTkLabel(main_frame, text="", font=("Arial", 15))  # Adicionado self
        self.footer_label.pack(pady=5)

        # Executando a janela
        window.mainloop()


DB = DataBase()
app = App(DB)
app.screen_login()
