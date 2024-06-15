# Desktop Application Project for Automation

## Index
- [Description](#Description)
- [Resources](#Resources)
- [Installation](#Installation)
- [Execution](#Execution)
- [Author](#Author)
- [References](#References)
- [License](#License)

## Description
Desktop Application Project + RPA (Robotic Process Automation) to automate login to the Amazon website and print the best-selling products using Python + pyautogui + tkinter.

![](images/App.png)

The project consists of automating the following process:
```
01. Press the Windows key;
02. Write chrome;
03. Press enter;
04. Click the mouse pointer on button 1 to maximize the screen;
05. Click the mouse pointer on button 2 for link website;
06. Write the website URL;
07. Press enter;
08. Click the mouse pointer on button 3 for login;
09. Write e-mail;
10. Press enter;
11. Write password;
12. Press enter;
13. Click on the position of img_0.png;
14. Click on the position of img_1.png;
15. Identify the position of image 2.png and start a 6x Loop to obtain a print of each session;
    11.1. Screenshot;
    11.2. Click button.
16. Return to top of page;
17. Position the mouse over the login area;
18. Log out of the website;
19. Open screenshots.
```

OBS: The generated prints will be stored in the "prints" folder.

OBS: The desired coordinates can be obtained by click on the coordinates buttons.

## Resources
```
Python 3.12.4

Python libraries: 
  - pyautogui
  - tkinter
  - time
  - threading
  - os
  - subprocess
```

## Installation

to install Python 3.12.4 access: 
```
python.org
```

to install pyautogui run: 
```
python3 -m pip install pyautogui
```

To install others libraries run: 
```
python3 pip install tkinter, time, threading, os, subprocess
```

## Execution

Run the "interface.py" file:
```
python3 interface.py
```

Enter the browser you want to use; 

Optional: Enter a valid email and password to log in to the Amazon website;

Click on the coordinate buttons and position the mouse pointer over the maximize, url and login coordinate locations;

Click on the run button and wait for the automation.

## Author

[André Medeiros](https://github.com/andreemedeiros)

Contribution to the project [Print Automation](https://github.com/andreemedeiros/Print-Automation/graphs/contributors)

## References

[Official pyautogui documentation](https://pyautogui.readthedocs.io/en/latest/#)


## License
This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for more details.
