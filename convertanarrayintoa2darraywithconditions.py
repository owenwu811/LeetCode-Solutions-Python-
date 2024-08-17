#medium
#acceptancerate87.2%
#2610

#You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

#The 2D array should contain only the elements of the array nums.
#Each row in the 2D array contains distinct integers.
#The number of rows in the 2D array should be minimal.
#Return the resulting array. If there are multiple answers, return any of them.

#Note that the 2D array can have a different number of elements on each row.

 

#Example 1:

#Input: nums = [1,3,4,1,2,3,1]
#Output: [[1,3,4,2],[1,3],[1]]
#Explanation: We can create a 2D array that contains the following rows:
#- 1,3,4,2
#- 1,3
#- 1
#All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
#It can be shown that we cannot have less than 3 rows in a valid array.


#my own solutiong using python3:


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        if len(set(nums)) == len(nums): return [nums]
        res = []
        cur = []
        while nums:
            cur = set(nums)
            curlst = []
            for n in cur:
                curlst.append(n)
                nums.remove(n)
            res.append(curlst)
            print(res)
        return res
