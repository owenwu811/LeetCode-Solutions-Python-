
#1474
#easy


#You are given the head of a linked list and two integers m and n.

#Traverse the linked list and remove some nodes in the following way:

#Start with the head as the current node.
#Keep the first m nodes starting with the current node.
#Remove the next n nodes
#Keep repeating steps 2 and 3 until you reach the end of the list.
#Return the head of the modified list after removing the mentioned nodes.


#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        print(tmp)
        i = 0
        new = []
        while i < len(tmp):
            window = tmp[i: i + m]
            print(window)
            for w in window:
                new.append(w)
            i = i + n + m
        print(new)
        dummy = ListNode(None)
        cur = dummy
        for n in new:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
