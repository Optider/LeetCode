def max_paths(node: TreeNode) -> (int, int):
    """
    The first member of the return value is the max path
    of the subtree with `node` as the root
            
    The second member is the max sum of a path in the subtree
	that could be extended through the parent of `node`
    """
    if not node:
        return float('-inf'), float('-inf')

    l_max, l_max_extendable = max_paths(node.left)
    r_max, r_max_extendable = max_paths(node.right)

    max_extendable = node.val + max(
        l_max_extendable,
        r_max_extendable,
        0
    )
        
    max_all = max(
        max_extendable,
        l_max_extendable + r_max_extendable + node.val,
        l_max,
        r_max
    )

    return max_all, max_extendable


class Solution(object):
    def maxPathSum(self, root: TreeNode) -> int:
        return max_paths(root)[0]
