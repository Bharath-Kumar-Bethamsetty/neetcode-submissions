class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        opn = '([{'
        cls = ')]}'
        if len(s) % 2 == 1:
            return False

        for ch in s:
            if ch in opn:
                stack.append(ch)
            elif ch in cls:
                if len(stack) == 0:
                    return False
                curr_ch = stack.pop()
                if (curr_ch == '{' and ch == '}') or (curr_ch == '(' and ch == ')') or (curr_ch == '[' and ch == ']'):
                    continue
                else:
                    return False
        return True if len(stack) == 0 else False
                



        