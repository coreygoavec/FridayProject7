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