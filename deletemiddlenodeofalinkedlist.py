
#You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

#The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

#For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

#Input: head = [1,3,4,7,1,2,6]
#Output: [1,3,4,1,2,6]


#my own solution in python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: #this line is for the edge case if head = [1], then return []
            return None
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        slow = slow.next
        return head
        
