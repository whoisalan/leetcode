import collections

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    a = collections.Counter(nums)
    res = []
    for k,v in a.items():
        if v>=2:
            res.append(k)
    
    return res