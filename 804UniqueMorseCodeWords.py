class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
        x = ""
        pattern = []

        for i in words:
            for j in i:
                x = x + letters[ord(j)-ord('a')] 
            pattern.append(x)
            x = ""

        
        return len(set(pattern))

a = Solution()
words = ["gin", "zen", "gig", "msg"]
a.uniqueMorseRepresentations(words)