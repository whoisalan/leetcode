class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bit = len(str(bin(num)))-2
        return num^(int("1"*bit,2))