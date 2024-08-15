#You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

 
#Example 1:

#Input: nums = [1,2,3], head = [1,2,3,4,5]

#Output: [4,5]

#my solution got time limit exceeded and passed 576 test cases out of 582, which is frustrating:

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        a = []
        for t in tmp:
            if t in nums:
                continue
            a.append(t)
        print(a)
        dummy = cur = ListNode()
        cur = dummy
        for g in a:
            cur.next = ListNode(g)
            cur = cur.next
        return dummy.next

#python3 solution:

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) membership checks
        nums_set = set(nums)
        
        # Create a dummy node to simplify list construction
        dummy = ListNode()
        cur = dummy
        
        # Traverse the original list
        while head:
            if head.val not in nums_set:
                # If the current value is not in nums_set, add it to the new list
                cur.next = ListNode(head.val)
                cur = cur.next
            # Move to the next node in the original list
            head = head.next
        
        # Return the new list starting after the dummy node
        return dummy.next
