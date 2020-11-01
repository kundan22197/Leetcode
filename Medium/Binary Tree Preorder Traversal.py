# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # ITERATIVE
        
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
            
        return res
            
        
        # RECURSIVE
        
        l = []
        def preorder(node, l):
            if node:
                l.append(node.val)
                preorder(node.left, l)
                preorder(node.right, l)
        preorder(root, l)
        return l


        # SHORTER RECURSIVE

         
        def preorder(root):
            if root:
                return [root.val]+preorder(root.left)+preorder(root.right)
            else:
                return []
        return preorder(root)