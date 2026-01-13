# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        treeBackTraverse = {}
        queue = [(root, 0)]
        deepest = []
        while queue:
            node, depth = queue.pop(0)
            if node is None:
                continue
            deepest.append((node, depth))

            if node.left is not None:
                treeBackTraverse[node.left.val] = node
            if node.right is not None:
                treeBackTraverse[node.right.val] = node
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        max_depth = max(depth for _, depth in deepest)
        deepest = [node for node, depth in deepest if depth == max_depth]

        queue = deepest
        while queue:
            if len(set(queue)) == 1:
                return queue[0]
            node = queue.pop(0)
            if node.val in treeBackTraverse:
                queue.append(treeBackTraverse[node.val])
