#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

 

#Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#Example 2:

#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#Example 3:

#Input: nums = [3,3], target = 6
#Output: [0,1]

#My Solution:

#flipping trick is applied here with reverse dictionary 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}  #using a double for loop here is slow, so we use a dictionary. 
        for i, j in enumerate(nums): # we are getting i and j as the index, value pair of the array
            complement = target - j # we are looking for the target value minus the current index's value, which is the complement
            if complement in mydict: #will always be false on the first turn since the dictionary is empty at start - if complement exists as a key in mydict, then return the corresponding value as a key in mydict to get the index as a reverse because complement will always have been j at some point
                return mydict[complement], i #returning the two indicies IF we find them in our dictionary
            mydict[j] = i #if the complement is not already a VALUE, not KEY, in our dictionary, then add the value as the Key and the array's index as the value so that, if and when you do find the complement in the dictionary, you can call the key to get the value, which happens to be the array's index because we flipped the two. This is because dictionarys in python as only one directinoal: you can only call the key to get the value; you can't call the value to get the key. 
#usually, you need to return 0 or nothing, but there is no such requirement in the question, so there is no need for a return at the end.

#NOTE THAT LINES 30 AND 31 WILL NEVER BE TRUE ON THE FIRST ITERATION BECAUSE WE'VE ONLY SEEN ONE DIGIT SO FAR, SO THERE'S NOT EVEN A SECOND DIGIT UNTIL THE 2ND ITERATION.


#4/8/24 refresher:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = dict()
        res = []
        for i, j in enumerate(nums):
            complement = target - j
            if complement in mydict:
                return mydict[complement], i
            mydict[j] = i


#5/16/24 refresher:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = dict()
        for i, j in enumerate(nums):
            complement = target - j
            if complement in mydict:
                return mydict[complement], i
            mydict[j] = i

#6/20/24 review:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in mydict:
                return mydict[complement], i
            mydict[j] = i


#7/26/24 refresher:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in mydict:
                return mydict[complement], i
            mydict[j] = i


#10/12/24 review:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in mydict:
                return mydict[complement], i
            mydict[n] = i


#my own solution using python3 (brute force way on 10/18/24):

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
