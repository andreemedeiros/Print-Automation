import pyautogui, time, os

# Log on website
def login_system(login_button, email, password):
    try:
        # 08. Click the mouse pointer on button 3 for login
        pyautogui.click(login_button)
        time.sleep(2)

        # 09. Write e-mail
        pyautogui.write(email)

        # 10. Press enter
        pyautogui.press('enter')
        time.sleep(2)
        
        # 11. Write password
        pyautogui.write(password)

        # 12. Press enter
        pyautogui.press('enter')
        time.sleep(2)

    except Exception as e:
        print(f"An error has occurred: {str(e)}")

# logoff on website
def logout_system(login_button):
    try:
        # 16. Return to top of page
        pyautogui.scroll(3350)

        # 17. Position the mouse over the login area
        pyautogui.moveTo(login_button)
        time.sleep(2)
        
        # 18. Logout on website
        if pyautogui.locateCenterOnScreen(os.path.join("images", "image_3.png")):
            pyautogui.moveTo(pyautogui.locateCenterOnScreen(os.path.join("images", "image_3.png")))
            pyautogui.click()
        else:
            print("Image not found on screen.")      
              
    except Exception as e:
        print(f"An error has occurred: {str(e)}")