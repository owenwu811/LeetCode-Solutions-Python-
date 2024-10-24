
#think about this problem like folding a piece of paper many times!


#Input: head = [1,2,3,4]
#Output: [1,4,2,3]

#Input: head = [1,2,3,4,5]
#Output: [1,5,2,4,3]

#python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        slow, fast = head, head.next
        while fast and fast.next: #2, 3
            slow = slow.next #2
            fast = fast.next.next #4
        second = slow.next #3
        prev = slow.next = None #3.next = None
        while second: #3, 4
            tmp = second.next #4, None
            second.next = prev #None, 3
            prev = second #3, 4
            second = tmp #4, None
        first, second = head, prev #1, 4
        while second: #4
            tmp1, tmp2 = first.next, second.next #2, 3
            first.next = second #4
            second.next = tmp1 #2
            first, second = tmp1, tmp2 #2, 3


#by the time we finish, slow will be at 2 if [1, 2, 3, 4]!, and slow.next will be 3!, so it will be one to the left if length is even!
#by the time we finish, slow will be perfectly in middle at 3 if [1, 2, 3, 4, 5]!, and slow.next will be 4! so it will be perfectly in middle if length is odd because just plopped in middle!


#5/11/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        #find the middle of the linked list as either the left as even length or exact middle as odd length input
        slow, fast = head, head.next
        while fast and fast.next: #2
            slow = slow.next #2
            fast = fast.next.next #4
        second = slow.next #3
        prev = slow.next = None #N
        #reverse 2nd half of the linked list
        while second: #3 4
            tmp = second.next #4 N
            second.next = prev #N 3
            prev = second #3 4
            second = tmp #4 N
        first, second = head, prev #1 4
        while second: #4 3
            tmp1, tmp2 = first.next, second.next #2 3, 3 4
            first.next = second #4
            second.next = tmp1 #2
            first, second = tmp1, tmp2 #2 3


#5/11/24 refresher again:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reversing 2nd half of list
        second = slow.next # slow would be on 2 if 1 2 3 4 , so connecting 2 to 3, so second = 3
        prev = slow.next = None #N
        while second: #3, 4
            tmp = second.next #4, N
            second.next = prev #N, 3
            prev = second #3, 4
            second = tmp #4, N
        #join together both halves of list
        first, second = head, prev #1 4
        while second: #4, 3
            tmp1, tmp2 = first.next, second.next #2 3, 4 
            first.next = second #4
            second.next = tmp1 #2
            first, second = tmp1, tmp2 #2 3


#5/13/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #3
        prev = slow.next = None #setting 2.next > 3
        while second: #3, 4, N
            tmp = second.next #4, N
            second.next = prev #keeps moving
            prev = second #3, 4
            second = tmp #4, N
        first, second = head, prev #1 4
        #join two halves together
        while second: #4
            tmp1, tmp2 = first.next, second.next #2 3
            first.next = second #4
            second.next = tmp1 #1
            first, second = tmp1, tmp2

#5/14/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        #find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #3
        prev = slow.next = None #breakage, so 2.next > None
        while second: #3, 4
            tmp = second.next #4
            second.next = prev #N
            prev = second #3
            second = tmp #4
        first, second = head, prev #1, 4
        while second:  #3
            tmp1, tmp2 = first.next, second.next #2, 3
            first.next = second #1 > 4
            second.next = tmp1 #4 > 2
            first, second = tmp1, tmp2 #2, 3

#5/17/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        #find mid
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second: #3 4
            tmp = second.next #4, N
            second.next = prev #N
            prev = second #3, 4
            second = tmp #4, N
        first, second = head, prev #1, 4
        while second:
            tmp1, tmp2 = first.next, second.next #2 3
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#5/22/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev #1 4
        while second:
            tmp1, tmp2 = first.next, second.next #2 3
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#5/27/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next #saving 3 (1st node of 2nd half)
        prev = slow.next = None #2.next > None
        while second: #3, 4
            tmp = second.next #4, N
            second.next = prev #N, 3
            prev = second #3
            second = tmp #4
        first, second = head, prev #1, 4
        while second: #4
            tmp1, tmp2 = first.next, second.next # 2 3
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#5/30/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev #1 4
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#6/19/24 review (missed 2 days ago):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next: #find middle of list, so 1 > 2 > 3 > 4 (2 is middle since even number means one to left)
            slow = slow.next 
            fast = fast.next.next
        second = slow.next #
        prev = slow.next = None
        while second: #reverse 2nd half of list
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev #1, 4
        while second: #merge two halves
            tmp1, tmp2 = first.next, second.next #2, 3
            first.next = second 
            second.next = tmp1
            first, second = tmp1, tmp2


#first.next = second (note that 4 is still connected to 3 from before):
1 -> 4
      |
      v
2     3

#second.next = tmp1
1 -> 4 -> 2
            |
            v
          3
#first, second = tmp1, tmp2
first:  2
second: 3

#iteration 2 - store next pointers: - why do they point to null? because the linked list looks like right before the final while loop (merging two halves step):
First half:  1 -> 2
Second half (reversed):  4 -> 3
#tmp1, tmp2 = first.next, second.next
tmp1: null
tmp2: null

#first.next = second
1 -> 4 -> 2 -> 3
#second.next = tmp1
1 -> 4 -> 2 -> 3 -> null

#move first and second to next nodes:
#first, second = tmp1, tmp2
first:  null
second: null

#since second is now None, our final linked list:
1 -> 4 -> 2 -> 3


#initial list: 1 -> 2 -> 3 -> 4
#find middle of linked list: initial pointers:
slow = 1
fast = 2
#Move slow and fast pointers:
slow = 2
fast = 4
#after finding middle:
1 -> 2  (slow)
      \
       3 -> 4  (fast)
#Step 2: Reversing the Second Half of the List
#split the list:
First half:  1 -> 2
Second half: 3 -> 4
#reverse second half:
3 -> 4
#after first iteration:
3 -> NULL
4 -> 3
#after reversing:
1 -> 2

4 -> 3
#merging two halves:
#Initial positions:
first = 1
second = 4
#Merge step-by-step:

#First iteration:
1 -> 4
     |
     v
2    3
#Second iteration:
1 -> 4 -> 2 -> 3

#final list:
1 -> 4 -> 2 -> 3

#7/9/24 refresher (missed yesterday):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev #1 4
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

#7/12/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first, second = head, prev 
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        

#7/14/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


#my own way of doing it on 10/24/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        beg = head
        tmp = deque()
        while beg:
            tmp.append(beg.val)
            beg = beg.next
        print(tmp)
        new = []
        turn = 0
        while tmp:
            if tmp:
                new.append(tmp.popleft())
            if tmp:
                new.append(tmp.pop())
        print(new)
        beg = head
        for n in new:
            beg.val = n
            beg = beg.next
