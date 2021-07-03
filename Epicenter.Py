# Backend Assignment 2
# Problem Name - Yet Another Coronavirus Question
# Code Written By - Ratnesh Kumar (ratneshkumar301@yahoo.com)

from collections import defaultdict

class Epicenters:
    def __init__(self, inputs):
        self.inputs = inputs
        # Variable used to store reached cities
        self.currentCities = set()
    
    # findEpicenter method is used to find the possible cities with given maximum distance    
    def findEpicenters(self, spot, distanceTravelled, paths):
        # Storing reached city into a set variable to avoid duplicacy
        self.currentCities.add(spot)
        
        # returning when the virus has reached to maximum distance
        if distanceTravelled <= 0:
            return
        
        for possibleSpot in paths[spot]:
            # Reaching to next connected city by road
            self.findEpicenters(possibleSpot, distanceTravelled-1, paths)
            
    # Solve Method is used to store input variables and finding number of possible epicenter as a result
    def solve(self):
        # storing input values to variables
        cityNumber = self.inputs[0][0]
        hotspotNumber = self.inputs[0][1]
        maxDistanceTravel = self.inputs[0][2]
        hotspots = list(self.inputs[1])
        
        # Variables used to store roads between u and v and counter for finding epicenter 
        paths = defaultdict(list)
        epicentersFound = 1
        
        # This variable is used to store number of possible epicenter count
        epicenterNumbers = 0
        
        # Storing linked cities u->v (bi-directional)
        for index in range(2, len(self.inputs)):
            paths[self.inputs[index][0]].append(self.inputs[index][1])
            paths[self.inputs[index][1]].append(self.inputs[index][0])
       
        # Looping over each cities to get possible reached another cities with given maximum distance
        for spot in range(1, cityNumber+1):
            self.findEpicenters(spot, maxDistanceTravel, paths)
          
            # Checking whether possible reached cities having all hotspots
            for spots in hotspots:
                if spots not in self.currentCities:
                    epicentersFound = 0
                    break
            
            # Increasing count of epicenters when epicenter is found
            if epicentersFound == 1:
                epicenterNumbers+=1
                
            # Resetting variable values
            self.currentCities = set()
            epicentersFound = 1
            
        
        # returning number of possible epicenters
        return epicenterNumbers
        
            

if __name__ == "__main__":
    # Creating sample input
    inputs = [[5, 2, 2], [2, 5], [1, 2], [2, 3], [2, 4], [4, 5]]
    # passing input to Epicenter class
    res = Epicenters(inputs)
    print(res.solve())
