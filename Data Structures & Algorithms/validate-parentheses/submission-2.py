class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(': stack.append(c)
            elif c == ')':
                if len(stack) == 0: return False
                if stack[-1] == '(': stack.pop()
                else: return False
            elif c == '{': stack.append(c)
            elif c == '}':
                if len(stack) == 0: return False
                if stack[-1] == '{': stack.pop()
                else: return False
            elif c == '[': stack.append(c)
            elif c == ']':
                if len(stack) == 0: return False
                if stack[-1] == '[':
                    stack.pop()
                else: return False
        if len(stack) > 0:
            return False
        return True