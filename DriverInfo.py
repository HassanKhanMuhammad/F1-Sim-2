import info
import random

class driverInfo:
    def __init__(self, nameInitials, team, driverSkill):
        self.nameInitials = nameInitials
        self.team = team

    def findResults(driverSkill, team):
        return team + driverSkill + random.randrange(1, 15) / 3
    

