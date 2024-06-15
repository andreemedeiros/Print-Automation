import pyautogui, time, os, subprocess

# Name of the folder to save the prints
prints = 'Prints'

# Create the folder if it does not exist
if not os.path.exists(prints):
    os.makedirs(prints)

def print_system(counter_print_i, counter_print_f):
    try:                
        # 15. Identify the position of image_2.png
        image2_path = os.path.join("images", "image_2.png")
        image2_pos = pyautogui.locateCenterOnScreen(image2_path)
        if image2_pos:
            pyautogui.moveRel(-100, 0, duration=1)
            pyautogui.moveTo(image2_pos)
            time.sleep(2)
        else:
            raise Exception(f"Image {image2_path} not found.")
        
        # 15. Start a 6x Loop to obtain a print of each session
        for counter_print_i in range(counter_print_i, counter_print_f):
          # Print to screen
          pyautogui.screenshot(os.path.join("prints", f"print_{counter_print_i}.png"))
          # Click the mouse na posição on image_2.png sucessivamente
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

        # 19. Abrir o primeiro print
        listar_prints = os.listdir(folder_prints)
        for file in listar_prints:
            if file.startswith("print_1"):
                subprocess.Popen(["explorer", os.path.join(folder_prints, file)])
                break
    except OSError:
        print("Erro", "Unable to open print folder.")
