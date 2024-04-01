import tkinter as tk
from tkinter import messagebox
import re

class UserPortal:
    def __init__(self, master):
        self.master = master
        self.master.title("User Portal")
        self.db = {}  # Database to store user credentials

        # Sign-up window
        self.sign_up_window = tk.Toplevel(master)
        self.sign_up_window.title("Sign Up")
        self.sign_up_window.withdraw()

        self.lbl_email = tk.Label(self.sign_up_window, text="Email:")
        self.lbl_email.grid(row=0, column=0)
        self.email_entry = tk.Entry(self.sign_up_window)
        self.email_entry.grid(row=0, column=1)

        self.lbl_password = tk.Label(self.sign_up_window, text="Password:")
        self.lbl_password.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.sign_up_window, show="*")
        self.password_entry.grid(row=1, column=1)

        self.lbl_confirm_password = tk.Label(self.sign_up_window, text="Confirm Password:")
        self.lbl_confirm_password.grid(row=2, column=0)
        self.confirm_password_entry = tk.Entry(self.sign_up_window, show="*")
        self.confirm_password_entry.grid(row=2, column=1)

        self.btn_signup = tk.Button(self.sign_up_window, text="Sign Up", command=self.signup)
        self.btn_signup.grid(row=3, columnspan=2)
        
        # Sign-in window
        self.sign_in_window = tk.Toplevel(master)
        self.sign_in_window.title("Sign In")
        self.sign_in_window.withdraw()

        self.lbl_email_login = tk.Label(self.sign_in_window, text="Email:")
        self.lbl_email_login.grid(row=0, column=0)
        self.email_login_entry = tk.Entry(self.sign_in_window)
        self.email_login_entry.grid(row=0, column=1)

        self.lbl_password_login = tk.Label(self.sign_in_window, text="Password:")
        self.lbl_password_login.grid(row=1, column=0)
        self.password_login_entry = tk.Entry(self.sign_in_window, show="*")
        self.password_login_entry.grid(row=1, column=1)

        self.btn_signin = tk.Button(self.sign_in_window, text="Sign In", command=self.signin)
        self.btn_signin.grid(row=2, columnspan=2)

        self.btn_show_signup = tk.Button(master, text="Show Sign Up", command=self.show_signup)
        self.btn_show_signup.pack()

        self.btn_show_signin = tk.Button(master, text="Show Sign In", command=self.show_signin)
        self.btn_show_signin.pack()

    def validate_email(self, email):
        # Regular expression for email validation
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex, email):
            return True
        else:
            return False