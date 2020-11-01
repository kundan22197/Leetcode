# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        # SHORTER RECURSIVE
        
        def inorder(root):
            if root:
                return inorder(root.left)+[root.val]+inorder(root.right)
            else:
                return []
        return inorder(root)
        
        
        # RECURSIVE
        
        l = []
        def inorder(node, l):
            if node:
                inorder(node.left, l)
                l.append(node.val)
                inorder(node.right, l)
        inorder(root, l)
        return l
        
        
        # ITERATIVE
        
        res = []
        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
        
        
            
            
            
            
            
            