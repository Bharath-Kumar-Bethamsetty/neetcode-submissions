class Solution:
    def reverse(self, x: int) -> int:

        if x == 0: return 0
        INT_MIN = -2 ** 31
        INT_MAX = (2 ** 31) - 1

        neg = x < 0
        if neg: x *= -1
        res = 0
        while x > 0:
            if res > (INT_MAX // 10):
                return 0
            res = (res * 10) + (x % 10)
            x = x // 10
        return -res if neg else res
        