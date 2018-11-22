class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count=[]

        for domain in cpdomains:
            word = domain.split(" ")
            num = word[0]
            
            while len(word)>1:
                try:
                    index = count.index(word[1])
                except ValueError:
                    count.append(num)
                    count.append(word[1])
                else: 
                    count[index-1]=str(int(num)+int(count[index-1]))
                word = word[1].split(".",1)

        for i in range(0,len(count)//2):
            num = count.pop(i)
            count[i] = num+ " " +count[i]
        
        return count

a =["9001 discuss.leetcode.com"]
b = Solution()
print(b.subdomainVisits(a))

# 我佛了
# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：

# >>> from collections import Counter
# >>> c = Counter()
# >>> for ch in 'programming':
# ...     c[ch] = c[ch] + 1
# ...
# >>> c
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})

def subdomainVisits(self, cpdomains):
    c = collections.Counter()
    for cd in cpdomains:
        n, d = cd.split()
        c[d] += int(n)
        for i in range(len(d)):
            if d[i] == '.': c[d[i + 1:]] += int(n)
    return ["%d %s" % (c[k], k) for k in c]