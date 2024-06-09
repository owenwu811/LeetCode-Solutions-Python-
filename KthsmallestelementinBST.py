

#Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.





#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #the number of elements visited for far in tree
        n = 0
        stack = []
        cur = root
        #while cur is not None or stack is not empty, we will traverse our tree
        while cur or stack:
            #keep going left
            while cur:
                stack.append(cur)
                cur = cur.left
            #while loop is done executing, cur is none, so we went to far down left or right and we pop the last element we added to the stack 
            #visiting / processing the node 
            cur = stack.pop()
            n += 1
            #current node we just popped is what we are looking for 
            if n == k:
                #we are gaurunteed k nodes in our tree, so this will ALWAYS EXECUTE at some point
                return cur.val
            #just processed current node, so go right since we are traversing inorder way
            cur = cur.right


#the idea behind this is that we do a inorder traversal, adding all nodes we visit to the stack, and once we hit a None node meaning current is null, then we pop the elements in order [1, 2, 3, 4], and this makes sense because inorder, although we are visiting root left right, we are actually popping from left root right
        
#solution with clearer names:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left #returns to while cur is not None to evaluate while cur is not None again
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


#pythontutor representation:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def kth_smallest(root, k):
    n, stack, cur = 0, [], root
    while cur is not None or len(stack) > 0:
        while cur is not None:
            stack.append(cur) 
            cur = cur.left
        cur = stack.pop() #note that this line only executes when cur becomes None! cur = 2, 1, 3
        n += 1
        if n == k:
            return cur.val #if this executes, the entire function call ends here
        cur = cur.right #if this executes, we go back to "while cur is not None or len(stack) > 0"

# Example usage:
# Constructing a sample BST
#         5
#        / \
#       3   6
#      / \
#     2   4
#      \
#       1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.right = TreeNode(1)

# Finding the kth smallest element
k = 3
print("The", k, "th smallest element is:", kth_smallest(root, k))

#another pythontutor example with different test case:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def kth_smallest(root, k):
    n, stack, cur = 0, [], root
    while cur is not None or len(stack) > 0:
        while cur is not None:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop() #cur = 1, 2, 3
        n += 1
        if n == k:
            return cur.val
        cur = cur.right
# Tree structure:
#
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
k = 3
print("The", k, "th smallest element is:", kth_smallest(root, k))


#-----




#practice run:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0 
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                #The reason why stack.append(cur) is used instead of stack.append(cur.val) is that if you only append the values (cur.val), you'll lose the entire node structure. This is important because you need to traverse the tree and keep track of each node to find the kth smallest element. If you only append the values, you won't be able to backtrack to the parent nodes when needed.
                stack.append(cur)
                cur = cur.left 
            cur = stack.pop() 
            n += 1 
            if n == k: 
                return cur.val #problem says to return the node's numerical value
            cur = cur.right


#2/12/24 practice:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur) #adding 3 NODE before we traverse left to 1 without losing where we are at in the tree structure 
                cur = cur.left #digging down left from 3 to 1
            cur = stack.pop() #visiting the node IN ORDER
            n += 1 #update n 
            if n == k:
                return cur.val
            cur = cur.right #root left right

#2/13/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we want to append the nodes to the list in an inorder fashion and then pop off exactly in order so that when the number of nodes we visited equals k, we know we have the kth smallest value 
        n = 0
        stack = []
        cur = root
        #just because you dug to leaf node dosen't mean there aren't nodes in the stack to still be visited, so use or instead of and
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left #keep digging left in inorder fashion
            cur = stack.pop() #visiting the node
            n += 1 #number of nodes we visited now increases by 1
            if n == k:
                return cur.val
            cur = cur.right #inorder 



#2/14/24:

 #we will traverse the tree in an inorder fashion, and when we pop back up, we will visit the node 
        n = 0
        stack = []
        cur = root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


#2/18/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #to do this, we traverse the tree in an inorder fashion, appending the nodes to our list, and then when we hit a leaf node, we pop back up and actually visit the node, so we will pop k times
        stack = []
        n = 0
        cur = root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() #visiting the node - popping off the stack inorder 
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

#2/20/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        n = 0
        cur = root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


#2/22/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #traverse the tree in an inorder fashion, and we pop in order k times
        stack = []
        cur = root
        n = 0
        while stack or cur is not None:
            while cur is not None:
                stack.append(cur)
                cur = cur.left #dig down left all the way until we hit a leaf node
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right #left root right, not root left right for inorder!!!


#2/23/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
        

#2/26/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() #visiting that node
            n += 1 #how many nodes we visited because if n == k, then we found the value of the node we want to return as the anwser
            if n == k: 
                return cur.val
            cur = cur.right #we are doing an inorder fashion 


#2/27/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur is not None or len(stack) > 0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
            

#3/1/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

#3/4/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [] #we want the kth smallest, so we traverse the tree in inorder fashion (LEFT ROOT RIGHT BECAUSE WE KNOW BST HAS SMALLEST VALUES TO THE VERY LEFT OF TREE) and add them to the tree, and we pop k times
        cur = root
        n = 0
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() #popping back up by visiting the node
            n += 1
            if n == k:
                return cur.val
            cur = cur.right



#3/15/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we want to return 1 value in the end
        stack = []
        n = 0
        cur = root #start traversing  
        while cur != None or stack:
            while cur != None:
                stack.append(cur) #remember append the node itself, not the value!
                cur = cur.left
            cur = stack.pop() #visiting the node by popping back up k times
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


#3/21/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

#3/25/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() #visiting the node
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

#3/29/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


#4/11/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = []
        n = 0
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop() #popping back up to visit node
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

#4/13/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        n = 0
        stack = []
        while cur != None or stack:
            while cur != None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right



#5/1/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        r = root
        l = []
        while r or l:
            while r:
                l.append(r)
                r = r.left
            r = l.pop()
            count += 1
            if count == k:
                return r.val
            r = r.right


#5/14/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stack = []
        n = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
            
#6/8/24 review:

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        n = 0
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

