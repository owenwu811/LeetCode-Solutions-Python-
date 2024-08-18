

#Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
#Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

#my incorrect solution that only passes 27/85 test cases:

#my solution dosen't account for when firstList and secondList are of different lengths

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList and not secondList or secondList and not firstList: return []
        #res = []
        #for i in range(len(secondList) - 1):
        #    if secondList[i][0] >= firstList[i][0]:
        #        res.append([secondList[i][0], firstList[i][1]])
        #    if secondList[i][1] <= firstList[i + 1][0]:
        #        res.append([secondList[i][1], firstList[i + 1][0]])
        
        res = firstList + secondList
        res.sort()
        print(res) #[[0, 2], [1, 5], [5, 10], [8, 12], [13, 23], [15, 24], [24, 25], [25, 26]]
        ans = []
        prevend = [res[0]]
        for start, end in res[1:]:
            if start > prevend[-1][1]:
                prevend = [[start, end]]
            elif start <= prevend[-1][1]:
                ans.append([start, prevend[-1][1]])
                prevend = [[start, end]]
        print(ans)
        return ans


#python3 solution - correct:

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0]) #we get the bigger of the two lows because hi is bigger than lo, and the left part of the interval has to be all encompassing
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi]) 
            if firstList[i][1] < secondList[j][1]: 
                i += 1
            else:
                j += 1 #when secondList is longer than firstList, we only move the pointer forward for the secondList
        return ans
