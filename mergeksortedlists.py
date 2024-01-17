
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
