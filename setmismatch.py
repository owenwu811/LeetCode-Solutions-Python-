
#You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

#You are given an integer array nums representing the data status of this set after the error.

#Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

#Example 1:

#Input: nums = [1,2,2,4]
#Output: [2,3]
#Example 2:

#Input: nums = [1,1]
#Output: [1,2]


#python3 solution:

#this is cyclic sort

#this question is identical to "find the corrupt pair" from the grokking course


#idea is to place each number in it's correct position during cyclic sort. intialize i to 0 and iterate over the array. while traversing, we perform the steps:
#the variable correct is calculated as nums[i] - 1, representing the index where the current number should be placed if the array were sorted
#if the current number, nums[i], is not equal to number at correct position, nums[correct], a swap is performed using the swap function to move the current number to its correct position
#if the numbers are already in their correct positions, i is incremented to move to the next element
#second steps is to traverse the array and detect the number that is not at its correct index. this will be the duplicated number. when we add 1 to that index, the resulting value will be our missing number
#third step: return the pair containing the missing and duplicated numbers (backwards for this problem)

#[3, 1, 2, 5, 2]
#we found that 3 isn't at its correct position, so we can swap it with the element at index 2
#[2, 1, 3, 5, 2]
#we've placed 3 at its correct position, but we need to check if the swapped element 2 is now in its correct position
#we found that 2 is not at its correct position, so we can swap it with the element at index 1
#[1, 2, 3, 5, 2]
#we've placed 2 at its correct position, but we need to check if the swapped element 1 is now at its correct position
#since 1 is already at its correct position, we can traverse the array until we find a number that is not
#[1, 2, 3, 5, 2]
#we found that 5 is not at its correct position, so we can swap it with the element at index 4
#[1, 2, 3, 2, 5]
#we've placed 5 at its correct position, but we need to check if the swapped element 2 is now at its correct position
#now, the number 2 is present at index 3 is at incorrect position. 2 also exists at a correct position in the array, so we identified this as the duplicate number. we can conclude that the index that contains the incorrect number should have held the missing number and can be calculated by index + 1
#the missing number is calculated as index + 1(3 + 1) is 4 and the duplicate number present is 2.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing = None
        duplicated = None
        def swap(arr, first, second): #function for swapping
            arr[first], arr[second] = arr[second], arr[first]
        #apply cyclic sort on the array
        i = 0
        #traversing the whole array
        while i < len(nums):
            #determining what position the specific element should be at
            correct = nums[i] - 1
           #check if the number is at wrong position
            if nums[i] != nums[correct]:
                #swapping the number to its correct position
                swap(nums, i, correct)
            else:
                i += 1
        #finding the corrupt pair (missing, duplicated)
        for j in range(len(nums)):
            if nums[j] != j + 1:
                duplicated = nums[j]
                missing = j + 1
        return [duplicated, missing]
            
