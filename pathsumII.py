
#Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

#A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

#Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
#Output: [[5,4,11,2],[5,8,4,5]]
#Explanation: There are two paths whose sum equals targetSum:
#5 + 4 + 11 + 2 = 22
#5 + 8 + 4 + 5 = 22

#                   5
#                4     8
#             11      13  4
#           7    2       5  1

#note that, even though 5 + 8 + 13 = 22, this is not valid because A PATH STARTS FROM THE ROOT AND ENDS AT ANY LEAF NODE, HENCE THE CHECK if pathsum == targetSum and not root.left and not root.right:


#python3 solution:

#before we backtrack, we must do extra checks aka recursive calls to ensure the leaf node's left and right children are None:

#   7
# N   N         ---- have to make sure both l and r children cause recursive calls that cause "if not root" to be True and return None

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def f(root, cur, pathsum):
            if not root:
                #if you do return None instead of return, it will work too!
                return #goes to next line (if 9 returns here (return is equivalent to returning None, then execute line 10. if line 10 executes return here, then execute line 11)
            cur.append(root.val)
            pathsum += root.val
            if pathsum == targetSum and not root.left and not root.right: #A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children. - explicitly stated in the problem. The condition and not root.left and not root.right checks whether the current node is a leaf node. A leaf node is defined as a node with no left or right children. This is important because the problem typically requires finding root-to-leaf paths that sum to the target value, not just any paths that sum to the target.
                res.append(cur.copy())
            f(root.left, cur, pathsum) #say this is line 9
            f(root.right, cur, pathsum) #say this is line 10
            cur.pop() #[5, 4, 11, 7] aka pathsum = 27 > [5, 4, 11] aka pathsum = 20, so cur.pop() AUTUOMATICALLY REDUCES THE PATHSUM WITHOUT HAVING TO DO ANYTHING ELSE
        f(root, [], 0)
        return res

  #if we include return after res.append(cur.copy()), this is incorrect and will return [[5,4,11,2],[5,4,8,4,5]] instead of the expected [[5,4,11,2],[5,8,4,5]] because 
      #Including return immediately after res.append(cur.copy()) causes the function to stop further exploration as soon as it finds the first valid path, resulting in an incomplete and incorrect output. Without the return, the function continues to explore all possible paths, ensuring that all valid paths are found and included in the result.

  #if we add cur.append(root.val) and pathsum += root.val after if pathsum == targetSum and not root.left and not root.right: res.append(cur.copy()) instead of before means the pathsum and cur WILL NOT INCLUDE THE CURRENT NODE'S VALUE WHEN PERFORMING THE CHECK. YOU WON'T BE CONSIDERING THE CURRENT NODE'S VALUE WHEN PERFORMING THE CHECK. INSTEAD, THE CHECK WILL BE BASED ON THE PATH SUM AND PATH UP TO THE PARENT OF THE CURRENT NODE (ONE LEVEL ABOVE), LEADING TO INCORRECT RESULTS
  #for example, when we reach a node, say, 4, pathsum would incorrectly be 5 instead of 9 if we added those two lines before instead of after 

  #6/2/24 review:

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #root to leaf paths only - starting from root and ending at leaf node only
        res = []
        def f(root, cur, pathsum):
            if not root:
                return
            cur.append(root.val)
            pathsum += root.val
            if pathsum == targetSum and not root.left and not root.right:
                #you use .copy() in backtracking scenarios!
                res.append(cur.copy()) #without cur.copy(), if you just use cur, you get [][] instead of [[5,4,11,2],[5,8,4,5]] for root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22 because you would be deleting and modifying THE SAME OBJECT INSIDE OF SELF.RES IN THE FUTURE THUS OVERRIDING AND ERASING WHAT WAS IN SELF.RES BEFORE!
            f(root.left, cur, pathsum)
            f(root.right, cur, pathsum)
            cur.pop()

        f(root, [], 0)
        return res

#the reason we are clearing the list is specifically because of cur.pop()? and when we do cur.pop() without appending cur.copy(), we are also, indirectly, popping from self.res because it's all just one object being changed aka popped!

#When you append cur to self.res without using cur.copy(), you are appending a reference to the same list object that cur points to. This means that any subsequent changes to cur (like appending or popping elements) will also affect the list inside self.res because both cur and the list inside self.res are referencing the same object.

#missed on 6/3/24:


#practice again on 6/3/24:

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def f(root, cur, pathsum):
            if not root:
                return
            cur.append(root.val)
            pathsum += root.val
            if pathsum == targetSum and not root.left and not root.right:
                self.res.append(cur.copy())
            f(root.left, cur, pathsum)
            f(root.right, cur, pathsum)
            cur.pop() #this auto takes care of the reduction of pathsum instead of us having to reset pathsum to 0
        f(root, [], 0)
        return self.res

#6/4/24 review:

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def f(root, pathsum, cur):
            if not root:
                return
            cur.append(root.val)
            pathsum += root.val
            if pathsum == targetSum and not root.left and not root.right:
                self.res.append(cur.copy())
            f(root.left, pathsum, cur)
            f(root.right, pathsum, cur)
            cur.pop()

        f(root, 0, [])
        return self.res

#6/7/24 review:

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def f(root, pathsum, cur):
            if not root:
                return
            pathsum += root.val
            cur.append(root.val)
            if pathsum == targetSum and not root.left and not root.right:
                self.res.append(cur.copy())
            f(root.left, pathsum, cur)
            f(root.right, pathsum, cur)
            cur.pop() #we've reached the bottom of tree
        f(root, 0, [])
        return self.res
            
#6/12/24 refresher:

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def f(root, pathsum, cur):
            if not root:
                return
            pathsum += root.val
            cur.append(root.val)
            if pathsum == targetSum and not root.left and not root.right:
                self.res.append(cur.copy())
            f(root.left, pathsum, cur)
            f(root.right, pathsum, cur)
            cur.pop()
            
            


        f(root, 0, [])
        return self.res

#7/1/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def f(root, pathsum, cur):
            if not root:
                return
            pathsum += root.val
            cur.append(root.val)
            if pathsum == targetSum and not root.left and not root.right:
                self.res.append(cur.copy())
            f(root.left, pathsum, cur)
            f(root.right, pathsum, cur)
            cur.pop()


        f(root, 0, [])
        return self.res

#7/18/24 review:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def f(root, pathsum, cur):
            if not root:
                return 
            cur.append(root.val)
            pathsum += root.val #5, 9, 20
            if pathsum == targetSum and not root.left and not root.right:
                self.res.append(cur.copy())
                print(self.res)
            f(root.left, pathsum, cur) 
            f(root.right, pathsum, cur)
            cur.pop()
        f(root, 0, [])
        print(self.res)
        return self.res


#9/29/24 refresher:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def f(root, ps, cur):
            if not root:
                return 0
            ps += root.val
            cur.append(root.val)
            if not root.left and not root.right and ps == targetSum:
                self.res.append(cur.copy())
                ps = 0
            f(root.left, ps, cur)
            f(root.right, ps, cur)
            cur.pop()

        f(root, 0, [])
        return self.res


#this works too as we don't care about if we put the if not root.left and not root.right check after or before the recursive calls because we only care about the pathsum:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        def f(root, ps, cur):
            if not root:
                return 0
            ps += root.val
            cur.append(root.val)
            #if not root.left and not root.right and ps == targetSum:
            #    self.res.append(cur.copy())
            #    ps = 0
            f(root.left, ps, cur)
            f(root.right, ps, cur)
            if not root.left and not root.right and ps == targetSum:
                self.res.append(cur.copy())
                ps = 0
            cur.pop()

        f(root, 0, [])
        return self.res
