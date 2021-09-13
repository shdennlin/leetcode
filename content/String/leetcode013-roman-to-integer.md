
# LeetCode 013. Roman To Integer

Questions link: <https://leetcode.com/problems/roman-to-integer/>  

## Solution

{% mdtabs title="Python" %}  

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = len(s)
        num = 0
        for i, let in enumerate(s):
            if i + 1 < n and roman[let] < roman[s[i + 1]]:
                num -= roman[let]
            else:
                num += roman[let]
        return num
```

{% endmdtabs %}  

My Solution Link: [013 Roman to Integer.py](https://github.com/shdennlin/leetcode/blob/main/content/.solution_record/python3/013_Roman_to_Integer.py)  
