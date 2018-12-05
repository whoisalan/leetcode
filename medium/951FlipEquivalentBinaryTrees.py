# 我日吗，绝妙！

def flipEquiv(self, root1, root2):
	# 两个都为空
    if not root1 and not root2:
		return True
	# 只有一个为空
    if not root1 or not root2:
		return False
	# 两个都不为空，但值不相同
    if root1.val!=root2.val:
		return False

    # 如果两个都不为空，而且值相同
    # (left,left) or (left,right) or (right,right) or (right,left)
	return (self.flipEquiv(root1.left,root2.left) or self.flipEquiv(root1.left,root2.right)) and  (self.flipEquiv(root1.right,root2.left) or self.flipEquiv(root1.right,root2.right))