

#Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#Input: root = [1,2,3,null,5,null,4]
#Output: [1,3,4]

#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       #we want to return the right most node from each level going from top to bottom, so this is similar to binary tree level order traversal in that the deque still represents all nodes at a particular level and that we are still traversing left to right
        res = []
        #represents all nodes at each level of the tree
        d = deque()
        #represents the root node of the tree (only one element in this iteration)
        d.append(root)
        while len(d) > 0:
           #since we are starting a new level of the input tree (one level down from the previous level), we set rightmost to None 
            rightmost = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    rightmost = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            #we iterated through an entire level, so we traversed from left to right in the level, setting the rightmost variable to the currentnode as long as it wasn't null
            #if we didn't have this not None check, if currentnode is not None were never true - after we processed all the levels for [1,2,3,null,5,null,4] meaning rightmost = 4, we still have a last level where every node is Null, so rightmost stays None since the if currentnode is not None never executes, and without the if rightmost is not None, we will still try to add None into our output, which isn't valid because None objects don't even have a value attribute. In other words, rightmost would stay None, and None object dosen't have a val attribute, and the problem asks for the value of the rightmost node
            if rightmost is not None:
                res.append(rightmost.val)
        return res



#important:

#if we had rightmost = None after the for loop instead of between while and for, it would fail the test case root = [1,2] because root = [1, 2] represents a tree like this:
#   1
# 2  

#this means that there is still a N like:

#   1
# 2   N

#so if you put rightmost = None right after the for loop, rightmost will get overriden to None instead of 2 for that level, which is incorrect, so you would return [1] instead of [1, 2] as the rightside view

#when constructing the tree nodes, if a node doesn't have a left or right child, the corresponding child attribute is set to None. This convention is common in tree data structures, where a None value indicates the absence of a child node.
#    1
#  /
# 2

#The tree node with value 1 has a left child with value 2, but its right child is set to None, indicating that there is no right child for the node with value 1.



#1/24/24 practice:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        d = deque()
        d.append(root)
        while len(d) > 0:
            rightside = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    rightside = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightside is not None:
                res.append(rightside.val)
        return res


#1/25/24:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #deque will store all the nodes at the current level of the binary tree as we will traverse from left to right
        res = []
        d = deque()
        #adding the first level of the tree
        d.append(root) 
        #while we haven't visited all levels of the input tree
        while len(d) > 0:
            rightside = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    rightside = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightside is not None:
                res.append(rightside.val)
        return res


#1/13/24 refresher:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #used to store all nodes at a particular level of our input tree
        d = deque()
        d.append(root)
        res = []
        while len(d) > 0:
            rightside = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    rightside = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            #covers the case where the if currentnode is not None block is never executed and prevents Nonetype error
            if rightside is not None:
                res.append(rightside.val)
        return res

#2/3/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        d = deque()
        d.append(root)
        while d:
            rightmost = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    rightmost = currentnode.val
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightmost is not None:
                res.append(rightmost)
        return res


#2/10/24:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #nodes at each level of input tree stored in deque
        d = deque()
        #1st level of input tree only has one node - the root node
        d.appendleft(root)
        res = []
        while d: # we have another level to process
            rightside = None
            for i in range(len(d)): # number of iterations in each level of input tree
                currentnode = d.pop()
                if currentnode is not None:
                    rightside = currentnode
                    d.appendleft(currentnode.left) #appendleft and popleft() work too, but you can't do popleft() and append() or appendleft() and pop() - we want FIFO here, not lIFO. using LIFO would lead to BINARY TREE LEFT SIDE VIEW, NOT LEFT SIDE VIEW 
                    d.appendleft(currentnode.right)
            if rightside is not None:
                res.append(rightside.val)
        return res

#2/19/24:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS = FIFO = RIGHT SIDE VIEW
        res = []
        d = deque()
        d.append(root)
        while d:
            rightmost = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    rightmost = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightmost is not None:
                res.append(rightmost.val)
        return res

#2/25/24:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        d.append(root)
        res = []
        while d:
            rightside = None
            for i in range(len(d)):
                currentnode = d.popleft() #BFS = FIFO
                if currentnode is not None:
                    rightside = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightside:
                res.append(rightside.val)
        return res


#remember: Inorder => Left, Root, Right while Preorder => Root, Left, Right!


#3/3/24:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        d.append(root)
        res = []
        while d:
            rightside = None
            for i in range(len(d)):
                current = d.popleft()
                if current != None:
                    rightside = current
                    d.append(current.left)
                    d.append(current.right)
            if rightside != None:
                res.append(rightside.val)
        return res


#3/9/24:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        d = deque()
        d.append(root)
        while d:
            rightside = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode != None:
                    rightside = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightside != None:
                res.append(rightside.val)
        return res

#3/11/24:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        d.append(root)
        res = []
        while d:
            rightmost = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode != None:
                    rightmost = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightmost != None:
                res.append(rightmost.val)
        return res

#4/3/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #all nodes at a certain level
        d = deque()
        d.append(root)
        res = [] #values of nodes at each level
        while d:
            rightside = None
            for i in range(len(d)):
                currentnode = d.popleft() #bfs = fifo
                if currentnode is not None:
                    rightside = currentnode.val
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightside is not None:
                res.append(rightside)
        return res

#5/3/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we want to return the values of nodes
        d = deque() #holds the nodes themselves
        res = []
        d.append(root) #first level only has one node
        while d:
            rightmost = None
            for i in range(len(d)):
                currentnode = d.popleft() #bfs level order
                if currentnode != None:
                    rightmost = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            if rightmost:
                res.append(rightmost.val)
        return res

#5/28/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        d = deque()
        res = []
        d.append(root)
        while d:
            rightmost = None
            for i in range(len(d)):
                current = d.popleft()
                if current:
                    rightmost = current
                    d.append(current.left)
                    d.append(current.right)
            if rightmost:
                res.append(rightmost.val)
        return res

#6/22/24 review:

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        d = deque()
        d.append(root)
        while d:
            rightside = None
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    rightside = cur
                    d.append(cur.left)
                    d.append(cur.right)
            if rightside:
                res.append(rightside.val)
        return res


#7/26/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        d = deque()
        d.append(root)
        while d:
            rightside = None
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    rightside = cur
                    d.append(cur.left)
                    d.append(cur.right)
            if rightside:
                self.res.append(rightside.val)

        return self.res


#10/15/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        d.append(root)
        res = []
        while d:
            rightmost = None
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    rightmost = cur
                    d.append(cur.left)
                    d.append(cur.right)
            if rightmost:
                res.append(rightmost.val)
        return res
