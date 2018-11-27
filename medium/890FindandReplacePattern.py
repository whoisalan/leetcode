

class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        b = pattern
        def is_iso(a):
            return len(a) == len(b) and len(set(a)) == len(set(b)) == len(set(zip(a, b)))
        return list(filter(is_iso, words))

# filter(func,list),返回一个迭代器
# 仅仅返回func判断为真的值
# zip这个绝了