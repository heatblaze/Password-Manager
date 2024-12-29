import tkinter as tk
from tkinter import messagebox
from database import add_password, get_password
from encryption import encrypt_password, decrypt_password

# Functions to add and retrieve password
def add_password_gui():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not service or not username or not password:
        messagebox.showerror("Error", "All fields are required")
        return

    encrypted_password = encrypt_password(password)
    add_password(service, username, encrypted_password)
    messagebox.showinfo("Success", "Password added successfully!")

def retrieve_password_gui():
    service = service_entry.get()
    if not service:
        messagebox.showerror("Error", "Service name is required")
        return

    result = get_password(service)
    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_password(encrypted_password)
        messagebox.showinfo("Password", f"Service: {service}\nUsername: {username}\nPassword: {decrypted_password}")
    else:
        messagebox.showerror("Error", "No password found for this service")

# GUI Design with Enhanced Styling
app = tk.Tk()
app.title("Password Manager")
app.geometry("400x300")
app.config(bg="#f0f0f0")

# Service label and entry
tk.Label(app, text="Service:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="e")
service_entry = tk.Entry(app, font=("Arial", 12), width=30)
service_entry.grid(row=0, column=1, padx=10, pady=10)

# Username label and entry
tk.Label(app, text="Username:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="e")
username_entry = tk.Entry(app, font=("Arial", 12), width=30)
username_entry.grid(row=1, column=1, padx=10, pady=10)

# Password label and entry
tk.Label(app, text="Password:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="e")
password_entry = tk.Entry(app, font=("Arial", 12), width=30, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons with improved design
add_button = tk.Button(app, text="Add Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=add_password_gui)
add_button.grid(row=3, column=0, padx=10, pady=20, sticky="ew")

retrieve_button = tk.Button(app, text="Retrieve Password", font=("Arial", 12), bg="#2196F3", fg="white", command=retrieve_password_gui)
retrieve_button.grid(row=3, column=1, padx=10, pady=20, sticky="ew")

# Adding some padding around the window to make the design more spacious
app.grid_columnconfigure(1, weight=1)

# Start the main loop
app.mainloop()
