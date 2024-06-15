
#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.

#python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            #l1 = [2,4,3], l2 = [5,6,4] > [7,0,8]
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry #last iteration, 3 + 4 + 1 = 8, so val = 8
            carry = val // 10 #print (7 // 10) = 0, not 7 because 7/10 = 0.7. floor division takes 0.7 and floors it to get 0, and then (10 // 10) > 1, so carry becomes 1, (8 // 10) > 0
            val = val % 10 # (7 % 10) results in 7, (10 % 10) results in 0, (8 % 10) > 8
            cur.next = ListNode(val) #creating a node with value 7, creating node with value 0 from above line val, creating node with value 8
            cur = cur.next #going to that new node 7, going to new node 0 because 4 + 6 = 10, which is supposed to be 0
            l1 = l1.next if l1 else None #in last iteration, l1 = None
            l2 = l2.next if l2 else None #in last iteration, l2 = None
        return dummy.next

#5/23/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


#5/24/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        cur = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry #7
            carry = val // 10 #
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

#5/25/24 practice:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

#5/30/24 practice (missed):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry
            carry = val // 10 #7 // 10 = 0.7 > round down to get 0
            val = val % 10 #7 % 10 = 7
            cur.next = ListNode(val) #ListNode(7) - we need ListNode wrapped around val or else none type has no attribute next error!
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

#5/31/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

#6/15/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        cur = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            val = l1val + l2val + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
