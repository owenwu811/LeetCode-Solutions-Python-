
#1980
#medium

#Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

#Example 1:

#Input: nums = ["01","10"]
#Output: "11"
#Explanation: "11" does not appear in nums. "00" would also be correct.
#Example 2:

#Input: nums = ["00","01"]
#Output: "11"
#Explanation: "11" does not appear in nums. "10" would also be correct.
#Example 3:

#Input: nums = ["111","011","001"]
#Output: "101"
#Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.


#my own solution using python3:

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        start = "0" * len(nums[0])
        end = "1" * len(nums[0])
        if start not in nums:
            return start
        if end not in nums:
            return end
        piecesstart = []
        piecesend = []
        for i in range(len(start)):
            for j in range(i, len(start)):
                substr = start[i: j + 1]
                piecesstart.append(substr)
        print(piecesstart)
        for a in range(len(end)):
            for b in range(a, len(end)):
                substr = end[a: b + 1]
                piecesend.append(substr)
        print(piecesend)
        for i in range(len(piecesstart)):
            for j in range(len(piecesend)):
                cur = piecesstart[i] + piecesend[j]
                if len(cur) == len(nums[0]):
                    for a in permutations(cur):
                        print(a)
                        if "".join(a) not in nums:
                            return "".join(a)
        
