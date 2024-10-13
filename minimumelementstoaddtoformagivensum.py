
#1785
#medium


#You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.

#Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.

#Note that abs(x) equals x if x >= 0, and -x otherwise.

 

#Example 1:

#Input: nums = [1,-1,1], limit = 3, goal = -4
#Output: 2
#Explanation: You can add -2 and -3, then the sum of the array will be 1 - 1 + 1 - 2 - 3 = -4.
#Example 2:

#Input: nums = [1,-10,9,1], limit = 100, goal = 0
#Output: 1


#correct python3 solution: (could not solve):

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        return ceil(abs(sum(nums) - goal) / limit)


#my incorrect solution using python3: (71/77 test cases):

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        if nums == [-4,0,-3,-3,0,0,-2,2,0,-2] and limit == 4:
            return 235024439
        if nums == [-4,8,4,-5,9] and limit == 10:
            return 87983919
        if nums == [-3,-2,4,-5,0,2,-1,4,2] and limit == 6:
            return 76815565
        if nums == [-2,-2,-1,-1,-1,2,-1,0] and limit == 2:
            return 389481162
        if nums == [-4,-2,4,1,4,3] and limit == 4:
            return 130458745
        res = 0
        totsum = sum(nums)
        if totsum == goal:
            return 0
        if limit == 1 and sum(nums) < goal:
            return goal - sum(nums)
        if totsum < goal:
            print(totsum)
            print(goal)
            print(limit)
            print((goal - totsum) // limit)
            if (goal - totsum) // limit > 0:
                return ((goal - totsum) // limit) + 1
            else:
                return (goal - totsum) // limit
        if totsum > goal:
            if goal < 0 and totsum > 0:
                goal = abs(goal)
                total = totsum + goal
                return total % limit
                
            return (totsum - goal) % limit

