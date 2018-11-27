

# 最大的被取消了
# a = [1,2,3,4,5]
# print(a[2:])
# print(a[3:])

class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        root, maxi = TreeNode(max(nums)), nums.index(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:maxi])
        root.right = self.constructMaximumBinaryTree(nums[maxi + 1:])
        return root
