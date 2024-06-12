import pyautogui, time, os

# Tempo total de execução em segundos
tempo_total = 10
# Intervalo entre as ações em segundos
intervalo = 1

# Posição do botão a ser clicado (x, y)
posicao_botao = (1312, 733)  # substitua pelos valores corretos

# Nome da pasta para salvar os prints
prints = 'Prints'

# Tempo inicial
inicio = time.time()

# Contador de prints
contador = 1

while (time.time() - inicio) < tempo_total:
    # Clique no botão
    pyautogui.click(posicao_botao)
    
    # Espera 1 segundo
    time.sleep(1)
    
    # Printa a tela
    screenshot = pyautogui.screenshot()
    screenshot.save(os.path.join(prints, f'print_{contador}.png'))
    
    # Incrementa o contador
    contador += 1

    # Espera 1 segundo
    time.sleep(1)

print("Automação concluída!")
