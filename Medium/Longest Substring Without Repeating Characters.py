class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = list(map(str, s))
        l = []
        m = 0
        j = 0
        while j < len(st):
            while j < len(st) and st[j] not in l:
                l.append(st[j])
                j += 1
            m = max(len(l), m)
            l = l[1:]
        return m   
                
