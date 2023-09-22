class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        frequency = [[] for i in range(len(nums)+1)]
        solution = []

        for number in nums:
            count[number] = count.get(number, 0) + 1

        for number, c in count.items():
            frequency[c].append(number)

        for i in range(len(frequency)-1, 0, -1):
            for number in frequency[i]:
                solution.append(number)
                if len(solution) == k:
                    return solution


obiekt = Solution()
print(obiekt.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=3))
