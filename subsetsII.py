#Given an integer array nums that may contain duplicates, return all possible 
#subsets
# (the power set).

#The solution set must not contain duplicate subsets. Return the solution in any order.

 

#Example 1:

#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#Example 2:

#Input: nums = [0]
#Output: [[],[0]]



#python3 solution:

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #sort the input - if we don't sort it, 
      #we will get [[4,4],[4,4,1,4],[4,4,4,4],[4,1,4],[4,4,1],[4],[1,4],[4,4,4],[1],[4,4,4,1,4],[],[4,1],[4,4,4,1]] instead of [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]] for test case nums =
#[4,4,4,1,4]
        def f(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            f(i + 1, cur) 
            cur.pop() 
            f(i + 1, cur)
        f(0, [])
        return (list(map(list,set(map(tuple,res))))) #remove duplicates
