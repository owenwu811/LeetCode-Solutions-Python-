
#Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

#You can return the answer in any order.

#Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
#Output: [7,4,1]
#Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

#python3 solution:

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.startp = None
        self.res = []
        def connectparent(root, prev=None):
            if not root: return
            if root == target:
                self.startp = root
            root.parent = prev
            #notice how we also pass root as prev in each iteration here, so prev changes to become the parent in each recursive call!
            connectparent(root.left, root)
            connectparent(root.right, root)
        connectparent(root)
        def findk(root, k, prev=None):
            if not root:
                return
            if k == 0:
                self.res.append(root.val)
                return
            #notice how we pass the current node in as prev in each turn this block executes!, so if 6's left child is not equal to prev, which starts at None, then we set prev = 6 now and continue down left!
            if root.left != prev: findk(root.left, k - 1, root) #This section of the code handles the recursive traversal in three directions: left child, right child, and parent. Let's go through it step by step:
            if root.right != prev: findk(root.right, k - 1, root)
            if root.parent != prev: findk(root.parent, k - 1, root)
        findk(self.startp, k)
        return self.res

#if root.left != prev: findk(root.left, k - 1, root) line:
#If the left child of the current node (root) is not the same as the previous node (prev), it means we haven't just come from the left child. In this case, we recursively call getNodeAtKDistance with the left child as the new root, k-1 as the new distance, and the current node (root) as the new previous node. This effectively moves us one step closer to the target node along the left subtree.


#practice again:

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.startp = None
        self.res = []
        def findparent(root, prev=None):
            if not root: return
            if root == target: #target is a NODE here, so we don't have to use .val
                self.startp = root
            root.parent = prev #setting parent attribute of root to prev, which starts with none and will be modified in subsequent iterations
            findparent(root.left, root)
            findparent(root.right, root)
        findparent(root, None)
        def distancek(root, k, prev=None):
            if not root: return
            if k == 0:
                self.res.append(root.val)
                return
            #prev=None first but will become root as soon as inner block executes
            #we have to explore all directions
            if root.left != prev: distancek(root.left, k - 1, root)
            if root.right != prev: distancek(root.right, k - 1, root)
            if root.parent != prev: distancek(root.parent, k - 1, root)
        distancek(self.startp, k, None) #we found our target node, so we do a bfs starting from it
        return self.res

#6/7/24 review:

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.startp = None
        self.res = []
        def f(root, prev=None):
            if not root: 
                return
            if root == target:
                self.startp = root
            root.parent = prev
            f(root.left, root)
            f(root.right, root)
        f(root)
        def a(root, k, prev=None):
            if not root: 
                return
            if k == 0:
                self.res.append(root.val)
                return
            if root.left != prev: a(root.left, k - 1, root)
            if root.right != prev: a(root.right, k - 1, root)
            if root.parent != prev: a(root.parent, k - 1, root) #if you put this line above if root.left != prev, it works too! we are exploring all directions regardless of which direction you want to explore first and then backtracking
        a(self.startp, k)
        return self.res
