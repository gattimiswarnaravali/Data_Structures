# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        
        def is_mirror(l_root, r_root):
            if l_root is None and r_root is None:
                return True
            if l_root is None or r_root is None:
                return False
            return (l_root.val == r_root.val) and is_mirror(l_root.left, r_root.right) and is_mirror(l_root.right, r_root.left)
        
        if root is None:
            return True
        return is_mirror(root.left,root.right)
            