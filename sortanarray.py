
#Given an array of integers nums, sort the array in ascending order and return it.

#You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

#Input: nums = [5,2,3,1]
#Output: [1,2,3,5]
#Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

#python3 solution using quicksort:

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quicksort(nums)
    def quicksort(self, nums):
        if len(nums) <= 1: #base case where input array only has only element, so it's already sorted
            return nums
        r = random.choice(nums) #chooses a random number from nums as the pivot point 
        smaller, equal, larger = [], [], []
        for n in nums:
            if n < r:
                smaller.append(n)
            elif n > r:
                larger.append(n)
            else:
                equal.append(n)
        return self.quicksort(smaller) + equal + self.quicksort(larger) #we have to keep sorting within the smaller and larger buckets until we hit the base case and we only have one element left
