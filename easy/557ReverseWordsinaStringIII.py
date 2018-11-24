class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list = s.split(" ")
        lists = []
        for word in list:
            word = "".join(reversed(word))
            lists.append(word)
        
        return " ".join(lists)


# Here I first reverse the order of the words and then reverse the entire string.

def reverseWords(self, s):
    return ' '.join(s.split()[::-1])[::-1]