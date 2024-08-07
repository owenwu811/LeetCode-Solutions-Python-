
#You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

#Return the head of the linked list after doubling it.

#Input: head = [1,8,9]
#Output: [3,7,8]
#Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.



#my own solution in python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ""
        cur = head
        while cur:
            tmp += str(cur.val)
            cur = cur.next
        print(tmp)
        sys.set_int_max_str_digits(100000) #important to note here that this is required, and, without it, you pass 1205/1265 test cases
        res = int(tmp) * 2 
        print(res)
        dummy = current = ListNode(0)
        for t in str(res):
            current.next = ListNode(t)
            current = current.next
        return dummy.next
