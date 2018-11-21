class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        for i in range(0,len(emails)):
            add = emails[i]
            list1 = add.split("@")
            list2 = list1[0].split("+")
            list3 = list2[0].split(".")
            name = "".join(list3) + "@" + list1[1]
            emails[i] = name
        
        return len(set(emails))
            


a = Solution()
input1=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(a.numUniqueEmails(input1))
