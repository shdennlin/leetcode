
# LeetCode 021. Merge Two Sorted Lists

Question link: <https://leetcode.com/problems/merge-two-sorted-lists/>  

## Solution

{% mdtabs title="Python" %}  

```python
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(None)

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            elif l1.val >= l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next

        curr.next = l1 or l2

        return dummy.next
```

{% endmdtabs %}  

Ref: [[Day 5] 從LeetCode學演算法 - 0021. Merge Two Sorted Lists (Easy)](https://ithelp.ithome.com.tw/articles/10213265)  

My Solution Link: [021 Merge Two Sorted Lists.py](https://github.com/shdennlin/leetcode/blob/main/content/.solution_record/python3/021_Merge_Two_Sorted_Lists.py)  
