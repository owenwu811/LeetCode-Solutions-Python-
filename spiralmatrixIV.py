
#2326
#medium



#You are given two integers m and n, which represent the dimensions of a matrix.

#You are also given the head of a linked list of integers.

#Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

#Return the generated matrix.

#Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
#Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
#Explanation: The diagram above shows how the values are printed in the matrix.
#Note that the remaining spaces in the matrix are filled with -1.


#my own different solution using python3:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        pre = [[-1] * n for i in range(m)]
        tmp = deque()
        while head:
            tmp.append(head.val)
            head = head.next
        r = c = d = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        seen = set()
        for i in range(m * n):
            seen.add((r, c))
            if tmp:
                pre[r][c] = tmp.popleft()
            newr, newc = r + directions[d][0], c + directions[d][1]
            if newr < 0 or newr >= m or newc < 0 or newc >= n or ((newr, newc)) in seen:
                d = (d + 1) % 4
                newr, newc = r + directions[d][0], c + directions[d][1]
            r, c = newr, newc
        return pre
