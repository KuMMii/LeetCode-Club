class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1, len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1

        return l

# My initial code
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                nums.pop(i+1)
            else:
                i+=1
        return len(nums)