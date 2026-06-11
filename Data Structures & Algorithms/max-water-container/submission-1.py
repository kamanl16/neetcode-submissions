class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        head_ptr = 0
        tail_ptr = len(heights)-1
        max_amt = 0

        while head_ptr < tail_ptr:
            max_amt = max(max_amt, (tail_ptr - head_ptr) * min(heights[head_ptr], heights[tail_ptr]))

            if heights[head_ptr] <= heights[tail_ptr]:
                head_ptr += 1
            elif heights[head_ptr] > heights[tail_ptr]:
                tail_ptr -= 1
            
        return max_amt