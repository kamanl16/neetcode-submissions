class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(n log n) + O(n^2)
        # Space Complexity: O(n)
        nums.sort()
        res = []
        
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            
            head_ptr = i + 1
            tail_ptr = len(nums) - 1
            
            while head_ptr < tail_ptr:
                total = nums[head_ptr] + nums[tail_ptr] + nums[i]

                if total > 0:
                    tail_ptr -= 1
                elif total < 0:
                    head_ptr += 1
                else:
                    res.append([nums[i], nums[head_ptr], nums[tail_ptr]])

                    head_ptr += 1

                    while head_ptr < tail_ptr and nums[head_ptr] == nums[head_ptr - 1]:
                        head_ptr += 1
            
        return res