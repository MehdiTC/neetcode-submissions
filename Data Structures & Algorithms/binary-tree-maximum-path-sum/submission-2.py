# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        def checkPath(root):
            if not root: return 0
            return max((root.val + max(checkPath(root.left),checkPath(root.right),0)),0)
        
        q = deque([root])
        while q:
            curr = q.pop()
            currSum = curr.val + checkPath(curr.left) + checkPath(curr.right)
            print(f"left path = {checkPath(curr.left)}\nright path = {checkPath(curr.right)}\ncurrSum = {currSum}")
            if currSum>maxSum:
                maxSum = currSum
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        
        return maxSum

        