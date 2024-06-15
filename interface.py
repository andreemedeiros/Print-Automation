import tkinter as tk
from tkinter import messagebox
import time, pyautogui, threading, script

class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation App")

        # Add the phrase at the top of the interface
        info_label = tk.Label(
            self.root, 
            text="Automation application for login into the website:\n'www.amazon.com.br' and print the products\nbest sellers.", 
            justify=tk.LEFT, 
            wraplength=400,
            font=("Arial", 8, "bold"),
            fg="black"
        )
        info_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Variables for storing button coordinates
        self.button_coords = [None] * 3  

        # Labels and entries for browser, email and password
        self.create_label_and_entry("browser:", 1)
        self.browser_entry = self.create_entry(1, default=script.browser)

        self.create_label_and_entry("E-mail:", 2)
        self.email_entry = self.create_entry(2, default=script.email)

        self.create_label_and_entry("password:", 3)
        self.password_entry = self.create_entry(3, show='*', default=script.password)

        # Buttons to obtain coordinates
        self.create_coord_button("Get Coordinates 1 (Maximize Screen)", 0, 4)
        self.create_coord_button("Get Coordinates 2 (Enter URL)", 1, 5)
        self.create_coord_button("Get Coordinates 3 (Login Button)", 2, 6)

        # Button to run automation
        execute_button = tk.Button(self.root, text="Run Automation", command=self.execute_automation, bg='steel blue', fg='white')
        execute_button.grid(row=7, column=0, columnspan=2, pady=10)

    def create_label_and_entry(self, text, row):
        """Create a label and entry in the graphical interface."""
        label = tk.Label(self.root, text=text)
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)

    def create_entry(self, row, show=None, default=""):
        """Create a text entry in the graphical interface."""
        entry = tk.Entry(self.root, show=show)
        entry.insert(0, default)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def create_coord_button(self, text, index, row):
        """Create a button to get coordinates of a specific button."""
        button = tk.Button(self.root, text=text, command=lambda: self.get_button_coords(index))
        button.grid(row=row, column=0, columnspan=2, pady=5)

    def get_coords(self):
        """Waits 5 seconds and returns the current mouse coordinates."""
        time.sleep(5)
        return pyautogui.position()

    def show_message_and_get_coords(self, index):
        """Shows a message, waits 5 seconds and gets the button coordinates."""
        messagebox.showinfo("Information", f"Getting Button coordinates {index+1} on 5 seconds...")
        coords = self.get_coords()
        self.button_coords[index] = coords
        messagebox.showinfo(f"Button Coordinates {index+1}", f"Coordinates: {coords}")

    def get_button_coords(self, index):
        """Starts a thread to obtain the button's Coordinates."""
        threading.Thread(target=self.show_message_and_get_coords, args=(index,)).start()

    def execute_automation(self):
        """Executes the automation process based on the Coordinates and information entered."""
        script.browser = self.browser_entry.get()
        script.email = self.email_entry.get()
        script.password = self.password_entry.get()

        if not all(self.button_coords):
            messagebox.showwarning("Warning", "Some Coordinates have not been defined.\nUsing standard Coordinates.")
            default_coords = [script.maximize_button, script.link_button, script.login_button]
            self.button_coords = [self.button_coords[i] if self.button_coords[i] is not None else default_coords[i] for i in range(3)]
        
        script.maximize_button, script.link_button, script.login_button = self.button_coords

        messagebox.showinfo("Getting started", "Automation started!")

        # Calls the automation function from the script.py file
        try:
            script.main()
            messagebox.showinfo("Completed", "Automation completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error has occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()
