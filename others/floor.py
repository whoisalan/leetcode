class Solution:
    def climbStairs(self, n):
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)


class Solution:
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
        a=1;b=2;c=3
        for i in range(3,n+1):
            c=a+b;a=b;b=c
        return c
