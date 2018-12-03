class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split('+')
        a[1]=a[1].strip('i')
        b = b.split('+')
        b[1]=b[1].strip('i')

        ans = ""

        ans = str(int(a[0])*int(b[0]) - int(a[1])*int(b[1]))
        ans += '+' +str(int(a[0])*int(b[1])+int(a[1])*int(b[0])) + 'i'

        return ans 
