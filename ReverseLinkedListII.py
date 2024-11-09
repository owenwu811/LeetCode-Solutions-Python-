#Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


#Example 1:


#Input: head = [1,2,3,4,5], left = 2, right = 4
#Output: [1,4,3,2,5]
#Example 2:

#Input: head = [5], left = 1, right = 1
#Output: [5]
 

#Constraints:

#The number of nodes in the list is n.
#1 <= n <= 500
#-500 <= Node.val <= 500
#1 <= left <= right <= n
 

#Follow up: Could you do it in one pass?



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #head is the next pointer dummy will point at
        leftprev, current = dummy, head 
        for i in range(left - 1): #each time we shift
            leftprev, current = current, current.next
        #next, we want to reverse the links in the portion of the linked list that left and right include as edges - this is phase 2 of algorithm
        #we need to execute the loop (right - left + 1) times because 4 - 2 = 2, but there are 3 nodes - 2, 3, and 4.
        #now, current is pointing to left, and left previous is pointing to the node before left
        prev = None
        for i in range(right - left + 1):
            #before reassigning, we have to save the node 
            tmpNext = current.next
            #each time we iterate, we want to break and reverse the link 
            current.next = prev
            prev, current = current, tmpNext
        #phase 3 is updating the pointers
        leftprev.next.next = current
        leftprev.next = prev #prev is right node
        return dummy.next #new head is here 


#11/18/23 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(None) 
        dummy.next = head #dummy can be set to 0 or None...
        leftprev = dummy
        cur = head
        for i in range(left - 1): # the purpose of this for loop and it's inner block is to iterate the current node right until current reaches left, which is the starting point of the window of the portion of the linked list
            leftprev = cur 
            cur = cur.next
        prev = None #this line and the below for loop is essentially the exact same algorithm as from the linked list 1 problem
        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev = cur 
            cur = tmpNext
        leftprev.next.next = cur
        leftprev.next = prev
        return dummy.next

        #the purpose of the 3rd and 2nd to last lines is reconnecting our new reversed list portion to the head and tail of the original, unreversed list? meaning that the variable on the right hand side of = is from the original, unreversed list


#my own solution using python3 on 11/9/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        print(tmp)
        first, second = left - 1, right - 1
        tmp[first: second + 1] = tmp[first: second + 1][::-1]
        dummy = ListNode(None)
        cur = dummy
        for t in tmp:
            cur.next = ListNode(t)
            cur = cur.next
        return dummy.next
