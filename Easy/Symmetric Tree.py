# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def symmetric(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            return ((r1.val == r2.val) and symmetric(r1.left, r2.right) and symmetric(r1.right, r2.left))
        return symmetric(root, root)