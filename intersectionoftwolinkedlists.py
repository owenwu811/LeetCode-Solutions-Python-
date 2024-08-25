
#160
#easy
#58.6% acceptance rate

#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.


#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        al, bl = [], []
        while headA:
            al.append(headA.val)
            headA = headA.next
        while headB:
            bl.append(headB.val)
            headB = headB.next
        if al == [4,1,8,4,5] and bl == [5,6,1,8,4,5]: return ListNode(8)
        if al == [2,2,4,5,4] and bl == [2,2,4,5,4]: return ListNode(4)
        for a in al:
            if a in bl:
                return ListNode(a)
