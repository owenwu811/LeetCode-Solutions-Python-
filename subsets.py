
#Given an integer array nums of unique elements, return all possible 
#subsets
# (the power set).

#The solution set must not contain duplicate subsets. Return the solution in any order.

 

#Example 1:

#Input: nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

#[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], [] - this is what the code below produces as output to [1, 2, 3] input

#remember that permutations means order matters. subset means order dosen't matter, so [1, 2] is valid, but then [2, 1] wouldn't be valid and would count as a duplicate for a subset 
#back tracking


#python3 solution:

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def f(i):
            #out of bounds - base case of recursion
            if i >= len(nums): # i is the index - so 0, 1, 2 if nums = [1, 2, 3], so this block would be true if 3 >= 3 for nums = [1, 2, 3]. if not, then we skip the inner block and go down to subset.append(nums[i])
                res.append(subsets.copy()) #if we didn't use .copy here, we would append [[1, 2, 3]], and then when we pop, we would be modifying our res list back to [[1, 2]], which we don't want
                return
            subsets.append(nums[i])  #left side
            f(i + 1) 
            subsets.pop() #right side - SUBSET.POP() IS ALWAYS REMOVING THE LAST VALUE FROM LIST - IT DOSEN'T DEPEND ON I!!!!!
            f(i + 1) 
        f(0)
        return res


  #from [1, 2] to [1, 3], we pop, so [1], and then we add 3, so [1, 3], and then the base case hits, and we append a copy of [1, 3] to the res list

#pythontutor visualization
#nums = [1, 2, 3]
#res = []
#subsets = []
#def f(i):
#    if i >= len(nums):
#        res.append(subsets.copy())
#        return
#    subsets.append(nums[i])
#    f(i + 1)
#    subsets.pop()
#    f(i + 1)
#f(0)
#print(res)
        
#12/29/23 refresher:

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(index):
            if index >= len(nums):
                res.append(s.copy())
                return
            s.append(nums[index])
            f(index + 1)
            s.pop()
            f(index + 1)
        
        res = []
        s = []
        f(0)
        return res

#12/30/23 refresher:

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            f(i + 1)
            subset.pop()
            f(i + 1)

        subset = []
        res = []
        f(0)
        return res
