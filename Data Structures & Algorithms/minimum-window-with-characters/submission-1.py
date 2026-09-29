from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""
        if s == t:
            return s
        if len(s) < len(t):
            return ""
        
        need = Counter(t)
        window = {}

        formed = 0
        required = len(need)

        best_len = float('inf')
        left = 0
        best_l = 0
        best_r = 0
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1
            
            while formed == required:
                curr_len = right - left + 1
                if curr_len < best_len:
                    best_len = curr_len
                    best_l = left
                    best_r = right
                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                left += 1

        return "" if best_len == float('inf') else s[best_l:best_r + 1]

                
            
