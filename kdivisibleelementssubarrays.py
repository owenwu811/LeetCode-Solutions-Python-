
#2261

#Given an integer array nums and two integers k and p, return the number of distinct subarrays, which have at most k elements that are divisible by p.

#Two arrays nums1 and nums2 are said to be distinct if:

#They are of different lengths, or
#There exists at least one index i where nums1[i] != nums2[i].
#A subarray is defined as a non-empty contiguous sequence of elements in an array.


#correct python3 solution:

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        #nums = [1, 2, 3, 4], k = 1, p = 2
        seen = set()
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0: #[1, 2, 3, 4] - nums[j] is 1, 2, 3, 4
                    cnt += 1
                if cnt > k: #cnt is the length of the current subarray that must not be bigger than k. if it is, break and go back to i for loop
                    break
                seen.add(tuple(nums[i: j + 1])) #[1], [1, 2], [1, 2, 3]
        return len(seen)
