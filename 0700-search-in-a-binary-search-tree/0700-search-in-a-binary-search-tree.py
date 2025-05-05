# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = None

        def search(root):
            if root:
                if root.val == val:
                    return root
                else:
                    lans = search(root.left)
                    rans = search(root.right)
                
                if lans:
                    return lans
                elif rans:
                    return rans

            return None

        ans = search(root)

        return ans