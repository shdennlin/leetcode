class Solution:

    # first
    # def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             t = nums[i] + nums[j]
    #             if t == target:
    #                 return [i, j]

    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        val = {}
        ans = []
        for i, n in enumerate(nums):
            diff = target - n
            if diff in val:
                ans.append(i)
                ans.append(val[diff])
                return ans
            val[n] = i


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
