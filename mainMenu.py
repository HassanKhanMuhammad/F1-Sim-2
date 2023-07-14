from raceSim import *
from info import *

import tkinter as tk
from tkinter import font

from raceSimGUI import exeRaceSim
from teamRandomizer import exeTeamRandomizer
# from teamRandomizer import exeTeamRandomizer

# menu that leads to:
# - team generator
# - race simulator
# - season simulator
# Add these features as buttons

window = tk.Tk()
window.title("F1 Simulator 2 | Main")
window.geometry("300x250")

headerFont = font.Font(family="Arial", size=20, weight="bold")
normFont = font.Font(family="Arial", size=12)

# label1 = tk.Label(window, text=sortedResults[0]).pack()

# main title.
titleLabel = tk.Label(window, text="F1 Simulator", font=headerFont)

# Linking Buttons:

raceSimButton = tk.Button(window, text="Race Simulator", font=normFont, command=exeRaceSim)
teamRandomizerButton = tk.Button(window, text="Team Randomizer", font=normFont, command=exeTeamRandomizer)
seasonSimulatorButton = tk.Button(window, text="Season Simulator", font=normFont, command=None)

titleLabel.grid(row=0, column=0)
raceSimButton.grid(row=2, column=0)
teamRandomizerButton.grid(row=3, column=0)


tk.mainloop()