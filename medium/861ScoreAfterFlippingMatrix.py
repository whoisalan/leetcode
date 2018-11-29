# A[i][0] is worth 1 << (N - 1) points, more than the sum of (A[i][1] + .. + A[i][N-1]).
# We need to toggle all A[i][0] to 1.


class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        sum=0
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[i])):
                    A[i][j] = 0 if A[i][j]==1 else 1  
                continue
        
        B = list(zip(*A))
        for i in range(len(B)):
            B[i] = list(B[i])
            if B[i].count(1)<len(B[i])/2:
                for j in range(len(B[i])):
                    B[i][j] = 0 if B[i][j]==1 else 1    
                continue
        
        A = zip(*B)        

        for i in A:
            sum+=int(''.join(str(j) for j in i),2)
        
        return sum


