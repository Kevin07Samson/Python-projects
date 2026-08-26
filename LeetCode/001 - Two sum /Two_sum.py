class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in numbers:
                return [numbers[difference], i]

            numbers[num] = i