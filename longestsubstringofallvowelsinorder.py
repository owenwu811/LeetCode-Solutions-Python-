
#1839
#medium

#A string is considered beautiful if it satisfies the following conditions:

#Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
#The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
#For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

#Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

#A substring is a contiguous sequence of characters in a string.

 

#Example 1:

#Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
#Output: 13
#Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.


#my own solution using python3:

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        d = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        letters = "aeiou"
        res = 0
        stack = []
        newd = defaultdict(int)
        for r in range(len(word)):
            if not stack:
                stack.append(word[r])
                newd[word[r]] += 1
                continue
            if stack and d[word[r]] >= d[stack[-1]]:
                stack.append(word[r])
                newd[word[r]] += 1
                if newd["a"] and newd["e"] and newd["i"] and newd["o"] and newd["u"]:
                    res = max(res, len(stack))
            else:
                stack.clear()
                newd.clear()
                stack.append(word[r])
                newd[word[r]] += 1
        return res
