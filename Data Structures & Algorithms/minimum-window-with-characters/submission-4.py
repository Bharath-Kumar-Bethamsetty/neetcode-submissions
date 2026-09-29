from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        window = {}
        need_count = len(need)
        have = 0
        left = 0
        res = [-1,-1]
        res_len = float('inf')

        m, n = len(s), len(t)
        for right in range(m):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == need_count:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if res_len != float('inf') else ""
            


        