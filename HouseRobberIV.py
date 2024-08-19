
#There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

#The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

#You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

#You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

#Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

#Input: nums = [2,3,5,9], k = 2
#Output: 5
#Explanation: 
#There are three ways to rob at least 2 houses:
#- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
#- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
#Therefore, we return min(5, 9, 9) = 5.

#correct python3 solution:

#nums = [2, 3, 5, 9]

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def possible(v, r): #(3, 2), (5, 2)
            i = 0 
            while i < len(nums) and r > 0: #always true on 1st turn - r represents k allowance
                if nums[i] <= v: #2 <= 3 True, 5 <= 3 is False, so go else, 9 <= 3 is False, so go else ; 2 <= 5 True, 5 <= 5 True
                    r -= 1 #r becomes 1
                    i += 2 #i becomes 2
                else:
                    i += 1 #i becomes 3, i becomes 4
            return r==0 #r == 1, so this returns False, r == 0 so this returns True
        items = list(sorted(set(nums)))
        lo, hi = 0, len(items) - 1 #0, 3
        while lo < hi: #0 < 3 is True, 2 < 3 is True
            m = (lo + hi) // 2 #1, 2
            if possible(items[m], k): #(3, 2), (5, 2)
                hi = m #high becomes 2, rendering lo < high false because 2 < 2 is False
            else:
                lo = m + 1 #lo becomes 2
        return items[lo] #return nums[2] = 5


#a more intutive solution:

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low, high = min(nums), max(nums)
        while low <= high:
            mid = (low+high)//2
            i=0
            c=0
            while i < len(nums):
                if nums[i]<=mid:
                    c+=1
                    i+=1
                i+=1
            if c>=k:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
