from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m, n = len(s1), len(s2)
        if m > n:
            return False
        
        s1_count = [0]*26
        win_count = [0]*26

        for i in range(m):
            s1_count[ord(s1[i])-ord('a')] += 1
            win_count[ord(s2[i])-ord('a')] += 1
        
        if win_count == s1_count:
            return True
            
        left = 0
        for right in range(m,n):
            win_count[ord(s2[right]) - ord('a')] += 1
            win_count[ord(s2[left]) - ord('a')] -= 1
            left += 1

            if win_count == s1_count:
                return True
        
        return False



            


        