
#47
#medium


#Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

#Example 1:

#Input: nums = [1,1,2]
#Output:
#[[1,1,2],
# [1,2,1],
# [2,1,1]]
#Example 2:

#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


#my own solution using python3:

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        myset = set()
        for a in permutations(nums):
            myset.add(a)
        print(myset)
        res = []
        for s in myset:
            res.append(list(s))
        return res
