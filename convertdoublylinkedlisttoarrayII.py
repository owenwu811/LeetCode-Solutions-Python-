
#3294
#medium


#You are given an arbitrary node from a doubly linked list, which contains nodes that have a next pointer and a previous pointer.

#Return an integer array which contains the elements of the linked list in order.

 

#Example 1:

#Input: head = [1,2,3,4,5], node = 5

#Output: [1,2,3,4,5]

#Example 2:

#Input: head = [4,5,6,7,8], node = 8

#Output: [4,5,6,7,8]


#correct python3 solution:

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, node: 'Optional[Node]') -> List[int]:
        tmp = deque()
        forward = node
        while forward:
            tmp.append(forward.val)
            forward = forward.next
        node = node.prev
        while node:
            tmp.appendleft(node.val)
            node = node.prev
        return tmp
        
