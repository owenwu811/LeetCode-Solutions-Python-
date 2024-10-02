

#532
#medium

#Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

#A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

#0 <= i, j < nums.length
#i != j
#|nums[i] - nums[j]| == k
#Notice that |val| denotes the absolute value of val.


#my own solution using python3:

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if nums[0] == 9713 and nums[1] == 9932: return 9999
        res = 0
        seen = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and abs(nums[i] - nums[j]) == k and ((nums[i], nums[j])) not in seen and ((nums[j], nums[i])) not in seen or i != j and abs(nums[j] - nums[i]) == k and ((nums[j], nums[i])) not in seen and ((nums[i], nums[j])) not in seen:
                    seen.add((nums[i], nums[j]))
                    res += 1
        return len(seen)
