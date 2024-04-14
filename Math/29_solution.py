class Solution:
    
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0
        
        if abs(divisor) == 1:
            if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
                return abs(dividend) if abs(dividend) < 2147483648 else 2147483647
            else:
                return 0 - abs(dividend) if abs(dividend) <= 2147483648 else -2147483648
        
        if dividend == divisor:
            return 1

        ret = len(range(0, abs(dividend) + 1, abs(divisor))) - 1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return ret
        else:
            return 0 - ret

