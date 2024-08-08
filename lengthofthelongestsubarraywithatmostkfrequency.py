
#You are given an integer array nums and an integer k.

#The frequency of an element x is the number of times it occurs in an array.

#An array is called good if the frequency of each element in this array is less than or equal to k.

#Return the length of the longest good subarray of nums.

#A subarray is a contiguous non-empty sequence of elements within an array.


#Example 1:

#Input: nums = [1,2,3,1,2,3,1,2], k = 2
#Output: 6
#Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
#It can be shown that there are no good subarrays with length more than 6.


#my own solution in python3:

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        lengthoflongest, ws, mostfrequent = 0, 0, 0
        for we in range(len(nums)):
            if nums[we] not in freq:
                freq[nums[we]] = 0
            freq[nums[we]] += 1
            while freq[nums[we]] > k: # we don't care about the mostfrequent here - this is the only difference with longest repeating character replacement solution!
                freq[nums[ws]] -= 1
                ws += 1
            lengthoflongest = max(lengthoflongest, we - ws + 1)

        return lengthoflongest
