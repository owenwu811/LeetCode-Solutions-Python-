
#25
#Hard

#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

#k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

#You may not alter the values in the list's nodes, only nodes themselves may be changed.


#my own solution using python3 on 12/3/24:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next 
        print(tmp)
        for i in range(0, len(tmp) - k + 1, k):
            subarr = tmp[i: i + k]
            print(subarr)
            tmp[i:i + k] = reversed(tmp[i: i + k])
            #print(tmp)
        print(tmp)
        dummy = ListNode(None)
        cur = dummy
        for t in tmp:
            cur.next = ListNode(t)
            cur = cur.next 
        return dummy.next

#high level overview:

#use a pointer to try to traverse k nodes in the linked list
#if the pointer successfully traverses a group of k nodes, reverse this group
#reconnect the reversed group of k nodes with the rest of the linked list
#repeat this process until less than k or no nodes are left in the linked list


#step by step explanation:

#initialize a node dummy, and attach it to start of linked list it by setting its next pointer equal to the head
#we set a pointer, ptr, equal to dummy. we will use this pointer to traverse the linked list
#we traverse the linked list till ptr becomes NULL:
    #we initialize a pointer, tracker, to ptr. this pointer will be used to keep track of the number of nodes in the current GROUUP in the linked list
    #we use a nested loop to try to move tracker k nodes forward in the linked list. If tracker becomes NULL before moving k nodes forward, the end of the linked list has been reached and the current group cannot be reversed since it contains less than k nodes. Therefore, we break out of the nested loop. Otherwise, the current group contains k nodes and tracker will pointer to the kth node of the current group. 
#after completion of the nested loop, we check if tracker points to NULL:
    #if it does, we've reached the end of the linked list. the current group contains less than k nodes and cannot be reversed. Therefore, we break out of the outer loop, and the algorithm ends
    #if it does not, the current group contains k nodes and can therefore be reversed



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_linked_list(head, k):
            prev, curr = None, head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, curr
        # Create a dummy node and set its next pointer to the head
        dummy = ListNode(0) #dummy = 0, head = 1
        dummy.next = head #connect to beg of list (0 to 1)
        ptr = dummy #ptr = 0 (dummy)
        while True:
            #tracker = 0 (ptr) because head (1)
            #k = distance, so k = 3 means move tracker forward 3 times
            #reason tracker starts at 0 and not 1 is because k = 3, so tracker = 0 head = 1, so for all 3 iterations (012), we move 3 times from (0 to 1), (1 to 2), and then (2 to 3) for i = 0, 1, 2
            tracker = ptr #tracker is to determine if a group of k nodes exists in the linked list
            # Check if there are k nodes left to reverse
            for i in range(k): 
                tracker = tracker.next #to move the tracker pointer k nodes forward
                if tracker == None: # 1 2 3 - if tracker = None, then we would only have 1 2 because tracker started at 0, so 3 jumps means k = 3 was satisfied
                    return dummy.next #dummy.next was head, so we return head if we cannot reverse the current group of k nodes (head is at position 1 but is now actually 3 for our test case - not important to remember the 3 but just know that dummy (0) and head (1) at beg AND HEAD STAYED AT POSITION 1 THROUGHOUT THE ENTIRE ALGORITHM!!!)
            #since k nodes have been successfully traversed, we can reverse the current group of k nodes. we will do this through the use of three pointers: current (initialized to the head pointer), previous (initialized to NULL), and next (initialized to NULL)
            # Reverse k nodes
            previous, current = reverse_linked_list(ptr.next, k)
            # Reconnect the reversed sublist with the previous part
            last_node_of_reversed_group = ptr.next #initialize a new pointer and set it equal to ptr.next, so this pointer will point to the last node of the reversed group - remember that ptr and head were stuck at 0 and 1, so last_node_of_reversed_group is now on head (ptr (0) and head + last_node_of_reversed_group(1))
            last_node_of_reversed_group.next = current #head (1) tracker (3) current (4) because k = 3, so last_node_of_reversed_group now pointers to (current) 4
            ptr.next = previous #ptr.next (0) head (1) now pointers to (3 tracker + previous) while 4 (current + next)
            # Move the pointer to the end of the reversed sublist
            ptr = last_node_of_reversed_group #ptr now pointers to last_node_of_reversed_group (1)
        return dummy.next




#ptr.next acts like head here!

#7/10/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def r(head, k):
            prev, cur = None, head
            while k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev, cur
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while True:
            traverse = ptr
            for i in range(k):
                traverse = traverse.next
                if not traverse:
                    return dummy.next
            previous, current = r(ptr.next, k)
            lastnode = ptr.next
            lastnode.next = current
            ptr.next = previous
            ptr = lastnode
        return dummy.next

#7/11/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def r(head, k):
            prev, cur = None, head
            while k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev, cur
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while True:
            traverse = ptr
            for i in range(k):
                traverse = traverse.next
                if not traverse:
                    return dummy.next
            previous, current = r(ptr.next, k) #notice the indentation here because we must finish looping through an entire group of k nodes before reversing!
            lastnode = ptr.next
            lastnode.next = current
            ptr.next = previous
            ptr = lastnode
        return dummy.next

#7/14/24 refresher (missed today):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        def reverse(head, k):
            prev, cur = None, head
            while k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev, cur
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while True:
            traverse = ptr
            for i in range(k):
                traverse = traverse.next
                if not traverse: return dummy.next
            previous, current = reverse(ptr.next, k)
            rightoneofptr = ptr.next
            rightoneofptr.next = current
            ptr.next = previous
            ptr = rightoneofptr
        return dummy.next

#7/15/24 practice:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, cur = None, head
            while k > 0:
                curnext = cur.next
                cur.next = prev
                prev = cur
                cur = curnext
                k -= 1
            return prev, cur
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        while True:
            traverse = ptr
            for i in range(k): #each group
                traverse = traverse.next
                if not traverse:
                    return dummy.next
            previous, current = reverse(ptr.next, k)
            leftfromcur = ptr.next
            leftfromcur.next = current
            ptr.next = previous
            ptr = leftfromcur
        return dummy.next

#7/21/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, cur = None, head
            while k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev, cur
        dummy = ListNode(None)
        dummy.next = head
        ptr = dummy
        while True:
            traverse = ptr
            for i in range(k):
                traverse = traverse.next
                if not traverse:
                    return dummy.next
            previous, current = reverse(ptr.next, k)
            rightone = ptr.next
            rightone.next = current
            ptr.next = previous
            ptr = rightone
        return dummy.next

#8/5/24 refresher (missed a couple of days ago):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, cur = None, head
            while k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev, cur
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while True:
            traverse = ptr
            for i in range(k):
                traverse = traverse.next
                if not traverse:
                    return dummy.next
            previous, current = reverse(ptr.next, k)
            rightone = ptr.next
            rightone.next = current
            ptr.next = previous
            ptr = rightone
        return dummy.next


#8/21/24 review (missed):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, cur = None, head
            while k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev, cur
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while True:
            traverse = ptr
            for i in range(k): #making the current part of length k
                traverse = traverse.next
                if not traverse:
                    return dummy.next
            #reversing the k length group
            previous, current = reverse(ptr.next, k)
            #same pattern as reversing linked list
            rightone = ptr.next #rightone is like nxt while ptr is like cur
            rightone.next = current
            ptr.next = previous
            ptr = rightone
        return dummy.next



