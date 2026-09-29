class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        m, n = len(s1), len(s2)
        target = sorted(s1)

        for left in range(n - m + 1):
            if sorted(s2[left:left+m]) == target:
                return True
        
        return False
            



        