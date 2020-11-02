# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # TOP DOWN
        
        def depth_max(root, depth):
            
            if not root:
                return
            if not root.left and not root.right:
                self.res = max(self.res, depth)
                
            depth_max(root.left, depth+1)
            depth_max(root.right, depth+1)
        
        
        depth_max(root, 1)
        return self.res
    
    
        # BOTTOM UP
        
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
        