class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            pair = target - v
            print(d)
            if pair in d:
                return [i, d[pair]]
            d[v] = i
