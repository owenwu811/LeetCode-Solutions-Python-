
#1524
#medium

#Given an array of integers arr, return the number of subarrays with an odd sum.

#Since the answer can be very large, return it modulo 109 + 7.

 

#Example 1:

#Input: arr = [1,3,5]
#Output: 4
#Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
#All sub-arrays sum are [1,4,9,3,8,5].
#Odd sums are [1,9,3,5] so the answer is 4.


#the correct python3 solution (could not solve by myself):

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        even = 1 #initialized to 1 because a sum of zero(before any elements are added) is considered even
        odd = 0 #no odd sums have been added yet
        rsum = 0
        for a in arr:
            rsum += a 
            if rsum % 2 == 1: #odd
                res += even #All previous cumulative sums that were even can form subarrays ending at this element with an odd sum. So, add the count of even to res.
                odd += 1 #increment odd because rsum is now odd - remember than odd started at 0
            else:
                res += odd #all previous cumulative sums that were odd can form subarrays ending at this element with an even sum
                even += 1 #increment even because rsum is now even
        return ans % ((10 ** 9) + 7)
            
