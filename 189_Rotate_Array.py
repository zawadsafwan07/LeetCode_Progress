# LeetCode Problem 189 Rotate Array 
# Date : June 4th 2024
# Abrar Zawad Safwan

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        index= 0 
        while index < k:
            temp = nums.pop()   #Remove the last element
            nums.insert(0, temp)   # Insert in front
            index+=1        #Increment index
             
        