class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0
        ans = 0
        sign = '+' if x > 0 else '-'
        if sign == '-':
            x = int(str(x)[1:])
        while x > 0:
            last_digit = x % 10
            ans = (ans * 10) + last_digit
            x = x // 10
        
        ans = -ans if sign == '-' else ans
        return ans if (-2**31 <= ans <= (2**31 - 1)) else 0
        