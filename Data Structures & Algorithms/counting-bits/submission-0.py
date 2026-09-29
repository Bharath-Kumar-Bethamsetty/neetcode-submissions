class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        i = 0
        while i <= n:
            k = i
            c = 0
            while k > 0:
                c += k & 1
                k >>= 1
            ans.append(c)
            i += 1
        return ans

        