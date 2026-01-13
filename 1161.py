class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        mm = {}
        def m(d,v):
            if not d in mm:
                mm[d] = 0 
            mm[d] += v
        q = [(root,1)]
        while q:
            n,d = q.pop(0)
            if n is None:
                continue 
            m(d,n.val)
            q.append((n.left,d+1))
            q.append((n.right,d+1))
        b = 0 
        bs = -float("inf")
        for d in mm:
            if mm[d] > bs:
                bs = mm[d]
                b = d 
        return b
