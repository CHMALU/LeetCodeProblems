class Solution(object):
    def romanToInt(self, s):
        liczby = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        result = 0

        for i in range(len(s)):
            if i < len(s)-1 and liczby[s[i]] < liczby[s[i+1]]:
                result -= liczby[s[i]]
            else:
                result += liczby[s[i]]

        return result


solution = Solution()
print(solution.romanToInt('MCD'))
