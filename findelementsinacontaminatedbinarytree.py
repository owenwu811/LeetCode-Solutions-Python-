

#1261
#medium

#Given a binary tree with the following rules:

#root.val == 0
#If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
#If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
#Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

#Implement the FindElements class:

#FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
#bool find(int target) Returns true if the target value exists in the recovered binary tree.

#my own solution using python3:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.new = TreeNode(0)
        def f(root):
            if not root:
                return 
            root.val = 0
            f(root.left)
            f(root.right)
        f(root)
        print(root)
        self.cur = root
        def f(node):
            if not node:
                return  
            if node.left:
                node.left.val = 2 * node.val + 1
            if node.right:
                node.right.val = 2 * node.val + 2
            f(node.left)
            f(node.right)
        f(self.cur)
        print(self.cur)
        self.bank = []
        self.res = False
        def dfs(n):
            if not n:
                return 
            self.bank.append(n.val)
            dfs(n.left)
            dfs(n.right)
        dfs(self.cur)
        
    def find(self, target: int) -> bool:
        return target in self.bank
        print(self.bank)
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
