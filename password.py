import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(entry_length.get())  
        if length < 1:
            messagebox.showerror("Error", "Password length must be greater than 0")
            return
        
        
        characters = string.ascii_letters + string.digits + string.punctuation
        
        
        password = ''.join(random.choice(characters) for i in range(length))
        
        
        label_password.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the password length")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")


label_instruction = tk.Label(root, text="Enter the desired length of the password:")
label_instruction.pack(pady=10)


entry_length = tk.Entry(root, width=20)
entry_length.pack(pady=5)


button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)


label_password = tk.Label(root, text="")
label_password.pack(pady=10)


root.mainloop()
