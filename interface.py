import tkinter as tk
from tkinter import messagebox
import subprocess, os, time

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

# Função para executar o script.py
def executar_rpa():
    try:
        subprocess.run(["python", "script.py"], check=True)
        messagebox.showinfo("Sucesso", "Script executado com sucesso!")
        abrir_prints()  # Chama a função para abrir os prints
        root.iconify()  # Minimiza a janela principal
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para abrir a pasta onde os prints foram gerados e abrir o primeiro print
def abrir_prints():
    try:
        pasta_prints = os.path.join(os.getcwd(), "prints")  # Caminho absoluto para a pasta "prints"
        subprocess.Popen(["explorer", pasta_prints])  # Abre a pasta "prints" no Explorador de Arquivos

        # Aguardar 2 segundos antes de abrir o primeiro print
        time.sleep(2)

        # Abrir o primeiro print (por exemplo, print_1.png)
        listar_prints = os.listdir(pasta_prints)
        for arquivo in listar_prints:
            if arquivo.startswith("print_1"):
                subprocess.Popen(["explorer", os.path.join(pasta_prints, arquivo)])
                break  # Para no primeiro arquivo encontrado
    except OSError:
        messagebox.showerror("Erro", "Não foi possível abrir a pasta de prints.")

# Função para alterar o total_time em script.py
def btn_modificar_tempo_click():
    novo_tempo = entry_tempo.get()

    try:
        with open('script.py', 'r') as file:
            lines = file.readlines()

        with open('script.py', 'w') as file:
            for line in lines:
                if line.startswith('total_time ='):
                    file.write(f'total_time = {novo_tempo}\n')
                else:
                    file.write(line)

        messagebox.showinfo("Sucesso", f"Tempo modificado para {novo_tempo}.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao modificar o tempo: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Interface RPA")
root.geometry("240x200")

# Botão para obter coordenadas do mouse
btn_coordenadas = tk.Button(root, text="Obter Coordenadas do ponteiro", command=obter_coordenadas)
btn_coordenadas.pack(pady=10)

# Botão para modificar o tempo
btn_modificar_tempo = tk.Button(root, text="Modificar Tempo de execução", command=btn_modificar_tempo_click)
btn_modificar_tempo.pack(pady=10)

# Campo de entrada para o novo tempo
tk.Label(root, text="Novo Tempo:").pack()
entry_tempo = tk.Entry(root)
entry_tempo.pack()

# Botão para executar o script
btn_executar = tk.Button(root, text="Executar Automação", command=executar_rpa)
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
