from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = Counter(s)
        for ch in t:
            freq[ch] -= 1
            if freq[ch] < 0:
                return False
                
        return True