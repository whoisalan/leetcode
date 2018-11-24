
# subset:子集
# 考虑了大小写

def findWords(self, words):
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    ret = []
    for word in words:
      w = set(word.lower())
      if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
        ret.append(word)
    return ret