class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = 0
        max_len = 0
        c_dict = {}
        for j in range(l):
            reps = c_dict.setdefault(s[j], [])
            #print(j, reps)
            if reps:
                i = max(max(reps), i)

            max_len = max(max_len, j - i)
            reps.append(j)

        return max_len


def test():
    sol = Solution()
    s1 = 'aaefabce'
    print(sol.lengthOfLongestSubstring(s1))


if __name__ == '__main__':
    test()
