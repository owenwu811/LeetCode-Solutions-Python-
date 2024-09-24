
#2074
#medium


#You are given the head of a linked list.

#The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

#The 1st node is assigned to the first group.
#The 2nd and the 3rd nodes are assigned to the second group.
#The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
#Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

#Reverse the nodes in each group with an even length, and return the head of the modified linked list.



#my own solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        print(tmp)
        new = []
        i = 0
        windowsize = 1
        while i + windowsize < len(tmp):
            new.append(tmp[i: i + windowsize])
            i = i + windowsize
            windowsize += 1
        new.append(tmp[i:])
        for i in range(len(new)):
            if len(new[i]) % 2 == 0:
                new[i] = new[i][::-1]
        dummy = ListNode(None)
        cur = dummy
        for i in range(len(new)):
            for j in range(len(new[i])):
                cur.next = ListNode(new[i][j])
                cur = cur.next
        return dummy.next
