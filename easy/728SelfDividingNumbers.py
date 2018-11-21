class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        list1 = [n for n in range(left,right+1)]
        ans = []
        for i in list1:
            ans.append(i)
            shang = i
            while(shang>1):
                yu = shang % 10
                if yu != 0:
                    if i%yu != 0:
                        ans.pop(-1)
                        break
                else:
                    ans.pop(-1)
                    break
                shang = shang // 10
        
        return ans

a = "123456"
for i in a:
    print(int(i))


