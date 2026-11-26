class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [None] * len(nums)
        suffixes = [None] * len(nums)

        prefixes[0] = 1
        suffixes[len(nums) - 1] = 1
        prefix_sum = 1
        for i in range(1, len(nums)):
            prefix_sum *= nums[i-1]
            prefixes[i] = prefix_sum
        suffix_sum = 1
        for i in range(len(nums)-2, -1, -1):
            suffix_sum *= nums[i+1]
            suffixes[i] = suffix_sum
        output = []
        for i in range(len(nums)):
            output.append(prefixes[i] * suffixes[i])
        return output