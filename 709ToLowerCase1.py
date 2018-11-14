


# ascii 大小写中间相差32
class Solution(object):
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)


# "".join(chr(ord(c)+32) if 'A'<=c<='Z' else c for c in str)

print('HBSE'.lower())

