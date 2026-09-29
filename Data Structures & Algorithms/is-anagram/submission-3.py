from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = Counter(s)
        for i in t:
            if i not in freq.keys():
                return False
            freq[i] -= 1
        for cnt in freq.values():
            if cnt != 0:
                return False
        return True