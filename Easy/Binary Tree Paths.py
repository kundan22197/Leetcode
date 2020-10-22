# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        # DFS RECURSIVE
        
        l = []
        def helper(root, st):
            if not root:
                return 
            if not root.left and not root.right:
                l.append(st+str(root.val))
                
            if root.left:
                helper(root.left, st+str(root.val)+'->')
            if root.right:
                helper(root.right, st+str(root.val)+'->')
                
        helper(root, '')
        return l
    
    
        # DFS USING STACK
        
        if not root:
            return []
        res, stack = [], [(root, '')]
        while stack:
            node, st = stack.pop()
            if not node.left and not node.right:
                res.append(st+str(node.val))
            if node.right:
                stack.append((node.right, st+str(node.val)+'->'))
            if node.left:
                stack.append((node.left, st+str(node.val)+'->'))
        return res
        
        
        # BFS USING QUEUE
        
        if not root:
            return []
        res, queue = [], [(root, '')]
        while queue:
            node, st = queue.pop(0)
            if not node.left and not node.right:
                res.append(st+str(node.val))
            if node.left:
                queue.append((node.left, st+str(node.val)+'->'))
            if node.right:
                queue.append((node.right, st+str(node.val)+'->'))
        return res
        
        
        