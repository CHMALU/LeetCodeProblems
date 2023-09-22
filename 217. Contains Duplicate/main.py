class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()

        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        return False


obiekt = Solution()
print(obiekt.containsDuplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
