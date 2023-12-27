
#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


#python3 solution:

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        result = 0
        l, r = 0, len(height) - 1 #two pointer problem
        leftside, rightside = height[l], height[r] 
        while l < r:
            if leftside < rightside:
                l += 1
                leftside = max(leftside, height[l])
                result += (leftside - height[l])
            else: 
                r -= 1
                rightside = max(rightside, height[r])
                result += (rightside - height[r])
        return result
