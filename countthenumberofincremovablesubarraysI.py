#2970
#easy

#You are given a 0-indexed array of positive integers nums.

#A subarray of nums is called incremovable if nums becomes strictly increasing on removing the subarray. For example, the subarray [3, 4] is an incremovable subarray of [5, 3, 4, 6, 7] because removing this subarray changes the array [5, 3, 4, 6, 7] to [5, 6, 7] which is strictly increasing.

#Return the total number of incremovable subarrays of nums.

#Note that an empty array is considered strictly increasing.

#A subarray is a contiguous non-empty sequence of elements within an array.

 

#Example 1:

#Input: nums = [1,2,3,4]
#Output: 10
#Explanation: The 10 incremovable subarrays are: [1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4], and [1,2,3,4], because on removing any one of these subarrays nums becomes strictly increasing. Note that you cannot select an empty subarray.


#my own solution using python3:

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subarr = nums[i: j + 1]
                new = nums[:i] + nums[j + 1:]
                if new == sorted(new):
                    if len(new) < 2:
                        res.append(subarr)
                    else:
                        if new[0] < new[-1] and len(set(new)) >= len(new):
                            res.append(subarr)
        print(res)
        return len(res)
