class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)

        return s == t


obiekt = Solution()
print(obiekt.isAnagram(s="anagram", t="nagaram"))
