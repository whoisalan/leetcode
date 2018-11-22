"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        depth = 1
        node = root
        if node:
            return self.recursion(node,depth)
        else :return 0

    def recursion(self,root,depth):
        childs = root.children
        depths=[]
        if childs:
            depth+=1
            for node in childs:
                depths.append(self.recursion(node,depth))
            return max(depths)
        else: return depth 

# 绝妙
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1