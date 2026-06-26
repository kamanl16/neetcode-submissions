class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        left = 0
        right = 0
        longest = 0
        max_freq = 0
        s_hash = {}

        for right in range(len(s)):
            s_hash[s[right]] = s_hash.get(s[right], 0) + 1
            max_freq = max(max_freq, s_hash[s[right]])

            while (right - left + 1) - max_freq > k:
                s_hash[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest