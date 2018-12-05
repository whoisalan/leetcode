# 我日吗，绝妙！
# 但只能说，太浪费时间了


def flipEquiv(self, root1, root2):
# 两个都为空
if not root1 and not root2:
return True
# 只有一个为空
if not root1 or not root2:
return False
# 两个都不为空，但值不相同
if root1.val != root2.val:
return False

# 如果两个都不为空，而且值相同
# (left,left) or (left,right) or (right,right) or (right,left)
return (self.flipEquiv(root1.left,root2.left) or self.flipEquiv(root1.left,root2.right)) and  (self.flipEquiv(root1.right,root2.left) or self.flipEquiv(root1.right,root2.right))



class Solution:
def flipEquiv(self, root1, root2):
"""
:type root1: TreeNode
:type root2: TreeNode
:rtype: bool
"""
if root1 is None and root2 is None:
return True
if root1 is None or root2 is None:
return False

# Each value in each tree will be a unique integer in the range [0, 99].
q1 = collections.deque()
q2 = collections.deque()
q1.append(root1)
q2.append(root2)


while len(q1) > 0 and len(q2) > 0:
n1 = q1.popleft()
n2 = q2.popleft()
if n1.val != n2.val:
return False

# 同为空算相同
# 数值相同也算相同
n1L = None if n1.left is None else n1.left.val
n1R = None if n1.right is None else n1.right.val
n2L = None if n2.left is None else n2.left.val
n2R = None if n2.right is None else n2.right.val

# 正匹配
if n1L == n2L and n1R == n2R:
if n1L is not None:
q1.append(n1.left)
q2.append(n2.left)
if n1R is not None:
q1.append(n1.right)
q2.append(n2.right)
# 反匹配
elif n1L == n2R and n1R == n2L:
if n1L is not None:
q1.append(n1.left)
q2.append(n2.right)
if n1R is not None:
q1.append(n1.right)
q2.append(n2.left)
else:
return False

return True

