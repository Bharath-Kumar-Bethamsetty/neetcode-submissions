class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return 0
        ans = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            last_digit = x % 10
            ans = (ans * 10) + last_digit
            x = x // 10
        
        ans *= sign
        return ans if (-2**31 <= ans <= (2**31 - 1)) else 0
        