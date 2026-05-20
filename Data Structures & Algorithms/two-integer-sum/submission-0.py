class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            pair2 = target - nums[i]

            if pair2 in dict:
                return [dict[pair2], i]
            else:
                if nums[i] in dict:
                    continue
                else:
                    dict[nums[i]] = i