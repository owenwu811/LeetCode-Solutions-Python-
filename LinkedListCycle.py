#Given head, the head of a linked list, determine if the linked list has a cycle in it.

#There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

#Return true if there is a cycle in the linked list. Otherwise, return false.

 

#Example 1:


#Input: head = [3,2,0,-4], pos = 1
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#Example 2:


#Input: head = [1,2], pos = 0
#Output: true
#Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#Example 3:


#Input: head = [1], pos = -1
#Output: false
#Explanation: There is no cycle in the linked list.


My Solution:

# cycle just means that every node are linked together as the fast pointer paves the path. In a no cycle condition, fast.next reaches a none node, which means that there is some breakage, which is the definition of no cycle, so we will return False. 
# so no cycle just means there is some breakage based on the slow and fast pointer's path

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head #we are using a two pointer approach with slow and fast pointers, both of which are starting at head of the linked list
        while fast is not None and fast.next is not None: #making sure the fast exists and we are not out of bounds 
            slow, fast = slow.next, fast.next.next  #fast pointer moves through the linked list at twice the speed of slow, jumping two nodes at once 
            if slow == fast: #if slow and fast ever meet, then there is a cycle aka no disconnect assuming fast pointer paves the path, which it does in this case
                return True
        return False #if you've trasversed through the entire list, and slow and fast never meet, or fast is on None, then there is not a cycle


#12/25/23 refresher - my solution in python3:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        #fast.next is not None is used to ensure the bridge between fast (current node) and fast.next.next (destination) exist to avoid Nonetype error
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


#2/28/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#3/2/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


#3/10/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow, fast = slow.next, fast.next.next
            if slow == fast: return True
        return False

#4/16/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#5/15/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#6/11/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


#7/14/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: #means they lapped each other aka cycle where no gaps if we use both pointers through entire rink
                return True
        return False

#10/18/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
