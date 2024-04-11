
#Given the head of a linked list, remove the nth node from the end of the list and return its head.
#head = [1,2,3,4,5], n = 2
#output: [1,2,3,5]

#python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next #create gap between left and right of exactly n nodes 
            n -= 1
        while right: #the idea is to keep the distance between left and right exactly n nodes, and when right reaches none too far to the right of the linked list, delete the nth node with left by cutting off by pointing left.next to left.next.next to cut it, so if n = 2, remove 4 from [1, 2, 3, 4, 5]
            left = left.next
            right = right.next
        left.next = left.next.next #cut off the nth node with left pointer
        return dummy.next
