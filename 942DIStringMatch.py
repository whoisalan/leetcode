class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        high = len(S)
        low = 0
        ans = []
       
        for i in range(0,len(S)):
            if S[i] == 'I':
                ans.append(low) 
                low = low+1
            else:
                ans.append(high) 
                high = high -1
        
        if S [-1]=='I':
            ans.append(low)
        else:
            ans.append(high)                
        return ans