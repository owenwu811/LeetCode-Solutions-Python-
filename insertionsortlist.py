
#medium
#54.4% acceptance rate
#147

#Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

#The steps of the insertion sort algorithm:

#Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
#At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
#It repeats until no input elements remain.
#The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        tmp.sort()
        dummy = cur = ListNode()
        for t in tmp:
            cur.next = ListNode(t)
            cur = cur.next
        return dummy.next
