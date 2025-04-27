# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            if root is None:
                return []
            
            leaves = dfs(root.left) + dfs(root.right)

            return leaves or [root.val]

        leaves1 = dfs(root1)
        leaves2 = dfs(root2)

        # print(f'leaves1: {leaves1}')
        # print(f'leaves2: {leaves2}')
        
        return leaves1 == leaves2
