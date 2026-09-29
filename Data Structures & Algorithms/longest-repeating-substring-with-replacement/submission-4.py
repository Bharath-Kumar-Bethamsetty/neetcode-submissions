class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        maxFreq = 0
        n = len(s)
        freq = {}
        ans = 0

        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans



        