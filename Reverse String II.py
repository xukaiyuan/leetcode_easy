class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if(len(s) < k):
            return self.reverse(s)
        res = ""
        for i in range(0, len(s), 2 * k):           
            sk = s[i:i + k]
            sk_re = self.reverse(sk)
            if((i + k) > len(s)):
                tmp = sk_re
            else:
                tmp = sk_re + s[i + k: min(i + 2 * k, len(s))]
            res += tmp
        return res

    def reverse(self, s):
        length = len(s)
        res = ""
        for i in range(length):
            res += s[length - 1 - i]
        return res