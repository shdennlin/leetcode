
# LeetCode 007. Reverse Number

Questions link: <https://leetcode.com/problems/reverse-integer/>  

## Solution

{% mdtabs title="Python" %}  

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            isPos = -1
            x *= -1
        else:
            isPos = 1
            res = 0

        while (x):
            res = res * 10 + x % 10
            x = x // 10

        if res <= -2147483648 or res >= 2147483647 or res == 0:
            return 0
        return res * isPos
```

{% endmdtabs %}  

My Solution Link: [007 Reverse Integer.py](https://github.com/shdennlin/leetcode/blob/main/content/.solution_record/python3/007_Reverse_Integer.py)  
