class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp = 'abcdefghijklmnopqrstuvwxyz1234567890'
        k = ''
        for ch in s:
            if ch in alp or ch in alp.upper():
                k += ch.lower()
        print(k, k[::-1])
        return k == k[::-1]
        

        