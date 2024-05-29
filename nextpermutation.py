#A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

#For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
#The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

#For example, the next permutation of arr = [1,2,3] is [1,3,2].
#Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
#Given an array of integers nums, find the next permutation of nums.

#The replacement must be in place and use only constant extra memory.

#Example 1:

#Input: nums = [1,2,3]
#Output: [1,3,2]

#Example 2:
#Input: nums = [3,2,1]
#Output: [1,2,3]

#Example 3:
#Input: nums = [1,1,5]
#Output: [1,5,1]



#python3 solution:

#basically, next permutation just means next largest number we can get by rearranging the numbers, so if 14587 was our input, 14758 is the next larger number we can get!

#[3, 2, 1] > if the input is sorted in descending order from left to right, then just return the reverse of the input as the anwser 


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, n = -1, len(nums)
        for i in range(n - 2, -1, -1): #start from 2nd to last element
            if nums[i] >= nums[i + 1]:
                continue #haven't found breakpoint yet
            bpoint = i #found bpoint
            for j in range(n - 1, i, -1): #iterate from the last element down one step not including the breakpoint
                if nums[j] > nums[bpoint]:
                    nums[j], nums[bpoint] = nums[bpoint], nums[j] #we only do the swap once, so break 
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])


