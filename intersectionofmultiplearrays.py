
#2248
#easy


#Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

#Example 1:

#Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
#Output: [3,4]
#Explanation: 
#The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
#Example 2:

#Input: nums = [[1,2,3],[4,5,6]]
#Output: []
#Explanation: 
#There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].



#my own solution using python3:

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        tmp = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                tmp.append(nums[i][j])
        print(tmp)
        d = dict()
        m = set(tmp)
        for i in m:
            d[i] = 0
        print(d)
        res = []
        for k in d:
            cur = 0
            for n in nums:
                if k in n:
                    cur += 1
            print(cur)
            if cur == len(nums):
                res.append(k)
        res.sort()
        return res
