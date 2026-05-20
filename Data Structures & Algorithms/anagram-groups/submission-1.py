from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity = O(n x m)
        # Space Complexity = O(n)
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            
            ans[tuple(count)].append(s)

        return list(ans.values())