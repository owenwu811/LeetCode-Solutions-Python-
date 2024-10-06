
#3264
#easy

#You are given an integer array nums, an integer k, and an integer multiplier.

#You need to perform k operations on nums. In each operation:

#Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
#Replace the selected minimum value x with x * multiplier.
#Return an integer array denoting the final state of nums after performing all k operations.

 

#Example 1:

#Input: nums = [2,1,3,5,6], k = 5, multiplier = 2

#Output: [8,4,6,5,6]


#my own solution using python3:

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        myheap = []
        res = []
        for i, n in enumerate(nums):
            heapq.heappush(myheap, [n, i])
        print(myheap)
        while k > 0:
            val, i = heapq.heappop(myheap)
            heapq.heappush(myheap, [val * multiplier, i])
            k -= 1
        print(myheap)
        print(res)
        myheap.sort(key=lambda a: a[1])
        print(myheap)
        for h in myheap:
            res.append(h[0])
        return res
