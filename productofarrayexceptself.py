#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

#You must write an algorithm that runs in O(n) time and without using the division operation.

#[1, 2, 3, 4]


#my solution - python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        result = [0] * len(nums)
        for i in range(len(nums)): #[1, 1, 2, 6] - no room for 24
            result[i] = prefixn
            prefixn *= nums[i]
        for i in range(len(nums) -1, -1, -1): #[24, 12, 8, 6] - multiplied by prefix array 
            result[i] *= postfixn
            postfixn *= nums[i]
        return result
            
#my solution - python3 - 12/17/23:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        res = [0] * len(nums) #create an empty array to declare it's length by filling it with zeros
        for number in range(len(nums)): 
            res[number] = prefixn #[1, 1, 2, 6]
            prefixn *= nums[number] # [1] [1*1] [1*1*2] [1*1*2*3]
        for number in range(len(nums) -1, -1, -1): 
            res[number] = postfixn * res[number] #[24, 12, 8, 6]
            postfixn *= nums[number] #[1 * 2 * 3 * 4] [1 * 3 * 4] [1 * 4 * 2] [6 * 1]
        return res

#12/25/23 refresher - my solution:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = 1
        backward = 1
        result = len(nums) * [0]
        for number in range(len(nums)):
            result[number] = forward
            forward *= nums[number]
        for number in range(len(nums)-1, -1, -1):
            result[number] *= backward
            backward *= nums[number]
        return result



#1/8/24 refresher - my solution:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        anwser = [0] * len(nums)
        prefixn = 1
        postfixn = 1
        for number in range(len(nums)):
            anwser[number] = prefixn
            prefixn *= nums[number]
        for number in range(len(nums)-1, -1, -1):
            anwser[number] *= postfixn
            postfixn *= nums[number]
        return anwser


#1/14 refresher - IMPORTANT INSIGHT

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        prefixn, postfixn = 1, 1
        for forward in range(len(nums)):
            result[forward] = prefixn
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            #result = [1, 1, 2, 6]
            #nums = [1, 2, 3, 4]
            #we want = [24, 12, 8, 6]
            #we don't get [24, 12, 12, 6] because result[2] = 2, and 2 * 4(postfixn) = 8. WE WANT POSTFIXN * RESULT[2] NOT POSTFIXN * NUMS[2] - POSTFIXN TIMES RESULT[2] NOT POSTFIXN TIMES NUMS[2] IS PLACED IN THE 2ND INDEX IN OUR FINAL LIST
            result[backward] = postfixn * result[backward]
            postfixn *= nums[backward]
        return result


#1/18/24 refresher:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        res = [1] * len(nums)
        for forward in range(len(nums)):
            res[forward] = prefixn 
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            res[backward] = postfixn * res[backward]
            postfixn *= nums[backward]
        return res

#1/21/24 refresher practice solution:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        #we use 1 to fill in every place in our eventual to be output array because 0 times anything is always 0
        res = [1] * len(nums)
        for number in range(len(nums)):
            res[number] = prefixn
            prefixn *= nums[number]
        for number in range(len(nums) - 1, -1, -1):
            res[number] *= postfixn
            postfixn *= nums[number]
        return res


#2/1/24 refresher:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        result = [1] * len(nums)
        for forward in range(len(nums)):
            result[forward] = prefixn
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            #note that we multiply postfixn by result[backward], not by nums[backward] - POSTFIXN TIMES RESULT[2] NOT POSTFIXN TIMES NUMS[2] 
            result[backward] *= postfixn
            postfixn *= nums[backward]
        return result


#2/6/24 practice:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        res = [1] * len(nums) #our final array has the same length as the input
        for forward in range(len(nums)):
            res[forward] *= prefixn
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1): #iterating through input array backward
            #times res[backward] and not nums[backward] because we build off of what we made when iterating forward
            res[backward] *= postfixn
            postfixn *= nums[backward]
        return res



#2/22/24: (missed - needs churning!)

#[1, 2, 3, 4] nums
# 0, 1, 2, 3  - 4 is out of bounds!


#[1, 1, 2, 6] res
# 0, 1, 2, 3
#postfixn *= nums[backward] 
#postfixn = 1 * nums[3]
#postfixn = 1 * 4
#postfixn = 4

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn, postfixn = 1, 1
        res = [0] * len(nums)
        for forward in range(len(nums)): #at forward = 3, we update res[forward] with 6 - [1, 1, 2, 6], and then prefix becomes 24 (6 * 4), and then forward increments to 4 in the for loop, which is out of bounds for [1, 2, 3, 4], so we go to the backward for loop
            res[forward] = prefixn
            prefixn *= nums[forward] #after executing, we first go to the for loop to increment forward before updating the new incremented res[forward]
        for backward in range(len(nums) -1, -1, -1): #backward starts at 3
            res[backward] *= postfixn #in the 1st iteration, 6 * 1 = 6, so the res[3] stays as 6
            postfixn *= nums[backward] #after executing, we first go to the for loop to decrement backward before updating the new decremented res[backward]
        return res


#2/23/24:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn = 1
        postfixn = 1
        res = [0] * len(nums)
        for forward in range(len(nums)):
            res[forward] = prefixn
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            res[backward] *= postfixn
            postfixn *= nums[backward]
        return res

#2/24/24:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn, postfixn = 1, 1
        res = [0] * len(nums)
        for forward in range(len(nums)):
            res[forward] = prefixn
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            res[backward] *= postfixn
            postfixn *= nums[backward]
        return res

#2/25/24:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we cannot use division
        prefixn, postfixn = 1, 1
        res = [0] * len(nums) #same length as input list
        for forward in range(len(nums)): 
            res[forward] = prefixn
            prefixn *= nums[forward] #1 [1, 1, 2, 6]
        for backward in range(len(nums) - 1, -1, -1):
            res[backward] *= postfixn #6 * 1
            postfixn *= nums[backward] #1 * 4 = 4
        return res

#2/26/24:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn, postfixn = 1, 1 #prefixn forward loop; postfixn backward loop
        res = [0] * len(nums)
        for forward in range(len(nums)): #0123
            res[forward] = prefixn #1126
            prefixn *= nums[forward] #126
        for backward in range(len(nums) -1, -1, -1): #3210
            res[backward] *= postfixn #24 12 8 6
            postfixn *= nums[backward] 
        return res

#2/29/24:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefixn, postfixn = 1, 1
        for forward in range(len(nums)):
            res[forward] = prefixn
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            res[backward] *= postfixn 
            postfixn *= nums[backward]
        return res

#3/5/24:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardf, backwardf = 1, 1
        res = [0] * len(nums)
        for forward in range(len(nums)):
            res[forward] = forwardf
            forwardf *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            res[backward] *= backwardf
            backwardf *= nums[backward]
        return res
 

#3/8/24:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixn, postfixn = 1, 1
        res = [0] * len(nums)
        for forward in range(len(nums)):
            res[forward] = prefixn
            prefixn *= nums[forward]
        for backward in range(len(nums) -1, -1, -1):
            res[backward] *= postfixn
            postfixn *= nums[backward]
        return res


#During the forward pass, result[i] stores the product of all elements to the left of nums[i]. if nums = [1, 2, 3, 4], when you say left of nums[i], you mean 1, 2, 3, but not 4. So, for example, if nums = [1, 2, 3, 4], and we are considering nums[2], which is 3, then the elements to the left of nums[2] are [1, 2]. In other words, the product stored in result[2] will be the product of all elements to the left of 3, which is 1 * 2 = 2.

#Similarly, for nums[3], which is 4, the elements to the left of it are [1, 2, 3], and the product stored in result[3] will be the product of all elements to the left of 4, which is 1 * 2 * 3 = 6.

#So, in essence, when we refer to "left of nums[i]" in this solution, we mean all the elements that appear before the element at index i, excluding the element at index i itself.

#This ensures that result[i] contains the product of all elements except nums[i] from the left side.

#During the backward pass, we multiply each element of result by the product of all elements to the right of nums[i]. 

#This effectively combines the products computed in the forward pass with the products computed in the backward pass, excluding nums[i].

#Thus, each element of the result list contains the product of all elements in the original list nums, except for the element at the corresponding index.

#By performing two passes through the nums list, we can achieve the desired result without using division and with a time complexity of O(n), where n is the length of the input list.




#During the backward pass, we multiply each element of result by the product of all elements to the right of nums[i]. This effectively combines the products computed in the forward pass with the products computed in the backward pass, excluding nums[i]. - so for example, for nums = [1, 2, 3, 4]:

#We initialize forward = 1 and iterate over the nums list from left to right.
#At each index i, we store the product of all elements to the left of nums[i] in the result list.
#After the forward pass, the result list will contain [1, 1, 2, 6], corresponding to the products of all elements to the left of each element in nums.
#Backward Pass:

#We initialize backward = 1 and iterate over the nums list from right to left.
#At each index i, we multiply the previously computed product (stored in result[i]) by the product of all elements to the right of nums[i].
#This effectively combines the products computed in the forward pass with the products computed in the backward pass, excluding nums[i].
#For example:
#For nums[3], which is 4, the product of all elements to the right of 4 is 1 (since there are no elements to the right of 4). So, result[3] *= 1, which remains 6.
#For nums[2], which is 3, the product of all elements to the right of 3 is 4. So, result[2] *= 4, which becomes 2 * 4 = 8.
#For nums[1], which is 2, the product of all elements to the right of 2 is 4 * 3 = 12. So, result[1] *= 12, which becomes 1 * 12 = 12.
#For nums[0], which is 1, the product of all elements to the right of 1 is 4 * 3 * 2 = 24. So, result[0] *= 24, which becomes 1 * 24 = 24.
#After completing both forward and backward passes, the result list will contain [24, 12, 8, 6], which are the products of all elements in the nums list except for the element at each corresponding index.
