import tkinter as tk

from generate_password import generate_password

root = tk.Tk()
root.title("Passord Generator")
root.geometry("400x200")

password_label = tk.Label(root, text="", font=("Arial", 14))
password_label.pack(pady=20)

def generate_real_password():
    pwd = generate_password(min_length=10, numbers=True, special_characters=True)
    password_label.config(text=pwd)

generate_button = tk.Button(root, text="Générer le mot de passe", command=generate_real_password)
generate_button.pack()



root.mainloop()

