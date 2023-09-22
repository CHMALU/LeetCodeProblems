class Solution(object):
    def groupAnagrams(self, strs):
        # """
        # :type strs: List[str]
        # :rtype: List[List[str]]
        # """
        solution = {}

        for element in strs:
            angram = "".join(sorted(element))
            if angram in solution:
                solution[angram].append(element)
            else:
                solution[angram] = [element]
        return solution.values()


obiekt = Solution()
print(obiekt.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
