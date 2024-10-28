
#3295
#medium

#You are given an array of strings message and an array of strings bannedWords.

#An array of words is considered spam if there are at least two words in it that exactly match any word in bannedWords.

#Return true if the array message is spam, and false otherwise.

 

#Example 1:

#Input: message = ["hello","world","leetcode"], bannedWords = ["world","hello"]

#Output: true

#Explanation:

#The words "hello" and "world" from the message array both appear in the bannedWords array.

#Example 2:

#Input: message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]

#Output: false

#Explanation:

#Only one word from the message array ("programming") appears in the bannedWords array.


#my own solution using python3:

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        freq = Counter(message)
        a = set(message)
        b = set(bannedWords)
        print(a, b)
        cur = 0
        for c in a:
            if c in b:
                cur += freq[c]
                if cur >= 2:
                    return True
        print(cur)
        if cur >= 2:
            return True
        else:
            return False
