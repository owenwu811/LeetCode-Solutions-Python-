#Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
#height-balanced
# binary search tree.


#python3 solution:

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = [] 
        while head: #put all values of linked list into an array
            nums.append(head.val)
            head = head.next
        # print(nums)

        def constructBST(nums):
            n = len(nums)
            if not n:
                return None
            mid = (n-1)//2 #find the midpoint of our list because we know the root will be the mid node
            root = TreeNode(nums[mid]) #creating root node with mid in nums array
            root.left = (constructBST(nums[:mid])) #building left subtree with elements to the left of mid in our nums array and will be cut in a half again over and over in recursion
            root.right = (constructBST(nums[mid+1:])) #building right subtree with element to the right of mid in our nums array
            return root #return entire tree that was constructed
        return constructBST(nums) #return result of recursive call with our nums array passed in 
