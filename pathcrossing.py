#1496
#easy

#Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

#Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

#Input: path = "NES"
#Output: false 
#Explanation: Notice that the path doesn't cross any point more than once.

#my own solution using python3:

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        startingx, startingy = 0, 0
        used = []
        used.append([startingx, startingy])
        curx, cury = startingx, startingy
        for p in path:
            if p == "N":
                curx -= 1
            elif p == "E":
                cury += 1

            elif p == "S":
                curx += 1

            elif p == "W":
                cury -= 1
            print(curx, cury)
            if [curx, cury] in used:
                return True
            used.append([curx, cury])
        return False
