
# LeetCode 009. Palindrome Number

Question link: <https://leetcode.com/problems/palindrome-number/>

## Solution

### convert to string

{% mdtabs title="Python" %}

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            return x == int(str(x)[::-1])
        return False
```

{% endmdtabs %}

### without convert to String

{% mdtabs title="Python" %}

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0):
            return False

        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
        return res == x or res // 10 == x
```

{% endmdtabs %}

My Solution Link: [009 Palindrome Number.py](https://github.com/shdennlin/leetcode/blob/main/content/.solution_record/python3/009_Palindrome_Number.py)
