from raceSim import *

def seasonSimulation(numberOfRacesInSeason):

    pointsThisSeason = {
            "pointsMV"
            "pointsSP"
            "pointsLH"
            "pointsGR"
            "pointsCL"
            "pointsCS"
            "pointsFA"
            "pointsLS"
            # TODO: add the rest
        }

    numberOfRacesCompleted = 0

    while numberOfRacesCompleted < numberOfRacesInSeason:
        for result in sortedResults:
            initials = score_initials[result]
            driver_names = [driver_initials[initial] for initial in initials]
            print(f"Result: {result}, Drivers: {', '.join(driver_names)}")

        numberOfRacesCompleted += 1

        