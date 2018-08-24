class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split(" ")
        res = ""
        for i in lst:
            tmp = self.reverse(i)
            res += tmp
            res += " "
        return res[:-1]


    def reverse(self, s):
        res = ""
        length = len(s)
        for i in range(length):
            res += s[length - 1 - i]
        return res