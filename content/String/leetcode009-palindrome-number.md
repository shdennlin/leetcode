
# LeetCode009 Palindrome Number

Questions link: <https://leetcode.com/problems/palindrome-number/>  

## My first solution

{% mdtabs title="Python" %}  

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <= -2**31 or x >= 2**31 - 1:
            return False

        x = str(x)
        for i in range(len(x)):
            if x[i] == x[-i - 1]:
                continue
            return False
        return True
```

{% endmdtabs %}  

## My final solution

faster and less memory usage  

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
