"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""



# 用队列和栈(list)实现 √
class Solution(object):
    def postorder(self, root):
        ret, stack = [], root and [root]
        while stack:
            node = stack.pop()
            ret.append(node.val)
            stack += [child for child in node.children if child] # 中-右-左 的逆序 左-右-中
        return ret[::-1]

# 递归实现
class Solution(object):
    def __init__(self):
        self.list = []
    def postorder(self, root):
        if root == None:
            return []
        children = root.children
        for c in children:
            self.preorder(c)
        self.list.append(root.val)
        return self.list

