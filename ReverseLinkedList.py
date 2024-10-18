#Given the head of a singly linked list, reverse the list, and return the reversed list.

 

#Example 1:


#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]
#Example 2:


#Input: head = [1,2]
#Output: [2,1]
#Example 3:

#Input: head = []
#Output: []

#this is a variation of two pointers 

My Solution (Python):

class Solution(object):
    def reverseList(self, head):
        current, previous = head, None #we initially set current to 1.               # NULL 1 2 3 4 5
        # we initially set previous to null behind 1 # P    C
        while current is not None:
            next = current.next # N 1 2 3 3 4 5 (previous is 1, current is 2, next is 3) becomes (previous is 2 from line 31, current is 3 from line 32, and next is 4 from this line aka 29)
            current.next = previous #let's assume that prev is on 1 and current is on 2. so we put 1 in front of 2 > 2 1. In the next iteration, if current is 3 and previous is 2, we put 2 in front of 3 > 3 2. Previous value is overriding current.next, so 2 overtakes 4's last place, with 4s last place being next > 3 2
            previous = current # we are just sandwiching together previous with current's original value
            current = next # current moves onto the next pointer of the CURRENT Iteration. Next will change in the very next line. 
        return previous # for example NULL 1 2 3 3 4 5, previous will point to 5 when tthe while loop becomes false because n 1 2 3 4 5
                                                                                                                                #    P C N > current is none, so false

#2/15/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head #head refers to the beginning node of the list - pointing to 1
        previous = None
        while current is not None:
            nxt = current.next
            current.next = previous #this is where the flipping of the railroad tracks happens from the next node to the previous node from the perspective of the currentnode
            previous = current #sandwiching together to move right
            current = nxt
        return previous #when current is None, previous is the last node, which has links pointing all the way to the start of the list

#2/28/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        previous = None
        while cur != None:
            nxt = cur.next
            cur.next = previous
            previous = cur
            cur = nxt
        return previous


#4/23/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

        
#5/18/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev


#10/18/24 (my own solution using python3):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        tmp = tmp[::-1]
        dummy = ListNode(None)
        cur = dummy
        for t in tmp:
            cur.next = ListNode(t)
            cur = cur.next
        return dummy.next
