#You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

#Return the head of the merged linked list.

#Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]


#Solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Create a dummy node that serves as the head of the merged list
    dummy, current = ListNode(), dummy
    #current will represent the merged list
    while list1 and list2:
        if list1.val <= list2.val: #if the values are equal, merge the values from list1 into the merged list
            # current.next = list1.val instead of current.next = list1 would lose the pointer because it only takes the value of the node, not the node itself because list1.val is the value of the node, not the node itself:
            current.next = list1
            list1 = list1.next
        else: 
            current.next = list2
            list2 = list2.next
        current = current.next
    # Append the remaining nodes from list1 or list2, if any
    #at this point, the while list1 and list2 is false, so either one of the lists has no nodes left, so we ask this question
    current.next = list1 if list1 else list2
    
    # Return the head of the merged list (skip the dummy node)
    #the reason we can't just return head is because head is the head of list1 or list2, not the merged list, which we set to dummy at the beginning
    return dummy.next
    #if list1 or list2 are empty, then append the rest of the nonempty elements to the merged list automatically.


#Another Solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #we are creating the head of the merged list we will eventually return
        previousoffirst, result = ListNode(0), previousoffirst
        #result = previousoffirst - is when the dummy node is actually associated with a new merged list called result, and result doesn't actually have a head node at this point, just a previous node to the head
        #make sure list1 and list2 are not empty and actually have nodes 
        while list1 and list2:
            if list1.val <= list2.val:
                # since list1 is the smaller value, append it to the merged list
                # result.next = list1.val instead of result.next = list1 would lose the pointer because it only takes the value of the node, not the node itself because list1.val is the value of the node, not the node itself:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            #takes the smaller node from either list1 or list2 and assigns the pointer of the merged list (current) to that smaller node:
            result = result.next
        #his is basically a boolean meaning the list that still has remaining nodes will be true while the other will be false, and the true list will take over result.next variable.
        result.next = list1 or list2
        #the next of previousoffirst must be first or head, which is what we want to return when either list dosen't have any more nodes and the one with ramining nodes is already appended to the end of the merged resulting list
        return previousoffirst.next


#6/8/23 refresher (my solution):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, result = ListNode(0), head
        while list1 and list2: #make sure both lists have node elements inside
            if list1.val <= list2.val: #<= or < both work since the logic works out as if they are equal, you can append either element
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next #my mistake was putting this in the same indentation level as while loop, which means the pointer of the merged list would never point to the next element to be appended to unless either list1 or list2 was empty, which is not what we want. After merging from either list1 or list2, we want to move the pointer of the new merged list so that the next time we append from either list1 or list2 into merged, we don't override the merged element from the previous iteration aka we want to add and not replace on each iteration of the while loop.
        if not list2: #list2 is empty, and since the while list1 and list2 same indentation level, we know that either one of them must be empty, so if list2 is empty, and both list1 and list2 being full is false, that means that list1 is the non empty one, so point the merged pointer to list1's nodes.
            result.next = list1
        else: #so list1 is the empty one here because either list1 or list2 have to be empty at this point, so point merged to list2's nodes, appending list2's nodes to the end of merged list
            result.next = list2
        return head.next #the mistake was not returning head.next as head acts as a dummy node, and instructions say to return head of new merged list



7/1/23 refresher (my solution):

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy, head = ListNode(0), dummy
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if not list1 and list2:
            head.next = list2 #if list1 is empty, then you have to append the rest of list2's nodes - the ordering of this matters - you can't put list1 here instead of list2 without changing the logic
        else:
            head.next = list1 #implies not list2 and list1, so list1 has nodes, so append the rest of list1's nodes to the head result
        return dummy.next #mistake was dummy.next, not head.next, because dummy was used to associate with the linked list itself.




#8/13/23 (solution also works, but logic of line 152 is just flipped compared to above to prove the point):
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

        dummy, head = ListNode(0), dummy
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 if list1 else list2 #cleaner version
        return dummy.next


#10/2/23 (refresher):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            elif list1.val == list2.val or list2.val < list1.val:
                res.next = list2
                list2 = list2.next
            res = res.next
        if list1 is not None and list2 is None:
            res.next = list1
        elif list2 is not None and list1 is None:
            res.next = list2
        return dummy.next

#my solution python3 12/2/2023 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1 and not list2:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2 #we don't need list2 = list2.next after this because the only nodes left are list2
        #we also don't need a final curr = curr.next here because the nodes are already placed at this point!
        return dummy.next

#my solution python3 12/24/23 refresher:

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(0)
        current = first
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 and not list2:
            current.next = list1 
        elif list2 and not list1:
            current.next = list2
        return first.next


#2/25/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(None)
        current = prev
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 and not list2:
            current.next = list1
        elif list2 and not list1:
            current.next = list2
        return prev.next

#3/22/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        cur = prev
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
        elif list2 and not list1:
            cur.next = list2
        return prev.next

#4/5/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        cur = prev
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
        elif list2 and not list1:
            cur.next = list2
        return prev.next

#5/1/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        cur = prev
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
        elif list2 and not list1:
            cur.next = list2
        return prev.next

#5/27/24 review:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
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

#7/31/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
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
        elif list2 and not list1:
            cur.next = list2
        return dummy.next


#my own solution using python3 on 10/22/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one, two = [], []
        while list1:
            one.append(list1.val)
            list1 = list1.next
        while list2:
            two.append(list2.val)
            list2 = list2.next
        print(one)
        print(two)
        new = []
        for i in range(len(one)):
            print(one[i])
            new.append(one[i])
        for i in range(len(two)):
            new.append(two[i])
        print(new)
        new.sort()
        dummy = ListNode(None)
        cur = dummy
        for n in new:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next

#11/9/24 (my own solution):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = [], []
        while list1:
            first.append(list1.val)
            list1 = list1.next
        while list2:
            second.append(list2.val)
            list2 = list2.next
        first.extend(second)
        first.sort()
        print(first)
        dummy = ListNode(None)
        cur = dummy
        for f in first:
            cur.next = ListNode(f)
            cur = cur.next
        return dummy.next
