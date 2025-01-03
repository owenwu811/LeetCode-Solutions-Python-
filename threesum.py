#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.

#Example 1:

#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation: 
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2].
#Notice that the order of the output and the order of the triplets does not matter.

#Example 2:

#Input: nums = [0,1,1]
#Output: []
#Explanation: The only possible triplet does not sum up to 0.
#Example 3:

#Input: nums = [0,0,0]
#Output: [[0,0,0]]
#Explanation: The only possible triplet sums up to 0.
 

#Constraints:

#3 <= nums.length <= 3000
#-105 <= nums[i] <= 105


My Solution:

class Solution(object):
    def threeSum(self, nums):
        result = [] #this is our final result
        nums.sort() # we need to sort our array so that we can use a three pointer approach
        for i, j in enumerate(nums): #i, j are the index, value of the array
            if i > 0 and j == nums[i - 1]: #i must be bigger than 0 so that we have an element before to even compare to. if the current value is the same as previous, keep moving to the next i, j (index, value) pair in the array until we reach the last element
                continue
            left, right = i + 1, len(nums) - 1        #i acts as our first pointer that only increments by one when the left < right condition is no longer true
            #right starts at the last index in our list 
            while (left < right): #the reason we need this is because we already sorted the nums array, so if left < right is false, we are pointing to values we already visited before. If this line is false, then we go back to the for loop at line 40 to move to the next i, j (ndex, value) pair in our array. 
                threesum = j + nums[left] + nums[right] #WE MUST MAKE SURE LEFT < RIGHT BEFORE CALCULATING THREESUM, OR ELSE WE WON'T HAVE VALID POINTERS
                if threesum > 0: # this takes advantage of the fact that the array is sorted
                    right -= 1
                elif threesum < 0: #same
                    left += 1
                else:
                    result.append([j, nums[left], nums[right]]) #we found a triplet to return
                    left += 1
                    while nums[left] == nums[left - 1] and left < right: #if left pointer is equal to the left pointer in the previous index, and left is still less than right, then we can increment to make sure that we don't return a duplicate triplet. We can do this by just making sure left pointer is different than left pointer was before. 
                        left += 1
        return result #once we have finished trasversing the entire array with the index, value pairs of each element, we can return the triplets we have found that are unique and sum to zero. 
                
                
     #it's important to note that line 54 must be WITHIN THE ELSE BLOCK. this is because we only check for duplicates because the previous, if duplicate, left pointer value was already returned as a valid triplet.
     #if line 54 was indented to the same level as the else above it, it would always execute, which we don't want
     #i in line 40 acts as the starting pointer, so left pointer always comes one after i. You don't need to purposely define another starting pointer.
     
     
 #My other solution:
      
 class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i, j in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threesum = j + nums[left] + nums[right]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    result.append([j, nums[left], nums[right]])
                    left, right = left + 1, right - 1 #this solution is even faster as we know we found a result, so we can reduce the time complexity by moving left and right towards each other instead of just left
                    while nums[left] == nums[left - 1] and left < right: #duplicate checking the outer pairs
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return result


#6/21/23 refresher (my solution):

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, j in enumerate(nums):
            if i > 0 and j == nums[i - 1]: #dumb mistake was forgetting i > 0 as there wouldn't be a previous element if i is at index 0 without this check in place 
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right] #i here is essentially the 1st pointer while left is 2nd and right is 3rd, which starts at the last index in the list pointing to the last element in the list 
                if threesum < 0: # we are comparing to 0 here, not a variable target number
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return result


#1/7/24 refresher solution (my own):

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum < 0:
                    second += 1
                elif threesum > 0:
                    third -= 1
                elif threesum == 0:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                            second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
        return res
            

#1/25/24 refresher:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum > 0:
                    third -= 1
                elif threesum < 0:
                    second += 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
        return res


#2/27/24 refresher:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum < 0:
                    second += 1
                elif threesum > 0:
                    third -= 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
        return res

#3/23/24:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum < 0:
                    second += 1
                elif threesum > 0:
                    third -= 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while nums[second] == nums[second - 1] and second < third:
                        second += 1
                    while nums[third] == nums[third + 1] and second < third:
                        third -= 1
        return res


#5/4/24 (missed):

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]: #do not forget checking duplicates for the 1st pointer!
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum < 0:
                    second += 1
                elif threesum > 0:
                    third -= 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while nums[second] == nums[second - 1] and second < third:
                        second += 1
                    while nums[third] == nums[third + 1] and second < third:
                        third -= 1
        return res

#5/6/24 refresher:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum < 0:
                    second += 1
                elif threesum > 0:
                    third -= 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while nums[second] == nums[second - 1] and second < third:
                        second += 1
                    while nums[third] == nums[third + 1] and second < third:
                        third -= 1
        return res


#5/15/24 practice:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second = first + 1 
            third = len(nums) - 1
            while second < third:
                threesum = nums[first] + nums[second] + nums[third]
                if threesum < 0:
                    second += 1
                elif threesum > 0:
                    third -= 1
                else:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
        return res


#10/12/24 review:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if sum(nums) == 0 and len(set(nums)) == 1 and nums[0] == 0:
            return [[0, 0, 0]]
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1]:
                continue
            second = i + 1
            third = len(nums) - 1
            while second < third:
                cursum = nums[i] + nums[second] + nums[third]
                if cursum < 0:
                    second += 1
                elif cursum > 0:
                    third -= 1
                else:
                    res.append([nums[i], nums[second], nums[third]])
                    second += 1
                    third -= 1
                    while nums[second] == nums[second - 1] and second < third:
                        second += 1
                    while nums[third] == nums[third + 1] and second < third:
                        third -= 1
        return res
