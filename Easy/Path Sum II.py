# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        # RECURSIVE TOP DOWN
        
        res = []
        def path(node, sum, ls):
            if not node:
                return 
            
            if not node.left and not node.right and sum == node.val:
                ls.append(node.val)
                res.append(ls)
                return
            
            if node.left:
                path(node.left, sum-node.val, ls+[node.val])
            if node.right:
                path(node.right, sum-node.val, ls+[node.val])
                
            
        path(root, sum, [])
        return res
    
    
    
    
        # DFS USING STACK
        
        if not root:
            return []
        
        res = []
        stack = [(root, sum-root.val, [root.val])]
        
        while stack:
            node, rem, ls = stack.pop()
            
            if not node.left and not node.right and rem == 0:
                res.append(ls)
                
            if node.right:
                stack.append((node.right, rem-node.right.val, ls+[node.right.val]))
            
            if node.left:
                stack.append((node.left, rem-node.left.val, ls+[node.left.val]))
        return res
            
    
    
    
    
    
    
        # BFS USING QUEUE
        
        if not root:
            return []
        res = []
        queue = [(root, sum-root.val, [root.val])]
        
        while queue:
            node, rem, ls = queue.pop(0)

            if not node.left and not node.right and rem == 0:
                res.append(ls)
            
            if node.left:
                queue.append((node.left, rem-node.left.val, ls+[node.left.val]))
            if node.right:
                queue.append((node.right, rem-node.right.val, ls+[node.right.val]))
            
        return res