class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        char_dict = {}
        for i in range(len(s)):
            char_dict.setdefault(s[i], [])
            char_dict[s[i]].append(i)

        print(char_dict)

        maker = [1] * len(s)
        '''
        sub = ''
        max_len = 0
        for i in range(len(s)):
            # print(s[i])
            if s[i] not in sub:
                sub = sub + s[i]
            else:
                if len(sub) > max_len:
                    max_len = len(sub)
                broken = sub.index(s[i])
                sub = sub[broken+1:]
                sub = sub + s[i]
            if i == len(s) - 1:
                if len(sub) > max_len:
                    max_len = len(sub)

        return max_len


def test():
    sol = Solution()
    s1 = 'aaaaabcdeafeHA'
    print(sol.lengthOfLongestSubstring(s1))


if __name__ == '__main__':
    test()

