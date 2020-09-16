import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class mclass:
    def __init__(self,  window):
        self.window = window
        self.box = Entry(window)
        self.button = Button (window, text="check", command=self.plot)
        self.box.pack ()
        self.button.pack()

    def plot (self):


        fig = Figure(figsize=(4,4))
        plt = fig.add_subplot(111)
        labels = 'Python', 'C++', 'Ruby', 'Java'
        sizes = [215, 130, 5, 210]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0, 0, 0, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()

        fig2= Figure(figsize=(4, 4))
        plt = fig2.add_subplot(111)
        labels = 'Python', 'C++', 'Ruby', 'Java'
        sizes = [215, 130, 5, 210]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0, 0, 0, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()


window= Tk()
start= mclass (window)
window.mainloop()