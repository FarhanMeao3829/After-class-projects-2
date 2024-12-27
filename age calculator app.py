import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calc_age():
    try:
        birth_dt = int(entry_dt.get())
        birth_mnth = int(entry_mnth.get())
        birth_yr = int(entry_yr.get())
        
        crnt_dt = datetime.now()
        
        age = crnt_dt.year - birth_yr
        
        if crnt_dt.month < birth_mnth or (crnt_dt.month == birth_mnth and crnt_dt.day < birth_dt):
            age -= 1
        
        messagebox.showinfo("Age", f"Your age is: {age} years")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter correct values.")

root = tk.Tk()
root.title("Age Calculator")

lbl_dt = tk.Label(root, text="Enter date of birth :")
lbl_dt.pack()

entry_dt = tk.Entry(root)
entry_dt.pack()

lbl_mnth = tk.Label(root, text="Enter month of birth :")
lbl_mnth.pack()

entry_mnth = tk.Entry(root)
entry_mnth.pack()

lbl_yr = tk.Label(root, text="Enter year of birth :")
lbl_yr.pack()

entry_yr = tk.Entry(root)
entry_yr.pack()

btn_calc = tk.Button(root, text="Calculate age", command=calc_age)
btn_calc.pack()

root.mainloop()