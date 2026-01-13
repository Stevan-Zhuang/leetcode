# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def r(n,m):
            if n is None:
                return 0
            s=n.val+r(n.left,m)+r(n.right,m)
            m[n] = s 
            return s 
        m={}
        def mm(n):
            if n is None:
                return 0 
            return m[n]*(r_s-m[n])
        r(root,m)
        r_s = m[root]
        def rr(n):
            if n is None:
                return 0
            return max([mm(n.left),mm(n.right),
                rr(n.left),rr(n.right)
                       ])
        return rr(root) % (10**9 + 7)
