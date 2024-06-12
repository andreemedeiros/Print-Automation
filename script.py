import pyautogui
import time

# Tempo total de execução em segundos
tempo_total = 500
# Intervalo entre as ações em segundos
intervalo = 1

# Posição do botão a ser clicado (x, y)
posicao_botao = (100, 200)  # substitua pelos valores corretos

# Tempo inicial
inicio = time.time()

while (time.time() - inicio) < tempo_total:
    # Clique no botão
    pyautogui.click(posicao_botao)
    
    # Espera 1 segundo
    time.sleep(1)
    
    # Printa a tela
    screenshot = pyautogui.screenshot()
    screenshot.save(f'screenshot_{int(time.time())}.png')
    
    # Espera 1 segundo
    time.sleep(1)

print("Automação concluída!")
