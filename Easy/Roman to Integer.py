class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        while i < len(s):
            if i < len(s)-1 and s[i] == 'I' and s[i+1] == 'V':
                num += 4
                i += 2
                continue
            if i < len(s)-1 and s[i] == 'I' and s[i + 1] == 'X':
                num += 9
                i += 2
                continue
            if i < len(s)-1 and s[i] == 'X' and s[i + 1] == 'L':
                num += 40
                i += 2
                continue
            if i < len(s)-1 and s[i] == 'X' and s[i + 1] == 'C':
                num += 90
                i += 2
                continue
            if i < len(s)-1 and s[i] == 'C' and s[i + 1] == 'D':
                num += 400
                i += 2
                continue
            if i < len(s)-1 and s[i] == 'C' and s[i + 1] == 'M':
                num += 900
                i += 2
                continue
            num += d[s[i]]
            i += 1
            
        return num 