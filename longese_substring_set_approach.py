class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        j = 0
        l = len(s)
        sub = set()
        sub_len = 0
        while i < l and j < l:
            # print(s[i])
            if s[j] not in sub:
                sub.add(s[j])
                j = j + 1
                sub_len = max(sub_len, j - i)

            else:
                sub.remove(s[i])
                i = i + 1

        return sub_len


def test():
    sol = Solution()
    s1 = 'aaaaabcdeafeHA'
    print(sol.lengthOfLongestSubstring(s1))


if __name__ == '__main__':
    test()
