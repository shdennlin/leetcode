class Solution:
    # node
    # def isPalindrome(self, x: int) -> bool:
    #     if x <= -2**31 or x >= 2**31 - 1:
    #         return False

    #     x = str(x)
    #     for i in range(len(x)):
    #         if x[i] == x[-i - 1]:
    #             continue
    #         return False
    #     return True

    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False
    #     return str(x) == str(x)[::-1]

    #  Follow up: Could you solve it without converting the integer to a string?
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False

    #     old = x
    #     new = 0
    #     while x:
    #         new = new * 10 + x % 10
    #         x = x // 10
    #     return new == old

    # faster
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0):
            return False

        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10
        return res == x or res // 10 == x


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(100))
    print(s.isPalindrome(11))
    print(s.isPalindrome(0))
    print(s.isPalindrome(313))
    print(s.isPalindrome(205))
    print(s.isPalindrome(123454321))
    print(s.isPalindrome(-1234321))
