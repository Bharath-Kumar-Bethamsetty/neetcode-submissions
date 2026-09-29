class Solution:
    def isPalindrome(self, s: str) -> bool:


        l_alpha = 'abcdefghijklmnopqrstuvwxyz'
        u_alpha = l_alpha.upper()
        digits = '1234567890'
        k = ''
        for ch in s:
            if ch in l_alpha or ch in u_alpha or ch in digits:
                k += ch.lower()
        l, r = 0, len(k)-1
        while l < r:
            if k[l] != k[r]:
                return False
            l += 1
            r -= 1
        return True

        