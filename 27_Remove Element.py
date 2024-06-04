# LeetCode Problem 27 Remove Element
# Date : June 3rd 2024
# Abrar Zawad Safwan

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)