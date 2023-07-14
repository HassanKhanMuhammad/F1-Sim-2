from raceSim import *

# def seasonSimulation(numberOfRacesInSeason):


#     numberOfRacesCompleted = 0

#     while numberOfRacesCompleted < numberOfRacesInSeason:
#         for result in sortedResults:
#             initials = score_initials[result]
#             driver_names = [driver_initials[initial] for initial in initials]
#             print(f"Result: {result}, Drivers: {', '.join(driver_names)}")

#         numberOfRacesCompleted += 1

class seasonSimulation():

    pointsThisSeason = {
        "pointsMV": 0,
        "pointsSP": 0,
        "pointsLH": 0,
        "pointsGR": 0,
        "pointsCL": 0,
        "pointsCS": 0,
        "pointsFA": 0,
        "pointsLS": 0
        # TODO: add the rest
        # points are zero in the start of the season.
    }


    POINTS_DISTRIBUTION = {
        "P1": 25,
        "P2": 18,
        "P3": 15,
        "P4": 12,
        "P5": 10,
        "P6": 8,
        "P7": 6,
        "P8": 4,
        "P9": 2,
        "P10": 1
    }

    def __init__(self, racesInSeason):
        self.racesInSeason = racesInSeason

    def GivePoints(driver=dict, position=str):
        return driver + position # returns value of the amount of points driver has. 

