class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            candidate = target - nums[i]
            if candidate in compliments.keys():
                return [compliments[candidate], i]
            else:
                compliments[nums[i]] = i
