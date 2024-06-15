import pyautogui, time

def initialize_system(browser):
    try:
        # 01. Press the Windows key
        pyautogui.press('win')
        time.sleep(2)
        
        # 02. Write chrome
        pyautogui.write(browser)
        
        # 03. Press enter
        pyautogui.press('enter')
        time.sleep(2)

    except Exception as e:
        print(f"An error has occurred: {str(e)}")

