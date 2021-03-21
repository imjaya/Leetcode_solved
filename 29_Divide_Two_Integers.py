class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == 0:
            return 0
        
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        while dividend >= divisor:
            val, n = divisor, 1
            while val + val <= dividend:
                val += val
                n += n
            
            res += n
            dividend -= val

        
        if sign == 1:
            return min(res, 2**31 -1)
        else: 
            return max(-res, -2**31)