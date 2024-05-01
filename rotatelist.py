#Given the head of a linked list, rotate the list to the right by k places.

#input: head = [1,2,3,4,5], k = 2
#output: [4,5,1,2,3]

#python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: #if our input is an empty linked list, we can't do any rotations, so just return the empty linked list
            return head
        #get the length of our linked list
        #since the above if condition failed, we know we have atleast one input node in our linked list, so set length to 1
        length, tail = 1, head #we also know our head node is not None at this point because the above if condition failed, so set tail to head
        while tail.next:
            tail = tail.next
            length += 1 #we are trying to get the length of our list, so increment length by 1 since we already checked that that next node is not None before moving to it
        k = k % length #reduce k to a number that is less than the length
        if k == 0: #if k is equal to 0, means that the number of rotations is a multiple of length of linked list, so don't do any rotations
            return head
        #move to pivot and perform the rotate
        cur = head
        #how many times to move to find the pivot point
        for i in range(length - k - 1): #because we already started on node 1, so two moves to get to 3, so if length = 5 and k = 2, 5 - 2 - 1 = 2 moves
            cur = cur.next
        #current is now at the node we will do the pivot aka 3
        newhead = cur.next
        cur.next = None #the pivot position because we end linked list with None, so to not have linked list overlap in the smaller valued half of the list aka what will go in 2nd half of output
        #set tail to beginning of linked list
        tail.next = head
        return newhead


#practice again 4/30/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail, length = head, 1
        while tail.next:
            tail = tail.next
            length += 1 #traversing the list and finding the length
        k = k % length
        if k == 0:
            return head
        cur = head
        for i in range(length - k - 1): #2 moves to go from 1 to 3
            cur = cur.next
        result = cur.next #4
        cur.next = None #3 > None
        tail.next = head
        return result
        

#5/1/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail, length = head, 1
        while tail and tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return head
        cur = head
        for i in range(length - k - 1): #move to pivot point
            cur = cur.next
        result = cur.next
        cur.next = None
        tail.next = head
        return result
