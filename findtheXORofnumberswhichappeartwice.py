
#3158
#easy


#You are given an array nums, where each number in the array appears either once or twice.

#Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.

 

#Example 1:

#Input: nums = [1,2,1,3]

#Output: 1

#Explanation:

#The only number that appears twice in nums is 1.


#my own solution using python3:

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = []
        for n in nums:
            if nums.count(n) == 2:
                res.append(n)
        myset = set()
        for r in res:
            myset.add(r)
        new = []
        for s in myset:
            new.append(s)
        if new:
            cur = new[0]
            for i in range(1, len(new)):
                cur = cur ^ new[i]
            return cur
        else:
            return 0
