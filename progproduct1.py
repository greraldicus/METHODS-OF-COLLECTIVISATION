# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LFjO0TifA5l4sYR3Z6n7gggbPdWXHn7p
"""

import tkinter as tk
from tkinter import messagebox
import cmath
import gettext

# Установка языка
lang = "en_US"  # Установите язык по умолчанию
locale = gettext.translation('messages', localedir='locale', languages=[lang])
locale.install()
_ = locale.gettext

def calculate_square_root():
    try:
        number = complex(entry.get())
        precision = int(precision_entry.get())
        result = extract_square_root(number, precision)
        result_label.config(text=result)
    except ValueError:
        messagebox.showerror(_("Error"), _("Please input correct number"))
    except Exception as e:
        messagebox.showerror(_("Error"), f"{_('Error')}: {e}")

def extract_square_root(x, precision=2):
    try:
        if x == 0:
            raise ValueError(_("Cannot calculate square root of zero"))
        result = cmath.sqrt(x)
        return f"{_('Square root of')} {x} = {result:.{precision}f}"
    except ValueError as e:
        return f"{_('Error')}: {e}"
    except Exception as e:
        return f"{_('Error')}: {e}"

root = tk.Tk()
root.title(_("Square Root Extraction"))

input_label = tk.Label(root, text=_("Enter a number:"))
input_label.pack()

entry = tk.Entry(root)
entry.pack()

precision_label = tk.Label(root, text=_("Enter precision:"))
precision_label.pack()

precision_entry = tk.Entry(root)
precision_entry.pack()

calculate_button = tk.Button(root, text=_("Calculate"), command=calculate_square_root)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()