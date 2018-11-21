"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""



class Solution(object):
    def preorder(self, root):
        # 中-左-右
        # and 如果成立，赋值就等于后面的语句,不然就是0
        ret, q = [], root and [root]
        while q:
            node = q.pop()
            ret.append(node.val)
            q += [child for child in node.children[::-1] if child] #只有从后往前加，才能实现从前往后pop

        return ret


class Solution(object):

    def __init__(self):
        self.list = []
    def preorder(self, root):
        if root == None:
            return []
        self.list.append(root.val)
        children = root.children
        for c in children:
            self.preorder(c)
        return self.list



