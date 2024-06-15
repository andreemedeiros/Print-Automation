import pyautogui, time, os, subprocess

# Name of the folder to save the prints
prints = 'Prints'

# Create the folder if it does not exist
if not os.path.exists(prints):
    os.makedirs(prints)

def print_click(counter_print_i, counter_print_f):
    try:                
        # Leva o mouse até a posicao da image_2.png 
        image2_path = os.path.join("images", "image_2.png")
        image2_pos = pyautogui.locateCenterOnScreen(image2_path)
        if image2_pos:
            pyautogui.moveRel(-100, 0, duration=1)
            pyautogui.moveTo(image2_pos)
            time.sleep(2)
        else:
            raise Exception(f"Imagem {image2_path} não encontrada na tela.")
        
        for counter_print_i in range(counter_print_i, counter_print_f):
          # Print to screen
          pyautogui.screenshot(os.path.join("prints", f"print_{counter_print_i}.png"))
          # Click the mouse na posição on image_2.png sucessivamente
          pyautogui.click(image2_pos)
          time.sleep(2)
          counter_print_i += 1

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

def abrir_prints():
    try:
        pasta_prints = os.path.join(os.getcwd(), "prints")  # Caminho para a pasta "prints"
        subprocess.Popen(["explorer", pasta_prints])  # Abre a pasta "prints"
        time.sleep(2)

        # 19. Abrir o primeiro print
        listar_prints = os.listdir(pasta_prints)
        for arquivo in listar_prints:
            if arquivo.startswith("print_1"):
                subprocess.Popen(["explorer", os.path.join(pasta_prints, arquivo)])
                break
    except OSError:
        print("Erro", "Não foi possível abrir a pasta de prints.")
