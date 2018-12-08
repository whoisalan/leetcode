
# Counter是一个简单的计数器，例如，统计字符出现的个数：
# 比如：
# counts = collections.Counter(T)
# 可以直接统计T中字符的个数
class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = []
        T = list(T)
        for i,j in enumerate(S):
            for n,m in enumerate(T):
                if m == j:
                    res.append(m)
                    T[n] = ''  

        res = "".join(res) + "".join(T)

        return res