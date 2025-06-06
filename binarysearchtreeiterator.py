


#173
#medium

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.



#correct python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.st.append(root.val)
            inorder(root.right)
        inorder(root)


    def next(self) -> int:
        return self.st.pop(0)


    def hasNext(self) -> bool:
        return self.st


#9/20/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.lst = []
        def f(root):
            if not root:
                return None
            f(root.left)
            self.lst.append(root.val)
            f(root.right)
        f(root)
        

    def next(self) -> int:
        return self.lst.pop(0)
        

    def hasNext(self) -> bool:
        return self.lst



#my own solution using python3 on 6/5/25:

#do the inorder traversal with a queue in the constructor and then just keep poplefting until you can't anymore

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.cur = deque()
        def f(root):
            if not root:
                return
            f(root.left)
            self.cur.append(root.val)
            f(root.right)
        f(root)
        print(self.cur)

    def next(self) -> int:
        return self.cur.popleft()
        
    def hasNext(self) -> bool:
        return len(self.cur) > 0
