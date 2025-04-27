# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        leftlca = self.lowestCommonAncestor(root.left, p, q)
        rightlca = self.lowestCommonAncestor(root.right, p, q)

        # print(f'root: {root.val}')
        # print(f'left: {leftlca}, right: {rightlca}')

        if leftlca and rightlca:
            return root

        return leftlca if leftlca else rightlca