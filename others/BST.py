def insert(self, root, val):
    '''二叉搜索树插入操作'''
    if root == None:
        root = TreeNode(val)
    elif val < root.val:
        root.left = self.insert(root.left, val)
    elif val > root.val:
        root.right = self.insert(root.right, val)
    return root

def query(self, root, val):
    '''二叉搜索树查询操作'''
    if root == None:
        return False
    if root.val == val:
        return True
    elif val < root.val:
        return self.query(root.left, val)
    elif val > root.val:
        return self.query(root.right, val)

def findMin(self, root):
    '''查找二叉搜索树中最小值点'''
    if root.left:
        return self.findMin(root.left)
    else:
        return root

def findMax(self, root):
    '''查找二叉搜索树中最大值点'''
    if root.right:
        return self.findMax(root.right)
    else:
        return root

def delNode(self, root, val):
    '''删除二叉搜索树中值为val的点'''
    if root == None:
        return 
    if val < root.val:
        root.left = self.delNode(root.left, val)
    elif val > root.val:
        root.right = self.delNode(root.right, val)
    # 当val == root.val时，分为三种情况：只有左子树或者只有右子树、有左右子树、即无左子树又无右子树
    else:
        if root.left and root.right:
            # 既有左子树又有右子树，则需找到右子树中最小值节点
            temp = self.findMin(root.right)
            root.val = temp.val
            # 再把右子树中最小值节点删除
            root.right = self.delNode(root.right, temp.val)
        elif root.right == None and root.left == None:
            # 左右子树都为空
            root = None
        elif root.right == None:
            # 只有左子树
            root = root.left
        elif root.left == None:
            # 只有右子树
            root = root.right
    return root

#深度
def depth(tree):
    if tree==None:
        return 0
    left,right=depth(tree.left),depth(tree.right)
    return max(left,right)+1
#前序遍历   
def pre_order(tree):
    if tree==None:
        return
    print tree.data
    pre_order(tree.left)
    pre_order(tree.right)
#中序遍历   
def mid_order(tree):
    if tree==None:
        return
    mid_order(tree.left)
    print tree.data
    mid_order(tree.right)    
#后序遍历   
def post_order(tree):
    if tree==None:
        return
    post_order(tree.left)
    post_order(tree.right)   
    print tree.data
    
#层次遍历    
def level_order(tree):
     if tree==None:
        return 
     q=[]
     q.append(tree)
     while q:
         current=q.pop(0)
         print current.data
         if current.left!=None:
            q.append(current.left)
         if current.right!=None:
            q.append(current.right)
#按层次打印
def level2_order(tree):
     if tree==None:
        return 
     q=[]
     q.append(tree)
     results={}
     level=0
     current_level_num=1
     nextlevelnum=0
     d=[]
     while q: 
         current=q.pop(0)
         current_level_num-=1
         d.append(current.data)
         if current.left!=None:
            q.append(current.left) 
            nextlevelnum+=1
         if current.right!=None:
            q.append(current.right) 
            nextlevelnum+=1   
         if current_level_num==0:
            current_level_num=nextlevelnum
            nextlevelnum=0
            results[level]=d
            d=[]
            level+=1
     print results    