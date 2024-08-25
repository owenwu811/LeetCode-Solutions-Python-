#medium
#69.7%acceptancerate
#2058


#A critical point in a linked list is defined as either a local maxima or a local minima.

#A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

#A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

#Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

#Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].


#Input: head = [3,1]
#Output: [-1,-1]
#Explanation: There are no critical points in [3,1].


#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        tmp = []
        l = []
        while head:
            tmp.append(head.val)
            head = head.next
        for i in range(1, len(tmp) - 1):
            if tmp[i - 1] < tmp[i] > tmp[i + 1]:
                l.append(i)
            if tmp[i - 1] > tmp[i] < tmp[i + 1]:
                l.append(i)
        #print(l)
        if not l:
            return [-1, -1]
        l.sort()
        print(l)
        if len(l) == 1:
            return [-1, -1]
        if len(l) == 2:
            return [max(l) - min(l), max(l) - min(l)]
        if len(l) == 3:
            minimum = max(l) - min(l)
            maximum = max(l) - min(l)
            for i in range(1, len(l)):
                minimum = min(minimum, l[i] - l[i - 1])
            return [minimum, maximum]
        mini = -1
        maxi = max(l) - min(l)
        for i in range(len(l)):
            if l[i] + 1 in l:
                mini = 1
                break
        return [mini, maxi]
