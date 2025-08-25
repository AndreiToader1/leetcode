class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(': ')',
            '[' : ']',
            '{': '}'
        }
        keys = list(pairs.keys())
        for c in s:
            if c in keys:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    last = stack.pop()
                    if pairs[last] != c:
                        return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("()"))
    print(solution.isValid("()[]{}"))
    print(solution.isValid("(]"))
    print(solution.isValid("([])"))
    print(solution.isValid("([)]"))
    print(solution.isValid('['))
    print(solution.isValid('(('))
