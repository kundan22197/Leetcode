import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == s:
            return True
        if re.match("^\w?$", p):
            return False
        p = "^" + p + "$"
        if re.match(p, s):
            return True
        return False