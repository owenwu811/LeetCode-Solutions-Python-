#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#Input: head = [1,2,3,4]
#Output: [2,1,4,3]


#python3 solution:

#idea is to get each pair of nodes, and reverse the pointer from the 2nd node in each pair to the 1st node in each pair, and you do this for each pair in the linked list input

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
            cur.next = nxt # so this is where the swapping takes place! so 1 > 2 now becomes 2 > 1!!!!! the positions change!
            #so after swapping, the pointers.next point to the same value, but in different positions now!!!!!
            prev.next = rightone #and because it's now swapped, rightone is still 2, so prev.next points to 2, which is now the 1st node in the linked list!
            prev = cur #and then prev actually goes to cur, which is 1, which is now the 2nd node in the linked list since positions were swapped!
            cur = nxt
        return dummy.next


# rightone = cur.next was essentially just saving the value of 2 so that when we point prev.next at rightone, it actually points to 1, but then we do prev = cur, which is actually setting prev to 1 since we swapped positions, which is the 2nd position node!
#cur.next = nxt  - so then this line is just paving the path so that we don't have empty nodes


# then in the end, dummy.next will point to 2 because dummy.next always points to the head of the new linked list


#5/14/24 practice:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prev, cur = dummy, head
        while cur and cur.next:
            tmp = cur.next.next
            rightone = cur.next
            rightone.next = cur #pointing 2 at 1, essentially swapping the positions, so 1 is now in 2nd place and 2 is now in 1st place
            cur.next = tmp #pointing 1 at 3 for connection lack of breakage
            prev.next = rightone
            prev = cur
            cur = tmp
        return dummy.next

#5/15/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next #saving the place for after swap
            second = cur.next #2
            second.next = cur #1
            cur.next = nxt
            prev.next = second
            prev = cur
            cur = nxt
        return dummy.next

#5/16/24 practice:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next
            rightone = cur.next #2
            rightone.next = cur # swapping positions from 1 2 to 2 1
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next

#5/19/24 practice (missed):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next
            rightone = cur.next
            rightone.next = cur
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next


#5/20/24 practice:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next
            rightone = cur.next
            rightone.next = cur #swapping places
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next


#5/21/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next
            rightone = cur.next
            rightone.next = cur
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next
        
#5/22/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next: #there are atleast 2 pairs to swap 
            nxt = cur.next.next #next node after pair 
            rightone = cur.next #2nd node of current pair
            rightone.next = cur #performing swap 
            cur.next = nxt
            prev.next = rightone
            prev = cur #move prev and cur pointers two steps forward to the next pair to be swapped 
            cur = nxt
        return dummy.next

#another solution that makes more sense:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        for i in range(0,len(lst)-1,2):
            lst[i],lst[i+1]=lst[i+1],lst[i]
        a = ListNode(0)
        temp = a
        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next

#6/7/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next
            rightone = cur.next
            rightone.next = cur
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next

#7/4/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next
            rightone = cur.next
            rightone.next = cur
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next

#7/5/24 review:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next
            rightone = cur.next
            rightone.next = cur
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next

#7/22/24 refresher:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        prev = dummy
        cur = head
        while cur and cur.next:
            nxt = cur.next.next
            rightone = cur.next
            rightone.next = cur
            cur.next = nxt
            prev.next = rightone
            prev = cur
            cur = nxt
        return dummy.next


#my own solution on 10/19/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        print(tmp)
        for i in range(1, len(tmp), 2):
            tmp[i], tmp[i - 1] = tmp[i - 1], tmp[i]
        print(tmp)
        dummy = ListNode(None)
        cur = dummy
        for t in tmp:
            cur.next = ListNode(t)
            cur = cur.next
        return dummy.next
