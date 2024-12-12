#1437
#easy

#Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

#Input: nums = [1,0,0,0,1,0,0,1], k = 2
#Output: true
#Explanation: Each of the 1s are at least 2 places away from each other.


#my own solution using python3:

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        onesindex = []
        for i, n in enumerate(nums):
            if n == 1:
                onesindex.append(i)
        print(onesindex)
        for i in range(1, len(onesindex)):
            if (onesindex[i] - onesindex[i - 1]) - 1 < k:
                return False  
        return True
        
