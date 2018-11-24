class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        length = len(S)
        list = [length]*length
        for i in range(length):
            if S[i] == C:
                list[i]=0
            if list[i]==0:
                for j in range(0,i):
                    list[j] = (i - j) if (i-j)<list[j] else list[j]
                for j in range(i+1,length):
                    list[j] = (j-i) if (j-i)<list[j] else list[j]

        return list 