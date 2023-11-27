#On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

#The north direction is the positive direction of the y-axis.
#The south direction is the negative direction of the y-axis.
#The east direction is the positive direction of the x-axis.
#The west direction is the negative direction of the x-axis.
#The robot can receive one of three instructions:

#"G": go straight 1 unit.
#"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
#"R": turn 90 degrees to the right (i.e., clockwise direction).
#The robot performs the instructions given in order, and repeats them forever.

#Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.



#Python3 solution 

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #(x, y)
        direction = (0,1) #direction we are facing is up/north by default as stated in the problem 
        start = [0,0] # the robot starts on the center coordinate of an x, y grid 
        for x in instructions: 
            if x == 'G': #go towards that direction we are facing in direction - pretty straightforward 
                start[0] += direction[0] 
                start[1] += direction[1]
            elif x == 'L': #(0, 1) > (-1, 0), for example - y axis is still 0 
                direction = (-direction[1], direction[0])
            elif x == 'R': # (1, 0) > (0, -1) for example 
                direction = (direction[1], -direction[0])
        return start == [0,0] or direction != (0,1) #if we are on a coordinate that's the same as we started, that's a cycle, but if we face a direction that's different than what we were originally facing, there's still a chance to get back to starting since instructions are repeated infinitely according to the problem
