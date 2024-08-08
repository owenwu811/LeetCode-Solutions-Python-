
#medium
#acceptancearate89.9%

#You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

#For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

#Return the head of the modified linked list.

#Input: head = [0,3,1,0,4,5,2,0]
#Output: [4,11]
#Explanation: 
#The above figure represents the given linked list. The modified list contains
#- The sum of the nodes marked in green: 3 + 1 = 4.
#- The sum of the nodes marked in red: 4 + 5 + 2 = 11.


#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        cur = head
        while cur:
            tmp.append(cur.val)
            cur = cur.next
        print(tmp)
        tmpsum = 0
        res = []
        for i in range(len(tmp)):
            if tmp[i] == 0:
                res.append(tmpsum)
                tmpsum = 0
                continue
            if tmp[i] > 0:
                tmpsum += tmp[i]
        for r in res:
            if r == 0:
                res.remove(r)
        print(res)
        dummy = cur = ListNode(0)
        for r in res:
            cur.next = ListNode(r)
            cur = cur.next
        return dummy.next

