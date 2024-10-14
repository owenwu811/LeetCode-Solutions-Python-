#2295
#medium


#You are given a 0-indexed array nums that consists of n distinct positive integers. Apply m operations to this array, where in the ith operation you replace the number operations[i][0] with operations[i][1].

#It is guaranteed that in the ith operation:

#operations[i][0] exists in nums.
#operations[i][1] does not exist in nums.
#Return the array obtained after applying all the operations.





#correct python3 solution:

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            d[n] = i
        for o in operations:
            idx = d[o[0]]
            nums[idx] = o[1]
            d[o[1]] = idx
        return nums


#my TLE 79/80 solution:

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = i #we know all elements are unique
        for o in operations:
            if o[0] in nums:
                nums[d[o[0]]] = o[1]
                d[o[1]] = d[o[0]]
        return nums
