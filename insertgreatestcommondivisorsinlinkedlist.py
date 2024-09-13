
#2807. Insert Greatest Common Divisors in Linked List
#Solved
#Medium

#Topics
#Companies
#Given the head of a linked list head, in which each node contains an integer value.

#Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

#Return the linked list after insertion.

#The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.


#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        if len(tmp) == 1:
            return ListNode(tmp[0])
        #print(tmp)
        res = deque()
        for i in range(1, len(tmp)):
            greatest = gcd(tmp[i], tmp[i - 1])
            #print(greatest)
            res.append(greatest)
        #print(res)
        reslen = len(res)
        for i in range(len(tmp) + reslen):
            #print(i)
            if i % 2 == 0:
                continue
            if i % 2 != 0:
                if res:
                    tmp.insert(i, res.popleft())
        dummy = ListNode(None)
        cur = dummy
        for t in tmp:
            cur.next = ListNode(t)
            cur = cur.next

        return dummy.next
