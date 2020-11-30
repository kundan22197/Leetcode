class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {k: 0 for k in s}
        for i in range(len(s)):
            dic[s[i]] += 1
        
        for i, ch in enumerate(s):
            if dic[ch] == 1:
                return i
        return -1            