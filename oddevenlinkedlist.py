
#Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

#The first node is considered odd, and the second node is even, and so on.

#Note that the relative order inside both the even and odd groups should remain as it was in the input.

#You must solve the problem in O(1) extra space complexity and O(n) time complexity.

#input: head = [1,2,3,4,5]
#output: [1,3,5,2,4]


#python3 solution:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        # head = [1,2,3,4,5]
        if not head or not head.next:
            return head
        #1st node NOT THE NONE NODE BEFORE FIRST (1) is odd, so odd_head becomes 1
        #odd_head just saves the 1
        odd_head = odd = head #odd_head becomes 1
        #2nd node is even (2) is even, so even_head becomes 2
        #even_head just saves the 2 that starts linking to 4 and 6
        even_head = even = head.next #even_head, even, head.next become 2
        while even and even.next: #even will end at 4, and even.next will be 5 because even starts at 2. when even becomes 6, this while loop will becomes False
            #remember that odd starts at 1, so odd.next becomes 3
            odd.next = even.next #since even was 2, even.next = 3, and if odd.next is set to even.next, odd.next becomes 3. odd.next becomes 5
            odd = odd.next #odd becomes 3. odd becomes 5
            #remember that even starts at 2, so even.next becomes 4
            even.next = odd.next #even.next becomes 4. even.next becomes 6
            even = even.next #even becomes 4. even becomes 6
        odd.next = even_head #odd.next becomes 2
        return odd_head #return 1