

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


