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


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        """
        result = []
        for word in words:
            if len(word) == len(pattern):
                word_to_pattern_dict = {}
                pattern_to_word_dict = {}
                flag = True
                for i, char in enumerate(pattern):
                    if char not in pattern_to_word_dict and word[i] not in word_to_pattern_dict:
                        pattern_to_word_dict[char] = word[i]
                        word_to_pattern_dict[word[i]] = char
                    elif char in pattern_to_word_dict and pattern_to_word_dict[char] == word[i]:
                        continue
                    else:
                        flag = False
                        break
                if flag: result.append(word)
        return result


# 我最开始的想法:
from collections import OrderedDict

class Solution(object):
    def getPattern(self, s):
        temp = OrderedDict()
        for ch in s:
            if ch not in temp.keys():
                temp[ch] = [i for i, x in enumerate(s) if x == ch]
        #print temp.values()
        return temp.values()

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        basePattern = self.getPattern(pattern)
        #basePattern2 = self.getPattern2(pattern)
        for word in words:
            if basePattern == self.getPattern(word):
                res.append(word)
        return res
        