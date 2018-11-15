class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        i = 0
        j = len(A)-1
        
        while(i <= j):
            if A[j]%2==0 and A[i]%2==1:
                A[i],A[j] = A[j],A[i]
            elif A[i]%2==0:
                i = i +1
            elif A[j]%2==1:
                j = j-1
            else:
                i = i+1
                j = j-1
        
        print(A)

a = Solution()
input = [3,1,2,4]
a.sortArrayByParity(input)