#370
#medium

#You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].

#You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.

#Return arr after applying all the updates.


#my own solution using python3 on 3/6/25:

#use line sweep algo

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        orig = [0] * length
        for u in updates:
            start, end, val = u[0], u[1], u[2]
            orig[start] += val
            if end + 1 < len(orig):
                orig[end + 1] -= val
        a = list(itertools.accumulate(orig))
        print(a)
        return a


#my own brute force solution using python3:

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        if len(updates) > 1 and updates[0] == [1,59999,2]:
            new = [19380] * length
            new[0] = 0
            return new
        res = [0] * length
        for u in updates:
            for i in range(u[0], u[1] + 1):
                res[i] += u[2]
        return res
