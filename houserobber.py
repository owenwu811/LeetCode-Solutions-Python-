

#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

#nums = [2,7,9,3,1]
#python3 solution:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2 #0, 2 (n is now on 7) because this represents how much we can rob up to the previous house, and n is the current amount of money. when n is 9 (current), rob1 becomes 7 and so on
            rob2 = temp
        return rob2



#explanation:

#This solution implements a dynamic programming approach to solve the House Robber problem. The problem statement typically involves finding the maximum amount of money you can rob without robbing adjacent houses, given an array of non-negative integers representing the amount of money of each house.

#Here's how the solution works:

#Initialize two variables rob1 and rob2 to keep track of the maximum amount of money that can be robbed up to the previous two houses.
#Iterate through the array of numbers representing the money in each house.
#For each house n, calculate the maximum amount of money that can be obtained if we choose to rob this house (n + rob1) or skip this house and stick with the maximum amount obtained from the previous house (rob2). Take the maximum of these two values and store it in a temporary variable temp.
#Update rob1 to be the previous value of rob2, as we are considering the next house now.
#Update rob2 to the value stored in temp, which represents the maximum amount of money that can be obtained up to the current house.
#Repeat steps 3-5 for all houses in the array.
#Finally, return rob2, which holds the maximum amount of money that can be robbed without robbing adjacent houses.
#The reason this approach works is because it considers the maximum amount of money that can be robbed up to the current house by either including the current house or excluding it, while ensuring that adjacent houses are not robbed. By keeping track of the maximum amounts up to the previous two houses (rob1 and rob2), the solution avoids considering adjacent houses simultaneously and ensures that the optimal solution is obtained.


#3/22/24 practice round 2:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            maxtemp = max(n + rob1, rob2)
            rob1 = rob2 #up to previous
            rob2 = maxtemp
        return rob2

#3/23/24:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for n in nums:
            maxnow = max(n + prev, cur)
            prev = cur
            cur = maxnow
        return cur

#3/23/24 again:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for n in nums:
            tempmax = max(n + prev, cur)
            prev = cur
            cur = tempmax
        return cur

#3/24/24:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for n in nums:
            tempmax = max(n + prev, cur) #we are choosing between robbing up to INCLUDING the previous house OR up to INCLUDING the current house because we have the constraint of having to skip a house 
            prev = cur
            cur = tempmax
        return cur

#3/25/24:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        for n in nums:
            tempmax = max(prev + n, cur)
            prev = cur
            cur = tempmax
        return cur

#3/27/24:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        #dynamic programming approach where we calculate the max amount we can rob up to previous vs. current house since we have to skip one house
        prev, cur = 0, 0
        for number in nums:
            tempmax = max(number + prev, cur)
            prev = cur
            cur = tempmax
        return cur

#3/29/24:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for number in nums:
            tempmax = max(number + rob1, rob2)
            rob1 = rob2
            rob2 = tempmax
        return rob2

#4/19/24:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tempmax = max(n + rob1, rob2) #max(up to previous house, up to current house)
            rob1 = rob2 #rob1 = rob2, which is 0 in the 1st iteration
            rob2 = tempmax
        return rob2

#5/18/24 refresher:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2

#6/12/24 review:

class Solution:
    import math
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2

#7/15/24 practice (my own solution):

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob2, n + rob1)
            rob1 = rob2
            rob2 = tmp
        return rob2

#9/8/24 review from grokking course:

def rob_houses(nums):

    rob1, rob2 = 0, 0
    for n in nums:
      tmp = max(n + rob1, rob2)
      rob1 = rob2
      rob2 = tmp
    return rob2
