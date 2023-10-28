#187. Repeated DNA Sequences
#Medium
#3.1K
#504
#Companies
#The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

#For example, "ACGAATTCCG" is a DNA sequence.
#When studying DNA, it is useful to identify repeated sequences within the DNA.

#Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

#Example 1:

#Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#Output: ["AAAAACCCCC","CCCCCAAAAA"]
#Example 2:

#Input: s = "AAAAAAAAAAAAA"
#Output: ["AAAAAAAAAA"]
 

Constraints:
#1 <= s.length <= 105
#s[i] is either 'A', 'C', 'G', or 'T'.
#Accepted
#345.4K
#Submissions
#722K
#Acceptance Rate
#47.8%



#Python3 solution:

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()
        for i in range(len(s) - 9): #len = 13, so index 3 is the last inclusive before out of bounds - 0, 1, 2, 3
            cur = s[i: i + 10] #3:13 means index 12 is the last inclusive - each 10 window character
            if cur in seen: #already appeared, so did occur more than once, so add to result since we want to return all substrings that occur more than once
                res.add(cur)
            seen.add(cur) #if current substring we are analyzing has not already been seen, then skip adding it to the result set and add it to just the seen set since it's the first time we have seen this substring #regardless of if this substring has been seen before, it is now seen, so add it to seen - we want to count as many times as the substring occurs in s from when it was seen from the 2nd time onewards
        return res
        
        #PYTHON SETS ORDER DOES NOT MATTER
        #s = "AAAAAAAAAAAAA" - len of 13 index 3 last inclusive windowstart
        #3:13 - index 12 last inclusive meaning last windowend that's valid 
        # since sets don't count order, as long as we have already seen this 10 character pair, we can add it to the result because we are looking for 10 letter long sequences that occur more than ONCE. seen.add(cur) adds every 10 character pair we ever see, and the pair is denoted by s[i:i + 10] instead of windowstart and windowend
