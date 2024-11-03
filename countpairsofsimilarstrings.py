
#2506
#easy


#You are given a 0-indexed string array words.

#Two strings are similar if they consist of the same characters.

#For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
#However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
#Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

 

#Example 1:

#Input: words = ["aba","aabb","abcd","bac","aabc"]
#Output: 2
#Explanation: There are 2 pairs that satisfy the conditions:
#- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
#- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 



#my own solution using python3:

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if set(words[i]) == set(words[j]):
                    res += 1
        return res
