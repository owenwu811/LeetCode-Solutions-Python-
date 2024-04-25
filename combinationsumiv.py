
#Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

#The test cases are generated so that the answer can fit in a 32-bit integer.

#nums = [1,2,3], target = 4 - output is 7


#python3 solution:

#bottom up dynamic programming approach:

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #we want to know how many ways we can add up to target of 4, so we are looking for dp[4] ultimately 
        #dp[4] [4] or the number inside of the brackets is the target value we want to sum to 
        #{targettosumto: numberofways} 
        #dp[1] = 1 means that there is 1 way to sum up to our target sum of 1 inside of [1, 2, 3] input
        #we know that every number in the input array will be positive 
        dp = {0: 1} #base case - epresents the specific case of target = 0, nums = [] -> 1 solution of emptiness -> 1 way to sum up to 0 - you don't
        for levelamount in range(1, target + 1):
            dp[levelamount] = 0
            for inputn in nums:
                #dp[4] = dp[4 - 1] + dp[4 - 2] + dp[4 - 3] on the final iteration of the for total loop because our input is [1, 2, 3], so the number to the right of the minus in each dp[] is each number in our input array!
                dp[levelamount] += dp.get(levelamount - inputn, 0) #if it becomes negative aka dosen't exist as a key in our dictionary, then we say 0 for that level to say 0 ways because we are only given positive numbers in our input, so we don't care about computing the number of ways to sum up to negative sums
        return dp[levelamount]

        #the dp[total] += dp.get(total - n, 0) line just calculates the number of ways to sum up to each number from 1 through target by adding the value of the current dictionary level with the value of previous dictionary values for caching purposes

#4/19/24:

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = {0: 1} #[], {levelamount:numberofways}
        for levelamount in range(1, target + 1):
            d[levelamount] = 0 #how many ways starts at 0
            for coinvalue in nums:
                d[levelamount] += d.get(levelamount - coinvalue, 0)
        return d[levelamount]

#4/20/24:

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = {0: 1} #][] - 1 way
        #remember we are building up from 1 in increments of 1 up to target, which is 4 in this case
        for levelamount in range(1, target + 1):
            d[levelamount] = 0
            for coinvalue in nums:
                #computing number of ways because {levelamount: numberofways}
                d[levelamount] += d.get(levelamount - coinvalue, 0)
        return d[levelamount]


#4/21/24:

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #thing of coin change without the minimum number of ways requirement
        #we want the number of ways to add up to target - duplicates are fine as long as shuffled
        d = {0: 1} #base case for [] > 1 way
        for levelamount in range(1, target + 1):
            d[levelamount] = 0 #each amount starts with 0 ways to add or sum up to it - that's what will be computed
            for coinvalue in nums:
                d[levelamount] += d.get(levelamount - coinvalue, 0)
        return d[levelamount]


#4/22/24:

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = {0: 1}
        for levelamount in range(1, target + 1):
            d[levelamount] = 0
            for coinvalue in nums:
                d[levelamount] += d.get(levelamount - coinvalue, 0)
        return d[levelamount]
    

#4/24/24 refresher:

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        d = {0: 1} #base case - [] - 1 way - you don't
        for levelamount in range(1, target + 1):
            d[levelamount] = 0 
            for coinvalue in nums:
                d[levelamount] += d.get(levelamount - coinvalue, 0)
        return d[levelamount] #bottom up dynamic programming approach 

        
 
