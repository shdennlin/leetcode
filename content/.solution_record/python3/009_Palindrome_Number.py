class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     if x <= -2**31 or x >= 2**31 - 1:
    #         return False

    #     x = str(x)
    #     for i in range(len(x)):
    #         if x[i] == x[-i - 1]:
    #             continue
    #         return False
    #     return True

    # faster and less memory
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            return x == int(str(x)[::-1])
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(100))
    print(s.isPalindrome(205))
    print(s.isPalindrome(123454321))
    print(s.isPalindrome(-1234321))
