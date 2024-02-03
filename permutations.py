#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

#Example 1:

#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


#note: with permutations, order matters. with combinations, it does not

#solution in python3:

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path): 
            if not nums: #when nums is empty, we know path has one of the possible permutations, so add it to the result list
                result.append(path) 
                return #after this line executes, we will backtrack 
            for i in range(len(nums)): 
                #we want to exclude the ith element from the nums list and add it to the end of path list
                #we backtrack to the state right before nums becomes empty
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) #we are appending i to the end of the path list
        result = [] 
        backtrack(nums, []) 
        return result 
     
#SUPER IMPORTANT: indentation for last 3 lines must be to the indentation of def backtrack(nums, path) because the execution goes from def backtrack(nums, path): > result = [] > backtrack(nums, []) in the beginning!!!
#nums resets to 0 when if block is skipped
      
#[1, 2, 3] example:
# nums = [2, 3] path = [1]
# if not nums > false, so skip back to the for loop
# i is still 0
# nums = [3] path = [1, 2]
# if not nums > false, so skip back to the for loop
# nums = [] path = [1, 2, 3]
# if not nums > true, so add [1, 2, 3] to the result list
# we back track to nums = [2] path = [1, 3]
# i = 0, so nums = [] path = [1, 3, 2] 
# nums is now empty, so add [1, 3, 2] to the result list
# we back to track to nums = [1, 2, 3] path = []
# i = 1, so nums = [1, 3] path = [2]
# i = 0, so nums = [3] path = [2, 1]
# nums = [] path = [2, 1, 3]
# nums is empty, so add [2, 1, 3] to the result list, and i becomes 1 because we returned 
# backtrack to nums = [1, 3] path = [2]
# i = 1, so we get nums = [1] path = [2, 3]
# nums is not empty, so i resets to 0 in the for loop
# now, because nums only has one element - [1], i has to be 0 and resets as usual, so nums = [] path = [2, 3, 1]
# nums is empty, so add [2, 3, 1] to the result list and return
# back track to nums = [1, 2, 3] path = []
# since i = 2 because we did indeed execute the if block and return, nums = [1, 2] path = [3]
# now, because nums is not empty, we skip the if block, and i resets to 0
# now that i = 0, nums = [2] path = [3, 1]
# again, we skip the if block since nums is not empty and i stays at 0 in the proceeding for loop like usual
# now that i = 0, nums = [] path = [3, 1, 2]
# now that nums is empty, we add [3, 1, 2] to our result list and return 
# i = 1 because we did indeed execute the if block and return, so we backtrack to nums = [1, 2] path = [3]
# because i = 1, nums = [1] path = [3, 2]
# again, nums is not empty, so we skip if block and i remains at 0
# i = 0, so nums = [] path = [3, 2, 1]
# nums is empty, so add [3, 2, 1] to the result list and return 
# i = 1 returns none and i = 2 returns none, so the execution ends, and we return the result list


#12/27/23 refresher - my solution in python3:
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def f(nums, path):
            if not nums:
                result.append(path)
                return
            for number in range(len(nums)):
                #:number, not number: because we are excluding everything up to number and not including number first!!!!!
                f(nums[:number] + nums[number + 1:], path + [nums[number]])
        result = []
        f(nums, [])
        return result

#12/28/23 refrehser - my solution in python3:

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(nums, ans):
            if not nums:
                res.append(ans)
                return
            #must be indented to the level of if, not def f because ans wouldn't exist because the for loop would be called before f(nums, []), resulting in an error
            for number in range(len(nums)):
                f(nums[:number] + nums[number + 1:], ans + [nums[number]])

        f(nums, [])
        return res

#12/29/23 refresher - my solution:

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def f(nums, ans):
            if not nums:
                result.append(ans)
                return
            for number in range(len(nums)):
                f(nums[:number] + nums[number + 1:], ans + [nums[number]])
        result = []
        f(nums, [])
        return result
     
#1/2/24 refresher - my solution:

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def f(nums, ans):
            if not nums:
                res.append(ans)
                return
            #when the if not nums block gets executed, then we increment number. this is because, once we start subarrays that start with each number in nums, then we are finished exploring all paths - for example, [1, 2, 3] permutation has 2 subarrays starting with 1 and 2 starting with 2 and 2 starting with 3, and we only increment the starting value after we have swapped the order of the order numbers - [1, 2, 3] and [1, 3, 2] - only then do we go onto permutations starting with [2
            for number in range(len(nums)):
                f(nums[:number] + nums[number + 1:], ans + [nums[number]])

        res = []
        f(nums, [])
        return res
        


#2/3/24 refresher:

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def p(nums, path):
            if not nums:
                res.append(path.copy())
                return
            for number in range(len(nums)):
                #appends to the end of the path list, so path is a list, and we are adding another list to the end of path - [nums[number]]
                #when we hit our base case, number increments, and nums and path also reset. Otherwise, we are excluding nums based on a smaller proportion 
                p(nums[:number] + nums[number + 1:], path + [nums[number]])

        res = []
        p(nums, [])
        return res
