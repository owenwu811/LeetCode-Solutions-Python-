
#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

#my solution in python3 using heap:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        mydict = Counter(nums)
        myheap = []
        for d in mydict:
            #we don't need to run heapify because heappush already enforces the heap invariant
            heapq.heappush(myheap, (-mydict[d], d)) #we know that python only has minheap, so the smaller a negative is, the bigger it's inverse will be, so if -3 is the smallest key in our dictionary, then we know 3 is the most frequent element
        while k > 0:
            freq, number = heapq.heappop(myheap)
            res.append(number)
            k -= 1
        return res
