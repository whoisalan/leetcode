class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        num = 0
        ext = 0
        for i in S:
            if i == '(':
                num += 1 
            elif i == ')':
                num -= 1
                if num == -1:
                    ext += 1
                    num = 0
        
        return num + ext
        
        
