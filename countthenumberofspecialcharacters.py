
#3120

#You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

#Return the number of special letters in word.

#my own solution using python3:

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        visited = set()
        for i in range(len(word)):
            visited.add(word[i])
            #print(word[i])
        lower, upper = [], []
        for v in visited:
            if v.islower():
                lower.append(v)
            elif v.isupper():
                upper.append(v)
        print(lower)
        print(upper)
        if lower and not upper or upper and not lower:
            return 0
        for l in lower:
            if l.upper() in upper:
                cnt += 1
        return cnt
            
            
