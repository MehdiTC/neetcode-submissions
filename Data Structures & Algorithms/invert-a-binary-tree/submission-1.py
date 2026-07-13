# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None 
        
        def swapNodes(node):
            new_left = None
            new_right = None
            if node.left: new_right = swapNodes(node.left)
            if node.right: new_left = swapNodes(node.right)

            node.left = new_left
            node.right = new_right


            return node
        return swapNodes(root)

