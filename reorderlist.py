



#Input: head = [1,2,3,4]
#Output: [1,4,2,3]

#Input: head = [1,2,3,4,5]
#Output: [1,5,2,4,3]

#python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        slow, fast = head, head.next
        while fast and fast.next: #2, 3
            slow = slow.next #2
            fast = fast.next.next #4
        second = slow.next #3
        prev = slow.next = None #3.next = None
        while second: #3, 4
            tmp = second.next #4, None
            second.next = prev #None, 3
            prev = second #3, 4
            second = tmp #4, None
        first, second = head, prev #1, 4
        while second: #4
            tmp1, tmp2 = first.next, second.next #2, 3
            first.next = second #4
            second.next = tmp1 #2
            first, second = tmp1, tmp2 #2, 3
