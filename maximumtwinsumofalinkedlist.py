

#In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

#For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
#The twin sum is defined as the sum of a node and its twin.

#Given the head of a linked list with even length, return the maximum twin sum of the linked list.


#Input: head = [5,4,2,1]
#Output: 6
#Explanation:
#Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
#There are no other nodes with twins in the linked list.
#Thus, the maximum twin sum of the linked list is 6.



#correct python3 solution:

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ll, ans = [], []
        while head:
            ll.append(head.val)
            head = head.next
        
        mid = len(ll) // 2
        while mid > 0:
            ans.append(ll[mid - 1] + ll[-mid])
            mid -= 1
        
        return max(ans)



#my own solution using python3 after looking at solution above - the key is that we know the input length is always even, so we have a left mid and right mid:

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        
        mid = len(tmp) // 2
        res = []
        lm, rm = mid - 1, mid
        while lm >= 0 and rm < len(tmp):
            res.append(tmp[lm] + tmp[rm])
            lm -= 1
            rm += 1
        return max(res)

#9/19/24 review (my own solution using python3):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        res = 0
        l, r = 0, len(tmp) - 1
        mid = ((l + r) // 2) + 1
        left, right = mid - 1, mid
        while left >= 0 and right < len(tmp):
            res = max(res, tmp[left] + tmp[right])
            left -= 1
            right += 1
        return res

