#2113
#medium

#You are given a 0-indexed integer array nums. Initially on minute 0, the array is unchanged. Every minute, the leftmost element in nums is removed until no elements remain. Then, every minute, one element is appended to the end of nums, in the order they were removed in, until the original array is restored. This process repeats indefinitely.

#For example, the array [0,1,2] would change as follows: [0,1,2] → [1,2] → [2] → [] → [0] → [0,1] → [0,1,2] → [1,2] → [2] → [] → [0] → [0,1] → [0,1,2] → ...
#You are also given a 2D integer array queries of size n where queries[j] = [timej, indexj]. The answer to the jth query is:

#nums[indexj] if indexj < nums.length at minute timej
#-1 if indexj >= nums.length at minute timej
#Return an integer array ans of size n where ans[j] is the answer to the jth query.

 

#Example 1:

#Input: nums = [0,1,2], queries = [[0,2],[2,0],[3,2],[5,0]]
#Output: [2,2,-1,0]
#Explanation:
#Minute 0: [0,1,2] - All elements are in the nums.
#Minute 1: [1,2]   - The leftmost element, 0, is removed.
#Minute 2: [2]     - The leftmost element, 1, is removed.
#Minute 3: []      - The leftmost element, 2, is removed.
#Minute 4: [0]     - 0 is added to the end of nums.
#Minute 5: [0,1]   - 1 is added to the end of nums.


#my own solution using python3:

class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        #[residx, resvalue]
        flatten = set()
        for q in queries:
            flatten.add(q[0])
            flatten.add(q[1])
        for n in nums:
            flatten.add(n)
        print(flatten)
        new = []
        for i in range(0, max(flatten) + 1):
            new.append(i)
        modify = deque(nums.copy())
        #print(modify)
        helper = deque()
        flag = False
        d = dict()
        for i in range(len(new)):
            #if new[i] <= len(queries):
            d[new[i]] = modify.copy()
            if modify and not flag:
                a = modify.popleft() 
                helper.append(a)    
            elif len(modify) >= len(nums):
                a = modify.popleft() 
                helper.append(a)
                flag = False
            elif len(modify) < len(nums):
                flag = True
                modify.append(helper.popleft())
            #print(modify, helper, flag)
        res = []
        for q in queries:
            minute = q[0]
            idx = q[1]
            if idx < len(d[minute]):
                res.append(d[minute][idx])
            else:
                res.append(-1)
        return res
