# LeetCode Problem 88 Merge Sorted Array 
# Date : June 3rd 2024
# Abrar Zawad Safwan

class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        # index
        n1_index = m - 1  # nums1 index
        n2_index = n - 1  # nums2 index
        sorted_index = m + n - 1  # sorted array index

        while n2_index >= 0:
            if n1_index >= 0 and nums1[n1_index] > nums2[n2_index]:
                nums1[sorted_index] = nums1[n1_index]
                n1_index -= 1
            else:
                nums1[sorted_index] = nums2[n2_index]
                n2_index -= 1
            sorted_index -= 1
