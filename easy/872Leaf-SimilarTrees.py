# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        ans1 = self.preorder(root1)
        ans2 = self.preorder(root2)

        return ans1 == ans2

    def preorder(self,root):
        if root == None:
            return []

        stack = [root]
        ans = []
        node = root
        while len(stack):
            node = stack.pop()
            if not node.right and not node.left:
                ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return ans


# 方法嵌套方法
# itertools.izip_longest 还没搞懂
 def leafSimilar(self, root1, root2):
        def dfs(node):
            if not node: return
            if not node.left and not node.right: yield node.val
            for i in dfs(node.left): yield i
            for i in dfs(node.right): yield i
        return all(a == b for a, b in itertools.izip_longest(dfs(root1), dfs(root2)))