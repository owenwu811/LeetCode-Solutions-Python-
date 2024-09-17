
#1887
#medium

#Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

#Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
#Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
#Reduce nums[i] to nextLargest.
#Return the number of operations to make all elements in nums equal.


#This solution works because it efficiently counts the number of reduction operations required to make all the elements of the nums list equal by following a greedy approach. Here's a step-by-step breakdown of how it works:

Problem Overview:
Given an array nums, you need to determine the minimum number of reduction operations required to make all elements equal. A reduction operation is defined as decreasing a larger element to the same value as any smaller element in the list.

Key Idea:
By sorting the array in descending order, the solution processes elements in decreasing value, ensuring that each operation targets the largest distinct element. Every time a reduction operation happens, all larger elements are reduced to the next largest value in the list.

Explanation of the Code:
Sorting the Array:
The array nums is sorted in descending order so that the largest elements come first.
This allows us to compare adjacent elements and count the number of operations needed to make a larger element equal to the next distinct smaller element.
Iterating Over the Array:
The loop goes from the first element (largest) to the second-to-last element.
For each adjacent pair, if the current element nums[i] is larger than nums[i + 1] (i.e., they are not the same), it means we need to "reduce" all previous elements (including this one) down to the smaller value nums[i + 1].
Counting the Operations:
If nums[i] > nums[i + 1], it means we need to perform i + 1 operations, since there are i + 1 elements before (and including) nums[i] that need to be reduced.
The res += (i + 1) statement counts these operations and adds them to the total result res.
Why the Loop Works:
At each step, we know that all previous elements (nums[0] to nums[i]) are larger than nums[i + 1], so reducing them to nums[i + 1] takes exactly i + 1 operations. The approach minimizes the number of operations by always reducing the largest values first.


#correct python3 solution - was unable to solve, so I need to review this one again:

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)  
        res = 0
        nums.sort(reverse=True)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]: #For each adjacent pair, if the current element nums[i] is larger than nums[i + 1] (i.e., they are not the same), it means we need to "reduce" all previous elements (including this one) down to the smaller value nums[i + 1].
                res += (i + 1)
        return res

