# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        
        
        # BFS USING QUEUE
        
        queue = []
        if root:
            queue = [(root, sum)]

        while queue:
            node, rem = queue.pop(0)
            if not node.left and not node.right and rem == node.val:
                return True
            if node.left:
                queue.append((node.left, rem-node.val))
            if node.right:
                queue.append((node.right, rem-node.val))   
        return False
    
    
    
        # RECURSIVE
        
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True

        sum -= root.val

        return (self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum))
    
    
        # DFS USING STACK
        
        stack = []
        if root:
            stack = [(root, sum)]
            
        while stack:
            node, rem = stack.pop()
            if not node.left and not node.right and rem == node.val:
                return True
            
            if node.right:
                stack.append((node.right, rem-node.val))
            if node.left:
                stack.append((node.left, rem-node.val))

        return False
            