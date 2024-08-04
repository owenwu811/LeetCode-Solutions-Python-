
#You are given the head of a linked list, and an integer k.

#Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

#Input: head = [1,2,3,4,5], k = 2
#Output: [1,4,3,2,5]

#my own solution in python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = [] #the idea is to put every element in an array, and then iterate until you hit k from both ends, swap them, and then convert the array back into a linked list
        while head:
            tmp.append(head.val)
            head = head.next
        end = len(tmp) - k
        for i in range(len(tmp) - end):
            print(i)
        beg = i
        tmp[beg], tmp[end] = tmp[end], tmp[beg]
        cur = dummy = ListNode(0)
        for e in tmp:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
