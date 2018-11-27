# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val>root.val:
            if root.right:
                self.insertIntoBST(root.right,val)
            else:
                node=TreeNode(val)
                root.right=node
        if val<root.val:
            if root.left:
                self.insertIntoBST(root.left,val)
            else:
                node = TreeNode(val)
                root.left = node
        
        return root