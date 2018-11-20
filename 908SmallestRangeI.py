class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ma = max(A)
        mi = min(A)
        
        dif = ma - mi
        
        if dif > 2*K:
            return dif - 2*K
        else:
            return 0



# return max(0, max(A) - min(A) - 2 * K)