class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        m = -1
        list1 = list(S)
        for c in J:
            for i in list1:
                if c == i :
                    num = num + 1
        return num

a = Solution()
a.numJewelsInStones("aA","aAAbbbb")

# a = "aAAbbbb"
# a = list(a)
# a.remove('a')
# a.remove('A')
# print(a)