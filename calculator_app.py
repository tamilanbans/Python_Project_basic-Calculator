import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid input.")

def append_to_entry(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current + value)

def clear_entry():
    entry_display.delete(0, tk.END)

def set_operation(op):
    current = entry_display.get()
    if current and current[-1] not in "+-*/":
        entry_display.insert(tk.END, f" {op} ")
    highlight_selected_operator(op)

def highlight_selected_operator(selected_op):
    for op, button in operator_buttons.items():
        if op == selected_op:
            button.config(bg="#FFA07A")  # Light salmon color
        else:
            button.config(bg="SystemButtonFace")

# Create the main application window
app = tk.Tk()
app.title("Basic Calculator")

# Display Entry
entry_display = tk.Entry(app, width=30, font=("Arial", 16), justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons_frame = tk.Frame(app)
buttons_frame.grid(row=1, column=0, columnspan=4, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('.', 4, 0), ('C', 4, 2)
]

for (text, row, col) in buttons:
    button = tk.Button(buttons_frame, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: append_to_entry(t) if t != 'C' else clear_entry())
    button.grid(row=row, column=col, padx=5, pady=5)

# Operators
operations_frame = tk.Frame(app)
operations_frame.grid(row=2, column=0, columnspan=4, pady=5)

operations = ['+', '-', '*', '/']
operator_buttons = {}

for i, op in enumerate(operations):
    button = tk.Button(operations_frame, text=op, width=5, height=2, font=("Arial", 14),
                       command=lambda o=op: set_operation(o))
    button.grid(row=0, column=i, padx=5, pady=5)
    operator_buttons[op] = button

# Calculate Button
button_calculate = tk.Button(app, text="=", width=5, height=2, font=("Arial", 14), command=calculate)
button_calculate.grid(row=3, column=0, columnspan=4, pady=10)

app.mainloop()
