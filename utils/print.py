import pyautogui, time, os, subprocess

# Nome da pasta para salvar as capturas
prints = 'Prints'

# Cria a pasta se ela não existir
if not os.path.exists(prints):
    os.makedirs(prints)

def print_system(counter_print_i, counter_print_f):
    try:
        # 14. Identifica a posição da image_2.png
        image2_path = os.path.join("images", "image_2.png")
        image2_pos = pyautogui.locateCenterOnScreen(image2_path)
        if image2_pos:
            pyautogui.moveRel(-100, 0, duration=1)
            pyautogui.moveTo(image2_pos)
            time.sleep(2)
        else:
            raise Exception(f"Image {image2_path} not found.")
        
        # 14. Inicia um loop 6x para obter uma captura de cada sessão
        while counter_print_i <= counter_print_f:
            # Captura de tela de uma região específica
            screenshot = pyautogui.screenshot(region=(220, 165, 1100, 600))
            # Salva a captura de tela no diretório especificado
            screenshot.save(os.path.join(prints, f"print_{counter_print_i}.png"))
            
            # Clica na posição da image_2.png sucessivamente
            pyautogui.click(image2_pos)
            time.sleep(2)
            counter_print_i += 1

    except Exception as e:
        print(f"An error has occurred: {str(e)}")

def openprint_system():
    try:
        folder_prints = os.path.join(os.getcwd(), "prints")
        subprocess.Popen(["explorer", folder_prints])
        time.sleep(2)

        # 18. Abrir o primeiro print
        listar_prints = os.listdir(folder_prints)
        for file in listar_prints:
            if file.startswith("print_1"):
                subprocess.Popen(["explorer", os.path.join(folder_prints, file)])
                break
    except OSError:
        print("Erro", "Unable to open print folder.")

