
#You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

#Every element less than pivot appears before every element greater than pivot.
#Every element equal to pivot appears in between the elements less than and greater than pivot.
#The relative order of the elements less than pivot and the elements greater than pivot is maintained.
#More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.
#Return nums after the rearrangement.

#Input: nums = [9,12,5,10,14,3,10], pivot = 10
#Output: [9,5,3,10,10,12,14]
#Explanation: 
#The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
#The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
#The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

#my own solution using python3:

#idea is to use 3 stacks to maintain the relative ordering of elements from the input - one for smaller elements than pivot, equal, and larger - and then join them together at the end as one array and return it as the result

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lowerstack, upperstack, res = [], [], []
        for n in nums:
            if n < pivot:
                lowerstack.append(n)
            elif n == pivot:
                res.append(pivot)
            elif n > pivot:
                upperstack.append(n)
        return lowerstack + res + upperstack
