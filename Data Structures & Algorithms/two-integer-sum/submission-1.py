class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        
        prev_map = {}

        for i in range(len(nums)):
            pair2 = target - nums[i]

            if pair2 in prev_map:
                return [prev_map[pair2], i]
            
            prev_map[nums[i]] = i