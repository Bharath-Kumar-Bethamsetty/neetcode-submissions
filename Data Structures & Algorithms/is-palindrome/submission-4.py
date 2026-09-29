class Solution:
    def isPalindrome(self, s: str) -> bool:

        k = ''
        for ch in s:
            if ch.isalnum():
                k += ch.lower()
        l, r = 0, len(k)-1
        while l < r:
            if k[l] != k[r]:
                return False
            l += 1
            r -= 1
        return True

        