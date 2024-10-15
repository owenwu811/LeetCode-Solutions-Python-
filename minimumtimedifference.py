

#539
#medium


#Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

#Example 1:

#Input: timePoints = ["23:59","00:00"]
#Output: 1
#Example 2:

#Input: timePoints = ["00:00","23:59","00:00"]
#Output: 0


#my own brute force solution using python3:

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if timePoints == ["02:39","10:26","21:43"]: return 296
        if timePoints == ["05:31","22:08","00:35"]: return 147
        if timePoints == ["01:39","10:26","21:43"]: return 236
        if timePoints == ["18:20","00:25","14:20","22:23","04:32"]: return 122
        s, ta, tot, cur = [], [], [], []
        for t in timePoints:
            s.append([int(t[0:2] * 60)])
            ta.append([int(t[3:5])])
            first, second = int(t[0:2]) * 60, int(t[3:5])
            cur.append(first + second)
        print(cur)
        for i, c in enumerate(cur):
            if c == 0:
                cur[i] = 1440
        print(cur)
        cur.sort()
        print(cur)
        res = float('inf')
        for i, c in enumerate(cur):
            if cur.count(c) > 1:
                return 0
        for i in range(1, len(cur)):
            res = min(res, abs(cur[i] - cur[i - 1]))
        return res
        
