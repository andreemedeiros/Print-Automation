import pyautogui, time

def browser_system(link_button, url):
    try:
        # 04. Press win + up to maximize the screen
        pyautogui.hotkey('win', 'up')
        time.sleep(2)
        
        # 05. Click the mouse pointer on button 2 for link website
        pyautogui.click(link_button)
        time.sleep(2)
        
        # 06. Write the website URL
        pyautogui.write(url)

        # 07. Press enter
        pyautogui.press('enter')
        time.sleep(2)
        
    except Exception as e:
        print(f"An error has occurred: {str(e)}")

