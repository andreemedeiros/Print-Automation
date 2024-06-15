import pyautogui
from utils.print import print_system
from utils.print import openprint_system
from utils.login import login_system
from utils.login import logout_system
from utils.browser import browser_system
from utils.initialize import initialize_system
from utils.position import position_system

# Global variables
browser = 'chrome'
maximize_button = (1306, 29)
link_button = (914, 60)
url = "https://www.amazon.com.br"
login_button = (1072, 114) 
email = "example@example.com"
password = "your_password_here"

# Automation principal script
def main():
    try:

        count_i = 0
        count_f = 5

        # 01 a 03
        initialize_system(browser)
        # 04 a 07
        browser_system(maximize_button, link_button, url)
        # 08 a 12
        login_system(login_button, email, password)
        # 13 a 14
        position_system()
        # 15
        while count_i < 30:
            print_system(count_i, count_f)
            pyautogui.scroll(-550)
            count_i += 5
            count_f += 5
        # 16 a 18
        logout_system(login_button)
        # 19
        openprint_system()

        print("Automation completed successfully!")

    except Exception as e:
        print(f"An error has occurred: {str(e)}")

if __name__ == "__main__":
    main()
