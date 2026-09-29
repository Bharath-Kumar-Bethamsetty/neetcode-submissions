class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        i = 0
        curr = ''
        while i < n:
            if tokens[i] in '+-*/':
                left = stack.pop()
                right = stack.pop()

                if tokens[i] == '+':
                    stack.append(left+right)
                elif tokens[i] == '-':
                    stack.append(right-left)
                elif tokens[i] == '*':
                    stack.append(left*right)
                else:
                    stack.append(int(right/left))
            else:
                stack.append(int(tokens[i]))
            i += 1
        return stack[0]
