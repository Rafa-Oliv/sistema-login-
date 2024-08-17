import cx_Freeze
import os
from cx_Freeze import setup, Executable

# Caminho da pasta BD (onde o banco de dados está)
include_files = ["BD","images"]  # Inclui a pasta BD no build

# Adiciona dependências extras, se necessário
build_exe_options = {
    "packages": ["os", "customtkinter", "PIL", "sqlite3", "bcrypt"],
    "include_files": include_files,  # Inclui a pasta BD
}

# Configura o executável
executables = [
    Executable("login.py", base="Win32GUI")
]

# Configura o setup
setup(
    name="Sistema de Login",
    version="1.0",
    description="Sistema de login com CustomTkinter e banco de dados SQLite.",
    options={"build_exe": build_exe_options},
    executables=executables
)
