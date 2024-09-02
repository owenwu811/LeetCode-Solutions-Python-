
#2656
#easy


#You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly k times in order to maximize your score:

#Select an element m from nums.
#Remove the selected element m from the array.
#Add a new element with a value of m + 1 to the array.
#Increase your score by m.
#Return the maximum score you can achieve after performing the operation exactly k times.

#my own solution using python3:

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = []
        while k > 0:
            m = nums.pop()
            res.append(m)
            nums.append(m + 1)
            print(nums)
            k -= 1
        return sum(res)
