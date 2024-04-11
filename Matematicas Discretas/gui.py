import tkinter as tk
from tkinter import messagebox

def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def not_gate(a):
    return not a

def calculate():
    gate = gate_var.get()
    a = bool(a_var.get())
    b = bool(b_var.get())

    if gate == "AND":
        result = and_gate(a, b)
    elif gate == "OR":
        result = or_gate(a, b)
    elif gate == "NOT":
        result = not_gate(a)
    else:
        result = "Invalid gate"

    messagebox.showinfo("Result", str(result))

root = tk.Tk()

gate_var = tk.StringVar()
gate_var.set("AND")

a_var = tk.IntVar()
b_var = tk.IntVar()

tk.Label(root, text="Gate").grid(row=0, column=0)
tk.OptionMenu(root, gate_var, "AND", "OR", "NOT").grid(row=0, column=1)

tk.Label(root, text="A").grid(row=1, column=0)
tk.Checkbutton(root, variable=a_var).grid(row=1, column=1)

tk.Label(root, text="B").grid(row=2, column=0)
tk.Checkbutton(root, variable=b_var).grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)

root.mainloop()