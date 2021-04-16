class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c  = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1      
        while i >= 0 or j >= 0: 
            if i >= 0 and j >= 0:
                carry += int(a[i]) + int(b[j])
                i, j = i-1, j-1
            elif i >= 0:
                carry += int(a[i])
                i -= 1
            else:
                carry += int(b[j])
                j -= 1

            c = str(carry % 2) + c
            carry //= 2

        return "1" + c if carry else c