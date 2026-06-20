class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        left = 0
        longest = 0
        s_hash = {}

        for right in range(len(s)):
            if s[right] in s_hash and s_hash[s[right]] >= left:
                left = s_hash[s[right]] + 1

            s_hash[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest
        