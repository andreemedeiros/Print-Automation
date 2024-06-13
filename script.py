import pyautogui, time, os

# Total execution time in seconds
total_time = 10
# Interval between actions in seconds
interval = 1

# Função para modificar o tempo total
def modificar_total_time(novo_tempo):
    global total_time
    total_time = novo_tempo

# Position of the button to be clicked (x, y)
button_position = (809, 456)

# Name of the folder to save the prints
prints = 'Prints'

# Create the folder if it does not exist
if not os.path.exists(prints):
    os.makedirs(prints)

# Start time
initial = time.time()

# Print counter
counter = 1

while (time.time() - initial) < total_time:
    # Click on the button
    pyautogui.click(button_position)
    
    # Whait 1 second
    time.sleep(1)
    
    # Print to screen
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(prints, f'print_{counter}.png'))
    
    # Increment the counter
    counter += 1

    # Whait 1 second
    time.sleep(1)

print("Automation complete!")
