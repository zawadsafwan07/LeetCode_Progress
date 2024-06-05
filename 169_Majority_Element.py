# LeetCode Problem 169
# Date : June 4th 2024
# Abrar Zawad Safwan

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # size/2
        size = len(nums)/2
        #Create a dictionary to keep count
        dic= dict()

        for n in nums:
            if n not in dic:
                dic[n]=1
            else :
                dic[n]+=1
            if dic[n] >= size:
                return n        