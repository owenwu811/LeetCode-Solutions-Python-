
#922
#easy

#Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

#Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

#Return any answer array that satisfies this condition.

 

#Example 1:

#Input: nums = [4,2,5,7]
#Output: [4,5,2,7]
#Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#Example 2:

#Input: nums = [2,3]
#Output: [2,3]


#my own solution using python3:

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for i, n in enumerate(nums):
            if n % 2 == 0:
                even.append([i, n])
            else:
                odd.append([i, n])
        print(even)
        print(odd)
        new = []
        for i, e in enumerate(even):
            new.append(e[1])
            new.append(odd[i][1])

        print(new)
        return new
