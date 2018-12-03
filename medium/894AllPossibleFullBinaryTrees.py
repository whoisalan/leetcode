# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 绝妙！！
# 一般要求返回所有答案的题都是递归

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        # 因为root占一个位置，而左右子树要么就有没有节点，
        # 要么就有两个节点，故一定总数为偶数
        N -= 1
        if N == 0: return [TreeNode(0)]
        res = []
        # N是总数，如果左子树里根的个数为1，右子树就为N-1
        for l in range(1, N, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l):
                    node = TreeNode(0)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
