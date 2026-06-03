class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i, nums in enumerate(nums):
            complement = target - nums
            if complement in num_map:
                return [num_map[complement],i]
            num_map[nums]=i
        