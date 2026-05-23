class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        start_ptr = 0
        end_ptr = len(numbers)-1

        while start_ptr < end_ptr:
            if numbers[start_ptr] + numbers[end_ptr] > target:
                end_ptr = end_ptr - 1
            elif numbers[start_ptr] + numbers[end_ptr] < target:
                start_ptr = start_ptr + 1
            else:
                return [start_ptr + 1, end_ptr + 1]