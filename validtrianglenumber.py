

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

This solution works by utilizing a two-pointer approach to efficiently count the number of valid triangles that can be formed from the array nums. Here’s a step-by-step breakdown of how and why this algorithm works:


Detailed Explanation:
Sorting the Array:
The first step is to sort the array nums in non-decreasing order. This is important because it ensures that, for any triplet, if nums[l] and nums[r] are the two smaller sides, then nums[i] is the largest side. Sorting simplifies the logic of checking the triangle condition since we can naturally assume nums[i] is the largest side in the triplet.
Fixing the Largest Side:
The main loop iterates from index i = 2 to the end of the array. For each i, nums[i] is treated as the largest side of the triangle (i.e., side c).
Using Two Pointers for the Smaller Sides:
For each i, the two-pointer approach is used to find the other two sides (nums[l] and nums[r]) that can form a triangle with nums[i]:
l starts at index 0 (the smallest side).
r starts at index i - 1 (just before nums[i]).
We check if the sum of the two smaller sides, nums[l] and nums[r], satisfies the condition:

nums[l]+nums[r]>nums[i]
If the condition is true, it means that all pairs between l and r (i.e., l, r, l+1, r, ..., r-1, r) will also form valid triangles with nums[i] because the array is sorted, and increasing the value of l would only make the sum larger. Therefore, r - l valid triangles are added to the result res.
Adjusting the Pointers:
If nums[l] + nums[r] > nums[i], the pointer r is decremented (r -= 1) to try smaller values for the second side (because we're trying to explore other potential valid triangles with nums[i] as the largest side).
If nums[l] + nums[r] <= nums[i], it means the sum of the two smaller sides is not large enough to form a triangle, so we increment l (l += 1) to try a larger value for the smallest side.
Returning the Result:
Once the loop finishes, the total count res of valid triangles is returned.


#correct python3 solution: - could not solve, so need to revisit

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        for i in range(2, len(nums)):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1
        return res
