import pyautogui, time, os

def img_posicao_system():
    try:
        # 13. Clica na posicao da image_0.png
        image0_path = os.path.join("images", "image_0.png")
        image0_pos = pyautogui.locateCenterOnScreen(image0_path)
        if image0_pos:
            pyautogui.click(image0_pos)
            time.sleep(3)
        else:
            raise Exception(f"Imagem {image0_path} não encontrada na tela.")
        
        # 14. Clica na posicao da image_1.png
        image1_path = os.path.join("images", "image_1.png")
        image1_pos = pyautogui.locateCenterOnScreen(image1_path)
        if image1_pos:
            pyautogui.click(image1_pos)
            time.sleep(3)
            pyautogui.scroll(-40)
        else:
            raise Exception(f"Imagem {image1_path} não encontrada na tela.")
        

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")