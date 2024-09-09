
#3121
#medium
#41.6% acceptance rate

#You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

#Return the number of special letters in word.

#my own solution using python3:

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower, upper = defaultdict(list), defaultdict(list)
        for i, n in enumerate(word):
            if n.islower():
                lower[n].append(i)
            elif n.isupper():
                upper[n].append(i)
        print(lower)
        print(upper)
        if lower and not upper or upper and not lower:
            return 0
        res = 0
        for k in lower:
            if k.upper() in upper and max(lower[k]) < min(upper[k.upper()]):
                res += 1
        return res
