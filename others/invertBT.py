class Solution:
    def flipBT(self,root):
        if root is None:
            return root
        
        stack = [root]


        while stack:
            node = stack.pop(0)
            node = self.flip(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right) 

    
    def flip(self,root):
        left = root.right
        right = root.left

        root.left = left
        root.right = right

        return root


# 别人的递归
def inverttree(self, treenode):      #真正的翻转只有这8行代码
        if treenode == None:
            return None
        temp = treenode.lchild
        treenode.lchild = treenode.rchild
        treenode.rchild = temp
        self.inverttree(treenode.lchild)
        self.inverttree(treenode.rchild)
