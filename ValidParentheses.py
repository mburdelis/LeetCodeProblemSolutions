class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in matching:
                if not stack or stack[-1] != matching[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))       # True
    print(solution.isValid("()[]{}"))   # True
    print(solution.isValid("(]"))       # False
    print(solution.isValid("([])"))     # True
    print(solution.isValid("([)]"))     # false
