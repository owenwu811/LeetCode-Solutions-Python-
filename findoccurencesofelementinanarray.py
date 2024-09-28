
#3159
#medium



#You are given an integer array nums, an integer array queries, and an integer x.

#For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array. If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.

#Return an integer array answer containing the answers to all queries.




#my own solution using python3 after getting a tiny trick about putting the nums.count(x) outside the loop:

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        res = [-1] * len(queries)
        indexarr = []
        if x not in nums:
            return res
        k = nums.count(x)
        c = Counter(nums)
        print(c)
        for i, n in enumerate(nums):
            if n == x:
                indexarr.append(i)
        for i in range(len(queries)):
            if k < queries[i]:
                continue
            res[i] = indexarr[queries[i] - 1] 
        return res
             
