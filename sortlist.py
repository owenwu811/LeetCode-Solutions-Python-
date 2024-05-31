#Given the head of a linked list, return the list after sorting it in ascending order.
#Input: head = [4,2,1,3]
#Output: [1,2,3,4]


#python3 solution:

#merge sort 
#1. start with left as head of input list and right as middle node
#2. chop list in a half for first time 
#3. chop left and right lists in a half with self.sortList
#4. merge the lists with sorting done in merge function by comparing node values 

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #this is the base case when the list can't be split anymore - left = sortList(4) when we have 4 > 2, and then we have 4, and right = 2, but left is just 4, and so 4.next = None, so just return head, or, 4, and right is just 2, so 2.next = None, so just return head, or, 2. since we now finished dividing, we go from "return head" to "self.merge(left, right)", and list1 = 4, and list2 = 2, so we want to merge them in order
            return head
        left, right = head, self.getMid(head) #left starts at 4 in 4 > 2 > 1 > 3, and right starts at the return value of getMid(4), which will return 2, so right becomes 2
        tmp = right.next #dividing in half for the first time. right is 2, so tmp = right.next means tmp becomes 1 in 4 > 2 > 1 > 3
        right.next = None #so since right is 2 in 4 > 2 > 1 > 3, we set 2 to None. linked list now looks like 4 > 2 > N with left = 4, and right = 2
        right = tmp #since the list now looks like 4 > 2 > N | 1 > 3, we set right to 1 when right was previously 2
        #this self.sortList(left) and self.sortList(right) should really be called cut in half because the merging and sorting part are done in the merge function by comparing node values and creating a new linked list
        left, right = self.sortList(left), self.sortList(right) #left = 4 in 4 > 2 > N, so we call sortList(4), and since there is a head and a head.next, we go onto skip base case, so we do left = 4 in 4 > 2 > N, and right = self.getMid(4) with 4 > 2 > N. slow = 4, fast = 2. fast.next is None, so we just return slow of 4. left and right in line 14 are now both on 4 - list still looks like 4 > 2 > N, but now tmp becomes 2, and right.next = None means list goes from 4 > 2 > N to 4 > N, and then right is set to 2, so list is now 4 > N | 2 > N. now, when we call self.sortList(4) and self.sortList(2), we get the base case where left = 4 > N, and right = 2 > N, and then we call "return self.merge(left, right)"
        return self.merge(left, right) #so we get 2 > 4 > N, and when we call self.sortList(right) to backtrack, so we call self.sortList(1) with the list being 1 > 3 > N, and since no base case reached, we call self.getMid(1), so slow = 1, fast = 3 in 1 > 3 > N. fast.next is None, so we just return the slow value of 1, so "left, right = head, self.getMid(head) " results in left = 1 and right = 1, and the linked list is 1 > 3 > N. tmp becomes right.next, which is 3, and then right.next = None, so 1.next = None, so list is 1 > N | 3 > N, with left and right being 1, but then right = tmp means that right becomes 3 in 1 > N | 3 > N, and then we cut in half again to call self.sortList(left), which is self.sortList(1), and the base case is hit because 1 > N | 3 > N where left = 1 and right = 3, so base case is hit for both self.sortList(1) and self.sortList(3), so now left = 1 > N, and right = 3 > N, so list1 becomes 1 > N, and list2 becomes 3 > N, and the merge function returns 1 > 3 > N 
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, list1, list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 and not list2:
            tail.next = list1
        elif list2 and not list1:
            tail.next = list2
        return dummy.next #the return values is 2 > 4 > N


#5/12/24 afternoon (missed):

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, self.getMid(head)
        #without "tmp = right.next" and "right = tmp", THE RIGHT POINTER IS NEVER MOVED TO THE NEXT NODE "RIGHT = TMP"!!! so the algorithm would consider the same sublist REPEATEDLY FOREVER! YOU WOULD JUST BE SORTING THE SAME SUBLIST OVER AND OVER AGAIN!
        tmp = right.next #without tmp, we wouldn't be getting to 2nd half of list, so we would have a cycle error 
        right.next = None
        right = tmp #MOVES RIGHT POINTER TO THE FIRST NODE OF THE RIGHT HALF AFTER SEPERATING THE LIST, ALLOWING THE ALGORITHM TO PROGRESS AND AVOID UNECESSARY ITERATIONS!
        left, right = self.sortList(left), self.sortList(right)
        return self.merge(left, right)
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, list1, list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 and not list2:
            tail.next = list1
        elif list2 and not list1:
            tail.next = list2
        return dummy.next


#5/13/24 refresher:

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        left, right = self.sortList(left), self.sortList(right)
        return self.merge(left, right)
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, list1, list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 and not list2:
            tail.next = list1
        elif list2 and not list1:
            tail.next = list2
        return dummy.next


#5/16/24 refresher:

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp 
        left, right = self.sortList(left), self.sortList(right)
        return self.merge(left, right)
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, list1, list2):
        dummy = cur = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2 
                list2 = list2.next
            cur = cur.next
        if list1 and not list2:
            cur.next = list1
        if list2 and not list1:
            cur.next = list2
        return dummy.next


#5/20/24:

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        left, right = self.sortList(left), self.sortList(right)
        return self.merge(left, right)
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, list1, list2):
        dummy = head = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1 and not list2:
            cur.next = list1
        if list2 and not list1:
            cur.next = list2
        return dummy.next


#5/24/24 review:

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp #2nd half of list
        left, right = self.sortList(left), self.sortList(right)
        return self.merge(left, right)
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 and not l2:
            cur.next = l1
        elif l2 and not l1:
            cur.next = l2
        return dummy.next

#5/31/24 review:

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, self.getMid(head)
        tmp = right.next #3
        right.next = None #N
        right = tmp #3
        left, right = self.sortList(left), self.sortList(right)
        return self.merge(left, right)
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, l1, l2):
        dummy = ListNode(None) 
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 and not l2:
            cur.next = l1
        elif l2 and not l1:
            cur.next = l2
        return dummy.next
