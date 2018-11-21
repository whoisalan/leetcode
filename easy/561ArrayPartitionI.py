class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        for i in range(0,len(nums),2):
            ans = ans + nums[i]
        return ans

# return sum(sorted(nums)[::2])