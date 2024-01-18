
#Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

#Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

#Example 1:

#Input: s = "leetcode", wordDict = ["leet","code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".



#python3 solution:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #we want to make sure every character in s meaning the entire string can be space segmented. if even one last character in s cannot be space segmented, we return false, which we assume by filling the array initially with false except for the first character in s 
        dp = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    #set the farthest cell between i and j + 1 that's not yet true to true - this is why we set i to true initially - we want it to trigger the farther cell to turn true so we can mark the progress we have made
                    dp[j + 1] = dp[i] or dp[j + 1]
        #if the entire string - every last character - can be space segmented, we return True as we have flipped that last character to True. Otherwise, we don't modify it, and it stays False
        return dp[-1]


#1/17/24 refresher:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    dp[j + 1] = dp[i] or dp[j + 1]
        return dp[-1]


#1/18/24 refresher:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [True] + ([False] * len(s))
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    res[j + 1] = res[i] or res[j + 1]
        return res[-1]
