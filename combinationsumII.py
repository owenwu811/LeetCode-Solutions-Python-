
#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

#Each number in candidates may only be used once in the combination.

#Note: The solution set must not contain duplicate combinations.

#Input: candidates = [10,1,2,7,6,1,5], target = 8
#Output: 
#[
#[1,1,6],
#[1,2,5],
#[1,7],
#[2,6]
#]

#my wrong solution with memory limit exceeded, passing 172/176 test cases:

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target: return []
        candidates.sort()
        self.res = []
        def f(i, cur):
            if sum(cur) == target:
                self.res.append(cur.copy())
                return
            if i >= len(candidates) or sum(cur) > target:
                return
            cur.append(candidates[i])
            f(i + 1, cur)
            cur.pop()
            f(i + 1, cur)
        f(0, [])
# convert to tuples
# convert to tuples to remove duplicates from self.res
        tupled_lst = set(map(tuple, self.res))
        lst = map(list, tupled_lst)
        return lst


#python3 solution - correct answer:

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        def backtrack(start, cur, cur_sum):
            if cur_sum == target:
                self.res.append(cur.copy())
                return
            if cur_sum > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  # Skip duplicates
                cur.append(candidates[i])
                backtrack(i + 1, cur, cur_sum + candidates[i])
                cur.pop()
        
        backtrack(0, [], 0)
        return self.res
