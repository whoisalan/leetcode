
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        
        for i in range(len(A)):
             A[i] = list(reversed(A[i]))
            A[i] = list(map(yihuo,A[i]))
            
        return A

def yihuo(x):
    return x^1    


a = Solution()
a.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])