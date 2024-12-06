#+===========================================================================+#
#| COS 360 Final Project                                                     |#
#| "Ben Gaudreau's Calculator"                                               |#
#| December 6, 2024                                                          |#
#|---------------------------------------------------------------------------|#
#| A simple four-function calculator implementated using Python's Tkinter    |#
#| package.                                                                  |#
#+===========================================================================+#

import numpy as np
import tkinter as tk
from tkinter import StringVar
from tkinter import ttk

# Global variables and flags
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 600

a = ""
b = ""
disp = "0"
op = None

# Appends NUM to the current number and displays it to the window.
def press_num(num):
    global a, b, disp, op, point
    if (op is None):
        if (num == "." and a.count(".") > 0):
            return
        a = a + str(num)
        disp = a
    else:
        if (num == "." and b.count(".") > 0):
            return
        b = b + str(num)
        disp = b
    display_string.set(disp)
    return

# Updates the global variable op with the value of OPERATION.
def press_op(operation):
    global op
    op = operation
    return

# Inverses the sign of the current number.
def flip():
    global a, b, op, disp
    if (op is None):
        if (a.count("-") == 0):
            a = "-" + a
        else:
            a = a.lstrip("-")
        disp = a
    else:
        if (b.count("-") == 0):
            b = "-" + b
        else:
            b = b.lstrip("-")
        disp = b
    display_string.set(disp)
    return

# Helper method for the four basic mathematical operations.
def comp_handler(a, b, op):
    match (op):
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case _:
            print("ERROR")
            exit()

# Calculates the result of function FUNC on the stored values of a and b, using
# the mathematical function stored in op.
def compute(func):
    global a, b, op, disp
    a = float(a)
    if (func == "sqrt"):
        a = np.sqrt(a)
    else:
        b = float(b)
        if (func == "percent"):
            c = a * (0.01 * b)
            if (op == "*"):
                a = c
            elif (op == "/"):
                a = a * comp_handler(a, c, op)
            else:
                a = comp_handler(a, c, op)
        else:
            a = comp_handler(a, b, op)
        b = ""
    # Trailing zero strip courtesy of https://stackoverflow.com/questions/2440692/formatting-floats-without-trailing-zeros
    a = ('%f' % a).rstrip('0').rstrip('.')
    disp = a
    display_string.set(disp)
    return

# Wipes all of the calculator's variables to their initial values.
def clear():
    global a, b, sign_a, sign_b, op, disp, point
    a = ""
    b = ""
    op = None
    disp = "0"
    display_string.set(disp)
    return

# Main method.
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ben Gaudreau's Calculator")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+50+50")
    root.resizable(False, False)
    root.configure(background="#AAAAAA")

    display_string = StringVar(root, disp)

    display = ttk.Entry(root,
                        font="TkTextFont 30",
                        justify="right",
                        textvariable=display_string)
    display.grid(column=0,
                 row=0,
                 columnspan=4,
                 padx=18, pady=5)

    # Create number buttons and place on grid.
    button_num_0 = tk.Button(root, text="0", font="TkTextFont 12",
                             command=lambda: press_num(0), width=6, height=3,)
    button_num_0.grid(column=0, row=5,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_1 = tk.Button(root, text="1", font="TkTextFont 12",
                             command=lambda: press_num(1), width=6, height=3,)
    button_num_1.grid(column=0, row=4,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_2 = tk.Button(root, text="2", font="TkTextFont 12",
                             command=lambda: press_num(2), width=6, height=3,)
    button_num_2.grid(column=1, row=4,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_3 = tk.Button(root, text="3", font="TkTextFont 12",
                             command=lambda: press_num(3), width=6, height=3,)
    button_num_3.grid(column=2, row=4,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_4 = tk.Button(root, text="4", font="TkTextFont 12",
                             command=lambda: press_num(4), width=6, height=3,)
    button_num_4.grid(column=0, row=3,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_5 = tk.Button(root, text="5", font="TkTextFont 12",
                             command=lambda: press_num(5), width=6, height=3,)
    button_num_5.grid(column=1, row=3,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_6 = tk.Button(root, text="6", font="TkTextFont 12",
                             command=lambda: press_num(6), width=6, height=3,)
    button_num_6.grid(column=2, row=3,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_7 = tk.Button(root, text="7", font="TkTextFont 12",
                             command=lambda: press_num(7), width=6, height=3,)
    button_num_7.grid(column=0, row=2,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_8 = tk.Button(root, text="8", font="TkTextFont 12",
                             command=lambda: press_num(8), width=6, height=3,)
    button_num_8.grid(column=1, row=2,
                      pady=(WINDOW_HEIGHT//36))
    
    button_num_9 = tk.Button(root, text="9", font="TkTextFont 12",
                             command=lambda: press_num(9), width=6, height=3,)
    button_num_9.grid(column=2, row=2,
                      pady=(WINDOW_HEIGHT//36))
    
    button_point = tk.Button(root, text=".", font="TkTextFont 12",
                             command=lambda: press_num("."), width=6, height=3,)
    button_point.grid(column=1, row=5,
                      pady=(WINDOW_HEIGHT//36))
    
    # Create operation buttons and place on grid.
    button_add = tk.Button(root, text="+", font="TkTextFont 12",
                             command=lambda: press_op("+"), width=6, height=3,)
    button_add.grid(column=3, row=5,
                      pady=(WINDOW_HEIGHT//36))
    
    button_subtract = tk.Button(root, text="-", font="TkTextFont 12",
                             command=lambda: press_op("-"), width=6, height=3,)
    button_subtract.grid(column=3, row=4,
                      pady=(WINDOW_HEIGHT//36))
    
    button_multiply = tk.Button(root, text="\u00D7", font="TkTextFont 12",
                             command=lambda: press_op("*"), width=6, height=3,)
    button_multiply.grid(column=3, row=3,
                      pady=(WINDOW_HEIGHT//36))
    
    button_divide = tk.Button(root, text="\u00F7", font="TkTextFont 12",
                             command=lambda: press_op("/"), width=6, height=3,)
    button_divide.grid(column=3, row=2,
                      pady=(WINDOW_HEIGHT//36))
    
    # Create function buttons and place on grid.
    button_clear = tk.Button(root, text="C", font="TkTextFont 12",
                             command=lambda: clear(), width=6, height=3,)
    button_clear.grid(column=0, row=1,
                      pady=(WINDOW_HEIGHT//36))
    
    button_sign = tk.Button(root, text="\u00B1", font="TkTextFont 12",
                             command=lambda: flip(), width=6, height=3,)
    button_sign.grid(column=1, row=1,
                      pady=(WINDOW_HEIGHT//36))
    
    button_sqrt = tk.Button(root, text="\u221A", font="TkTextFont 12",
                             command=lambda: compute("sqrt"), width=6, height=3,)
    button_sqrt.grid(column=3, row=1,
                      pady=(WINDOW_HEIGHT//36))
    
    button_percent = tk.Button(root, text="%", font="TkTextFont 12",
                             command=lambda: compute("percent"), width=6, height=3,)
    button_percent.grid(column=2, row=1,
                      pady=(WINDOW_HEIGHT//36))
    
    button_equals = tk.Button(root, text="=", font="TkTextFont 12",
                             command=lambda: compute("equals"), width=6, height=3,)
    button_equals.grid(column=2, row=5,
                      pady=(WINDOW_HEIGHT//36))
    
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    finally:
        root.mainloop()