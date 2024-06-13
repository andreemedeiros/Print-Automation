import pyautogui

# Obter as coordenadas atuais do mouse
x, y = pyautogui.position()
print(f"Coordenadas do mouse: ({x}, {y})")

# Atualizar a variável button_position no script.py
with open('script.py', 'r') as f:
    lines = f.readlines()

with open('script.py', 'w') as f:
    for line in lines:
        if line.startswith('button_position'):
            f.write(f'button_position = ({x}, {y})\n')
        else:
            f.write(line)

# Escrever as coordenadas em um arquivo para serem lidas pela interface.py
with open('coordenadas.txt', 'w') as f:
    f.write(f'{x}, {y}')
