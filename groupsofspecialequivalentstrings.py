
#893
#medium

#You are given an array of strings of the same length words.

#In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].

#Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == words[j].

#For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves "zzxy" -> "xzzy" -> "xyzz".
#A group of special-equivalent strings from words is a non-empty subset of words such that:

#Every pair of strings in the group are special equivalent, and
#The group is the largest size possible (i.e., there is not a string words[i] not in the group such that words[i] is special-equivalent to every string in the group).
#Return the number of groups of special-equivalent strings from words.

#my own solution using python3:

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        cnt = []
        for w in words:
            evenl, oddl = "", ""
            for i in range(len(w)):
                if i % 2 == 0:
                    evenl += w[i]
                else:
                    oddl += w[i]
            print(evenl)
            print(oddl)
            cnt.append([evenl, oddl])
        print(cnt)
        myset = set()
        tmp = []
        for c in cnt:
            a = "".join(sorted(c[0]) + sorted(c[1]))
            if a not in myset:
                myset.add(a)
        return len(myset)
            
            
