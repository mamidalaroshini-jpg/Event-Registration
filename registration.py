import tkinter as tk
from tkinter import messagebox

def register():
    if name.get() and email.get():
        messagebox.showinfo("Success", "Registration Successful!")
    else:
        messagebox.showerror("Error", "Fill all fields")

root = tk.Tk()
root.title("College Event Registration Form")
root.geometry("350x400")

tk.Label(root, text="Event Registration",
         font=("Arial", 18)).pack(pady=15)

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack(pady=5)

tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack(pady=5)

tk.Label(root, text="Phone").pack()
phone = tk.Entry(root)
phone.pack(pady=5)

tk.Label(root, text="Event").pack()

event = tk.StringVar(value="Tech Workshop")

tk.OptionMenu(
    root,
    event,
    "Tech Workshop",
    "Sports Event",
    "Music festival"
    "Cultural Event"    
).pack()

tk.Button(
    root,
    text="Register",
    command=register,
    bg="green",
    fg="white"
).pack(pady=20)

root.mainloop()

