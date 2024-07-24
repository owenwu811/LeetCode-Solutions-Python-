
#Given the root of a binary tree, return the maximum width of the given tree.

#The maximum width of a tree is the maximum width among all levels.

#The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

#It is guaranteed that the answer will in the range of a 32-bit signed integer.

#Input: root = [1,3,2,5,3,null,9]
#Output: 4
#Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

#python3 solution:

from collections import deque

#we are doing BFS

#          1 (position 1)
#        3   2 (3 is at position 2) and (2 is at position 3)
#      5  3    9 #(9 is at position 7)

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #null nodes are also counted, so that's why the last level of the 1st example is 4 instead of 3
        max_width = 0
        d = deque()
        d.append([root, 1, 0]) #[node, position, level] - no value here!
        #d = [root, 1, 0]
        curlevel, positionofleftmost = 0, 1
        while d: #True in 1st turn because d = [root, 1, 0], True in 2nd turn because d = [node, 2, 1], [node, 3, 1]
            #node, 1, 0 = d.popleft(), node, 2, 1 = d.popleft(), node, 3, 1 = d.popleft()
            node, position, level = d.popleft()
            #d = [], d = [node, 3, 1], d = ([node, 4, 2], [node, 5, 2]), 
            if level > curlevel: #if 0 > 0 - False, if 1 > 0 - True, 1 > 1 - False
                curlevel = level #0 > 1,
                positionofleftmost = position #1 > 2,
            #max_width = max(0, 1 - 1 + 1), max_width = max(1, 2 - 2 + 1)
            max_width = max(max_width, position - positionofleftmost + 1)
            if node.left: #True because 1 has a left child of 3, True because 3 has a left child of 5,
                d.append([node.left, 2 * position, level + 1])
                #d = [node, 2, 1], d = ([node, 3, 1], [node, 4, 2])
            if node.right: #True because 1 has a right child of 2, True because 3 has a right child of 3
                d.append([node.right, 2 * position + 1, level + 1])
                #d = [node, 2, 1], [node, 3, 1], d = ([node, 3, 1], [node, 4, 2], [node, 5, 2]) aka nodes 2, 5, 3

        return max_width 
        
#6/9/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        d = deque()
        d.append([root, 1, 0]) #[root, pos, level]
        currentlevel, leftmostpos = 0, 1
        while d:
            node, position, level = d.popleft()
            if level > currentlevel:
                currentlevel = level
                leftmostpos = position
            res = max(res, position - leftmostpos + 1)
            if node.left:
                d.append([node.left, 2 * position, 1 + level])
            if node.right:
                d.append([node.right, 2 * position + 1, 1 + level])
        return res

#6/11/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        d = deque()
        d.append([root, 1, 0])
        curlevel, leftmostpos = 0, 1
        while d:
            node, pos, level = d.popleft()
            if level > curlevel:
                curlevel = level
                leftmostpos = pos
            self.res = max(self.res, pos - leftmostpos + 1)
            if node.left:
                d.append([node.left, 2 * pos, 1 + level])
            if node.right:
                d.append([node.right, 2 * pos + 1, 1 + level])
        return self.res

#6/16/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        d = deque()
        d.append([root, 1, 0]) #for some reason, we can't just do d = deque([root, 1, 0]) - we have to make it 2 lines with the seperate append line to work
        currentlevel, leftmostpos = 0, 1
        while d:
            node, pos, level = d.popleft()
            if level > currentlevel:
                currentlevel = level
                leftmostpos = pos
            self.res = max(self.res, pos - leftmostpos + 1)
            if node.left:
                d.append([node.left, 2 * pos, 1 + level])
            if node.right:
                d.append([node.right, 2 * pos + 1, 1 + level])
        return self.res


#7/16/24 review (missed a couple of days ago):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        d = deque()
        d.append([root, 1, 0])
        currentlevel, leftmostpos = 0, 1
        while d:
            node, position, level = d.popleft()
            if level > currentlevel:
                currentlevel = level
                leftmostpos = position
            self.res = max(self.res, position - leftmostpos + 1)
            if node.left:
                d.append([node.left, 2 * position, 1 + level])
            if node.right:
                d.append([node.right, 2 * position + 1, 1 + level])
        return self.res

#7/18/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        d = deque()
        d.append([root, 1, 0])
        currentlevel, leftmostpos = 0, 1
        while d:
            node, pos, level = d.popleft()
            if level > currentlevel:
                currentlevel = level
                leftmostpos = pos
            self.res = max(self.res, pos - leftmostpos + 1)
            if node.left:
                d.append([node.left, 2 * pos, 1 + level])
            if node.right:
                d.append([node.right, 2 * pos + 1, 1 + level])
        return self.res

#7/23/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        d = deque()
        d.append([root, 1, 0])
        currentlevel, leftmostpos = 0, 1
        while d:
            node, position, level = d.popleft()
            if level > currentlevel:
                currentlevel = level
                leftmostpos = position
            self.res = max(self.res, position - leftmostpos + 1)
            if node.left:
                d.append([node.left, 2 * position, 1 + level])
            if node.right:
                d.append([node.right, 2 * position + 1, 1 + level])
        return self.res


