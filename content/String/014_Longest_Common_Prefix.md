
# LeetCode 014. Longest Common Prefix

Questions link:	<https://leetcode.com/problems/longest-common-prefix/>   

## Solution

{% mdtabs title="Python" %}  

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = strs[0]
        if len(strs) == 1:
            return ret

        while True:
            retC = True
            for letter in strs[1:]:
                if letter.startswith(ret):
                    continue
                else:
                    ret = ret[:-1]
                    retC = False
                    break
            if retC == True:
                return ret
```

{% endmdtabs %}  

My Solution Link: [014 Longest Common Prefix.py](https://github.com/shdennlin/leetcode/blob/main/content/.solution_record/python3/014_Longest_Common_Prefix.py)  
