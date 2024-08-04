
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
        while right: #r = 3. the idea is to keep the distance between left and right exactly n nodes, and when right reaches none too far to the right of the linked list, delete the nth node with left by cutting off by pointing left.next to left.next.next to cut it, so if n = 2, remove 4 from [1, 2, 3, 4, 5]
            left = left.next 
            right = right.next #r turns from 3 to 4, so it dosen't matter if right = right.next or left = left.next comes first. use [1, 2, 3, 4, 5] n = 2 example
        left.next = left.next.next #cut off the nth node with left pointer
        return dummy.next

#practice again:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None, head) #none or 0 works here. look at ListNode class definition. None and head are parameters passed to the constructor of the ListNode class!
        l = dummy
        r = head
        while n > 0 and r:
            r = r.next
            n -= 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next
            

#4/12/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while right and n > 0:
            right = right.next
            n -= 1
        while right: #we always need to check that right is not too far out of bounds to the right of the linked list
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

#practice again:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

#4/13/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while n > 0 and r: #make gap between l and r exactly n length nodes
            r = r.next
            n -= 1
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next #the list is already with the nth element cut off, so return the head of the list, synonymous with the entire list at that point cause linked lists are pointers to the next node

#4/15/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while n > 0 and r:
            r = r.next
            n -= 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next

#4/20/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while r and n > 0:
            r = r.next
            n -= 1 #the difference between l and r pointers to be n LENGTH of nodes
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next


#4/29/24 (missed):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0, head)
        l = prev
        r = head
        while r and n > 0: #use n as decrementer
            r = r.next
            n -= 1 #use n as decrementer to signal n distance length between l and r
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return prev.next

#4/29/24 practice again:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode(0, head)
        l = prev
        r = head
        while n > 0 and r:
            r = r.next
            n -= 1 #0 > 0 is False, so l and r are n distance length nodes apart
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return prev.next

#4/30/24 refresher:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        prev = ListNode(0, head)
        l = prev
        r = head
        while n > 0 and r:
            r = r.next
            n -= 1
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return prev.next
        
        

#5/11/24 practice (my own solution):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #remove the nth to last node and return the head
        #make the difference between slow and fast n length!
        prev = ListNode(0, head)
        cur = head
        while cur and n > 0:
            cur = cur.next
            n -= 1
        slow = prev
        while cur:
            cur = cur.next
            slow = slow.next
        slow.next = slow.next.next
        return prev.next


#5/16/24 practice:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        while n > 0 and fast: # we want to make distance of n from slow and fast
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        

#8/4/24 refresher (missed today and on 7/22/24!):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        while right and n > 0: #we must use n > 0 here because we want to make a difference in length between left and right exactly n length!
            right = right.next
            n -= 1 #accounts for how big we want the gap to be
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
        
