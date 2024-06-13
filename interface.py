import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Função para executar o script.py
def executar_rpa():
    try:
        subprocess.run(["python", "script.py"], check=True)
        messagebox.showinfo("Sucesso", "Script RPA executado com sucesso!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para exibir mensagem e executar coordinates.py após 5 segundos
def obter_coordenadas():
    messagebox.showinfo("Aguardando", "O script de coordenadas será executado em 5 segundos.")
    root.after(5000, executar_coordinates)

# Função para ler as coordenadas do arquivo e exibir na caixa de diálogo
def exibir_coordenadas():
    try:
        with open('coordenadas.txt', 'r') as f:
            coordenadas = f.read()
        messagebox.showinfo("Coordenadas do Mouse", f"As coordenadas do mouse são: {coordenadas}")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de coordenadas não encontrado.")

# Função para executar coordinates.py
def executar_coordinates():
    try:
        subprocess.run(["python", "coordinates.py"], check=True)
        exibir_coordenadas()
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Interface RPA")
root.geometry("300x200")

# Adicionando um botão para obter coordenadas do mouse
btn_coordenadas = tk.Button(root, text="Obter Coordenadas do Mouse", command=obter_coordenadas)
btn_coordenadas.pack(pady=10)

# Adicionando um botão para executar o script RPA
btn_executar = tk.Button(root, text="Executar RPA", command=executar_rpa)
btn_executar.pack(pady=10)

# Função a ser chamada quando a janela for fechada
def on_close():
    try:
        os.remove('coordenadas.txt')
        print("Arquivo coordenadas.txt removido com sucesso.")
    except FileNotFoundError:
        print("Arquivo coordenadas.txt não encontrado.")
    root.destroy()

# Configurar a função on_close para ser chamada ao fechar a janela
root.protocol("WM_DELETE_WINDOW", on_close)

# Executar o loop da interface
root.mainloop()
