class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        seen = {}
        ans = 0
        n = len(s)
        for right in range(n):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans





        