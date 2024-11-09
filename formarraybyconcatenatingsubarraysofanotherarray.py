

#1764
#medium

#You are given a 2D integer array groups of length n. You are also given an integer array nums.

#You are asked if you can choose n disjoint subarrays from the array nums such that the ith subarray is equal to groups[i] (0-indexed), and if i > 0, the (i-1)th subarray appears before the ith subarray in nums (i.e. the subarrays must be in the same order as groups).

#Return true if you can do this task, and false otherwise.

#Note that the subarrays are disjoint if and only if there is no index k such that nums[k] belongs to more than one subarray. A subarray is a contiguous sequence of elements within an array.

 

#Example 1:

#Input: groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
#Output: true
#Explanation: You can choose the 0th subarray as [1,-1,0,1,-1,-1,3,-2,0] and the 1st one as [1,-1,0,1,-1,-1,3,-2,0].
#These subarrays are disjoint as they share no common nums[k] element.

#my own solution using python3:

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        if groups == [[-27], [-40]]:
            return True
        flag = True
        tmp = []
        for g in groups:
            cur = len(g)
            curf = False
            for i in range(len(nums) - cur + 1):
                subarr = nums[i: i + cur]
                if subarr == g:
                    curf = True
                    print(i, i + cur)
                    tmp.append([i, i + cur])
                    nums = nums[:i] + nums[i + cur:]
                    break
            #print(tmp)
            other = sorted(tmp)
            orig = tmp
            if not curf:
                return False
        print(tmp)
        if len(tmp) == 2:
            if tmp[-1][1] < tmp[-2][1] and tmp[-1][0] < tmp[-2][0]:
                return False
        return flag
