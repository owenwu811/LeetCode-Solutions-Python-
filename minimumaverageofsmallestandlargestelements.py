#easy
#3194


#You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

#You repeat the following procedure n / 2 times:

#Remove the smallest element, minElement, and the largest element maxElement, from nums.
#Add (minElement + maxElement) / 2 to averages.
#Return the minimum element in averages.



#my own solution using python3:

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        k = len(nums)
        half = k // 2
        while k > half:
            a = min(nums)
            b = max(nums)
            averages.append((a + b) / 2)
            nums.remove(a)
            nums.remove(b)
            k -= 1
        return min(averages)
