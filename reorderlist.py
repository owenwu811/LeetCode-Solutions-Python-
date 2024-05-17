



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


#by the time we finish, slow will be at 2 if [1, 2, 3, 4]!, and slow.next will be 3!, so it will be one to the left if length is even!
#by the time we finish, slow will be perfectly in middle at 3 if [1, 2, 3, 4, 5]!, and slow.next will be 4! so it will be perfectly in middle if length is odd because just plopped in middle!


#5/11/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        #find the middle of the linked list as either the left as even length or exact middle as odd length input
        slow, fast = head, head.next
        while fast and fast.next: #2
            slow = slow.next #2
            fast = fast.next.next #4
        second = slow.next #3
        prev = slow.next = None #N
        #reverse 2nd half of the linked list
        while second: #3 4
            tmp = second.next #4 N
            second.next = prev #N 3
            prev = second #3 4
            second = tmp #4 N
        first, second = head, prev #1 4
        while second: #4 3
            tmp1, tmp2 = first.next, second.next #2 3, 3 4
            first.next = second #4
            second.next = tmp1 #2
            first, second = tmp1, tmp2 #2 3


#5/11/24 refresher again:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reversing 2nd half of list
        second = slow.next # slow would be on 2 if 1 2 3 4 , so connecting 2 to 3, so second = 3
        prev = slow.next = None #N
        while second: #3, 4
            tmp = second.next #4, N
            second.next = prev #N, 3
            prev = second #3, 4
            second = tmp #4, N
        #join together both halves of list
        first, second = head, prev #1 4
        while second: #4, 3
            tmp1, tmp2 = first.next, second.next #2 3, 4 
            first.next = second #4
            second.next = tmp1 #2
            first, second = tmp1, tmp2 #2 3


#5/13/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #3
        prev = slow.next = None #setting 2.next > 3
        while second: #3, 4, N
            tmp = second.next #4, N
            second.next = prev #keeps moving
            prev = second #3, 4
            second = tmp #4, N
        first, second = head, prev #1 4
        #join two halves together
        while second: #4
            tmp1, tmp2 = first.next, second.next #2 3
            first.next = second #4
            second.next = tmp1 #1
            first, second = tmp1, tmp2

#5/14/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        #find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #3
        prev = slow.next = None #breakage, so 2.next > None
        while second: #3, 4
            tmp = second.next #4
            second.next = prev #N
            prev = second #3
            second = tmp #4
        first, second = head, prev #1, 4
        while second:  #3
            tmp1, tmp2 = first.next, second.next #2, 3
            first.next = second #1 > 4
            second.next = tmp1 #4 > 2
            first, second = tmp1, tmp2 #2, 3

#5/17/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        #find mid
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second: #3 4
            tmp = second.next #4, N
            second.next = prev #N
            prev = second #3, 4
            second = tmp #4, N
        first, second = head, prev #1, 4
        while second:
            tmp1, tmp2 = first.next, second.next #2 3
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
