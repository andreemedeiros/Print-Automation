import pyautogui, time, os

def position_system():
    try:
        # 13. Click on the position of image_0.png
        image0_path = os.path.join("images", "image_0.png")
        image0_pos = pyautogui.locateCenterOnScreen(image0_path)
        if image0_pos:
            pyautogui.click(image0_pos)
            time.sleep(3)
        else:
            raise Exception(f"Image {image0_path} not found.")
        
        # 14. Click on the position of image_1.png
        image1_path = os.path.join("images", "image_1.png")
        image1_pos = pyautogui.locateCenterOnScreen(image1_path)
        if image1_pos:
            pyautogui.click(image1_pos)
            time.sleep(3)
            pyautogui.scroll(-40)
        else:
            raise Exception(f"Image {image1_path} not found.")
        
    except Exception as e:
        print(f"An error has occurred: {str(e)}")