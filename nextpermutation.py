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

#1. find pivot (go from right to left to find point where stops increasing, so 1 4 5 | 8 7 - 8 is the point where stops increasing, so 5 is the pivot 
#2. swap with the 1st number to the right of the pivot (swap 5 with 7)
#3. now we have 1 4 7 | 8 5, so we want to reverse the 2nd half for 1 4 7 8 5 to become 1 4 7 5 8


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, n = -1, len(nums)
        for i in range(n - 2, -1, -1): #start from 2nd to last element
            if nums[i] >= nums[i + 1]: #we start from 2nd to last element to ensure we can actually do the nums[i + 1] part
                continue #haven't found breakpoint yet
            bpoint = i #found bpoint
            for j in range(n - 1, i, -1): #iterate from the last element down one step not including the breakpoint
                if nums[j] > nums[bpoint]:
                    nums[j], nums[bpoint] = nums[bpoint], nums[j] #we only do the swap once, so break 
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])


#solution with better comments:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Initialize the breakpoint index to -1
        bPoint, n = -1, len(nums)
        
        # Step 1: Find the longest non-increasing suffix
        for i in range(n-2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue  # Skip the non-increasing sequence
            bPoint = i  # Found the breakpoint
            # Step 2: Find the rightmost successor to the pivot in the suffix
            for j in range(n-1, i, -1):
                if nums[j] > nums[bPoint]:
                    # Step 3: Swap the pivot with the successor
                    nums[j], nums[bPoint] = nums[bPoint], nums[j]
                    break  # Swap done, break the inner loop
            break  # Breakpoint found and swap done, break the outer loop
        
        # Step 4: Reverse the suffix to get the next permutation
        nums[bPoint + 1:] = reversed(nums[bPoint + 1:])

#5/30/24 review:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, n = -1, len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            bpoint = i
            for j in range(n - 1, i, -1):
                if nums[j] > nums[bpoint]:
                    nums[bpoint], nums[j] = nums[j], nums[bpoint]
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])

#5/30/24 review (missed in afternoon):

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        #14587 = test case
        bpoint, inputlen = -1, len(nums) #inputlen = 5
        for i in range(inputlen - 2, -1, -1):
            if nums[i] >= nums[i + 1]: #nums[3] >= nums[4] > 14587
                continue
            bpoint = i #2
            for j in range(inputlen - 1, i, -1):
                if nums[j] > nums[bpoint]: #inputlen = 5, so j starts at 4, so nums[4] > nums[2] - 7 > 5 - Yes
                    nums[j], nums[bpoint] = nums[bpoint], nums[j] #14587 becomes 14785
                    break
            break
        #14785
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:]) #14785 becomes 14758

#5/31/24 review morning of:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, inputlen = -1, len(nums)
        for i in range(inputlen - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            bpoint = i
            for j in range(inputlen - 1, i, -1):
                if nums[j] > nums[bpoint]:
                    nums[bpoint], nums[j] = nums[j], nums[bpoint]
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])


#6/1/24 review:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, inputlen = -1, len(nums)
        for i in range(inputlen - 2, -1, -1):
            if nums[i] >= nums[i + 1]: #nums[i + 1], not nums[i - 1]!
                continue
            bpoint = i
            for j in range(inputlen - 1, i, -1):
                if nums[j] > nums[bpoint]:
                    nums[bpoint], nums[j] = nums[j], nums[bpoint]
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])

#6/2/24 review:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, inputlen = -1, len(nums)
        for i in range(inputlen - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            bpoint = i
            for j in range(inputlen - 1, i, -1):
                if nums[j] > nums[bpoint]:
                    nums[bpoint], nums[j] = nums[j], nums[bpoint]
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])
        
#6/14/24 review (missed yesterday):

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, inputlen = -1, len(nums)
        for i in range(inputlen - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            bpoint = i
            for j in range(inputlen - 1, i, -1):
                if nums[j] > nums[bpoint]:
                    nums[bpoint], nums[j] = nums[j], nums[bpoint]
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])

#6/16/24 refresher:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, inputlen = -1, len(nums)
        for i in range(inputlen - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            bpoint = i
            for j in range(inputlen - 1, i, -1):
                if nums[j] > nums[bpoint]:
                    nums[j], nums[bpoint] = nums[bpoint], nums[j]
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])
         

#6/22/24 review:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, inputlen = -1, len(nums)
        for i in range(inputlen -2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            bpoint = i
            for j in range(inputlen - 1, i, -1):
                if nums[j] > nums[bpoint]:
                    nums[j], nums[bpoint] = nums[bpoint], nums[j]
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])


#missed on 7/17/24:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bpoint, inputlen = -1, len(nums)
        for i in range(len(nums) -2, -1, -1): #start from 2nd to last number to compare adjacent pairs one to the right
            if nums[i] >= nums[i + 1]:
                continue #haven't found smaller to right one adjacent pair
            bpoint = i #did find smaller to right one adjacent pair
            for j in range(len(nums) - 1, i, -1): #start from end of array because we will reverse from bpoint + 1 to the end, we want to get the largest in the place to the left and then the smallest number to the current place
                if nums[j] > nums[bpoint]:
                    nums[bpoint], nums[j] = nums[j], nums[bpoint] #14587 becomes 14785, so we've swapped the next biggest place ONCE since we want the smallest after that place, so we can break
                    break
            break
        #don't return anything
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:]) #14785 becomes 14758 #the smallest of the very next biggest number from input

#7/20/24 refresher:

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        #14587 > 14785 > 14758
        bpoint, inputlen = -1, len(nums)
        for i in range(inputlen - 2, -1, -1):
            if nums[i] >= nums[i + 1]: #we only want to compare adjacent pairs to see if we hit breakpoint
                continue
            bpoint = i
            for j in range(inputlen -1, i, -1):
                if nums[j] > nums[bpoint]:
                    nums[bpoint], nums[j] = nums[j], nums[bpoint]
                    break
            break
        nums[bpoint + 1:] = reversed(nums[bpoint + 1:])
        
        


