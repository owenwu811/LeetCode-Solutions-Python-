

#611
#medium


#array that can make triangles if we take them as side lengths of a triangle.

 

#Example 1:

#Input: nums = [2,2,3,4]
#Output: 3
#Explanation: Valid combinations are: 
#2,3,4 (using the first 2)
#2,3,4 (using the second 2)
#2,2,3
#Example 2:

#Input: nums = [4,2,3,4]
#Output: 4



#explanation:

#This solution works by utilizing a two-pointer approach to efficiently count the number of valid triangles that can be formed from the array nums. Here’s a step-by-step breakdown of how and why this algorithm works:


#Detailed Explanation:
#Sorting the Array:
#The first step is to sort the array nums in non-decreasing order. This is important because it ensures that, for any triplet, if nums[l] and nums[r] are the two smaller sides, then nums[i] is the largest side. Sorting simplifies the logic of checking the triangle condition since we can naturally assume nums[i] is the largest side in the triplet.
#Fixing the Largest Side:
#The main loop iterates from index i = 2 to the end of the array. For each i, nums[i] is treated as the largest side of the triangle (i.e., side c).
#Using Two Pointers for the Smaller Sides:
#For each i, the two-pointer approach is used to find the other two sides (nums[l] and nums[r]) that can form a triangle with nums[i]:
#l starts at index 0 (the smallest side).
#r starts at index i - 1 (just before nums[i]).
#We check if the sum of the two smaller sides, nums[l] and nums[r], satisfies the condition:

#nums[l]+nums[r]>nums[i]
#If the condition is true, it means that all pairs between l and r (i.e., l, r, l+1, r, ..., r-1, r) will also form valid triangles with nums[i] because the array is sorted, and increasing the value of l would only make the sum larger. Therefore, r - l valid triangles are added to the result res.
#Adjusting the Pointers:
#If nums[l] + nums[r] > nums[i], the pointer r is decremented (r -= 1) to try smaller values for the second side (because we're trying to explore other potential valid triangles with nums[i] as the largest side).
#If nums[l] + nums[r] <= nums[i], it means the sum of the two smaller sides is not large enough to form a triangle, so we increment l (l += 1) to try a larger value for the smallest side.
#Returning the Result:
#Once the loop finishes, the total count res of valid triangles is returned.


#correct python3 solution: - could not solve, so need to revisit

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort() #we must sort it in order for the else: l += 1 to work because if we have [2, 2, 3, 4], and nums[l] + nums[r] is not bigger than nums[i], then we have to make the sum bigger, and we know moving left up will make the sum bigger because the input array is sorted!
        l, r = 0, len(nums) - 1
        for i in range(2, len(nums)):
            #in short, we start r at i - 1 because the first and second sides must be different and to the left of the third side, not the same position and number as the third side itself, so nums[i] is the third side
            l, r = 0, i - 1 #notice how we start at i - 1, which is index 1 in the beginning of [2, 2, 3, 4]. this is because if we started at i, we are coming nums[r] to itself. Starting r at i - 1 ensures that the second side of the triangle is smaller than the third side (nums[i]). If you were to start r at i, then you'd be comparing a number (nums[r]) to itself (nums[i]), which doesn't make sense when trying to find THREE distinct numbers that form a triangle where the 1st and 2nd (different from 3rd) sides added must be bigger than the 3rd side by itself, so not 1 + 3 > 3, but like 1 + 2 > 3 or 1 + 4 > 3
            while l < r:
                if nums[l] + nums[r] > nums[i]: #[2, 2, 3, 4] - lets say l is on index 0 2 and r is on index 3's 4. if we know 2 + 4 is bigger than nums[i], than we know anything plus 2 + 4 aka in between left and right will also be bigger than nums[i], so that's why l, r = 0, i + 1 - left starts at index 0 initially because we need 2, 3, 4 + 2, 3, 4 + 2, 2, 3 for [2, 2, 3, 4] as 2, 3, 4 can be used twice skipping elements but still counting, which is why we have to start l at 0!
                    res += (r - l) #we don't do (r - l + 1) because l and r equals 2 pointers, not a triplet! we only care about in between elements added to l and r one at a time because we already know l and r indexed values together are already bigger than nums[i], so anything added further will always be bigger than nums[i]!
                    r -= 1
                else:
                    l += 1 #because array is sorted, and we know nums[l] + nums[r] wasn't bigger than nums[i], we can increment l to try to make the triplet sum bigger 
        return res

#9/23/24 review:

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        seen = set()
        for i in range(2, len(nums)):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
        return res
