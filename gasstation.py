

#There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

#Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

#input: gas = [1,2,3,4,5], cost = [3,4,5,1,2] 
# output = 3

#python3 solution:

class Solution:
   def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        #return starting gas station's index if you can travel around the circut once in clockwise direction
        if sum(gas) < sum(cost): return -1 #already not possible
        tank, idx = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0: #if we run out of gas before reaching a gas station, we have to disregard everything up to that path as successful and start our count over from the next station for one, complete counterclockwise trip
                tank, idx = 0, i + 1
        return idx


#3/23/24 practice (missed)!:

class Solution:
   def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        currentamount, index = 0, 0 #currentamount = 0 because we begin the jourey with an empty tank at one of the gas stations - mentioned in the problem
        for i in range(len(gas)):
            currentamount += gas[i] - cost[i] #+= because we still have leftover gas if we won out!
            if currentamount < 0: #if we make it to this gas station with 0, it still counts, so <= is not needed and fails gas = [3, 1, 1] cost = [1, 2, 2]
                currentamount = 0
                index = i + 1
        return index #return the starting index as stated in the problem!

#Using <= instead of < in the condition if tank < 0: would not work as intended because it would allow tank to become zero, indicating that you can start from the current position. 
      

#3/23/24 practice again:

class Solution:
   def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        gasamount, startingindex = 0, 0 #we begin the journey with an empty tank
        for i in range(len(gas)): #the trips we will take
            gasamount += gas[i] - cost[i] #we have gas leftover from previous trip
            if gasamount < 0: #we can't make it to the next station, so we have to restart our progress
                gasamount, startingindex = 0, i + 1
        return startingindex #we want the starting station's index - only one is garunteed 


#3/23/24 again:

class Solution:
   def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        howmuch, index = 0, 0
        for i in range(len(gas)):
            howmuch += gas[i] - cost[i]
            if howmuch < 0:
                howmuch, index = 0, i + 1
        return index
    
