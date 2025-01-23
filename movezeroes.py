###Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero,i=0,0
        n=len(nums)
        while i<n:
            if nums[i]!=0:
                nums[i],nums[nonzero]=nums[nonzero],nums[i]
                nonzero+=1
            i+=1