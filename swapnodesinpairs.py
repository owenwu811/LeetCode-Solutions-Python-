#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]


#python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            nxt = cur.next.next 
            rightone = cur.next
            rightone.next = cur
            cur.next = nxt # so this is where the swapping takes place! so 1 > 2 now becomes 2 > 1!!!!!
            #so after swapping, the pointers.next point to the same value, but in different positions now!!!!!
            prev.next = rightone #and because it's now swapped, rightone is still 2, so prev.next points to 2, which is now the 1st node in the linked list!
            prev = cur #and then prev actually goes to cur, which is 1, which is now the 2nd node in the linked list since positions were swapped!
            cur = nxt
        return dummy.next


# rightone = cur.next was essentially just saving the value of 2 so that when we point prev.next at rightone, it actually points to 1, but then we do prev = cur, which is actually setting prev to 1 since we swapped positions, which is the 2nd position node!
#cur.next = nxt  - so then this line is just paving the path so that we don't have empty nodes


# then in the end, dummy.next will point to 2 because dummy.next always points to the head of the new linked list
