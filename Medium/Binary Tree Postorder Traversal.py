# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # SHORTER RECURSIVE
        
        def postorder(root):
            if root:
                return postorder(root.left)+postorder(root.right)+[root.val]
            else:
                return []
        return postorder(root)
        
        
        
        # RECURSIVE
        
        l = []
        def postorder(root, l):
            if root:
                postorder(root.left, l)
                postorder(root.right, l)
                l.append(root.val)
        postorder(root, l)
        return l
        
        
        
        # ITERATIVE
        
        l, stack = [], [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    l.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return l
                
        