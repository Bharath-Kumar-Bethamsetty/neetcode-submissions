from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = sorted(Counter(nums).items(), key=lambda x:x[1], reverse=True)
        ans = []
        c = 0
        for num, cnt in freq:
            if c < k:
                ans.append(num)
                c += 1
        return ans
        