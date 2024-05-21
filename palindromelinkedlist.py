
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


#4/23/24:

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        right = head
        while right:
            res.append(right.val)
            right = right.next
        return res == res[::-1]

#4/25/24:

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        r = head
        while r:
            res.append(r.val)
            r = r.next
        return res == res[::-1]


#5/21/24 (missed):

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res == res[::-1] # we compare res[::-1] to res, not res[::-1] to head because head is not an array!
