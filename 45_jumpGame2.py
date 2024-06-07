# LeetCode Problem 45 Jump Game
# Date : June 5th 2024
# Abrar Zawad Safwan

class Solution:
    def jump(self, nums: List[int]) -> int:
        #number of jumps
        jumps=0
        #assign pointer
        left_p = right_p =0
        #while r< last index 
        while right_p < len(nums)-1:
            farthest=0  #assign furthest
            for i in range(left_p, right_p+1):
                farthest= max(farthest, i+nums[i])
            left_p = right_p +1
            right_p = farthest
            jumps+=1
        return jumps
