import pyautogui, time

def browser_system(url):
    try:
        # 04. Press win + up to maximize the screen
        pyautogui.hotkey('win', 'up')
        time.sleep(2)
        
        # 05. Write the website URL
        pyautogui.write(url)

        # 06. Press enter
        pyautogui.press('enter')
        time.sleep(2)
        
    except Exception as e:
        print(f"An error has occurred: {str(e)}")

