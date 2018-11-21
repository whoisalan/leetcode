class Solution(object):
    def sortArrayByParity(self, A):
        s, e = 0, len(A) - 1
        while s < e: 
            while A[s] % 2 == 0 and s < e:
                s += 1
            while A[e] % 2 == 1 and s < e: 
                e -= 1
            A[s], A[e] = A[e], A[s]
            
        return A