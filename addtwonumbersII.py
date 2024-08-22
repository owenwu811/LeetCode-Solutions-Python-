
#You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: l1 = [7,2,4,3], l2 = [5,6,4]
#Output: [7,8,0,7]
#Example 2:

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [8,0,7]
#Example 3:

#Input: l1 = [0], l2 = [0]
#Output: [0]



#correct python3 solution (the way I was trying to do it):


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1l, l2l = [], []
        
        # Convert linked lists to lists of integers
        while l1:
            l1l.append(l1.val)
            l1 = l1.next
        while l2:
            l2l.append(l2.val)
            l2 = l2.next
        
        res = []
        carry = 0
        
        # Handle each digit from the end to the start
        while l1l or l2l or carry:
            l1val = l1l.pop() if l1l else 0
            l2val = l2l.pop() if l2l else 0
            total = l1val + l2val + carry
            carry = total // 10
            res.append(total % 10)
        
        # Convert the result list back to a linked list
        dummy = ListNode(None)
        cur = dummy
        for r in reversed(res):
            cur.next = ListNode(r)
            cur = cur.next
        
        return dummy.next
