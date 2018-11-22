# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BST 的顺序遍历就是二叉树的中序遍历：左-中-右
class Solution:
    # 栈实现
    def searchBST(self,root,val):
        if root==None:
            return
        # 定义一个栈,存储节点
        stack = []
        node = root
        while stack or node:
            #一直查找树的左节点,一直进栈
            while node:
                stack.append(node)
                node=node.lchild
            node=stack.pop()#该节点不存在左节点，该节点出栈，查找右节点
            if node.val == val :
                return node
            elif node.val>node:
                return []
            node=node.rchild
        

# 先序
def front_queueAndStack(self,root):
    if root==None:
        return
    #定义一个栈,存储节点
    stack=[]
    node=root
    while stack or node:
        #从树根开始一直输出左孩子
        while node:
            print node.data,
            #将输出的节点加入栈中
            stack.append(node)
            node=node.lchild
        #该节点不存在左节点时,该节点出栈,搜索该节点右节点，
        node=stack.pop()
        node=node.rchild

# 后序
def post_queueAndStack(self,root):
    if root == None:
        return
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left :
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().data)
    


# 先序：
def preorder(self,root):
    if root == None:
        return
    stack=[]
    node = root
    while stack or node:
        while node:
            print(node.data)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node=node.right

# 中序：
def inorder(self,root):
    if root == None:
        return
    
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.data)
        node = node.left





# 绝妙 ：
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        trav = root
        while trav:
            if trav.val == val:
                return trav
            elif trav.val < val:
                trav = trav.right
            else:
                trav = trav.left

class Solution:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root