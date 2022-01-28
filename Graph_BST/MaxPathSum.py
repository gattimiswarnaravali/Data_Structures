class Solution:
    def maxPathSum(self, root):
        max_path = float('-inf')
        
        def get_max_path(node):
            nonlocal max_path
            if node is None:
                return 0
            
            left_node_gain = max(get_max_path(node.left),0)
            right_node_gain = max(get_max_path(node.right),0)
            
            cuurent_val = node.val + left_node_gain + right_node_gain
            max_path = max(max_path, cuurent_val)     
                       
            
            return node.val + max(left_node_gain, right_node_gain)
        get_max_path(root)
        return max_path
    
from collections import deque
class Solution1:
    def maxPathSum(self, root) -> int:
        
        childrenSum = dict()
        centerNode = None
        maxSum = float('-inf')
        
        def getSubTreeSum(node):
            nonlocal maxSum
            nonlocal centerNode
            if not node:
                return 0
            
            leftTreeSum  = max(getSubTreeSum(node.left), 0)
            rightTreeSum = max(getSubTreeSum(node.right), 0)
            childrenSum[node] = (leftTreeSum, rightTreeSum)
            
            nodeSum = node.val + leftTreeSum + rightTreeSum
            if nodeSum > maxSum:
                centerNode = node
                maxSum = nodeSum
            return node.val + max(leftTreeSum, rightTreeSum)
        

        def buildPath(node, childrenSum, path, left=True):
            left_val, right_val = childrenSum[node]
            if left_val==0 and right_val==0:
                return
            if left_val > right_val:
                if left:
                    path.appendleft(node.left.val)
                else:
                    path.append(node.left.val)
                node = node.left
            else:
                if left:
                    path.appendleft(node.right.val)
                else:
                    path.append(node.right.val)
                node = node.right

            buildPath(node, childrenSum, path, left)


        def getPath(centerNode, childrenSum):
            path = deque()
            path.append(centerNode.val)
            left_val, right_val = childrenSum[centerNode]

            if left_val > 0:
                path.appendleft(centerNode.left.val)
                node = centerNode.left
                buildPath(node, childrenSum, path, left=True)

            if right_val > 0:
                path.append(centerNode.right.val)
                node = centerNode.right
                buildPath(node, childrenSum, path, left=False)
            return path

        getSubTreeSum(root)
        print(getPath(centerNode, childrenSum))   
        return maxSum