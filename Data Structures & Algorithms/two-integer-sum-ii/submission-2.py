class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, ele in enumerate(numbers):
            complement = target - numbers[i]
            if complement in seen:
                return [seen[complement]+1, i+1]
            seen[ele] = i
        return [-1, -1]