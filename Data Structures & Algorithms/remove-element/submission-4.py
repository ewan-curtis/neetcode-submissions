class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0: return 0
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] < val:
            i += 1
        removedCount = 0
        if i < len(nums):
            while nums[i] == val:
                removedCount += 1
                nums[i] = 51
                i += 1
                if i == len(nums): break
        nums.sort()
        return len(nums) - removedCount