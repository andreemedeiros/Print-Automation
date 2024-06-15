import pyautogui, time

def navegador_system(maximize_button, link_button, url):
    try:
        # 04. Click the mouse pointer on button 1 for maximize a tela
        pyautogui.click(maximize_button)
        time.sleep(2)
        
        # 05. Click the mouse pointer on button 2 for link website
        pyautogui.click(link_button)
        time.sleep(2)
        
        # 06. Escreve o link do site
        pyautogui.write(url)

        # 07. Aperta enter
        pyautogui.press('enter')
        time.sleep(2)
        
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

