


#1743
#medium

#There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

#You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

#It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

#Return the original array nums. If there are multiple solutions, return any of them.

 

#Example 1:

#Input: adjacentPairs = [[2,1],[3,4],[3,2]]
#Output: [1,2,3,4]
#Explanation: This array has all its adjacent pairs in adjacentPairs.
#Notice that adjacentPairs[i] may not be in left-to-right order.


#my own solution using python3:

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for a in adjacentPairs:
            d[a[0]].append(a[1])
            d[a[1]].append(a[0])
        print(d)
        tmp = []
        corners = []
        for k in d:
            if len(d[k]) == 1:
                corners.append(k)
            else:
                cur = []
                cur.append(k)
                for a in d[k]:
                    cur.append(a)
                tmp.append(cur)
        ans = []
        mid = []
        q = deque()
        seen = set()
        for c in corners:
            q.append(c)
            seen.add(c)
        while q:
            cur = q.pop() 
            ans.append(cur)
            for nei in d[cur]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
        return ans[::-1]
       
