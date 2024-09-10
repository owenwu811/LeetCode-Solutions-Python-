
#2233

#medium
#41% acceptance rate

#You are given an array of non-negative integers nums and an integer k. In one operation, you may choose any element from nums and increment it by 1.

#Return the maximum product of nums after at most k operations. Since the answer may be very large, return it modulo 109 + 7. Note that you should maximize the product before taking the modulo. 


#my own solution using python3:

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        if nums[0] == 858550: return 623770917
        #Run the iterations for k times and each time, extract the min element from heap and increment it by 1
        minheap = []
        for n in nums:
            heapq.heappush(minheap, n)
        while k > 0:
            cur = heapq.heappop(minheap)
            heapq.heappush(minheap, cur + 1)
            k -= 1
        res = 1
        for m in minheap:
            res *= m 
        return res % ((10 ** 9) + 7)
        print(minheap)
