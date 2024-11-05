
#1272
#medium

#A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

#You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

#Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.


#my own solution using python3:

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for i in range(len(intervals)):
            if intervals[i][0] == toBeRemoved[0] and intervals[i][1] == toBeRemoved[1] and intervals[i][0] < intervals[i][1]:
                print(ans)
                continue
            if intervals[i][0] > toBeRemoved[0] and intervals[i][1] < toBeRemoved[1]:
                continue
            if intervals[i][0] < toBeRemoved[0] < toBeRemoved[1] <= intervals[i][1]:
                ans.append([intervals[i][0], toBeRemoved[0]])
                ans.append([toBeRemoved[1], intervals[i][1]])
                print(ans)
                continue
            if intervals[i][0] < toBeRemoved[0] < intervals[i][1] < toBeRemoved[1]:
                ans.append([intervals[i][0], toBeRemoved[0]])
                print(ans)
            elif intervals[i][0] < toBeRemoved[1] < intervals[i][1]:
                ans.append([toBeRemoved[1], intervals[i][1]])
                print(ans)
            else:
                ans.append(intervals[i])
        print(ans)
        final = []
        for i, a in enumerate(ans):
            if a[0] == a[1]:
                continue 
            final.append(ans[i])
        return final
