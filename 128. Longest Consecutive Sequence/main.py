def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for number in nums:
        if (number-1) not in numSet:
            length = 0
            while (number + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest


print(longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
