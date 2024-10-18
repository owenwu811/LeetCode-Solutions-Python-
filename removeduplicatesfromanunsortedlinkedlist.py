
#1836
#medium


#Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.

#Return the linked list after the deletions.

#Input: head = [1,2,3,2]
#Output: [1,3]
#Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].


#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        print(tmp)
        d = dict()
        for t in tmp:
            if t not in d:
                d[t] = 0
            d[t] += 1
        ans = []
        for t in tmp:
            if t in d:
                if d[t] > 1:
                    continue
                ans.append(t)
            else:
                ans.append(t)
        print(ans)
        dummy = ListNode(None)
        cur = dummy
        for a in ans:
            cur.next = ListNode(a)
            cur = cur.next
        return dummy.next
