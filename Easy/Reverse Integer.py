class Solution:
    def reverse(self, x: int) -> int:
        x1 = list(map(str, str(abs(x))))
        x1.reverse()
        x2 = int(''.join(x1))
        if x2 < -pow(2, 31) or x2 > pow(2, 31) - 1:
            return 0
        if x < 0:
            return -x2
        else:
            return x2
