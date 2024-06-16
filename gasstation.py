

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

#3/25/24:

class Solution:
   def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        #we only have one solution at most
        #we want to return the starting index as to where it's possible
        if sum(gas) < sum(cost): return -1 #based on totals, we can rul this out right away
        amount, index = 0, 0
        for i in range(len(gas)):
            amount += gas[i] - cost[i]
            if amount < 0:
                amount, index = 0, i + 1
        return index

#3/25/24 refresher again:

class Solution:
   def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        #costs cost[i] gas to travel to i + 1 station. begin journey with empty tank
        #we want to return the starting index if it's possible to travel in one cycle
        if sum(gas) < sum(cost): return -1
        amountofgas, currentindex = 0, 0
        for i in range(len(gas)):
            amountofgas += gas[i] - cost[i]
            if amountofgas < 0:
                amountofgas, currentindex = 0, i + 1
        return currentindex

#3/27/24:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #we have n number of gas stations along a circular route where the amount of gas at each station is the value in the gas array
        #it costs the value in the cost array of gas to travel from the current index in gas array to the index to the right in gas array 
        #we begin the journey with an empty gas tank
        #we want the starting gas station's index if we can travel around the circut once counterclockwise or -1 if not possible at all from any of the indexes in gas array
        if sum(gas) < sum(cost): return -1 #already not possible given total rule
        amountofgas, currentindex = 0, 0
        for i in range(len(gas)):
            amountofgas += gas[i] - cost[i] #we have leftover gas from before
            if amountofgas < 0: #we cannot make it to the next station
                amountofgas, currentindex = 0, i + 1
        return currentindex


#4/1/24:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        amount, index = 0, 0
        for i in range(len(gas)):
            amount += gas[i] - cost[i]
            if amount < 0:
                amount, index = 0, i + 1
        return index

#4/9/24 refresher:

class Solution:
   def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost): return -1
        amount, index = 0, 0
        for i in range(len(gas)):
            amount += gas[i] - cost[i]
            if amount < 0:
                amount, index = 0, i + 1
        return index

#4/27/24 refresher (really struggled with but solved):

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        starting, index = 0, 0
        for i in range(len(gas)):
            starting += gas[i] - cost[i]
            if starting >= 0:
                continue
            else:
                starting, index = 0, i + 1
        return index

#4/30/24 refresher:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startingwith, startingindex = 0, 0
        if sum(gas) < sum(cost): return -1
        for i in range(len(gas)):
            startingwith += gas[i] - cost[i]
            if startingwith < 0:
                startingwith, startingindex = 0, i + 1
        return startingindex
 
#5/26/24 review (missed on 5/25/24):

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1 #if the entire array is less than entire array, then we can't start anywhere, so return -1. Otherwise, we will track the starting index and return that starting index at the end as res. 
        amount = 0 #start with empty tank
        res = 0 #track starting index if possible
        for i in range(len(gas)): #loop through gas array 
            amount += (gas[i] - cost[i])
            if amount < 0:
                amount, res = 0, i + 1
        return res

#6/5/24 review:

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        startinggastankamount = 0
        res = 0
        for i in range(len(gas)):
            startinggastankamount += (gas[i] - cost[i])
            if startinggastankamount < 0:
                startinggastankamount, res = 0, i + 1
        return res

#6/16/24 review:

class Solution:
   def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        starting = 0
        res = 0
        if sum(gas) < sum(cost): return -1
        for i in range(len(gas)):
            starting += (gas[i] - cost[i])
            if starting < 0:
                starting, res = 0, i + 1
        return res
            
