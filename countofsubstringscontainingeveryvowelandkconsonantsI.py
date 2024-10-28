
#3305
#medium

#You are given a string word and a non-negative integer k.

#Return the total number of 
#substrings
# of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

#Example 1:

#Input: word = "aeioqq", k = 1

#Output: 0

#Explanation:

#There is no substring with every vowel.

#Example 2:

#Input: word = "aeiou", k = 0

#Output: 1

#Explanation:

#The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".


#my own solution using python3:

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        d = defaultdict(int)
        res = 0
        vowels = "aeiou"
        for i in range(len(word)):
            d.clear()
            for j in range(i, len(word)):
                substr = word[i: j + 1]
                d[substr] += 1
                vc, cc = 0, 0
                for s in substr:
                    if s not in vowels:
                        cc += 1
                    else:
                        vc += 1
                if cc == k and "a" in substr and "e" in substr and "i" in substr and "o" in substr and "u" in substr:
                    res += 1
        return res
