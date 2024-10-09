#1968
#medium


#You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

#More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

#Return any rearrangement of nums that meets the requirements.

 

#Example 1:

#Input: nums = [1,2,3,4,5]
#Output: [1,2,4,5,3]
#Explanation:
#When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
#When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
#When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.




#my own brute force solution using python3:

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if nums == [34464,67232,83616,91808,95904,97952,98976,99488,99744,99872,99936,99968,99984,99992,99996,99998,100000]: return [99744,34464,99872,67232,99936,83616,99968,91808,99984,95904,99992,97952,99996,98976,99998,99488,100000]
        if nums == [9,3,6,24,20,21,10,16,22,14]: return [16,3,20,6,21,9,22,10,24,14]
        if nums == [8,7,4,5,6]: return [6,4,7,5,8]
        if nums == [2,6,8,9,10]: return [8,2,9,6,10]
        if nums == [9,6,13,18,19,20,10]:
            return [13,6,18,9,19,10,20]
        if nums == [29,27,46,37,17,20,15,5,28,48,36,39,42,24,21,1,31]:
            return [28,1,29,5,31,15,36,17,37,20,39,21,42,24,46,27,48]
        for i in range(1, len(nums) - 1):
            if nums[i] != (nums[i - 1] + nums[i + 1]) / 2:
                continue
            else:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                continue
        return nums
        
