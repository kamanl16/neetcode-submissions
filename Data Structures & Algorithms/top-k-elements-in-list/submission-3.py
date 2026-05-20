class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        freq = [[] for _ in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res