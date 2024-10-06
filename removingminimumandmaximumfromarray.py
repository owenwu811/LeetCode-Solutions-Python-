
#2091
#medium


#You are given a 0-indexed array of distinct integers nums.

#There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.

#A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

#Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

#Input: nums = [2,10,7,5,4,1,8,6]
#Output: 5
#Explanation: 
#The minimum element in the array is nums[5], which is 1.
#The maximum element in the array is nums[1], which is 10.
#We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
#This results in 2 + 3 = 5 deletions, which is the minimum number possible.


#my own solution using python3:

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 2
        minn, maxn = min(nums), max(nums)
        tmp = []
        for i, j in enumerate(nums):
            if j == minn:
                tmp.append(i)
            if j == maxn:
                tmp.append(i)
        print(tmp)
        a = 0
        for i, j in enumerate(nums):
            if i == tmp[1]:
                print(i)
                a += (i + 1)
        b = 0
        for i in range(len(nums) -1, -1, -1):
            if i == tmp[0]:
                print(i)
                b += (len(nums) - abs(i))
        h = len(nums) 
        print(h)
        c = (tmp[0] + 1) + (h - tmp[1])
        print(a, b, c)
        return min(a, b, c)
