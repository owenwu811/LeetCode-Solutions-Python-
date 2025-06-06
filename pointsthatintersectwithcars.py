
#2848
#easy

#You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

#Return the number of integer points on the line that are covered with any part of a car.

 

#Example 1:

#Input: nums = [[3,6],[1,5],[4,7]]
#Output: 7
#Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.
#Example 2:

#Input: nums = [[1,3],[5,8]]
#Output: 7
#Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.

#my own solution using python3:

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        print(nums)
        tmp = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                tmp.append(nums[i][j])
        tmp.sort()
        smallest, largest = min(tmp), max(tmp)
        new = []
        for i in range(smallest, largest + 1):
            new.append(i)
        print(tmp)
        tmp = new
        res = 0
        for t in tmp:
            flag = False
            for n in nums:
                if t >= n[0] and t <= n[1]:
                    flag = True
            if flag:
                res += 1
        return res
