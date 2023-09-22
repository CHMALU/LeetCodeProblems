class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        print(result)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            print(i, postfix, result)
            result[i] *= postfix
            postfix *= nums[i]

        return result


obiekt = Solution()
print(obiekt.productExceptSelf(nums=[1, 2, 3, 4]))
