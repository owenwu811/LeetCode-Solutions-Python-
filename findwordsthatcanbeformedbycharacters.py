
#1160
#easy


#You are given an array of strings words and a string chars.

#A string is good if it can be formed by characters from chars (each character can only be used once).

#Return the sum of lengths of all good strings in words.

 

#Example 1:

#Input: words = ["cat","bt","hat","tree"], chars = "atach"
#Output: 6
#Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
#Example 2:

#Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
#Output: 10
#Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


#my own solution using python3:

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        key = "".join(sorted(chars))
        #print(key)
        for w in words:
            print("".join(sorted(w)))
            print(key)
            flag = True
            for c in w:
                if c not in key or chars.count(c) < w.count(c):
                    flag = False
            if flag:
                res += len(w)
        return res
