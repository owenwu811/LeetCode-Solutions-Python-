#medium
#61.2% acceptance rate

#You are given the head of a linked list with n nodes.

#For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

#Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

#correct python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        tmp = []
        while head: #put all nodes in linked list into an array
            tmp.append(head.val)
            head = head.next
        res = [0] * len(tmp) #create a result array the same length as the input
        stack = []
        for i in range(len(tmp)):
            while stack and tmp[stack[-1]] < tmp[i]: #as soon as the current is bigger than the rear of stack, set rear of stack index in res to be this element value
                res[stack.pop()] = tmp[i] #setting the res's appropriate index to the current value in the temp array we created since current is bigger than value of index saved in stack
            stack.append(i) #stack saves the indicies where there was nothing smaller before than current 
        return res
