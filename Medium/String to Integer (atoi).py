import re
class Solution:
    def myAtoi(self, str: str) -> int:
        
        
        def check(l):
            if not l or l[0:2] in ['+', '-']:
                return 0
            if l[0] == "+":
                if int(l[1:]) > pow(2, 31) - 1:
                    return pow(2, 31) - 1
            elif l[0] == "-":
                if int(l[1:]) > pow(2, 31):
                    return -pow(2, 31)
            else:
                if int(l) > pow(2, 31) - 1:
                    return pow(2, 31) - 1
            return int(l)

        s = str.lstrip(" ")
        pattern = "^-?\+?\d+"
        pattern1 = "[^0-9]"
        l = ''
        if re.match(pattern, s):
            i = 0
            while i < len(s):
                l += ''.join(s[i])
                i += 1
                if (i < len(s) and re.match(pattern1, s[i])):
                    return check(l)
            return check(l)
        else:
            return 0