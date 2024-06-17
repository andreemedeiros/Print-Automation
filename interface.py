import tkinter as tk
from tkinter import messagebox
import script

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

        # Button to open login window
        login_button = tk.Button(self.root, text="Login", command=self.open_login_window, bg='white', fg='black')
        login_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Button to run automation
        execute_button = tk.Button(self.root, text="Run Automation", command=self.execute_automation, bg='steel blue', fg='white')
        execute_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Initialize email and password variables
        self.email_entry = None
        self.password_entry = None

    def open_login_window(self):
        """Open the login window for email and password input."""
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")

        # Default email and password
        default_email = "example@example.com"
        default_password = "your_password_here"

        # Labels and entries for email and password
        tk.Label(login_window, text="E-mail:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(login_window)
        self.email_entry.insert(0, default_email)  # Insert default email
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.password_entry = tk.Entry(login_window, show='*')
        self.password_entry.insert(0, default_password)  # Insert default password
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Button to save login credentials
        save_button = tk.Button(login_window, text="Save", command=lambda: self.save_credentials(login_window), bg='steel blue', fg='white')
        save_button.grid(row=2, column=0, columnspan=2, pady=10)

    def save_credentials(self, login_window):
        """Save the login credentials to script.py and close the login window."""
        script.email = self.email_entry.get()
        script.password = self.password_entry.get()

        # Read current content of script.py
        with open('script.py', 'r') as f:
            lines = f.readlines()

        # Update email and password lines
        updated_lines = []
        for line in lines:
            if line.startswith('email = '):
                updated_lines.append(f"email = '{script.email}'\n")
            elif line.startswith('password = '):
                updated_lines.append(f"password = '{script.password}'\n")
            else:
                updated_lines.append(line)

        # Write updated lines back to script.py
        with open('script.py', 'w') as f:
            f.writelines(updated_lines)

        login_window.destroy()

    def execute_automation(self):
        """Executes the automation process."""
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
