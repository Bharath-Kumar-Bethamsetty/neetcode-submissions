class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False
        stack = []

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    return False

                k = stack.pop()
                if ch == ')':
                    if k != '(':
                        return False
                elif ch == ']':
                    if k != '[':
                        return False
                elif ch == '}':
                    if k != '{':
                        return False
        return True if not stack else False
        