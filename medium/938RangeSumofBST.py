    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None


class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return
        stack = []
        node = root
        sum = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                if node.val >= L and node.val <=R:
                    sum += node.val
                elif node.val>R:
                    break       
                node = node.right
        return sum


# 绝妙：

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root: return 0
        if root.val<L: return self.rangeSumBST(root.right, L, R)
        elif root.val>R: return self.rangeSumBST(root.left, L, R)
        else: return root.val+self.rangeSumBST(root.left, L, R)+self.rangeSumBST(root.right, L, R)
        
            