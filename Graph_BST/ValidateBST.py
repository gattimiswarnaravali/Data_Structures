# BST
# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        return self.validate(root, -math.inf, math.inf)
        
    def validate(self,root, low,high):
        if not root:
            return True
        
        if root.val < low or root.val > high:
            return False
        
        return (self.validate(root.right, root.val, high)) and (self.validate(root.left, low, root.val))
    
class Solution1:
    prev = math.inf
    def isValidBST(self, root) -> bool:
        return self.in_order(root)
        
    def in_order(self,root):
        if not root:
            return True
        if not self.in_order(root.left):
            return False
        
        if root.val >= self.prev:
            return False
        self.prev = root.val
        return self.in_order(root.right)

        
Solution1().isValidBST(None)
        