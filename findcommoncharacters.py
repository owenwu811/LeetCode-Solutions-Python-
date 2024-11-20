
#1002
#easy

#Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

#Example 1:

#Input: words = ["bella","label","roller"]
#Output: ["e","l","l"]
#Example 2:

#Input: words = ["cool","lock","cook"]
#Output: ["c","o"]


#my own solution using python3:

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        bank = []
        for w in words[0]:
            bank.append(w)
        print(bank)
        ans = []
        for b in bank:
            flag = True
            for a in words[1:]:
                if b not in a:
                    flag = False
            if flag:
                ans.append(b)
        new = []
        d = defaultdict(list)
        for w in words:
            cur = []
            for a in w:
                if a in ans:
                    d[a].append(w.count(a))
        print(d)
        print(ans)
        newd = dict()
        for k in d:
            newd[k] = min(d[k])
        print(newd)
        final = []
        for k in newd:
            cur = newd[k]
            while cur > 0:
                final.append(k)
                cur -= 1
        print(final)
        return final
