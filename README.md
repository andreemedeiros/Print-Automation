# Print-Automation

## Índice
- [Descrição](#Descrição)
- [Recursos](#Recursos)
- [Execução](#Execução)
- [Autor](#Autor)
- [Licença](#Licença)

## Descrição
Projeto de automação da GUI (Interface Gráfica do Usuário) utilizando python + pyautogui.

O projeto consiste em automatizar o seguinte processo: 

1. Clica com o ponteiro do mouse sob uma coordenada da tela.
2. Esperar 1s
3. printar a tela
4. Esperar 1s
5. Repetir o processo

O processo é repetido sucessivamente durante um período de tempo estabelecido em "scripy.py".

Os prints gerados serão armazenados na pasta "prints".

As coordenadas desejadas podem ser obtidas executando o arquivo "coordenadas.py".

## Recursos:

```
Python 3.12.4

pyautogui
```
## Execução

Opcional: Para obter as coordenadas, desloque o ponteiro do mouse até o local desejado e execute o arquivo "coordenadas.py".

```
python3 coordenadas.py
```
opcional: Modifique as coordenadas na linha 9 no arquivo "scripy.py".

```
posicao_botao = (1312, 733)
```

opcional: Modifique o tempo de execução na linha 4 no arquivo "scripy.py".

```
tempo_total = 10
```

Execute o arquivo "scripy.py".

```
python3 script.py
```

## Autor

* **André Medeiros** - [André Medeiros](https://github.com/andreemedeiros)

Contribuição no projeto [Print Automation](https://github.com/andreemedeiros/Print-Automation/graphs/contributors).

## Licença
Este projeto está licenciado sob a MIT License - veja a [LICENSE.md](LICENSE.md) para mais detalhes.
