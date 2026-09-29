class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        seen = set()
        n = len(s)
        ans = 0
        if n <= 1:
            return n
        
        for right in range(n):
            curr = s[right]
            while curr in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans





        