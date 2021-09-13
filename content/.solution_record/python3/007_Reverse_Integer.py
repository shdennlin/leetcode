class Solution:
    # My first Answer
    # def reverse(self, x: int) -> int:
    #     max_num = 2**31 - 1
    #     min_num = 2**31 * (-1)

    #     x = str(x)
    #     if x[0] == "-":
    #         x = x[1:]
    #         x = "-" + x[::-1]
    #     else:
    #         x = x[::-1]

    #     x = int(x)
    #     if x <= min_num or x >= max_num or x == 0:
    #         return 0
    #     return x

    # def reverse(self, x: int) -> int:
    #     max_num = 2147483647
    #     min_num = -2147483647

    #     x = str(x)
    #     if x[0] == "-":
    #         x = x[1:]
    #         x = "-" + x[::-1]
    #     else:
    #         x = x[::-1]

    #     x = int(x)
    #     if x <= min_num or x >= max_num or x == 0:
    #         return 0
    #     return x

    def reverse(self, x: int) -> int:
        if x < 0:
            isPos = -1
            x *= -1
        else:
            isPos = 1
        res = 0

        while (x):
            res = res * 10 + x % 10
            x = x // 10

        if res <= -2147483648 or res >= 2147483647 or res == 0:
            return 0
        return res * isPos


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(120))
    print(s.reverse(0))
    print(s.reverse(-123))
    print(s.reverse(1534236469))
    print(s.reverse(9999999999999999))
