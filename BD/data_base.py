import sqlite3
import bcrypt
import os


class DataBase:
    # Função para criar o banco de dados e a tabela de usuários únicos,
    def __init__(self):
        # Diretório atual do módulo
        module_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Caminho do banco de dados dentro da pasta BD
        self.db_path = os.path.join(module_dir,'users.db')

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')
        conn.commit()
        conn.close()

    # Função para criptografar a senha
    def hash_password(self,password):
        # Gera o salt e criptografa a senha
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    # Função para cadastrar usuário
    #retornando um texto indicando a situação do cadastro, cor do texto
    def register_user(self,username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        hashed_password = self.hash_password(password)
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
            return f"Usuário {username} cadastrado com sucesso!","green"
        except sqlite3.IntegrityError:
            return f"Usuário {username} já existe!","red"
        conn.close()

    # Função para verificar se o usuário existe e se a senha está correta
    #retornando um texto indicando a situação da requisição, cor do texto
    def verify_user(self,username, password):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT password,username FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            hashed_password = result[0]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return f"Bem vindo {result[1]}","green"
                
            else:
                return "Senha incorreta","red"
        else:
            return "Usuário não registrado","red"
