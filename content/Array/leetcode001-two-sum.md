
# LeetCode 001. Two Sum

Questions link: <https://leetcode.com/problems/two-sum>  

## Solution

{% mdtabs title="Python" %}  

```python
class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                t = nums[i] + nums[j]
                if t == target:
                    return [i, j]
```

{% endmdtabs %}  

My Solution Link: [001 Two Sum.py](https://github.com/shdennlin/leetcode/blob/main/content/.solution_record/python3/001_Two_Sum.py)  
