
#114
#medium


#Given the root of a binary tree, flatten the tree into a "linked list":

#The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
#The "linked list" should be in the same order as a pre-order traversal of the binary tree.




#my own solution using python3 after changing it a bit from someone else's solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        d = deque()
        d.append(root)
        d.append(None)
        while d:
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    if cur.right:
                        d.appendleft(cur.right)
                    if cur.left:
                        d.appendleft(cur.left) #so because the left subtree is smaller, now the smaller one goes in front for us to set the right pointer to later
                    cur.left = None # as neetcode said, we always want to set the left child to None in the picture below:
                    cur.right = d[0]
        return root


#picture below:

                        # notice below here how the left is set to N, but the right is always connected to the next number as neetcode mentioned, so this explaines the two lines after the two appendlefts above:

    #     1              #  1
    #    / \             #    2
    #   2   5            #      3
    #  / \   \           #        4
    # 3   4   6          #          5
                         #            6


#original op's solution:

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        q = deque()
        q.append(root)
        q.append(None)
        def print_stack():
            print("Current deque state: ", [node.val if node else None for node in q])
        
        print_stack()
        print(q)
        while q[0] is not None:
            node = q.popleft() 
            if node.right:
                q.appendleft(node.right) 
            if node.left:
                q.appendleft(node.left) 
            node.left = None 
            node.right = q[0] 
            print_stack()
        return root

#original op's solution put into pythontutor:
    
    # Build the binary tree:
    #     1
    #    / \
    #   2   5
    #  / \   \
    # 3   4   6

#Original tree (in level order):
#[1, 2, 5, 3, 4, None, 6]
#Current deque state:  [1, None]
#deque([<__main__.TreeNode object at 0x7f24078b30d0>, None])
#Current deque state:  [2, 5, None]
#Current deque state:  [3, 4, 5, None]
#Current deque state:  [4, 5, None]
#Current deque state:  [5, None]
#Current deque state:  [6, None]
#Current deque state:  [None]

#Flattened tree (as linked list):
#1 -> 2 -> 3 -> 4 -> 5 -> 6


#9/30/24 review (could not resolve):

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        d = deque()
        d.append(root)
        d.append(None)
        while d:
            for i in range(len(d)):
                cur = d.popleft()
                if cur:
                    if cur.right:
                        d.appendleft(cur.right)
                    if cur.left:
                        d.appendleft(cur.left)
                    cur.left = None
                    cur.right = d[0]
        return root
