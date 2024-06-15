import pyautogui, time, os

# Faz login no site
def login_system(login_button, email, password):
    try:
        # 08. Click the mouse pointer on button 3 for login
        pyautogui.click(login_button)
        time.sleep(2)

        # 09. Write e-mail
        pyautogui.write(email)

        # 10. Aperta enter
        pyautogui.press('enter')
        time.sleep(2)
        
        # 11. Write password
        pyautogui.write(password)

        # 12. Aperta enter
        pyautogui.press('enter')
        time.sleep(2)

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

# Faz logout no site
def logout_system(login_button):
    try:
        # 16. Volta para o início da página
        pyautogui.scroll(3350)

        # 17. Posiciona o mouse sobre a área de login
        pyautogui.moveTo(login_button)
        time.sleep(2)
        
        # 18. Faz logout no site
        if pyautogui.locateCenterOnScreen(os.path.join("images", "image_3.png")):
            pyautogui.moveTo(pyautogui.locateCenterOnScreen(os.path.join("images", "image_3.png")))
            pyautogui.click()
        else:
            print("Imagem não encontrada na tela.")      
              
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")