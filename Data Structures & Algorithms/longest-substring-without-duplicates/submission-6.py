class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            seen[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans
        