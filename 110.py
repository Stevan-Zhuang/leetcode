# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isBalancedRecursive(node):
    l = 0
    if node.left is not None:
        l, b = isBalancedRecursive(node.left)
        if not b:
            return 0, False
    r = 0
    if node.right is not None:
        r, b = isBalancedRecursive(node.right)
        if not b:
            return 0, False
    return max(l, r) + 1, abs(l - r) <= 1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        _, b = isBalancedRecursive(root)
        return b
