class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = 0
        r=len(A)-1
        while(l<len(A)-1 and r>0):
            if A[l]%2 != 0 and A[r]%2 ==0:
                A[l],A[r] = A[r],A[l]
                l = l+2
                r = r-2  
            elif A[l]%2==0 and A[r]%2==0:
                l = l+2
            elif A[l]%2!=0 and A[r]%2!=0:
                r = r-2
            else:
                l = l+2
                r = r-2  
        return A   
a = Solution()
a.sortArrayByParityII([888,505,627,846]) 


class Solution:
    def sortArrayByParityII(self, A):
        even, odd = [a for a in A if not a % 2], [a for a in A if a % 2]
        return [even.pop() if not i % 2 else odd.pop() for i in range(len(A))]