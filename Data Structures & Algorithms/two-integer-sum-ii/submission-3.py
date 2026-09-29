class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # seen = {}

        # for i, ele in enumerate(numbers):
        #     complement = target - numbers[i]
        #     if complement in seen:
        #         return [seen[complement]+1, i+1]
        #     seen[ele] = i
        # return [-1, -1]

        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l+=1
            else:
                r-=1
        return [-1,-1]