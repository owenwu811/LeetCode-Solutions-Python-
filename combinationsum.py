
#Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

#The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
#frequency
# of at least one of the chosen numbers is different.

#The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

#Example 1:

#Input: candidates = [2,3,6,7], target = 7
#Output: [[2,2,3],[7]]
#Explanation:
#2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#7 is a candidate, and 7 = 7.
#These are the only two combinations.


#python3 solution:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def f(index, sublist, sublisttotal):
            if sublisttotal == target: 
                res.append(sublist.copy()) #we don't want to mess up result's copy of sublist, so we make a copy just for it because we will add to sublist 
                return
            elif index >= len(candidates) or sublisttotal > target: #if we are out of bounds or the value of our sublist is bigger than target
                return
            sublist.append(candidates[index]) 
            f(index, sublist, sublisttotal + candidates[index]) #recursive call that leads to adding the same element again = [2, 2, 2, 2]
            sublist.pop() #note that the sublisttotal value from the above recursive call is SEPERATE AND LIVES ONLY IN THAT RECURSIVE CALL 
            #recursive call that leads to adding a different element by moving i to the right - [2, 2, 3] because we kept popping [2, 2, 2, 2] until the sum became < 7 - [2, 2], and then we will call f(index + 1...) which will lead to sublist.append(candidates[index]), which is adding the 3 to [2, 2, 3]
            f(index + 1, sublist, sublisttotal) #sublisttotal is equal to sublist + candidates[index] and then popped meaning the absence of adding the value of candidates[index]
        f(0, [], 0)
        return res
        

#12/29/23 refresher: 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def f(index, sublist, sublistsum):
            if sublistsum == target:
                res.append(sublist.copy())
                return
            elif index >= len(candidates) or sublistsum > target:
                return
            sublist.append(candidates[index])
            f(index, sublist, sublistsum + candidates[index])
            #from [2, 2, 2, 2] to [2, 2, 2] because 2222 is 8, which is bigger than 7
            sublist.pop()
            #from [2, 2, 2] to [2, 2, 2, 3]
            f(index + 1, sublist, sublistsum)
        f(0, [], 0)
        return res


#1/1/24 refresher:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def f(index, ans, windowsum):
            if windowsum == target:
                res.append(ans.copy())
                return
            elif index >= len(candidates) or windowsum > target:
                return
            ans.append(candidates[index])
            f(index, ans, windowsum + candidates[index])
            ans.pop()
            #223 now instead of 222 from 22 backtracked because we need to explore a new path instead of the same path again, which would lead to infinite recursion because it would be bigger than target as 2 + 2 + 2 + 2 = 8, which is bigger than our target of 7
            f(index + 1, ans, windowsum)
        f(0, [], 0)
        return res

#1/3/24 refresher:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def f(index, ans, windowsum):
            if windowsum == target:
                res.append(ans.copy())
                return
            if index >= len(candidates) or windowsum > target:
                return
            ans.append(candidates[index])
            f(index, ans, windowsum + candidates[index])
            ans.pop()
            f(index + 1, ans, windowsum)

        res = []
        f(0, [], 0)
        return res


#1/7/24 my refresher solution with my explanation:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, ans, sublistsum):
            if sublistsum == target:
                res.append(ans.copy())
                return
            elif index >= len(candidates) or sublistsum > target:
                return
            ans.append(candidates[index])
            #the same number can be chosen an uliminted number of times for this problem, not subsets, so index is acceptable
            dfs(index, ans, sublistsum + candidates[index])
            ans.pop()
            #the absence of adding candidates[index] has the same affect on the sublistsum integer as popping from the end of the list
            #we've reached a dead end - 2222 > 7, so we have to pop - 222 and then try maybe 2223 - eventually, we will find that we need to pop again from 222 to 22 and add 223, which will trigger this below line - dfs(index + 1, ans, sublistsum + candidates[index]) because 3 is an index to the right of 2 in our candidates input array
            dfs(index + 1, ans, sublistsum)

        res = []
        dfs(0, [], 0)
        return res


#1/12/24 refresher:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(index, ans, windowsum):
            if windowsum == target:
                res.append(ans.copy())
                return
            elif index >= len(candidates) or windowsum > target:
                return
            ans.append(candidates[index])
            func(index, ans, windowsum + candidates[index])
            ans.pop()
            func(index + 1, ans, windowsum)
        res = []
        func(0, [], 0)
        return res


#1/17/24 refresher(made a mistake with index >= len(candidates) - 1 instead of index >= len(candidates) - using -1 would stop trying before trying the last element 7 in the array, which is why the output returned just 223 without 7:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(index, ans, windowsum):
            if windowsum == target:
                res.append(ans.copy())
                return
            #if we are trying to add a number that is out of bounds to the right - past 7. if 7 has already been tried in [2, 3, 6, 7]
            elif index >= len(candidates) or windowsum > target:
                return
            ans.append(candidates[index])
            dfs(index, ans, windowsum + candidates[index])
            ans.pop()
            dfs(index + 1, ans, windowsum)
        res = []
        dfs(0, [], 0)
        return res
