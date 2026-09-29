class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m, n = len(nums1), len(nums2)
        total = m+n
        isOdd = total % 2
        n1p = n2p = 0
        prev = curr = 0
        for _ in range(total//2 + 1):
            prev = curr
            if n1p < m and n2p < n:
                if nums1[n1p] <= nums2[n2p]:
                    curr = nums1[n1p]
                    n1p += 1
                else:
                    curr = nums2[n2p]
                    n2p += 1
            elif n1p < m:
                curr = nums1[n1p]
                n1p += 1
            else:
                curr = nums2[n2p]
                n2p += 1
        if isOdd:
            return curr
        
        return (prev + curr) / 2