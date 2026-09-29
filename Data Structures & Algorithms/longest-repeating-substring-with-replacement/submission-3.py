class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        maxFreq = 0
        seen = [0] * 26

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            seen[idx] += 1
            maxFreq = max(maxFreq, seen[idx])

            if (right - left + 1) - maxFreq > k:
                seen[ord(s[left])-ord('A')] -= 1
                left += 1
            
        return len(s) - left

                




