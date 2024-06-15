import pyautogui, time

def inicializar_system(navegador):
    try:
        # 01. Aperta tecla windows
        pyautogui.press('win')
        time.sleep(2)
        
        # 02. Escreve chrome
        pyautogui.write(navegador)
        
        # 03. Aperta Enter
        pyautogui.press('enter')
        time.sleep(2)

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

