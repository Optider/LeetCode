# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        best = 0
        
        def dfs(node) :
            nonlocal best
            
            if node is None :
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            best = max(best, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return best
