#Given the head of a linked list, return the list after sorting it in ascending order.
#Input: head = [4,2,1,3]
#Output: [1,2,3,4]


#python3 solution:

#merge sort 

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #this is the base case when the list can't be split anymore - left = sortList(4) when we have 4 > 2, and then we have 4, and right = 2, but left is just 4, and so 4.next = None, so just return head, or, 4, and right is just 2, so 2.next = None, so just return head, or, 2. since we now finished dividing, we go from "return head" to "self.merge(left, right)", and list1 = 4, and list2 = 2, so we want to merge them in order
            return head
        left, right = head, self.getMid(head) #left starts at 4 in 4 > 2 > 1 > 3, and right starts at the return value of getMid(4), which will return 2, so right becomes 2
        tmp = right.next #dividing in half for the first time. right is 2, so tmp = right.next means tmp becomes 1 in 4 > 2 > 1 > 3
        right.next = None #so since right is 2 in 4 > 2 > 1 > 3, we set 2 to None. linked list now looks like 4 > 2 > N with left = 4, and right = 2
        right = tmp #since the list now looks like 4 > 2 > N | 1 > 3, we set right to 1 when right was previously 2
        left, right = self.sortList(left), self.sortList(right) #left = 4 in 4 > 2 > N, so we call sortList(4), and since there is a head and a head.next, we go onto skip base case, so we do left = 4 in 4 > 2 > N, and right = self.getMid(4) with 4 > 2 > N. slow = 4, fast = 2. fast.next is None, so we just return slow of 4. left and right in line 14 are now both on 4 - list still looks like 4 > 2 > N, but now tmp becomes 2, and right.next = None means list goes from 4 > 2 > N to 4 > N, and then right is set to 2, so list is now 4 > N | 2 > N. now, when we call self.sortList(4) and self.sortList(2), we get the base case where left = 4 > N, and right = 2 > N, and then we call "return self.merge(left, right)"
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
            
