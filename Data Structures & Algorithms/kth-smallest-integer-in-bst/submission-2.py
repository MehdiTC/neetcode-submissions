# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        iters = k

        def inOrder(root):
            nonlocal res, iters

            if not root: return 

            inOrder(root.left)
            iters-=1

            if iters == 0: res = root.val

            inOrder(root.right)
        
        inOrder(root)
        return res

        