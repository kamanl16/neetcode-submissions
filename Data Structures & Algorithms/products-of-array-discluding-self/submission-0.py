class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        n = len(nums)
        
        left_products = [1] * n
        right_products = [1] * n
        answer = [1] * n

        for index in range(1, n):
            left_products[index] = left_products[index-1] * nums[index-1]
        for index in range(n-2, -1, -1):
            right_products[index] = right_products[index+1] * nums[index+1]

        for index in range(n):
            answer[index] = left_products[index] * right_products[index]
       
        return answer