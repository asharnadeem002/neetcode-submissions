class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in temp:
                return [temp[diff], i]
            temp[v] = i