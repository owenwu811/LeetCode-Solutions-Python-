
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


#3/5/24:

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
            merged = [] #merge each pair of lists together
            #if len(lists) = 2, we would only have one iteration - 0
            for i in range(0, len(lists), 2): #starting from 0 inclusive and up to not including len(lists), moving forward 2 steps at a time
                list1 = lists[i]
                #if len(lists) = 2, (i + 1) = (0 + 1) = 1, which must be less than 2 because indexes must be one less than length
                if (i + 1) < len(lists): # we have room for a 2nd pointer
                    list2 = lists[i + 1]
                else:
                    list2 = None
                #merging the pair of linked lists into one
                merged.append(self.ml(list1, list2))
            lists = merged #moving towards termination of while loop above
        return lists[0] #we only have one list left
    def ml(self, list1, list2):
        prev = ListNode(0) #to avoid Nonetype error, use prev = ListNode(0) or ListNode(None) as pass by reference instead of prev = None
        cur = prev
        while list1 and list2: #trying to merge two linked lists into one
            if list1.val < list2.val:
                cur.next = list1 #if you did prev = None, then Nonetype error here because cur is None, and Nonetype object has no next attribute
                list1 = list1.next #move next in the list which you took one node away from
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next #move next in our output list that we will join to merged eventually
        if list1 and not list2:
            cur.next = list1
        elif list2 and not list1:
            cur.next = list2
        return prev.next


#3/8/24:


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
        prev = ListNode(None)
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


#3/9/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1: #keep merging together
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
        prev = ListNode(None) #the class ListNode above has a next attribute to avoid NoneType has no attribute next error! classListNode has a val and next attribute above! The val attribute holds the value of the node.
#The next attribute holds a reference to the next node in the linked list.
#By initializing prev as a ListNode object with prev = ListNode(None), you're ensuring that prev has both val and next attributes. This is necessary for the merging logic in the code to work properly, as it relies on manipulating these attributes when merging two linked lists.
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


#3/15/24:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #we have k number of linked lists, and each linked list is sorted in ascending order
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
        prev = ListNode(None)
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
    


#3/17/24:

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
        prev = ListNode(None)
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


#3/26/24:

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
        prev = ListNode(None)
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
