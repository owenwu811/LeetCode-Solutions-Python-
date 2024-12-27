#1634
#medium

#A polynomial linked list is a special type of linked list where every node represents a term in a polynomial expression.

#Each node has three attributes:

#coefficient: an integer representing the number multiplier of the term. The coefficient of the term 9x4 is 9.
#power: an integer representing the exponent. The power of the term 9x4 is 4.
#next: a pointer to the next node in the list, or null if it is the last node of the list.
#For example, the polynomial 5x3 + 4x - 7 is represented by the polynomial linked list illustrated below:

#Input: poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]]
#Output: [[5,2],[2,0]]
#Explanation: poly1 = 2x2 + 4x + 3. poly2 = 3x2 - 4x - 1. The sum is 5x2 + 2. Notice that we omit the "0x" term.


#my own solution using python3:

# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        tmp1, tmp2 = [], []
        myd = defaultdict(list)
        while poly1:
            myd[poly1.power].append(poly1.coefficient)
            tmp1.append([poly1.coefficient, poly1.power])
            poly1 = poly1.next
        while poly2:
            myd[poly2.power].append(poly2.coefficient)
            tmp2.append([poly2.coefficient, poly2.power])
            poly2 = poly2.next
        res = []
        for k in myd:
            if sum(myd[k]) == 0:
                continue 
            res.append([sum(myd[k]), k])
        print(res)
        res.sort(key=lambda x: x[1], reverse=True)
        dummy = PolyNode()
        cur = dummy
        for r in res:
            print(r)
            cur.next = PolyNode(r[0], r[1])
            cur = cur.next
        return dummy.next
