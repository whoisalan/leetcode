class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
       
        res=[]
        while S:
            length = len(S)
            S1 = list(reversed(S))
            idx_old = length-S1.index(S[0])
            idx = max([length-S1.index(S[j]) for j in range(idx_old)])    
            while(idx!=idx_old):
                idx_old = idx
                idx = max([length-S1.index(S[j]) for j in range(idx_old)])
            res.append(idx)
            S = S[idx:]
        return res

S = "qiejxqfnqceocmy"
a = Solution()
a.partitionLabels(S)