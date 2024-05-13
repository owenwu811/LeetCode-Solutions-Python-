#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]


#python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            nxt = cur.next.next #3
            rightone = cur.next #2
            rightone.next = cur
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next
