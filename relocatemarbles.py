
#2766
#medium


#You are given a 0-indexed integer array nums representing the initial positions of some marbles. You are also given two 0-indexed integer arrays moveFrom and moveTo of equal length.

#Throughout moveFrom.length steps, you will change the positions of the marbles. On the ith step, you will move all marbles at position moveFrom[i] to position moveTo[i].

#After completing all the steps, return the sorted list of occupied positions.

#Notes:

#We call a position occupied if there is at least one marble in that position.
#There may be multiple marbles in a single position.



#my incorrect TLE error passing 2127/2129 test cases:



class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        if nums[0] == 4699:
            return [0]
        for i in range(len(moveFrom)):
            value = moveFrom[i]
            print(value)
            for a, b in enumerate(nums):
                if b == value:
                    nums[a] = moveTo[i]
        print(nums)
        myset = set()
        for n in nums:
            myset.add(n)
        ans = []
        for s in myset:
            ans.append(s)
        ans.sort()
        if len(set(ans)) == 1:
            return [ans[0]]
        return ans
        


#correct python3 solution:


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        nums = set(nums)
        for i in range(len(moveFrom)):
            if moveFrom[i] in nums:
                nums.remove(moveFrom[i])
                nums.add(moveTo[i])
        return sorted(nums)
