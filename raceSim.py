from info import *
import random
import tkinter as tk
from DriverInfo import driverInfo

# Race Sim BTS.
# TODO: work on GUI on seperate file.
# For loop at the end for debugging. (Do not remove)

driver_initials = {
    "MV": "Max Verstappen",
    "SP": "Sergio Perez",
    "LH": "Lewis Hamilton",
    "GR": "George Russell",
    "FA": "Fernando Alonso",
    "LS": "Lance Stroll",
    "CL": "Charles Leclerc",
    "CS": "Carlos Sainz",
    "EO": "Esteban Ocon",
    "PG": "Pierre Gasly",
    "LN": "Lando Norris",
    "OP": "Oscar Piastri",
    "KM": "Kevin Magnussen",
    "NH": "Nico Hulkenburg",
    "VB": "Valtteri Bottas",
    "ZG": "Zhou Guanyu",
    "YT": "Yuki Tsunoda",
    "NV": "Nyck De Vries",
    "AA": "Alex Albon",
    "LSA": "Logan Sargeant"
}

# finalFix = carpower + driverskill + randomnumber / 3

resultsMV = teams["Red Bull"] + drivers["MV"] + random.randrange(1, 15) / 3
resultsSP = teams["Red Bull"] + drivers["SP"] + random.randrange(1, 15) / 3
resultsLH = teams["Mercedes"] + drivers["SP"] + random.randrange(1, 15) / 3
resultsGR = teams["Mercedes"] + drivers["GR"] + random.randrange(1, 15) / 3
resultsFA = teams["Aston Martin"] + drivers["FA"] + random.randrange(1, 15) / 3
resultsLS = teams["Aston Martin"] + drivers["LS"] + random.randrange(1, 15) / 3
resultsCL = teams["Ferrari"] + drivers["CL"] + random.randrange(1, 15) / 3
resultsCS = teams["Ferrari"] + drivers["CS"] + random.randrange(1, 15) / 3
resultsEO = teams["Alpine"] + drivers["EO"] + random.randrange(1, 15) / 3
resultsPG = teams["Alpine"] + drivers["PG"] + random.randrange(1, 15) / 3
resultsLN = teams["Mclaren"] + drivers["LN"] + random.randrange(1, 15) / 3
resultsOP = teams["Mclaren"] + drivers["OP"] + random.randrange(1, 15) / 3
resultsKM = teams["Haas"] + drivers["KM"] + random.randrange(1, 15) / 3
resultsNH = teams["Haas"] + drivers["NH"] + random.randrange(1, 15) / 3
resultsVB = teams["Alfa Romeo"] + drivers["VB"] + random.randrange(1, 15) / 3
ResultsZG = teams["Alfa Romeo"] + drivers["ZG"] + random.randrange(1, 15) / 3
resultsYT = teams["Alpha Tauri"] + drivers["YT"] + random.randrange(1, 15) / 3
resultsNV = teams["Alpha Tauri"] + drivers["NV"] + random.randrange(1, 15) / 3
resultsAA = teams["Williams"] + drivers["AA"] + random.randrange(1, 15) / 3
resultsLSA = teams["Williams"] + drivers["LSA"] + random.randrange(1, 15) / 3

results = [
    resultsMV,
    resultsSP,
    resultsLH,
    resultsGR,
    resultsFA,
    resultsLS,
    resultsCL,
    resultsCS,
    resultsEO,
    resultsPG,
    resultsLN,
    resultsOP,
    resultsKM,
    resultsNH,
    resultsVB,
    ResultsZG,
    resultsYT,
    resultsNV,
    resultsAA,
    resultsLSA
]

score_initials = {}  # Dictionary to associate scores with initials

# Build the dictionary of scores and initials
for i in range(len(results)):
    score = results[i]
    initials = list(driver_initials.keys())[i]
    
    if score in score_initials:
        score_initials[score].append(initials)
    else:
        score_initials[score] = [initials]

sortedResults = sorted(results, reverse=True)

# print
for result in sortedResults:
    initials = score_initials[result]
    driver_names = [driver_initials[initial] for initial in initials]
    print(f"Result: {result}, Drivers: {', '.join(driver_names)}")
