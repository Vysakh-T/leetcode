# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recf(self, root,a):
        if root==None:
            return a
        self.recf(root.left,a)
        a.append(root.val)
        self.recf(root.right,a)
        return a
        
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.recf(root,[])