
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


#1/1/24 refresher:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(index):
            if index >= len(nums):
                res.append(ans.copy())
                return
            ans.append(nums[index])
            f(index + 1)
            ans.pop()
            f(index + 1)
        res = []
        ans = []
        #I think: since the recursive parameter is being used to control the index, and we can't have duplicates, we have to keep increasing with every recursive call because a subet can't have two of the same numbers in it
        f(0)
        return res

#explanation:

#ans.append(nums[index]): Add the current element to the subset.
#f(index + 1): Recursively call the function with the next index to include the current element in the subset.
#ans.pop(): Remove the current element from the subset (backtrack).
#f(index + 1): Recursively call the function with the next index to exclude the current element from the subset.

#If you were to replace f(index + 1) with f(index) in the code, it would result in an infinite loop. You would keep calling the same index element over and over again without ever hitting the base case of if index >= len(nums) to stop recursion and return a value (nothing in this case) back to the parent function


#1/3/24 refresher - my solution python3:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(index, ans):
            if index >= len(nums):
                res.append(ans.copy())
                return
            ans.append(nums[index])
            f(index + 1, ans)
            ans.pop()
            f(index + 1, ans)

        res = []
        f(0, [])
        return res


#1/4/24 refresher - my solution in python3:

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(index, subset):
            if index >= len(nums):
                result.append(subset.copy())
                return
            #left side - add
            subset.append(nums[index])
            f(index + 1, subset)
            #right side - don't include aka pop from before
            #123 12 13 1 23 2 
            subset.pop()
            f(index + 1, subset)
        result = []
        f(0, [])
        return result


#1/6/24 refresher solution:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(index, subset):
            if index >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            f(index + 1, subset)
            subset.pop()
            f(index + 1, subset)

        res = []
        f(0, [])
        return res


#1/17/24 refresher:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path, nums):
            if index >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[index])
            dfs(index + 1, path, nums)
            path.pop()
            dfs(index + 1, path, nums)
        res = []
        dfs(0, [], nums)
        return res


#1/18/24 refresher:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(index, nums, ans):
            if index >= len(nums):
                res.append(ans.copy())
                return
            ans.append(nums[index])
            f(index + 1, nums, ans)
            ans.pop()
            f(index + 1, nums, ans)

        res = []
        f(0, nums, [])
        return res


#1/22/24 refresher:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, path):
            if i >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)

        res = []
        dfs(0, [])
        return res


#2/6/24 practice:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def find(nums, path, i):
            if i >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            find(nums, path, i + 1)
            path.pop()
            find(nums, path, i + 1)
            
        res = []
        find(nums, [], 0)
        return res

#2/15/24:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(i, path):
            if i >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            f(i + 1, path)
            path.pop()
            f(i + 1, path)
        
        res = []
        f(0, [])
        return res

#2/26/24:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(i, path, nums):
            if i >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            f(i + 1, path, nums)
            path.pop()
            f(i + 1, path, nums)


        res = []
        f(0, [], nums)
        return res

#3/4/24:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(i, path):
            if i >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            f(i + 1, path)
            path.pop()
            f(i + 1, path)

                
        res = []
        f(0, [])
        return res


#3/9/24:


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #input array has only unique elements
        def dfs(i, path):
            if i >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)
        res = []
        dfs(0, [])
        return res
