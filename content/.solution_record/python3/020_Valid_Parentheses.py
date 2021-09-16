from typing import List


class Solution:
    # reference https://leetcode.com/problems/valid-parentheses/discuss/1344275/Simple-python-solution-(4ms-135mb-memory-usage)
    def isValid(self, s: str) -> bool:
        m = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for i in s:
            if i in m:
                stack.append(m[i])
            elif len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))  #True
    print(s.isValid("(]"))  #False
    print(s.isValid("([)]"))  #False
    print(s.isValid("{[]}"))  #True
    print(s.isValid("(){}}{"))  #False
