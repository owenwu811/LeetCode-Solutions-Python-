
#369
#medium


#Given a non-negative integer represented as a linked list of digits, plus one to the integer.

#The digits are stored such that the most significant digit is at the head of the list.

 

#Example 1:

#Input: head = [1,2,3]
#Output: [1,2,4]
#Example 2:

#Input: head = [0]
#Output: [1]


#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        print(tmp)
        mystr = ""
        for t in tmp:
            mystr += str(t)
        b = int(mystr)
        print(int(mystr))
        final = b + 1
        print(final)
        dummy = ListNode(None)
        cur = dummy
        for f in str(final):
            cur.next = ListNode(f)
            cur = cur.next
        return dummy.next
