# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        l = [root.val]
        queue = [root]
        
        while queue:
            node = queue.pop(0)

            if node.left:
                l.append(node.left.val)
                queue.append(node.left)
            else:
                l.append('null')
                
                
            if node.right:
                l.append(node.right.val)
                queue.append(node.right)
            else:
                l.append('null')

        return l
                
                
        
        
        
        
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        
        if not data:
            return None

        root = TreeNode(data[0])
        queue = [root]
        index = 1
        while queue:
            
            node = queue.pop(0)
            
            if data[index] != 'null':
                node.left = TreeNode(data[index])
                queue.append(node.left)
            index += 1
            if data[index] != 'null':
                node.right = TreeNode(data[index])
                queue.append(node.right)
            index += 1
             
        
        return root
      
            
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))