# fail!!!

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
        else:
            return t1 or t2



class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if not t1 and not t2: return None
        if t1:
            v1, L1, R1 = t1.val, t1.left, t1.right
        else:
            v1, L1, R1 = 0, None, None
        if t2:
            v2, L2, R2 = t2.val, t2.left, t2.right
        else:
            v2, L2, R2 = 0, None, None

        node = TreeNode(v1+v2)
        node.left = self.mergeTrees(L1, L2)
        node.right = self.mergeTrees(R1, R2)
        return node


class Solution(object):
    def mergeTrees(self, t1, t2):
        if (t2 is None): return t1
        if (t1 is None): return t2
        merged = TreeNode(t1.val + t2.val)
        merged.left = self.mergeTrees(t1.left, t2.left)
        merged.right = self.mergeTrees(t1.right, t2.right)
        return merged
                `