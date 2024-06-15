import tkinter as tk
from tkinter import messagebox
import time, pyautogui, threading, script

class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation App")

        # Adiciona a frase na parte superior da interface
        info_label = tk.Label(
            self.root, 
            text="Aplicativo de automação para fazer login no site:\n'www.amazon.com.br' e printar os produtos\nmais vendidos.", 
            justify=tk.LEFT, 
            wraplength=400,
            font=("Arial", 8, "bold"),
            fg="black"
        )
        info_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Variáveis para armazenar as coordenadas dos botões
        self.button_coords = [None] * 3  # Coordenadas para maximizar tela, digitar URL e login

        # Labels e entradas para navegador, email e senha
        self.create_label_and_entry("Navegador:", 1)
        self.browser_entry = self.create_entry(1, default=script.navegador)

        self.create_label_and_entry("E-mail:", 2)
        self.email_entry = self.create_entry(2, default=script.email)

        self.create_label_and_entry("Senha:", 3)
        self.password_entry = self.create_entry(3, show='*', default=script.password)

        # Botões para obter coordenadas
        self.create_coord_button("Obter Coordenadas 1 (Maximizar Tela)", 0, 4)
        self.create_coord_button("Obter Coordenadas 2 (Digitar URL)", 1, 5)
        self.create_coord_button("Obter Coordenadas 3 (Botão Login)", 2, 6)

        # Botão para executar a automação
        execute_button = tk.Button(self.root, text="Executar Automação", command=self.execute_automation, bg='steel blue', fg='white')
        execute_button.grid(row=7, column=0, columnspan=2, pady=10)

    def create_label_and_entry(self, text, row):
        """Cria um rótulo e uma entrada na interface gráfica."""
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)

    def create_entry(self, row, show=None, default=""):
        """Cria uma entrada de texto na interface gráfica."""
        entry = tk.Entry(self.root, show=show)
        entry.insert(0, default)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def create_coord_button(self, text, index, row):
        """Cria um botão para obter coordenadas de um botão específico."""
        button = tk.Button(self.root, text=text, command=lambda: self.get_button_coords(index))
        button.grid(row=row, column=0, columnspan=2, pady=5)

    def get_coords(self):
        """Espera 5 segundos e retorna as coordenadas atuais do mouse."""
        time.sleep(5)
        return pyautogui.position()

    def show_message_and_get_coords(self, index):
        """Mostra uma mensagem, espera 5 segundos e obtém as coordenadas do botão."""
        messagebox.showinfo("Informação", f"Obtendo coordenadas do Botão {index+1} em 5 segundos...")
        coords = self.get_coords()
        self.button_coords[index] = coords
        messagebox.showinfo(f"Coordenadas do Botão {index+1}", f"Coordenadas: {coords}")

    def get_button_coords(self, index):
        """Inicia uma thread para obter as coordenadas do botão."""
        threading.Thread(target=self.show_message_and_get_coords, args=(index,)).start()

    def execute_automation(self):
        """Executa o processo de automação com base nas coordenadas e informações inseridas."""
        script.navegador = self.browser_entry.get()
        script.email = self.email_entry.get()
        script.password = self.password_entry.get()

        if not all(self.button_coords):
            messagebox.showwarning("Aviso", "Algumas coordenadas não foram definidas. Utilizando coordenadas padrão.")
            default_coords = [script.maximize_button, script.link_button, script.login_button]
            self.button_coords = [self.button_coords[i] if self.button_coords[i] is not None else default_coords[i] for i in range(3)]
        
        script.maximize_button, script.link_button, script.login_button = self.button_coords

        messagebox.showinfo("Iniciando", "Automação iniciada!")

        # Chama a função de automação do arquivo script.py
        try:
            script.main()
            messagebox.showinfo("Concluído", "Processo concluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()
