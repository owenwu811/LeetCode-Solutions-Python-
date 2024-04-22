
#Given the head of a singly linked list, return true if it is a palindromeor false otherwise.
#head = [1,2,2,1] > True

#python3 intuitive solution:

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return a == a[::-1]
