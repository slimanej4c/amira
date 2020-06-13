import tkinter as tk
from tkinter import ttk

values = ['mustang', 'focus', 'tesla']
root = tk.Tk()
labels = dict((value, tk.Label(root, text=value)) for value in values)

def handler(event):
    current = combobox.current()
    if current != -1:
        for label in labels.values():
            label.config(relief='flat')
        value = values[current]
        label = labels[value]
        label.config(relief='raised')

combobox = ttk.Combobox(root, values=values)
combobox.bind('<<ComboboxSelected>>', handler)
combobox.pack()
for value in labels:
    labels[value].pack()

root.mainloop()