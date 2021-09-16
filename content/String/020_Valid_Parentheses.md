
# LeetCode 020. Valid Parentheses

Question link: <https://leetcode.com/problems/valid-parentheses/>  

## Solution

{% mdtabs title="Python" %}  

```python
class Solution:
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
```

{% endmdtabs %}  

Ref: [Simple python solution (4ms, 13,5mb memory usage)](https://leetcode.com/problems/valid-parentheses/discuss/1344275/Simple-python-solution-(4ms-135mb-memory-usage))  

My Solution Link: [020 Valid Parentheses.py](https://github.com/shdennlin/leetcode/blob/main/content/.solution_record/python3/020_Valid_Parentheses.py)  
