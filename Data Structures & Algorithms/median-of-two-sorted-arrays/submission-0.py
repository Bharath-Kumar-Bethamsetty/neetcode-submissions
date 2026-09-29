class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr = sorted(nums1 + nums2)
        l = len(arr)
        
        if l % 2:  # odd length
            return arr[l // 2]
        else:  # even length
            return (arr[l // 2 - 1] + arr[l // 2]) / 2
        