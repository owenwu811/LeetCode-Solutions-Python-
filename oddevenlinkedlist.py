
#Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

#The first node is considered odd, and the second node is even, and so on.

#Note that the relative order inside both the even and odd groups should remain as it was in the input.

#You must solve the problem in O(1) extra space complexity and O(n) time complexity.

#input: head = [1,2,3,4,5]
#output: [1,3,5,2,4]


#python3 solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        # head = [1,2,3,4,5]
        if not head or not head.next:
            return head
        #1st node NOT THE NONE NODE BEFORE FIRST (1) is odd, so odd_head becomes 1
        #odd_head just saves the 1
        odd_head = odd = head #odd_head becomes 1
        #2nd node is even (2) is even, so even_head becomes 2
        #even_head just saves the 2 that starts linking to 4 and 6
        even_head = even = head.next #even_head, even, head.next become 2
        while even and even.next: #even will end at 4, and even.next will be 5 because even starts at 2. when even becomes 6, this while loop will becomes False
            #remember that odd starts at 1, so odd.next becomes 3
            odd.next = even.next #since even was 2, even.next = 3, and if odd.next is set to even.next, odd.next becomes 3. odd.next becomes 5
            odd = odd.next #odd becomes 3. odd becomes 5
            #remember that even starts at 2, so even.next becomes 4
            even.next = odd.next #even.next becomes 4. even.next becomes 6
            even = even.next #even becomes 4. even becomes 6
        odd.next = even_head #odd.next becomes 2
        return odd_head #return 1


#practice again:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first node = odd while second node = even
        if not head or not head.next:
            return head #return type of of listnode
        oddstart = odd = head 
        evenstart = even = head.next 
        while even and even.next: #ends on 4 being the last True
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenstart
        return oddstart


#4/27/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #no comparisons to be done if 0 elements or 1 element in input linked list
            return head
        oddsaver = odd = head  #1
        evensaver = even = head.next #2
        while even and even.next: 
            odd.next = even.next
            odd = odd.next
            even.next = odd.next 
            even = even.next #during the last iteration, odd = 5, and even becomes None, not 6, so then while loop will evaluate and become False - in python, the end of a linked list is always signaled by None!
        odd.next = evensaver #odd is 5, and evensaver is 2, so odd.next becomes 2
        return oddsaver

        #in python, the end of a linked list is always signaled by None, so the output of [1, 3, 5, 2, 4] is really the same as [1, 3, 5, 2, 4, N]!!!!

#4/28/24 refresher practice:

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next: #only 1 element or 0 elements
            return head 
        oddstart = odd = head
        evenstart =  even = head.next
        while even and even.next: #the end of a linked list always ends in None, so even won't ever be 6. in the last iteration, odd = 5, and even becomes None! and then the while loop will return False
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenstart
        return oddstart
        

#4/29/24 practice:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        oddstart = odd = head
        evenstart = even = head.next
        while even and even.next: #4 is last valid even. when this is False, the while loop terminates, and even = None while odd = 5
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next #even becomes 4
        odd.next = evenstart
        return oddstart


#5/1/24 practice:

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        oddstart = odd = head
        evenstart = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenstart
        return oddstart


#5/5/24:

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        oddstart = odd = head
        evenstart = even = head.next
        while even and even.next: #must not be while head and head.next because even is the one determining termination of the loop, not head! you will get a NoneTye error if you use head instead!
            odd.next = even.next 
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenstart
        return oddstart

#5/9/24 refresher:

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next: #0 or 1 nodes in input linked list
            return head
        oddstart = odd = head
        evenstart = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenstart
        return oddstart

#5/15/24 refresher:

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        oddstart = odd = head 
        evenstart = even = head.next 
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenstart
        return oddstart
