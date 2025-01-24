import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main application window
app = tk.Tk()
app.title("Basic Calculator")

# Input fields and labels
label_num1 = tk.Label(app, text="Number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5)

entry_num1 = tk.Entry(app)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(app, text="Number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5)

entry_num2 = tk.Entry(app)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Dropdown for operations
operation_var = tk.StringVar(value="+")
operations_menu = tk.OptionMenu(app, operation_var, "+", "-", "*", "/")
operations_menu.grid(row=2, column=0, columnspan=2, pady=5)

# Calculate button
button_calculate = tk.Button(app, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(app, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, pady=5)

# Run the application
app.mainloop()
