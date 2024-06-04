

#Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

#Input: root = [3,9,20,null,null,15,7]
#Output: [[3],[20,9],[15,7]]

#             3
#           9  20
#            15  7

#my incorrect solution that passed only 7/33 test cases, outputting [[3],[20,9],[15],[7]] instead of [[3],[20,9],[15,7]] as expected for test case root = [3,9,20,null,null,15,7]:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        d = deque()
        d.append(root) #3
        turn = 1
        while d: #deque([9, 20])
            turn += 1 #1, 2
            level = []
            for i in range(len(d)): #0, 0, 1
                if turn % 2 == 0: #1 % 2 == 0 > False, 2 % 2 == 0 > True
                    current = d.pop() #current = 20
                    if current: #20
                        level.append(current.val) #[] > [20]
                        d.append(current.right) #deque([9]) > deque([9, 7])
                        d.append(current.left) #deque([9, 7, 15])
                elif turn % 2 != 0: #1 % 2 != 0 > True
                    current = d.popleft() #current = 3
                    if current: #3 is not None > True
                        level.append(current.val) #[] > [3]
                        d.append(current.right) #deque([9])
                        d.append(current.left) #deque([9, 20])
            if level:
                res.append(level) #[] > [[3]]
        return res

#correct python3 solution:

#note that we start with from left to right direction as mentioned in the problem

#note that: d.appendleft(3)
#d.appendleft(3)
#d.appendleft(2)

#results in: [2, 3]

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        d = deque() #holds nodes at each level
        d.append(root)
        turn = 0
        while d:
            level = []
            for i in range(len(d)):
                #0 % 2 == 0 > True, so we start with d.popleft() for the 1st level aka left to right as starting level order as mentioned in problem
                if turn % 2 == 0:  # left to right
                    current = d.popleft()
                    if current:
                        level.append(current.val)
                        if current.left:
                            d.append(current.left)
                        if current.right:
                            d.append(current.right)
                else:  # right to left
                    #1 % 2 > else, so we use d.pop() for the 2nd level aka right to left ordering
                    current = d.pop()
                    if current:
                        level.append(current.val)
                        if current.right:
                            d.appendleft(current.right)
                        if current.left:
                            d.appendleft(current.left)
            res.append(level)
            turn += 1
        return res

#res = []
#d = deque([3])
#turn = 0
#while d > True
#level = []
#i = 0 (only iteration)
#if 0 % 2 == 0 > True, so current = d.popleft()
#d = []
#current = 3
#if current > True, so level.append(3)
#level = [3]
#if current.left > True, so d.append(current.left)
#d = [9]
#if current.right > True, so d.append(current.right)
#d = [9, 20]
#i loop ends
#res.append(level)
#res = [[3]]
#turn increments to 1

#while d > True
#level = []
#i = 0 (0, 1) for [9, 20]
#1 % 2 == 0 - False, so execute else block with current = d.pop()
#d = [9]
#current = 20
#if current > True, so level.append(20)
#level = [20]
#current.right > True, so d.appendleft(7)
#d = [7, 9]
#current.left > True, so d.appendleft(15)
#d = [15, 7, 9]

#i = 1
#1 % 2 == 0 - False, so execute else block with current = d.pop()
#d = [15, 7]
#current = 9
#if current > True, so level.append(9)
#level = [20, 9]
#if current.right > False
#if current.left > False

#for loop hits limit with i
#res.append([20, 9])
#res = [[3], [20, 9]]
#turn becomes 2

#while d > True
#level = []
#i = 0
#2 % 2 == 0 > True, so current = d.popleft()
#d = [7]
#current = 15
#if current > True, so level.append(15)
#level = [15]
#if current.left > False
#if current.right > False


#the reason we do appendleft(r), appendleft(l) is because we then do d.pop() and then d.popleft() in next iteration to get right to left ordering

#i = 1
#2 % 2 == 0 > True, so current = d.popleft()
#d = []
#current = 7
#if current > True, so level.append(7)
#level = [15, 7]
#if current.left > False
#if current.right > False

#for loop hits limit with i
#res.append([15, 7])
#res = [[3], [20, 9], [15, 7]]
#turn = 3

#while d > False
#return res

#6/4/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        d = deque()
        d.append(root)
        turn = 0
        while d:
            level = []
            for i in range(len(d)):
                if turn % 2 == 0:
                    current = d.popleft()
                    if current:
                        level.append(current.val)
                        if current.left:
                            d.append(current.left)
                        if current.right:
                            d.append(current.right)
                else:
                    current = d.pop()
                    if current:
                        level.append(current.val)
                        if current.right:
                            d.appendleft(current.right)
                        if current.left:
                            d.appendleft(current.left)
            res.append(level)
            turn += 1
        return res
