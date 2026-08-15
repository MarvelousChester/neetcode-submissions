class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for val in nums:
            counts[val] = counts.get(val, 0) + 1

        sorted_counts = sorted(
            counts.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [value for value, count in sorted_counts[:k]]