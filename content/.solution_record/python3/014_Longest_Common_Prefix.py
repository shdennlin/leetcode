class Solution:
    # def longestCommonPrefix(self, strs: 'List[str]') -> str:

    #     maxletterlen = float('inf')
    #     for i in strs:
    #         maxletterlen = min(maxletterlen, len(i))

    #     res = ""
    #     for li in range(maxletterlen):
    #         check = True
    #         for i in range(1, len(strs)):
    #             if strs[0][li] != strs[i][li]:
    #                 check = False
    #                 break
    #         if check == True:
    #             res += strs[0][li]
    #         else:
    #             break
    #     return res

    # def longestCommonPrefix(self, strs: 'List[str]') -> str:
    #     maxletterlen = float('inf')
    #     for i in strs:
    #         maxletterlen = min(maxletterlen, len(i))

    #     res = ""
    #     for li in range(maxletterlen):
    #         for i in range(1, len(strs)):
    #             if strs[0][li] != strs[i][li]:
    #                 return res
    #         res += strs[0][li]
    #     return res

    def longestCommonPrefix(self, strs: 'List[str]') -> str:
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


if __name__ == '__main__':
    s = Solution()
    print("=" * 10)
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
    print(s.longestCommonPrefix(["cir", "car"]))
    print("=" * 10)
