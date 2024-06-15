import pyautogui
from utils.print import print_click
from utils.print import abrir_prints
from utils.login import login_system
from utils.login import logout_system
from utils.navegador import navegador_system
from utils.inicializar import inicializar_system
from utils.img_posicao import img_posicao_system

navegador = 'chrome'

maximize_button = (1306, 29)
link_button = (708, 61)
url = "https://www.amazon.com.br"

login_button = (1051, 146) 
email = "example@example.com"
password = "sua_senha_aqui"

def main():
    try:

        count_i = 0
        count_f = 5

        # 01 a 03
        inicializar_system(navegador)
        # 04 a 07
        navegador_system(maximize_button, link_button, url)
        # 08 a 12
        login_system(login_button, email, password)
        # 13 a 14
        img_posicao_system()
        # 15
        while count_i < 30:
            print_click(count_i, count_f)
            pyautogui.scroll(-550)
            count_i += 5
            count_f += 5
        # 16 a 18
        logout_system(login_button)
        # 19
        abrir_prints()

        print("Processo concluído com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()
