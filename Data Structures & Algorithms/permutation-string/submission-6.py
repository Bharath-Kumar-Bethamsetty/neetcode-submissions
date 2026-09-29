from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m, n = len(s1), len(s2)
        target = Counter(s1)

        for left in range(n - m + 1):
            window = Counter(s2[left:left+m])
            if window == target:
                return True
        
        return False
            



        