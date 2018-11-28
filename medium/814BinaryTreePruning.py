# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return root
        if root.left :
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)
        
        if not root.left and not root.right and root.val == 0:
            return None
        else:
            return root

        return root