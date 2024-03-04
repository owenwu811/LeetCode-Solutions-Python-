
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.

 

#Example 1:

#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6

#python3 solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
            #there's nothing to merge
            if len(lists) == 0 or not lists:
                return None
            #as long as there is more than one sublist in lists, we have to keep merging because we want to return the last list
            while len(lists) > 1:
                merged = []
                #we want pairs of lists
                for i in range(0, len(lists), 2):
                    list1 = lists[i]
                    if (i + 1) < len(lists):
                        list2 = lists[i + 1]
                    else:
                        list2 = None
                    merged.append(self.ml(list1, list2))
                lists = merged
            return lists[0]
        def ml(self, list1, list2):
            dummy = ListNode(0)
            current = dummy
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
            return dummy.next




#IMPORTANT: 

Here, the loop condition # while len(lists) > 1 depends on the length of the original lists variable. Inside the loop, you are updating the res variable #with the merged lists, 
#but this doesn't affect the length of the original lists. Therefore, the loop condition may not change, leading to an infinite loop.

while len(lists) > 1:
    res = []  # Creating a new list
    merged = []
    for i in range(0, len(lists), 2):
        list1 = lists[i]
        if (i + 1) < len(lists):
            list2 = lists[i + 1]
        else:
            list2 = None
        merged.append(self.ml(list1, list2))
    res = merged  # Assigning the value of merged to res
return res[0]


VS. 

while len(lists) > 1:
    merged = []
    for i in range(0, len(lists), 2):
        list1 = lists[i]
        if (i + 1) < len(lists):
            list2 = lists[i + 1]
        else:
            list2 = None
        merged.append(self.ml(list1, list2))
    lists = merged  # Overwriting the original lists variable
return lists[0]





#another practice run:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
            if not lists or len(lists) <= 0:
                return None
            #we still have merging to do 
            while len(lists) > 1:
                merged = []
                for i in range(0, len(lists), 2):
                    list1 = lists[i]
                    if (i + 1) < len(lists):
                        list2 = lists[i + 1]
                    else:
                        list2 = None
                    merged.append(self.ml(list1, list2))
                lists = merged
            return lists[0]
            
        def ml(self, list1, list2):
            dummy = ListNode(0)
            current = dummy
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
            return dummy.next

#1/18/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
            if not lists or len(lists) <= 0:
                return None
            while len(lists) > 1:
                mergedlists = []
                for i in range(0, len(lists), 2):
                    list1 = lists[i]
                    if (i + 1) < len(lists):
                        list2 = lists[i + 1]
                    else:
                        list2 = None
                    mergedlists.append(self.ml(list1, list2))
                lists = mergedlists
            return lists[0]
        def ml(self, list1, list2):
            dummy = ListNode(0)
            current = dummy
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
            return dummy.next


#another practice run:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
            if len(lists) == 0 or not lists:
                return None
            #we need to keep merging
            while len(lists) > 1:
                #we placed mergedlist above for loop. bceause we don't want to clear mergedlist everytime we want to merge because our progress would be lost
                mergedlist = []
                for i in range(0, len(lists), 2):
                    
                    list1 = lists[i]
                    if (i + 1) < len(lists):
                        list2 = lists[i + 1]
                    else:
                        list2 = None
                    mergedlist.append(self.ml(list1, list2))
                lists = mergedlist
            return lists[0]
        def ml(self, list1, list2):
            dummy = ListNode(0)
            current = dummy
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
            return dummy.next
                    


#1/24/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
            if not lists:
                return None
            while len(lists) > 1:
                #we don't want duplicate nodes 
                mergedlists = []
                for i in range(0, len(lists), 2):
                    list1 = lists[i]
                    if (i + 1) < len(lists):
                        list2 = lists[i + 1]
                    else:
                        list2 = None
                    mergedlists.append(self.ml(list1, list2))
                lists = mergedlists
            return lists[0]
        def ml(self, list1, list2):
            dummy = ListNode(0)
            current = dummy
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
            return dummy.next



#1/29/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            if not lists:
                return None
            while len(lists) > 1:
                merged = []
                for i in range(0, len(lists), 2):
                    list1 = lists[i]
                    if (i + 1) < len(lists):
                        list2 = lists[i + 1]
                    else:
                        list2 = None
                    merged.append(self.ml(list1, list2))
                lists = merged
            return lists[0]
        def ml(self, list1, list2):
            previous = ListNode(0)
            current = previous
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
            return previous.next


#1/31/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            #return [] or ListNode(0) or ListNode(None) dosen't work here because that's not a valid listnode type
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged.append(self.merge(list1, list2))
            lists = merged
        return lists[0]
        
    def merge(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list2.val < list1.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        if list1 and not list2:
            current.next = list1
        elif list2 and not list1:
            current.next = list2
        return dummy.next


#2/3/24 refresher:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged.append(self.ml(list1, list2))
            lists = merged
        return lists[0]
    def ml(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
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
        return dummy.next


#2/7/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged.append(self.ml(list1, list2))
            lists = merged
        return lists[0]
    def ml(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
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
        return dummy.next

#2/9/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged.append(self.ml(list1, list2))
            lists = merged
        return lists[0]
    def ml(self, list1, list2):
        prev = ListNode(0)
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

#2/16/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None #head of nothing
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged.append(self.find(list1, list2))
            lists = merged
        return lists[0]
    def find (self, list1, list2):
        previous = ListNode(None)
        current = previous
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
        else:
            current.next = list2
        return previous.next
                    

#2/25/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: #input list is empty
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2): #we want pairs of lists
                list1 = lists[i]
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged.append(self.ml(list1, list2))
            lists = merged
        return lists[0]
    def ml(self, list1, list2):
        prev = ListNode(0)
        current = prev
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 and not list2: current.next = list1
        elif list2 and not list1: current.next = list2
        return prev.next
            



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: #if lists is empty, we return nothing aka None
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2): #we want to grab pairs of lists
                list1 = lists[i]
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged.append(self.ml(list1, list2))
            lists = merged
        return lists[0]
    def ml(self, list1, list2):
        dummy = ListNode(0) - using #None here would throw a NoneType has no attribute next because we would be trying access the next attribute of None since cur.next = List1 is trying to access next of None, and since cur is None, it has no next attribute!!!!!
        cur = dummy
        while list1 and list2 and cur != None:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1 and not list2:
            cur.next = list1
        elif list2 and not list1 and cur != None:
            cur.next = list2
        return dummy.next
