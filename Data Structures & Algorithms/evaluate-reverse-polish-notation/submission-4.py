class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        
        for ch in tokens:
            if ch not in '+-*/':
                stack.append(ch)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if ch == '+':
                    stack.append(str(left+right))
                elif ch == '-':
                    stack.append(str(left-right))
                elif ch == '*':
                    stack.append(str(left*right))
                elif ch == '/':
                    stack.append(str(int(left/right)))
        return int(stack[-1])
                
                



        