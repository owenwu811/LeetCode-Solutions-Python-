
#2958
#medium

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


#my own solution using python3 on 3/25/25:

#use a sortedlist to keep track of the max frequency at any point to avoid tle

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        d = defaultdict(int)
        l = 0
        s = SortedList()
        for r in range(len(nums)):
            d[nums[r]] += 1
            s.add(d[nums[r]])
            while s[-1] > k and l <= r:
                s.remove(d[nums[l]])
                #4 > 3
                d[nums[l]] -= 1
                s.add(d[nums[l]])
                
                if d[nums[l]] == 0:
                    if 0 in s:
                        s.remove(0)
                    del d[nums[l]]
                l += 1
            if s[-1] <= k:
                res = max(res, r - l + 1)
        return res
