
#You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

#Return the string that represents the kth largest integer in nums.

#Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

#acceptancerate45.7%
#companies
#medium

#Example 1:

#Input: nums = ["3","6","7","10"], k = 4
#Output: "3"
#Explanation:
#The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
#The 4th largest integer in nums is "3".

#my own solution in python3:

#you can simply use the same minheap pattern as with lots of other problems that involve finding the kth largest or smallest or some element and then just turn the result back into a string

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minheap = []
        for n in nums:
            heapq.heappush(minheap, -int(n)) #you know that minheap in python means the smallest number will be at the top of the heap 
        res = 0
        while k > 0: #pop k times 
            a = heapq.heappop(minheap)
            res = a
            k -= 1
        return str(abs(res)) #convert the negative back into a positive and then into a string
