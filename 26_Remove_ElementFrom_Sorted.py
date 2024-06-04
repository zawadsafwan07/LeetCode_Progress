# LeetCode Problem 26 
# Date : June 3rd 2024
# Abrar Zawad Safwan

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1

        return i        