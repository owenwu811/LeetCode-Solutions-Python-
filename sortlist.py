#Given the head of a linked list, return the list after sorting it in ascending order.
#Input: head = [4,2,1,3]
#Output: [1,2,3,4]


#python3 solution:

#merge sort 

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, self.getMid(head)
        tmp = right.next #dividing in half for the first time 
        right.next = None #setting the 2 to None
        right = tmp
        left, right = self.sortList(left), self.sortList(right) #need to keep dividing in half until can't anymore
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
            
