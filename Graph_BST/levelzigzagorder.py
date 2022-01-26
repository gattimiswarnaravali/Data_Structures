# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root) :
        
        # final_arr = []
        # def in_level(root, fianl_arr):
        #     if root is None:
        #         # final_arr.append([])
        #         return
        #     else:
        #         arr = []
        #         if root.left:
        #             arr.append(root.left.val)
        #         if root.right:
        #             arr.append(root.right.val)
        #         final_arr.append(arr) if len(arr) > 0 else None
            
        # if root is not None:
        #     final_arr.append([root.val])
        # else:
        #     final_arr.append([])
        # in_level(root, final_arr)
        # in_level(root.left, final_arr)
        # in_level(root.right,final_arr)
        # return final_arr
        levels = []
        def helper(node, level):
            if node:
                if len(levels) == level:
                     levels.append([])
                    
                if level % 2 != 0:
                    levels[level].insert(0,node.val)
                else:
                    levels[level] += [node.val]
                helper(node.left, level+1)
                helper(node.right, level+1)
            
        helper(root,0)
        return levels

from collections import deque
class Solution1:
    def levelOrder(self, root) :
        levels = []
        if root is None:
            return levels
        level = 0
        q=deque([root,])
        
        while q:
            levels.append([])
            len_levels = len(q)
            
            for i in range(len_levels):
                node = q.popleft()
                if level % 2 != 0:
                    levels[level].insert(0, node.val)
                else:
                    levels[level].append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            level+=1
        return levels
    
            
        
            
TN = TreeNode(3)    
TN.left= TreeNode(9)
TN.right= TreeNode(20)
TN.left.left= TreeNode(11)
TN.right.left= TreeNode(15)
TN.right.right = TreeNode(7)

print(Solution1().levelOrder(TN))