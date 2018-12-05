class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        res = []
        for i in range(num+1):
            s = str(bin(i))
            res.append(s.count('1'))
        
        return res