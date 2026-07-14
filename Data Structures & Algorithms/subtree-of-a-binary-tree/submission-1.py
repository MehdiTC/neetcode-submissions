# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(subTree, subRoot):
            if not subTree and not subRoot:
                return True 
            if subTree and subRoot and subTree.val == subRoot.val:
                return sameTree(subTree.left, subRoot.left) and sameTree(subTree.right, subRoot.right)
            else:
                return False
        
        if not root:
            return False
        print(root.val)
        if sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        