class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        m_stack = []
        result = [0] * n

        for i, num in enumerate(temperatures):
            while m_stack and temperatures[i] > temperatures[m_stack[-1]]:
                prev_idx = m_stack.pop()
                result[prev_idx] = i - prev_idx 
            m_stack.append(i)
        
        return result


        