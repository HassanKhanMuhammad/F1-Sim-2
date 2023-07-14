import tkinter as tk
from tkinter import font 
from raceSim import *
from raceSim import initials

def exeRaceSim():

    headerFont = font.Font(family="Arial", size=20, weight="bold")
    normFont = font.Font(family="Arial", size=12)


    x = 1

    window = tk.Tk()
    window.title("F1 Sim 2 | Race Simulator")
    window.geometry("750x600")

    for i, result in enumerate(sortedResults):
        initials = score_initials[result]
        driver_names = [driver_initials[initial] for initial in initials]
        result_label = tk.Label(window, text=f"P{x}: {', '.join(driver_names)}", font=normFont)
        x += 1
        result_label.pack(pady=3)

    tk.mainloop()
