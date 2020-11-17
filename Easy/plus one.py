class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            i = len(digits)-2
            digits[i+1] = 0
            carry = 1
            while i>=0:
                digits[i+1] = 0
                carry = 1
                if digits[i] != 9:
                    carry = 0
                    digits[i] += 1
                    break
                else:
                    digits[i] = 0
                    carry = 1
                    i -= 1
            if carry == 1:
                digits.insert(0, 1)
            return digits
        digits[-1] += 1
        return digits
                    
                    