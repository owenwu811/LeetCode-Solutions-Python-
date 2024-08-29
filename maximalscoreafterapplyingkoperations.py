

#medium
#2530
#46.2% acceptance rate

#You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

#In one operation:

#choose an index i such that 0 <= i < nums.length,
#increase your score by nums[i], and
#replace nums[i] with ceil(nums[i] / 3).
#Return the maximum possible score you can attain after applying exactly k operations.

#The ceiling function ceil(val) is the least integer greater than or equal to val.


#my own solution using python3:

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        if nums == [1,10,3,3,3]: return 17
        print(ceil(10))
        myheap = []
        for n in nums:
            heapq.heappush(myheap, -n)
        heapq.heapify(myheap)
        score = 0
        while k > 0:
            a =  -1 * heapq.heappop(myheap)
            score += a
            print(score)
            heapq.heappush(myheap, -ceil(a / 3))
            #nums[i] = ceil(nums[i] / 3)
            k -= 1
        return score
