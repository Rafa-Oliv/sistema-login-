import customtkinter as ctk
from PIL import Image
from  BD.banco_dados import BancoDeDados


BD = BancoDeDados()

def modify_footer_text(text, color):
    footer_label.configure(text=text, text_color=color)

def handle_user_action(action_function,failure_message):
    username = username_entry.get()
    password = password_entry.get()

    if username != '' and password != '':
        text, color = action_function(username, password)
        modify_footer_text(text, color)
    
    else:
        modify_footer_text(failure_message, 'red')

def login():
    handle_user_action(BD.verify_user, "Digite usuário e senha")

def sign_up():
    handle_user_action(BD.register_user, "Digite usuário e senha")


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
username_entry = ctk.CTkEntry(main_frame, placeholder_text="Username")
username_entry.pack(pady=10, padx=10, fill="x")

# Entrada de senha
password_entry = ctk.CTkEntry(main_frame, placeholder_text="Password", show="*")
password_entry.pack(pady=10, padx=10, fill="x")

# Criando frame para os botões de login e cadastro
button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
button_frame.pack(pady=10)

# Botão de Login
login_button = ctk.CTkButton(button_frame, text="LOGIN", width=150, command=login)
login_button.grid(row=0, column=0, padx=10)

# Botão de Cadastro
sign_up_button = ctk.CTkButton(button_frame, text="SIGN UP", width=150, command=sign_up)
sign_up_button.grid(row=0, column=1, padx=10)

# Texto de informação para o usuário
footer_label = ctk.CTkLabel(main_frame, text="", font=("Arial", 15))
footer_label.pack(pady=5)

# Executando a janela
window.mainloop()
