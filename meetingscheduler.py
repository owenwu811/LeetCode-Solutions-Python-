

#1229
#medium

#Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

#If there is no common time slot that satisfies the requirements, return an empty array.

#The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

#It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

#Example 1:

#Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
#Output: [60,68]
#Example 2:

#Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
#Output: []

#my own solution using python3:

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        tmp = []
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            if slots1[i][1] - slots1[i][0] < duration:
                i += 1
                continue
            if slots2[j][1] - slots2[j][0] < duration:
                j += 1
                continue
            if slots1[i][1] >= slots2[j][1]:
                bigger = max(slots1[i][0], slots2[j][0])
                if slots2[j][1] >= bigger and slots2[j][1] - bigger >= duration:
                    tmp.append([bigger, bigger + duration])
                if slots1[i][1] >= slots2[j][1]:
                    j += 1
                    continue
            if slots2[j][1] >= slots1[i][1]:
                print("h")
                print(slots1[i], slots2[j])
                bigger = max(slots1[i][0], slots2[j][0])
                if bigger <= slots1[i][1] and slots1[i][1] - bigger >= duration:
                    tmp.append([bigger, bigger + duration])
                if slots2[j][0] > slots1[i][1]:
                    i += 1
                    continue
            i += 1
            j += 1
        tmp.sort()
        #print(tmp)
        if tmp:
            return tmp[0]
        return []
