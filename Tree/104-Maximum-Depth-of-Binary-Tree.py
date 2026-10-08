# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        function dfs(root,curr):
            if root==null:
                return 0
            maxLength = 1 + max(dfs(left,curr),dfs(right,curr))
            max = max(max,maxLength)
            return max
        

        """
        def dfs(root):
            if not root:
                return 0
            left_length = dfs(root.left)
            right_length = dfs(root.right)

            return 1+max(left_length,right_length)
        return dfs(root)