# Project Print Automation

## Índice
- [Description](#Description)
- [Resources](#Resources)
- [Execution](#Execution)
- [Author](#Author)
- [License](#License)

## Description
GUI (Graphical User Interface) automation project using python + pyautogui.

The project consists of automating the following process:
```
1. Click the mouse pointer on a coordinate on the screen;
2. Whait 1s;
3. Print to screen;
4. Whait 1s;
5. Repeat the process.
```

OBS: The process is repeated successively over a period of time established in "scripy.py".

OBS: The generated prints will be stored in the "prints" folder.

OBS: The desired coordinates can be obtained by running the "coordinates.py" file.

## Resources
```
Python 3.12.4

pyautogui
```

## Execution

Optional: To obtain the coordinates, move the mouse pointer to the desired location and run the "coordinates.py" file.
```
python3 coordinates.py
```
optional: Modify the coordinates in line 9 in the "scripy.py" file.
```
button_position = (1312, 733)
```

optional: Modify the runtime on line 4 in the "scripy.py" file.
```
total_time = 10
```

Run the "scripy.py" file.
```
python3 script.py
```

## Author

* **André Medeiros** - [André Medeiros](https://github.com/andreemedeiros)

Contribution to the project [Print Automation](https://github.com/andreemedeiros/Print-Automation/graphs/contributors).

## License
This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for more details.
