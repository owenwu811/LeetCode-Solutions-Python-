#You are given a 0-indexed integer array nums and an integer k.

#A subarray is called equal if all of its elements are equal. Note that the empty subarray is an equal subarray.

#Return the length of the longest possible equal subarray after deleting at most k elements from nums.

#A subarray is a contiguous, possibly empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [1,3,2,3,1,3], k = 3
#Output: 3
#Explanation: It's optimal to delete the elements at index 2 and index 4.
#After deleting them, nums becomes equal to [1, 3, 3, 3].
#The longest equal subarray starts at i = 1 and ends at j = 3 with length equal to 3.
#It can be proven that no longer equal subarrays can be created.



#my own solution in python3:

#extremely similar to longest repeating character replacement

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        freq = {}
        lengthoflongest, ws, mostfrequent = 0, 0, 0
        for we in range(len(nums)):
            if nums[we] not in freq:
                freq[nums[we]] = 0
            freq[nums[we]] += 1
            mostfrequent = max(mostfrequent, freq[nums[we]])
            if (we - ws + 1) - mostfrequent > k:
                freq[nums[ws]] -= 1
                ws += 1
        return mostfrequent
