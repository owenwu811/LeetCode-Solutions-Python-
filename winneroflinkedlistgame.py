#3062
#easy


#You are given the head of a linked list of even length containing integers.

#Each odd-indexed node contains an odd integer and each even-indexed node contains an even integer.

#We call each even-indexed node and its next node a pair, e.g., the nodes with indices 0 and 1 are a pair, the nodes with indices 2 and 3 are a pair, and so on.

#For every pair, we compare the values of the nodes in the pair:

#If the odd-indexed node is higher, the "Odd" team gets a point.
#If the even-indexed node is higher, the "Even" team gets a point.
#Return the name of the team with the higher points, if the points are equal, return "Tie".

 

#Example 1:

#Input: head = [2,1]

#Output: "Even"

#Explanation: There is only one pair in this linked list and that is (2,1). Since 2 > 1, the Even team gets the point.

#Hence, the answer would be "Even".



#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        print(tmp)
        even, odd = [], []
        for i in range(len(tmp)):
            if i % 2 == 0:
                even.append(tmp[i])
            else:
                odd.append(tmp[i])
        print(even)
        print(odd)
        e, o = 0, 0
        for i in range(len(even)):
            if even[i] > odd[i]:
                e += 1
            elif odd[i] > even[i]:
                o += 1
        print(e, o)
        if e > o:
            return "Even"
        elif o > e:
            return "Odd"
        else:
            return "Tie"
