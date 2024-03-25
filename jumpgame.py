
#You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

#Return true if you can reach the last index, or false otherwise.



#Example 1:

#Input: nums = [2,3,1,1,4]
#Output: true
#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#Example 2:

#Input: nums = [3,2,1,0,4]
#Output: false
#Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 


Python Solution :

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True

#3/24/24 refresher (missed):

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #reachable variable represents the farthest index that can be reached from previous positions but is updated based on the current position (the max reachable index from all positions processed so far)
        reachable = 0
        for i in range(len(nums)):
            if i > reachable: #remember that i is always <= the last index, so if i is bigger than reachable up to the current position, we can already return False
                return False
            #adding i to nums[i] gives us the index that can be reached by taking these steps. 
            reachable = max(reachable, i + nums[i]) #nums[i] = number of steps we can take from current position i. if nums[i] = 3, we can take 3 steps forward from index i. 
        return True

#3/24/24 refresher again:

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableindex = 0
        for curindex in range(len(nums)):
            howmanyjumps = nums[curindex]
            if curindex > reachableindex:
                return False
            reachableindex = max(reachableindex, curindex + howmanyjumps)
        return True

#3/25/24 refresher:

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #we can jump the value of the array from the current index and want to know if we can reach the last index or not
        reachableindex = 0
        for currentindex in range(len(nums)):
            if currentindex > reachableindex:
                return False
            reachableindex = max(reachableindex, currentindex + nums[currentindex])
        return True

#3/25/24 refresher again:

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableindex = 0
        for currentindex in range(len(nums)):
            if currentindex > reachableindex:
                return False
            reachableindex = max(reachableindex, currentindex + nums[currentindex])
        return True
        
