
# LeetCode 009. Palindrome Number

Question link: <https://leetcode.com/problems/palindrome-number/>

## Solution

{% mdtabs title="Python" %}

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            return x == int(str(x)[::-1])
        return False
```

{% endmdtabs %}

My Solution Link: [009 Palindrome Number.py](https://github.com/shdennlin/leetcode/blob/main/content/.solution_record/python3/009_Palindrome_Number.py)
