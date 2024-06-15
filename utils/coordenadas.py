import pyautogui, time

# Obter as coordenadas
time.sleep(5)
x, y = pyautogui.position()
print(f"Coordenadas do mouse: ({x}, {y})")
